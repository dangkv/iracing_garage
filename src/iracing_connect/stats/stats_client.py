import inspect

import iracing_connect.endpoints as endpoints
from iracing_connect.client import iRacingConnectClient


class StatsClient(iRacingConnectClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "stats"

    def member_bests(self, customer_id: int, car_id: int) -> dict:
        endpoint = endpoints.URL_STATS_MEMBER_BESTS
        func_name = inspect.stack()[0][3]

        params = {"customer_id": customer_id, "car_id": car_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )

    def member_career(self, customer_id: int) -> dict:
        endpoint = endpoints.URL_STATS_MEMBER_CAREER
        func_name = inspect.stack()[0][3]

        params = {"customer_id": customer_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )

    def member_summary(self, customer_id: int) -> dict:
        endpoint = endpoints.URL_STATS_MEMBER_SUMMARY
        func_name = inspect.stack()[0][3]

        params = {"customer_id": customer_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )

    def member_yearly(self, customer_id: int) -> dict:
        endpoint = endpoints.URL_STATS_MEMBER_YEARLY
        func_name = inspect.stack()[0][3]

        params = {"customer_id": customer_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )

    def member_recent_races(self, customer_id: int) -> dict:
        endpoint = endpoints.URL_STATS_MEMBER_RECENT_RACES
        func_name = inspect.stack()[0][3]

        params = {"customer_id": customer_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )
