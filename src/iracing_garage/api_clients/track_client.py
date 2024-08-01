import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class TrackClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "track"

    def get(self) -> dict:
        endpoint = endpoints.URL_TRACK_GET
        func_name = inspect.stack()[0][3]

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name
        )

    def assets(self) -> dict:
        endpoint = endpoints.URL_TRACK_ASSETS
        func_name = inspect.stack()[0][3]

        return self._get(
            url=endpoint, api_group=self.api_group, func_name=func_name
        )
