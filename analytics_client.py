import asyncio
from google.analytics.data_v1beta import BetaAnalyticsDataAsyncClient
from google.analytics.data_v1beta.types import RunReportRequest


class AnalyticsClient:
    def __init__(self):
        self.client = BetaAnalyticsDataAsyncClient()

    async def get_report(self, property_id, date_range, dimensions, metrics):
        request = RunReportRequest(
            property=f"properties/{property_id}",
            date_ranges=[date_range],
            dimensions=dimensions,
            metrics=metrics
        )
        return await self.client.run_report(request)