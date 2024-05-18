import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class ResultsClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "results"

    def get(self, subsession_id: int, include_licenses: bool = None) -> dict:

        endpoint = endpoints.URL_RESULTS_GET
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "include_licenses": include_licenses,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def event_log(self, subsession_id: int, simsession_number: int) -> dict:

        endpoint = endpoints.URL_RESULTS_EVENT_LOG
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def lap_chart_data(
        self, subsession_id: int, simsession_number: int
    ) -> dict:

        endpoint = endpoints.URL_RESULTS_LAP_CHART_DATA
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def lap_data(
        self,
        subsession_id: int,
        simsession_number: int,
        cust_id: int = None,
        team_id: int = None,
    ) -> dict:

        endpoint = endpoints.URL_RESULTS_LAP_DATA
        func_name = inspect.stack()[0][3]

        params = {
            "subsession_id": subsession_id,
            "simsession_number": simsession_number,
            "cust_id": cust_id,
            "team_id": team_id,
        }

        response = self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

        chunks = self._get_chunks(response)
        response["chunks"] = chunks

        return response

    def search_hosted(
        self,
        start_range_begin: str = None,
        start_range_end: str = None,
        finish_range_begin: str = None,
        finish_range_end: str = None,
        cust_id: int = None,
        team_id: int = None,
        host_cust_id: int = None,
        session_name: str = None,
        league_id: int = None,
        league_season_id: int = None,
        car_id: int = None,
        track_id: int = None,
        category_ids: int = None,
    ) -> dict:

        endpoint = endpoints.URL_RESULTS_SEARCH_HOSTED
        func_name = inspect.stack()[0][3]

        params = {
            "start_range_begin": start_range_begin,
            "start_range_end": start_range_end,
            "finish_range_begin": finish_range_begin,
            "finish_range_end": finish_range_end,
            "cust_id": cust_id,
            "team_id": team_id,
            "host_cust_id": host_cust_id,
            "session_name": session_name,
            "league_id": league_id,
            "league_season_id": league_season_id,
            "car_id": car_id,
            "track_id": track_id,
            "category_ids": category_ids,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def search_series(
        self,
        season_year: int = None,
        season_quarter: int = None,
        start_range_begin: str = None,
        start_range_end: str = None,
        finish_range_begin: str = None,
        finish_range_end: str = None,
        cust_id: int = None,
        team_id: int = None,
        series_id: int = None,
        race_week_num: int = None,
        official_only: bool = None,
        event_types: int = None,
        category_ids: int = None,
    ) -> dict:

        endpoint = endpoints.URL_RESULTS_SEARCH_SERIES
        func_name = inspect.stack()[0][3]

        params = {
            "season_year": season_year,
            "season_quarter": season_quarter,
            "start_range_begin": start_range_begin,
            "start_range_end": start_range_end,
            "finish_range_begin": finish_range_begin,
            "finish_range_end": finish_range_end,
            "cust_id": cust_id,
            "team_id": team_id,
            "series_id": series_id,
            "race_week_num": race_week_num,
            "official_only": official_only,
            "event_types": event_types,
            "category_ids": category_ids,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_results(
        self, season_id: int, event_type: int = None, race_week_num: int = None
    ) -> dict:

        endpoint = endpoints.URL_RESULTS_SEASON_RESULTS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "event_type": event_type,
            "race_week_num": race_week_num,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
