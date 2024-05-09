import json
import requests
from requests_toolbelt.utils import dump

import iracing_connect.endpoints as endpoints
import iracing_connect.helpers as helpers


class HTTPMethod:
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    PATCH = "PATCH"
    DELETE = "DELETE"


class iRacingConnectTransport:
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
        json_data = json.dumps(data)

        login_response = requests.post(
            endpoints.URL_LOGIN, data=json_data, headers=headers
        )
        return login_response.cookies

    def get(self, url: str, params: dict = None):
        response = self.request(url, HTTPMethod.GET, params)
        self.logger.info(f"Request sent for URL: {response.url}")
        self.logger.info(
            f"Status code of the response: {response.status_code}"
        )
        self.logger.debug(f"Response object: {response.__dict__}")

        return response

    def dump_response(self, response):
        data = dump.dump_all(response)
        return str(data.decode("utf-8"))
