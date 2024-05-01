import inspect
import logging
import json
import requests
import iracing_connect.endpoints
import iracing_connect.helpers
import iracing_connect.transport


class iRacingConnectClient:
    def __init__(self, transport, logger):
        self.logger = logger
        self.transport = transport

    def _get(self, url: str, api_group: str, func_name: str, params=None) -> dict:
        response = self.transport.get(url=url, params=params)

        if response.status_code == requests.codes.OK:
            gateway_response_dict = json.loads(response.text)
            api_link = gateway_response_dict.get("link")

            # TODO: raise if fails
            response_data = self.transport.get(url=api_link)
            return response_data.json()

        else:
            self.logger.debug(
                f"Error retrieving {api_group} - {func_name}: {self.transport.dump_response(response)}"
            )
            raise Exception(
                f"Error retrieving {api_group} - {func_name}: {response.text}"
            )


class Client:
    def __init__(self, username: str, password: str):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.username = username
        self.password = password
        self.cookies = self._login()

    def _login(self):
        password = helpers.encode_pw(self.username, self.password)
        data = {"email": self.username, "password": password}
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(data)

        login_response = requests.post(
            endpoints.URL_LOGIN, data=json_data, headers=headers
        )
        return login_response.cookies

    def _get(self, url: str, params: dict, has_chunks: bool = False):
        if not self.cookies:
            logging.info("No cookies in cookie jar.")
            self.cookies = self._login()

        logging.info(f"Request being sent to: {url} with params: {params}")

        # TODO: Add a try except raise for failed requests
        response = requests.get(
            url,
            params=params,
            cookies=self.cookies,
            allow_redirects=False,
            timeout=10.0,
        )
        logging.info(f"Request sent for URL: {response.url}")
        logging.info(f"Status code of the response: {response.status_code}")
        logging.debug(f"Response object: {response.__dict__}")

        response_dict = json.loads(response.text)
        link = response_dict.get("link")

        # TODO: Add a try except raise for failed requests
        response_text = requests.get(link).text

        payload_dict = json.loads(response_text)

        payload = json.dumps(payload_dict)  # TODO: delete

        print()

        return payload_dict

    def _get_chunks(self, payload):
        chunks = []
        chunk_info = payload.get("chunk_info")
        chunk_download_url = chunk_info.get("base_download_url")
        chunk_file_names = [x for x in chunk_info.get("chunk_file_names")]

        for i, chunk_file_name in enumerate(chunk_file_names):
            full_url = chunk_download_url + chunk_file_name

            try:
                response = requests.get(
                    full_url,
                    cookies=self.cookies,
                    allow_redirects=False,
                    timeout=10.0,
                ).text
            except:
                # TODO: build exceptions
                msg = f"API extraction error at {chunk_file_name}, {i}/{len(chunk_file_names)}"
                pass

            chunks.append(response)

        print()
        return chunks

    def _wrap_payload(self, payload, method, endpoint, parameters):
        ## {timestamp, payload, method, endpoint, parameters, username}
        record = {
            "timestamp": helpers.get_current_utc_time(),
            "method": method,
            "endpoint": endpoint,
            "parameters": parameters,
            "username": self.username,
            "payload": payload,
        }
        return record

    def member_bests(self, customer_id, car_id):
        params = {"cust_id": customer_id, "car_id": car_id}
        endpoint = endpoints.URL_STATS_MEMBER_BESTS
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record

    def member_career(self, customer_id):
        params = {"cust_id": customer_id}
        endpoint = endpoints.URL_STATS_MEMBER_CAREER
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record

    def member_recent_races(self, customer_id):
        params = {"cust_id": customer_id}
        endpoint = endpoints.URL_STATS_MEMBER_RECENT_RACES
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record

    def member_summary(self, customer_id):
        params = {"cust_id": customer_id}
        endpoint = endpoints.URL_STATS_MEMBER_SUMMARY
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record

    def member_yearly(self, customer_id):
        params = {"cust_id": customer_id}
        endpoint = endpoints.URL_STATS_MEMBER_YEARLY
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record

    def membership(self, customer_id: int):
        params = {"customer_id": customer_id}
        endpoint = endpoints.URL_MEMBERSHIP
        func_name = inspect.stack()[0][3]

        results_response = self._get(endpoint, params)
        record = self._wrap_payload(results_response, func_name, endpoint, params)
        return record
