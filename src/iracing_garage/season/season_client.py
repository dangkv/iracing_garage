import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class SeasonClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "season"

    def list(self, season_year: int, season_quarter: int) -> dict:

        endpoint = endpoints.URL_SEASON_LIST
        func_name = inspect.stack()[0][3]

        params = {"season_year": season_year, "season_quarter": season_quarter}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def race_guide(
        self, from_ts: str = None, include_end_after_from: bool = None
    ) -> dict:

        endpoint = endpoints.URL_SEASON_RACE_GUIDE
        func_name = inspect.stack()[0][3]

        params = {
            "from": from_ts,
            "include_end_after_from": include_end_after_from,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def spectator_subsessionids(self, event_types: int = None) -> dict:

        endpoint = endpoints.URL_SEASON_SPECTATOR_SUBSESSIONIDS
        func_name = inspect.stack()[0][3]

        params = {"event_types": event_types}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
