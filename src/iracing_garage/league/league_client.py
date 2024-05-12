import inspect

import iracing_garage.endpoints as endpoints
from iracing_garage.client import iRacingGarageClient


class LeagueClient(iRacingGarageClient):
    def __init__(self, transport, logger):
        super().__init__(transport, logger)
        self.api_group = "league"

    def cust_league_sessions(
        self, mine: bool = None, package_id: int = None
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_CUST_LEAGUE_SESSIONS
        func_name = inspect.stack()[0][3]

        params = {"mine": mine, "package_id": package_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def directory(
        self,
        search: str = None,
        tag: str = None,
        restrict_to_member: bool = None,
        restrict_to_recruiting: bool = None,
        restrict_to_friends: bool = None,
        restrict_to_watched: bool = None,
        minimum_roster_count: int = None,
        maximum_roster_count: int = None,
        lowerbound: int = None,
        upperbound: int = None,
        sort: str = None,
        order: str = None,
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_DIRECTORY
        func_name = inspect.stack()[0][3]

        params = {
            "search": search,
            "tag": tag,
            "restrict_to_member": restrict_to_member,
            "restrict_to_recruiting": restrict_to_recruiting,
            "restrict_to_friends": restrict_to_friends,
            "restrict_to_watched": restrict_to_watched,
            "minimum_roster_count": minimum_roster_count,
            "maximum_roster_count": maximum_roster_count,
            "lowerbound": lowerbound,
            "upperbound": upperbound,
            "sort": sort,
            "order": order,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def get(self, league_id: int, include_licenses: bool = None) -> dict:

        endpoint = endpoints.URL_LEAGUE_GET
        func_name = inspect.stack()[0][3]

        params = {"league_id": league_id, "include_licenses": include_licenses}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def get_points_systems(
        self, league_id: int, season_id: int = None
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_GET_POINTS_SYSTEMS
        func_name = inspect.stack()[0][3]

        params = {"league_id": league_id, "season_id": season_id}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def membership(
        self, cust_id: int = None, include_league: bool = None
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_MEMBERSHIP
        func_name = inspect.stack()[0][3]

        params = {"cust_id": cust_id, "include_league": include_league}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def roster(self, league_id: int, include_licenses: bool = None) -> dict:

        endpoint = endpoints.URL_LEAGUE_ROSTER
        func_name = inspect.stack()[0][3]

        params = {"league_id": league_id, "include_licenses": include_licenses}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def seasons(self, league_id: int, retired: bool = None) -> dict:

        endpoint = endpoints.URL_LEAGUE_SEASONS
        func_name = inspect.stack()[0][3]

        params = {"league_id": league_id, "retired": retired}

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_standings(
        self,
        league_id: int,
        season_id: int,
        car_class_id: int = None,
        car_id: int = None,
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_SEASON_STANDINGS
        func_name = inspect.stack()[0][3]

        params = {
            "league_id": league_id,
            "season_id": season_id,
            "car_class_id": car_class_id,
            "car_id": car_id,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )

    def season_sessions(
        self, league_id: int, season_id: int, results_only: bool = None
    ) -> dict:

        endpoint = endpoints.URL_LEAGUE_SEASON_SESSIONS
        func_name = inspect.stack()[0][3]

        params = {
            "league_id": league_id,
            "season_id": season_id,
            "results_only": results_only,
        }

        return self._get(
            url=endpoint,
            api_group=self.api_group,
            func_name=func_name,
            params=params,
        )
