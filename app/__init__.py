from flask import Flask, render_template, current_app
from flask_bootstrap import Bootstrap
from datetime import datetime, date
from .config import *
import psycopg2


app = Flask(__name__)
bootstrap = Bootstrap(app)

runtime = []


@app.route("/")
def index():
    """Creates index.html root page with the initial data.
    """
    run_date = date.today()
    games, rows = get_games(run_date)
    return render_template("index.html", title="NBA Daily Scores",
                           games=games,
                           rows=rows,
                           run_date=str(run_date))


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
                      "WHERE away_game_date_est = ('{}'::DATE - '1 day'::INTERVAL);".format(table_names[0], run_date))
    data = db_cursor.fetchall()
    rows = db_cursor.rowcount
    return data, rows


if __name__ == "__main__":
    app.run(threaded=True)
