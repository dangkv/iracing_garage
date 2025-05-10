import logging

from iracing_garage.transport import iRacingGarageTransport

from iracing_garage.api_clients import ResultsClient
from iracing_garage.api_clients import CarClient
from iracing_garage.api_clients import CarClassClient
from iracing_garage.api_clients import ConstantsClient
from iracing_garage.api_clients import HostedClient
from iracing_garage.api_clients import LeagueClient
from iracing_garage.api_clients import LookupClient
from iracing_garage.api_clients import MemberClient
from iracing_garage.api_clients import SeasonClient
from iracing_garage.api_clients import SeriesClient
from iracing_garage.api_clients import StatsClient
from iracing_garage.api_clients import TeamClient
from iracing_garage.api_clients import TimeAttackClient
from iracing_garage.api_clients import TrackClient


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
