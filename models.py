# coding: utf-8
from app import alchemy

Base = alchemy.make_declarative_base(alchemy.Model)
metadata = alchemy.Model.metadata


class QueryTable:
    """
    Custom class to extend the Model's class interface
    to Table, to enable easier querying.
    Shamelessly based on: https://stackoverflow.com/a/45362962
    """
    def __init__(self, *args, **kwargs):
        table = alchemy.Table(*args, **kwargs)
        super().__setattr__('_flask_sa_table', table)

    @property
    def query(self):
        return alchemy.session.query(self._flask_sa_table)

    def __getattr__(self, name):
        return getattr(self.__dict__['_flask_sa_table'], name)

    def __setattr__(self, name, value):
        return setattr(self._flask_sa_table, name, value)


t_east_conference_standings_by_day = QueryTable(
    'east_conference_standings_by_day', metadata,
    alchemy.Column('index', alchemy.BigInteger, index=True),
    alchemy.Column('TEAM_ID', alchemy.BigInteger),
    alchemy.Column('LEAGUE_ID', alchemy.Text),
    alchemy.Column('SEASON_ID', alchemy.Text),
    alchemy.Column('STANDINGSDATE', alchemy.Text),
    alchemy.Column('CONFERENCE', alchemy.Text),
    alchemy.Column('TEAM', alchemy.Text),
    alchemy.Column('G', alchemy.BigInteger),
    alchemy.Column('W', alchemy.BigInteger),
    alchemy.Column('L', alchemy.BigInteger),
    alchemy.Column('W_PCT', alchemy.Float(53)),
    alchemy.Column('HOME_RECORD', alchemy.Text),
    alchemy.Column('ROAD_RECORD', alchemy.Text)
)


t_last_meeting = QueryTable(
    'last_meeting', metadata,
    alchemy.Column('index', alchemy.BigInteger, index=True),
    alchemy.Column('GAME_ID', alchemy.Text),
    alchemy.Column('LAST_GAME_ID', alchemy.Text),
    alchemy.Column('LAST_GAME_DATE_EST', alchemy.Text),
    alchemy.Column('LAST_GAME_HOME_TEAM_ID', alchemy.BigInteger),
    alchemy.Column('LAST_GAME_HOME_TEAM_CITY', alchemy.Text),
    alchemy.Column('LAST_GAME_HOME_TEAM_NAME', alchemy.Text),
    alchemy.Column('LAST_GAME_HOME_TEAM_ABBREVIATION', alchemy.Text),
    alchemy.Column('LAST_GAME_HOME_TEAM_POINTS', alchemy.BigInteger),
    alchemy.Column('LAST_GAME_VISITOR_TEAM_ID', alchemy.BigInteger),
    alchemy.Column('LAST_GAME_VISITOR_TEAM_CITY', alchemy.Text),
    alchemy.Column('LAST_GAME_VISITOR_TEAM_NAME', alchemy.Text),
    alchemy.Column('LAST_GAME_VISITOR_TEAM_CITY1', alchemy.Text),
    alchemy.Column('LAST_GAME_VISITOR_TEAM_POINTS', alchemy.BigInteger)
)


