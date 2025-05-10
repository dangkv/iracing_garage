import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class MemberClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "member"

    def awards(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_MEMBER_AWARDS
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def chart_data(
        self, category_id: int, chart_type: int, cust_id: int = None
    ) -> dict:

        endpoint = endpoints.URL_MEMBER_CHART_DATA
        func_name = inspect.stack()[0][3]

        params = {
            "category_id": category_id,
            "chart_type": chart_type,
            "cust_id": cust_id,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def get(self, cust_ids: int, include_licenses: bool = None) -> dict:

        endpoint = endpoints.URL_MEMBER_GET
        func_name = inspect.stack()[0][3]

        params = {"cust_ids": cust_ids, "include_licenses": include_licenses}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def info(self) -> dict:

        endpoint = endpoints.URL_MEMBER_INFO
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def participation_credits(self) -> dict:

        endpoint = endpoints.URL_MEMBER_PARTICIPATION_CREDITS
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def profile(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_MEMBER_PROFILE
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
