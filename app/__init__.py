from flask import Flask, render_template, current_app, url_for, redirect
from datetime import datetime, date
from flask_wtf.csrf import CSRFProtect
from app.forms import DateForm
from .config import *
import psycopg2


app = Flask(__name__)
csrf = CSRFProtect(app)
app.config.from_object(config[os.environ.get('FLASK_ENV')])
runtime = []


@app.route("/")
def index():
    """Creates games.html root page with the initial data.
    """
    d = datetime.today()
    ts = str(datetime.timestamp(d))
    fd = d.strftime("%d-%m-%Y")
    games, rows = get_games(d)
    return render_template('games.html', games=games, rows=rows, date=fd)


@app.route("/games/NaN")
def games_nan():
    return redirect(url_for('index'))


@app.route("/games/<timestamp>")
def games(timestamp):
    date = datetime.fromtimestamp(int(timestamp)/1000.0)
    formatted_date = date.strftime("%d-%m-%Y")
    games,rows = get_games(date)
    return render_template("games.html", games=games, rows=rows, date=formatted_date)


def get_games(run_date=None):
    """Get Data Frame of games for today (dates set for dev and debug.
    Args:
        date : datetime object for the day we want games from
    Return:
        games : Data Frame object of games played at a given day
    """

    db_url = config[os.environ['FLASK_ENV']].db_url
    table_names = config[os.environ['FLASK_ENV']].table_names
    ssl = config[os.environ['FLASK_ENV']].sslmode

    # use the db url to connect to postgresql db
    conn = psycopg2.connect(db_url, sslmode=ssl)
    db_cursor = conn.cursor()

    # execute queries
    db_cursor.execute("SELECT * FROM {} "
                      "WHERE away_game_date_est = ('{}'::DATE - '2 day'::INTERVAL);".format(table_names[0], run_date))
    data = db_cursor.fetchall()
    rows = db_cursor.rowcount
    return data, rows
