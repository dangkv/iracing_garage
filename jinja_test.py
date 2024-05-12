def assets(self) -> dict:

    endpoint = endpoints.URL_CAR_ASSETS
    func_name = inspect.stack()[0][3]

    params = None

    return self._get(
        url=endpoint,
        api_group=self.api_group,
        func_name=func_name,
        params=params,
    )


def get(self) -> dict:

    endpoint = endpoints.URL_CAR_GET
    func_name = inspect.stack()[0][3]

    params = None

    return self._get(
        url=endpoint,
        api_group=self.api_group,
        func_name=func_name,
        params=params,
    )
