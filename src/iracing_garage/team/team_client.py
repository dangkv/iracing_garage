import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class TeamClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "team"

    def get(self, team_id: int, include_licenses: bool = None) -> dict:

        endpoint = endpoints.URL_TEAM_GET
        func_name = inspect.stack()[0][3]

        params = {"team_id": team_id, "include_licenses": include_licenses}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
