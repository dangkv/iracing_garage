import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class StatsClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "stats"

    def member_bests(self, cust_id: int = None, car_id: int = None) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_BESTS
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id, "car_id": car_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_career(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_CAREER
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_division(self, season_id: int, event_type: int) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_DIVISION
        func_name = inspect.stack()[0][3]

        params = {"season_id": season_id, "event_type": event_type}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_recap(
        self, cust_id: int = None, year: int = None, season: int = None
    ) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_RECAP
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id, "year": year, "season": season}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_recent_races(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_RECENT_RACES
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_summary(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_SUMMARY
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def member_yearly(self, cust_id: int = None) -> dict:

        endpoint = endpoints.URL_STATS_MEMBER_YEARLY
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_driver_standings(
        self,
        season_id: int,
        car_class_id: int,
        club_id: int = None,
        division: int = None,
        race_week_num: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_DRIVER_STANDINGS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "club_id": club_id,
            "division": division,
            "race_week_num": race_week_num,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_supersession_standings(
        self,
        season_id: int,
        car_class_id: int,
        club_id: int = None,
        division: int = None,
        race_week_num: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_SUPERSESSION_STANDINGS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "club_id": club_id,
            "division": division,
            "race_week_num": race_week_num,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_team_standings(
        self, season_id: int, car_class_id: int, race_week_num: int = None
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_TEAM_STANDINGS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "race_week_num": race_week_num,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_tt_standings(
        self,
        season_id: int,
        car_class_id: int,
        club_id: int = None,
        division: int = None,
        race_week_num: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_TT_STANDINGS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "club_id": club_id,
            "division": division,
            "race_week_num": race_week_num,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_tt_results(
        self,
        season_id: int,
        car_class_id: int,
        race_week_num: int,
        club_id: int = None,
        division: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_TT_RESULTS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "race_week_num": race_week_num,
            "club_id": club_id,
            "division": division,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_qualify_results(
        self,
        season_id: int,
        car_class_id: int,
        race_week_num: int,
        club_id: int = None,
        division: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_SEASON_QUALIFY_RESULTS
        func_name = inspect.stack()[0][3]

        params = {
            "season_id": season_id,
            "car_class_id": car_class_id,
            "race_week_num": race_week_num,
            "club_id": club_id,
            "division": division,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def world_records(
        self,
        car_id: int,
        track_id: int,
        season_year: int = None,
        season_quarter: int = None,
    ) -> dict:

        endpoint = endpoints.URL_STATS_WORLD_RECORDS
        func_name = inspect.stack()[0][3]

        params = {
            "car_id": car_id,
            "track_id": track_id,
            "season_year": season_year,
            "season_quarter": season_quarter,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
