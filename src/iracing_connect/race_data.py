import client
import inspect
import endpoints
import requests


class RaceData(client):
    def __init__(self, client):
        super().__init__(client)
        self.api_group = inspect.stack().f_locals["self"].__class__.__name__

    def lap_data(self, subsession_id: int):
        endpoint = endpoints.URL_LAP_DATA
        func_name = inspect.stack()[0][3]
        full_session = []

        # The main event is 0; the preceding event is -1, and so on
        for simsession_number in [0, -1, -2]:

            params = {
                "subsession_id": subsession_id,
                "simsession_number": simsession_number,
            }

            results_response = self._build_requests(endpoint, params)
            record = self._wrap_payload(results_response, func_name, endpoint, params)

            full_session.append(record)

        return full_session
