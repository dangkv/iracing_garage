import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class LookupClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "lookup"

    def club_history(self, season_year: int, season_quarter: int) -> dict:

        endpoint = endpoints.URL_LOOKUP_CLUB_HISTORY
        func_name = inspect.stack()[0][3]

        params = {"season_year": season_year, "season_quarter": season_quarter}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def countries(self) -> dict:

        endpoint = endpoints.URL_LOOKUP_COUNTRIES
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def drivers(self, search_term: str, league_id: int = None) -> dict:

        endpoint = endpoints.URL_LOOKUP_DRIVERS
        func_name = inspect.stack()[0][3]

        params = {"search_term": search_term, "league_id": league_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def get(self) -> dict:

        endpoint = endpoints.URL_LOOKUP_GET
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def licenses(self) -> dict:

        endpoint = endpoints.URL_LOOKUP_LICENSES
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
