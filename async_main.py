import asyncio
from prettytable import PrettyTable
from google.analytics.data_v1beta.types import DateRange, Dimension, Metric
from analytics_client import AnalyticsClient
from database import Database
from config_reader import read_config

# Read the config file for configurations
config = read_config('config.yml')

# Set each configuration to respective varibles
property_digit = config['property']
database_name = config['database_name']
start_date = config['date_range']['start_date']
end_date = config['date_range']['end_date']
all_dimensions = config['dimension']
all_metrics = config['metrics']
query = config['query']
view_query = config['select_query']


async def main_executor():
    analytics_client = AnalyticsClient()
    db = Database(f'{database_name}.db')

    property_id = property_digit
    date_range = DateRange(start_date=start_date, end_date=end_date)
    dimensions = [Dimension(name=name) for name in all_dimensions]
    metrics = [Metric(name=name) for name in all_metrics]

    response = await analytics_client.get_report(property_id, date_range, dimensions, metrics)
    db.connect()
    db.create_table()
    db.insert_data(response)
    db.select_data(query)
    db.commit()
    
  

if __name__ == "__main__":
    asyncio.run(main_executor())
    db = Database(f'{database_name}.db')
    db.connect()
    table = PrettyTable() # Used pretty table for a tabular view of the data

    table.field_names = ['id', 'city', 'country', 'browser', 'activeUsers', 'sessions', 'bounceRate']
    rows = db.select_data(view_query)
    for row in rows:
        table.add_row(row)
    print(table)