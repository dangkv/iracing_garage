import logging

from iracing_garage.transport import iRacingGarageTransport

from iracing_garage.car.car_client import CarClient
from iracing_garage.carclass.carclass_client import CarClassClient
from iracing_garage.constants.constants_client import ConstantsClient
from iracing_garage.hosted.hosted_client import HostedClient
from iracing_garage.league.league_client import LeagueClient
from iracing_garage.lookup.lookup_client import LookupClient
from iracing_garage.member.member_client import MemberClient
from iracing_garage.results.results_client import ResultsClient
from iracing_garage.season.season_client import SeasonClient
from iracing_garage.series.series_client import SeriesClient
from iracing_garage.stats.stats_client import StatsClient
from iracing_garage.team.team_client import TeamClient
from iracing_garage.time_attack.time_attack_client import TimeAttackClient
from iracing_garage.track.track_client import TrackClient

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s (Line :%(lineno)d [%(filename)s])",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
parent_logger = logging.getLogger("iracing_garage")


class iRacingGarage:
    def __init__(self, username, password):
        self.logger = parent_logger

        self.transport = iRacingGarageTransport(
            username=username, password=password, logger=self.logger
        )

        self.car = CarClient(self.transport, self.logger)
        self.carclass = CarClassClient(self.transport, self.logger)
        self.constants = ConstantsClient(self.transport, self.logger)
        self.hosted = HostedClient(self.transport, self.logger)
        self.league = LeagueClient(self.transport, self.logger)
        self.lookup = LookupClient(self.transport, self.logger)
        self.member = MemberClient(self.transport, self.logger)
        self.results = ResultsClient(self.transport, self.logger)
        self.season = SeasonClient(self.transport, self.logger)
        self.series = SeriesClient(self.transport, self.logger)
        self.stats = StatsClient(self.transport, self.logger)
        self.team = TeamClient(self.transport, self.logger)
        self.time_attack = TimeAttackClient(self.transport, self.logger)
        self.track = TrackClient(self.transport, self.logger)
