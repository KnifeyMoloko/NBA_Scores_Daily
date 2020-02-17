from flask import Flask, render_template, url_for, redirect
from datetime import datetime, timedelta
from .config import *
from flask_sqlalchemy import SQLAlchemy


# app initiation
app = Flask(__name__)
app.config.from_object(config[os.environ.get('FLASK_ENV')])
alchemy = SQLAlchemy(app=app)


# model imports need to be made after app is initialized
from models import t_line_score, t_east_conference_standings_by_day, \
    t_west_conference_standings_by_day


# route definitions
@app.route("/")
def index():
    """
    Creates games.html root page with the initial data.
    """
    today = datetime.today()
    yesterday = today - timedelta(days=1)
    tformat = "%d-%m-%Y"
    fd = yesterday.strftime(tformat)

    # get games
    games, rows, team_ids = get_games(tformat)

    # check if there were any games played last evening
    if rows == 0:
        return render_template('nogames.html', date=fd)
    else:
        return render_template('games.html', games=games, rows=rows,
                               date=fd, team_ids=team_ids)


@app.route("/games/NaN")
def games_nan():
    return redirect(url_for('index'))


@app.route("/games/<timestamp>")
def games(timestamp):
    # set date
    date = datetime.fromtimestamp(int(timestamp)/1000.0)
    tformat = "%Y-%m-%d"
    formatted_date = date.strftime(tformat)

    # get games
    games, rows, team_ids = get_games(formatted_date)

    if rows == 0:
        return render_template('nogames.html', date=formatted_date)
    else:
        return render_template('games.html', games=games, rows=rows,
                               date=formatted_date, team_ids=team_ids)


@app.route("/standings/<conference>")
def standings(conference):
    # get standings
    date_format = "%m/%d/%Y"
    yesterday = datetime.today() - timedelta(days=1)
    standings_date = yesterday.strftime(date_format)
    standings = get_standings(standings_date="02/08/2020")

    # dates need to be formatted for the date picker object
    return render_template('standings.html',
                           standings=standings,
                           conference=conference,
                           date=standings['date'].strftime("%d-%m-%Y"))


# helper functions
def get_games(games_date: str):
    """
    Get Data Frame of games for a given date.
    :param games_date: string representation for the date that the
    games should be retrieved for
    :return: data, rows, team_ids triplet
    """
    # config constants
    db_formatted_date = games_date + "T00:00:00"
    print(db_formatted_date)

    # extract data
    data = t_line_score.query.filter_by(GAME_DATE_EST_away=db_formatted_date).all()
    rows = len(data)

    # extract team ids from the data for logo discovery
    team_ids = [(str(x[4]), str(x[32])) for x in data]
    return data, rows, team_ids


def get_standings(standings_date: str):
    """
    Retrieve the standings table for a given date and conference.

    :param standings_date: string representation of the date for
    which the standings need to be retrieved
    :return:
    """
    # get config constants
    east = t_east_conference_standings_by_day.query.filter_by(
        STANDINGSDATE=standings_date).all()
    west = t_west_conference_standings_by_day.query.filter_by(
        STANDINGSDATE=standings_date).all()
    return {'east': east,
            'west': west,
            'date': datetime.strptime(standings_date, "%m/%d/%Y")
            }
