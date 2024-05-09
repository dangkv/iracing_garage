import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class ResultsClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "results"

    def event_log(self, subsession_id: int, simsession_number: int) -> dict:
        endpoint = endpoints.URL_RESULTS_EVENT_LOG
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def lap_chart_data(
        self, subsession_id: int, simsession_number: int
    ) -> dict:
        endpoint = endpoints.URL_RESULTS_LAP_CHART_DATA
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def lap_data(self, subsession_id: int, simsession_number: int) -> dict:
        endpoint = endpoints.URL_RESULTS_LAP_DATA
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def summary(self, subsession_id: int, simsession_number: int) -> dict:
        endpoint = endpoints.URL_RESULTS_SUMMARY
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
