import inspect

import iracing_connect.endpoints as endpoints
from iracing_connect.client import iRacingConnectClient


class TimeAttackClient(iRacingConnectClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "time_attack"

    def member_season_results(self, ta_comp_season_id: int) -> dict:
        endpoint = endpoints.URL_TIME_ATTACK_MEMBER_SEASON_RESULTS
        func_name = inspect.stack()[0][3]

        params = {"ta_comp_season_id": ta_comp_season_id}

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name, params=params
        )
