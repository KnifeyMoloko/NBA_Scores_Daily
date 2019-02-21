import os


class Config:
    db_url = None
    table_names = []
    sslmode = None


class ProductionConfig(Config):
    db_url = os.environ.get('DATABASE_URL')
    table_names = ["line_score", "series_standing", "last_meeting",
                    "east_conference_standings_by_day",
                    "west_conference_standings_by_day"
                    ]
    sslmode = 'require'


class DevelopmentConfig(Config):
    db_url = os.environ.get('DEV_DATABASE_URL')
    table_names = ['nba1819_line_score',
                   'nba1819_series_standing',
                   'nba1819_last_meeting',
                   'nba1819_east_conference_standings_by_day',
                   'nba1819_west_conference_standings_by_day'
                   ]


class TestingConfig(Config):
    db_url = os.environ.get('TEST_DATABASE_URL')
    table_names = []


config = {'production': ProductionConfig,
          'development': DevelopmentConfig,
          'testing': TestingConfig}
