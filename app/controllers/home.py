# -*- coding: utf-8 -*-
from flask import Blueprint, render_template, redirect, url_for, request
import requests

blueprint = Blueprint('home', __name__)


@blueprint.route('/results', methods=['POST'])
def results():
    veggies = int(request.form['one'] or 0)
    fruits = int(request.form['two'] or 0)
    chicken = int(request.form['three'] or 0)
    beef = int(request.form['four'] or 0)
    milk = int(request.form['five'] or 0)
    cheese = int(request.form['six'] or 0)
    bagels = int(request.form['seven'] or 0)
    bread = int(request.form['eight'] or 0)

    vegTotal = veggies * .67
    fruitTotal = fruits * .71
    chickenTotal = chicken * 1.54
    beefTotal = beef * 4.08
    milkTotal = milk * 3.45
    cheeseTotal = cheese * 4.27
    breadTotal = bread * 2.08

    total = vegTotal + fruitTotal + chickenTotal + beefTotal + milkTotal + cheeseTotal + breadTotal

    return render_template('home/result.html', total=total)


def input_info(vegetable, fruits, beef, chicken, milk, cheese, bagel, bread):
    input_values = [vegetable, fruits, beef, chicken, milk, cheese, bagel, bread]
    return

@blueprint.route('/')
def index():
    # Search GitHub's repositories for requests
    response = requests.get(
        'https://api.github.com/search/repositories',
        params={'q': 'requests+language:python'},
    )

    # Inspect some attributes of the `requests` repository
    json_response = response.json()
    repository = json_response['items'][0]

    return render_template('home/index.html', helpfuldata=repository["description"])


@blueprint.route('/result')
def result():
    return render_template('home/result.html')


@blueprint.route('/result')
def total():
    global total_price
    if request.method == 'POST':
        input_info(request.form['vegetable'], request.form['fruits'], request.form['beef'], request.form['chicken'], request.form['milk'], request.form['cheese'], request.form['bagel'], request.form['bread'])
        total_price = input_values[0]*0.67 + input_values[1]*0.71+input_values[2]*1.54 + input_values[3] * 4.08+input_values[4]*3.45+input_values[5]*4.27+input_values[6]*0.35 + input_values[7]*2.08
    return render_template("home/result.html", total=total_price)



