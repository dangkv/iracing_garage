import inspect
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
            except:  # noqa
                # TODO: build exceptions
                msg = f"API extraction error at {chunk_file_name}, {i}/{len(chunk_file_names)}"  # noqa
                pass

            chunks.append(response)

        print()
        return chunks

    def _get_constants(self):
        pass  # TODO: constants does not have a gateway

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