t_line_score = QueryTable(
    'line_score', metadata,
    alchemy.Column('index', alchemy.BigInteger, index=True),
    alchemy.Column('GAME_DATE_EST_away', alchemy.Text),
    alchemy.Column('GAME_SEQUENCE', alchemy.BigInteger),
    alchemy.Column('GAME_ID_away', alchemy.Text),
    alchemy.Column('TEAM_ID_away', alchemy.BigInteger),
    alchemy.Column('TEAM_ABBREVIATION_away', alchemy.Text),
    alchemy.Column('TEAM_CITY_NAME_away', alchemy.Text),
    alchemy.Column('TEAM_NAME_away', alchemy.Text),
    alchemy.Column('TEAM_WINS_LOSSES_away', alchemy.Text),
    alchemy.Column('PTS_QTR1_away', alchemy.BigInteger),
    alchemy.Column('PTS_QTR2_away', alchemy.BigInteger),
    alchemy.Column('PTS_QTR3_away', alchemy.BigInteger),
    alchemy.Column('PTS_QTR4_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT1_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT2_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT3_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT4_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT5_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT6_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT7_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT8_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT9_away', alchemy.BigInteger),
    alchemy.Column('PTS_OT10_away', alchemy.BigInteger),
    alchemy.Column('PTS_away', alchemy.BigInteger),
    alchemy.Column('FG_PCT_away', alchemy.Float(53)),
    alchemy.Column('FT_PCT_away', alchemy.Float(53)),
    alchemy.Column('FG3_PCT_away', alchemy.Float(53)),
    alchemy.Column('AST_away', alchemy.BigInteger),
    alchemy.Column('REB_away', alchemy.BigInteger),
    alchemy.Column('TOV_away', alchemy.BigInteger),
    alchemy.Column('GAME_DATE_EST_home', alchemy.Text),
    alchemy.Column('GAME_ID_home', alchemy.Text),
    alchemy.Column('TEAM_ID_home', alchemy.BigInteger),
    alchemy.Column('TEAM_ABBREVIATION_home', alchemy.Text),
    alchemy.Column('TEAM_CITY_NAME_home', alchemy.Text),
    alchemy.Column('TEAM_NAME_home', alchemy.Text),
    alchemy.Column('TEAM_WINS_LOSSES_home', alchemy.Text),
    alchemy.Column('PTS_QTR1_home', alchemy.BigInteger),
    alchemy.Column('PTS_QTR2_home', alchemy.BigInteger),
    alchemy.Column('PTS_QTR3_home', alchemy.BigInteger),
    alchemy.Column('PTS_QTR4_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT1_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT2_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT3_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT4_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT5_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT6_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT7_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT8_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT9_home', alchemy.BigInteger),
    alchemy.Column('PTS_OT10_home', alchemy.BigInteger),
    alchemy.Column('PTS_home', alchemy.BigInteger),
    alchemy.Column('FG_PCT_home', alchemy.Float(53)),
    alchemy.Column('FT_PCT_home', alchemy.Float(53)),
    alchemy.Column('FG3_PCT_home', alchemy.Float(53)),
    alchemy.Column('AST_home', alchemy.BigInteger),
    alchemy.Column('REB_home', alchemy.BigInteger),
    alchemy.Column('TOV_home', alchemy.BigInteger)
)


class Monitor(Base):
    __tablename__ = 'monitor'

    id = alchemy.Column(alchemy.Integer, 
                        primary_key=True,
                        server_default=alchemy.text("nextval('monitor_id_seq'::regclass)"))
    date = alchemy.Column(alchemy.Date)
    item = alchemy.Column(alchemy.String)
    pre_offset = alchemy.Column(alchemy.Integer)
    post_offset = alchemy.Column(alchemy.Integer)
    size = alchemy.Column(alchemy.Integer)
    success = alchemy.Column(alchemy.Boolean)


t_series_standings = QueryTable(
    'series_standings', metadata,
    alchemy.Column('index', alchemy.BigInteger, index=True),
    alchemy.Column('GAME_ID', alchemy.Text),
    alchemy.Column('HOME_TEAM_ID', alchemy.BigInteger),
    alchemy.Column('VISITOR_TEAM_ID', alchemy.BigInteger),
    alchemy.Column('GAME_DATE_EST', alchemy.Text),
    alchemy.Column('HOME_TEAM_WINS', alchemy.BigInteger),
    alchemy.Column('HOME_TEAM_LOSSES', alchemy.BigInteger),
    alchemy.Column('SERIES_LEADER', alchemy.Text)
)


t_west_conference_standings_by_day = QueryTable(
    'west_conference_standings_by_day', metadata,
    alchemy.Column('index', alchemy.BigInteger, index=True),
    alchemy.Column('TEAM_ID', alchemy.BigInteger),
    alchemy.Column('LEAGUE_ID', alchemy.Text),
    alchemy.Column('SEASON_ID', alchemy.Text),
    alchemy.Column('STANDINGSDATE', alchemy.Text),
    alchemy.Column('CONFERENCE', alchemy.Text),
    alchemy.Column('TEAM', alchemy.Text),
    alchemy.Column('G', alchemy.BigInteger),
    alchemy.Column('W', alchemy.BigInteger),
    alchemy.Column('L', alchemy.BigInteger),
    alchemy.Column('W_PCT', alchemy.Float(53)),
    alchemy.Column('HOME_RECORD', alchemy.Text),
    alchemy.Column('ROAD_RECORD', alchemy.Text)
)
