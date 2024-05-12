import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class SeriesClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "series"

    def assets(self) -> dict:

        endpoint = endpoints.URL_SERIES_ASSETS
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def get(self) -> dict:

        endpoint = endpoints.URL_SERIES_GET
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def past_seasons(self, series_id: int) -> dict:

        endpoint = endpoints.URL_SERIES_PAST_SEASONS
        func_name = inspect.stack()[0][3]

        params = {"series_id": series_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def seasons(self, include_series: bool = None) -> dict:

        endpoint = endpoints.URL_SERIES_SEASONS
        func_name = inspect.stack()[0][3]

        params = {"include_series": include_series}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def stats_series(self) -> dict:

        endpoint = endpoints.URL_SERIES_STATS_SERIES
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
