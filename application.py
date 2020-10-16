from flask import Flask
from flask import render_template
from datetime import datetime
from helpers.stats_helper import StatsHelper
from helpers.dashboard_card import DashboardCard
from helpers.dashboard_list import DashboardList

app = Flask(__name__)
stats_helper = StatsHelper()


@app.route('/')
def homepage():
    # CARDS
    average_beer_rating = DashboardCard('Average Beer Rating', get_average_overall_rating())
    average_aroma_rating = DashboardCard('Average Aroma Rating', get_average_aroma_rating())

    cards = [average_beer_rating, average_aroma_rating]

    # LISTS
    average_beer_rating_list = DashboardList('Top Beers by Rating', ['Beer Name', 'Average Rating'], get_average_overall_rating_list())

    lists = [average_beer_rating_list]

    # HINT: Pass variables through to the HTML using Flask -
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#rendering-templates
    return render_template('index.html',
                           todays_date=datetime.now(),
                           cards=cards,
                           lists=lists)


# HINT: This could be your first statistic!
def get_average_overall_rating():
    return str(round(stats_helper.caculate_ave_overall_rating(), 1)) + ' / 5'


def get_average_aroma_rating():
    return str(round(stats_helper.caculate_ave_aroma_rating(), 1)) + ' / 5'


def get_average_overall_rating_list():
    all_ratings = stats_helper.get_ordered_by_ave_overall_rating()
    ratings_arrays = {}
    averaged_ratings = {}

    for rating in all_ratings:
        # print(rating)
        if rating[0] not in ratings_arrays:
            ratings_arrays[rating[0]] = [rating[1]]
        else:
            ratings_arrays[rating[0]].append(rating[1])

    for rating in all_ratings:
        # if rating[0] in averaged_ratings:
        #     break

        total = 0.0
        # print(ratings_arrays[rating[0]])
        for x in range(len(ratings_arrays[rating[0]])):
            total += ratings_arrays[rating[0]][x]
        averaged_ratings[rating[0]] = round(total / len(ratings_arrays[rating[0]]), 1)
    print(averaged_ratings)

    return averaged_ratings
