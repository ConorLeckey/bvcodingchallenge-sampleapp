from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper
from helpers.dashboard_card import DashboardCard

app = Flask(__name__)
stats_helper = StatsHelper()


@app.route('/')
def homepage():
    average_beer_rating = DashboardCard('Average Beer Rating', get_average_overall_rating())
    average_aroma_rating = DashboardCard('Average Aroma Rating', get_average_aroma_rating())

    cards = [average_beer_rating, average_aroma_rating]

    # HINT: Pass variables through to the HTML using Flask -
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    return render_template('index.html',
                           todays_date=datetime.now(),
                           cards=cards)


# HINT: This could be your first statistic!
def get_average_overall_rating():
    return str(round(stats_helper.caculate_ave_overall_rating(), 1)) + " / 5"


def get_average_aroma_rating():
    return str(round(stats_helper.caculate_ave_aroma_rating(), 1)) + ' / 5'
