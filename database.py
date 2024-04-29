import duckdb
from config_reader import read_config

config = read_config('config.yml')
database_name = config['database_name']


class Database:
    def __init__(self, db_path):
        self.db_path = db_path
        self.connection = None

    def connect(self):
        '''
        Creates a connection to the db based on the path that is passed
        '''
        self.connection = duckdb.connect(self.db_path)

    def table_exists(self, table_name):
        '''
        Checks if the table exists and returns True if it does
        '''
        result = self.connection.execute(f"SELECT * FROM information_schema.tables WHERE table_name='{table_name}'")
        return len(result.fetchall()) > 0

    def create_table(self):
        if not self.table_exists(f"{database_name}_data"):
            self.connection.execute(f"""
                CREATE SEQUENCE seq_bronze_analytics_data_id;
                CREATE TABLE IF NOT EXISTS {database_name}_data (
                uid INTEGER DEFAULT nextval('seq_bronze_analytics_data_id') PRIMARY KEY,
                city VARCHAR,
                country VARCHAR,
                browser VARCHAR,
                activeUsers INTEGER,
                sessions INTEGER,
                bounceRate FLOAT
                )
            """)

    def insert_data(self, response):
        for row in response.rows:
            self.connection.execute(f"""
            INSERT INTO {database_name}_data (city, country, browser, activeUsers, sessions, bounceRate)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (
                row.dimension_values[0].value, 
                row.dimension_values[1].value, 
                row.dimension_values[2].value, 
                row.metric_values[0].value, 
                row.metric_values[1].value, 
                row.metric_values[2].value
                )
            )

    def select_data(self, query):
        cursor = self.connection.cursor() 
        cursor.execute(query) 
        rows = cursor.fetchall() 
        return rows
    
    def commit(self):
        self.connection.commit()