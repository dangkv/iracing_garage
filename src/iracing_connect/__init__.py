import logging

from iracing_connect.transport import iRacingConnectTransport
from iracing_connect.league.league_client import LeagueClient
from iracing_connect.results.results_client import ResultsClient
from iracing_connect.stats.stats_client import StatsClient
from iracing_connect.time_attack.time_attack_client import TimeAttackClient
from iracing_connect.track.track_client import TrackClient


parent_logger = logging.getLogger("iracing_connect")
parent_logger.setLevel(logging.WARNING)


class iRacingConnect:

    def __init__(self, username, password):
        self.logger = parent_logger
        self.transport = iRacingConnectTransport(
            username=username, password=password, logger=self.logger
        )

        self.league = LeagueClient(self.transport, self.logger)
        self.results = ResultsClient(self.transport, self.logger)
        self.stats = StatsClient(self.transport, self.logger)
        self.time_attack = TimeAttackClient(self.transport, self.logger)
        self.track = TrackClient(self.transport, self.logger)
