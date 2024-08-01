import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class HostedClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "hosted"

    def combined_sessions(self, package_id: int = None) -> dict:

        endpoint = endpoints.URL_HOSTED_COMBINED_SESSIONS
        func_name = inspect.stack()[0][3]

        params = {"package_id": package_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def sessions(self) -> dict:

        endpoint = endpoints.URL_HOSTED_SESSIONS
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
