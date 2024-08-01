import logging
import json
import requests
import iracing_garage.endpoints
import iracing_garage.helpers
import iracing_garage.transport


class iRacingGarageClient:
    def __init__(self, transport, logger):
        self.logger = logger
        self.transport = transport

    def _get(
        self, url: str, api_group: str, func_name: str, params=None
    ) -> dict:
        response = self.transport.get(url=url, params=params)
        response_json = response.json()

        if response.status_code != requests.codes.OK:
            self.logger.debug(
                f"Error retrieving {api_group} - {func_name}: {self.transport.dump_response(response)}"
            )
            raise Exception(
                f"Error retrieving {api_group} - {func_name}: {response.text}"
            )
        # TODO:
        # payload can either be a dict or a list
        # payload can be a dict without link

        api_link = response_json.get("link")
        api_data_json = self.transport.get(url=api_link).json()
        return api_data_json

    def _get_chunks(self, payload):
        chunks = []
        chunk_info = payload.get("chunk_info")
        chunk_download_url = chunk_info.get("base_download_url")
        chunk_file_names = [x for x in chunk_info.get("chunk_file_names")]

        for chunk_file_name in chunk_file_names:
            full_url = chunk_download_url + chunk_file_name
            response = self.transport.get(full_url).json()
            chunks.extend(response)

        return chunks

    def _get_entry(
        self, url: str, api_group: str, func_name: str, params=None
    ) -> dict:
        response = self.transport.get(url=url, params=params)

        if response.status_code != requests.codes.OK:
            self.logger.debug(
                f"Error retrieving {api_group} - {func_name}: {self.transport.dump_response(response)}"
            )
            raise Exception(
                f"Error retrieving {api_group} - {func_name}: {response.text}"
            )

        gateway_response_dict = json.loads(response.text)
        api_link = gateway_response_dict.get("link")

        # TODO: raise if fails
        response_data = self.transport.get(url=api_link)
        return response_data.json()

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
