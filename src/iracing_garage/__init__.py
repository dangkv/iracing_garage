import logging

from iracing_garage.transport import iRacingGarageTransport
from iracing_garage.league.league_client import LeagueClient
from iracing_garage.results.results_client import ResultsClient
from iracing_garage.stats.stats_client import StatsClient
from iracing_garage.time_attack.time_attack_client import TimeAttackClient
from iracing_garage.track.track_client import TrackClient


parent_logger = logging.getLogger("iracing_garage")
parent_logger.setLevel(logging.WARNING)


class iRacingGarage:

    def __init__(self, username, password):
        self.logger = parent_logger
        self.transport = iRacingGarageTransport(
            username=username, password=password, logger=self.logger
        )

        self.league = LeagueClient(self.transport, self.logger)
        self.results = ResultsClient(self.transport, self.logger)
        self.stats = StatsClient(self.transport, self.logger)
        self.time_attack = TimeAttackClient(self.transport, self.logger)
        self.track = TrackClient(self.transport, self.logger)
