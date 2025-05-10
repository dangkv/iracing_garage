import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class ConstantsClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "constants"

    def categories(self) -> dict:

        endpoint = endpoints.URL_CONSTANTS_CATEGORIES
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def divisions(self) -> dict:

        endpoint = endpoints.URL_CONSTANTS_DIVISIONS
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def event_types(self) -> dict:

        endpoint = endpoints.URL_CONSTANTS_EVENT_TYPES
        func_name = inspect.stack()[0][3]

        params = None

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
