import json
import requests
from requests_toolbelt.utils import dump

import iracing_garage.endpoints as endpoints
import iracing_garage.helpers as helpers


class HTTPMethod:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class iRacingGarageTransport:
    def __init__(self, username, password, logger):
        self.username = username
        self.password = password
        self.logger = logger
        self.cookies = self._get_cookies()

    def request(self, url, method, params=None):
        request_args = {
            "method": method,
            "url": url,
            "params": params,
            "cookies": self.cookies,
            "allow_redirects": False,
            "timeout": 10.0,
        }
        return requests.request(**request_args)

    def _get_cookies(self):
        password = helpers.encode_pw(self.username, self.password)
        data = {"email": self.username, "password": password}
        headers = {"Content-Type": "application/json"}

        login_response = requests.post(
            endpoints.URL_LOGIN, data=json.dumps(data), headers=headers
        )
        return login_response.cookies

    def get(self, url: str, params: dict = None):
        self.logger.info(f"Request sent to: {url}")
        response = self.request(url, HTTPMethod.GET, params)
        self.logger.info(f"Payload received from: {response.url}")

        return response

    def dump_response(self, response):
        data = dump.dump_all(response)
        return str(data.decode("utf-8"))
