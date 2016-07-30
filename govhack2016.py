from flask import Flask, render_template,request
import json
from datalogic import competition, average_person, labour_availability


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('frontpage.html')


@app.route('/form')
def biz_form():
    return render_template('form.html')


@app.route('/result')
def biz_result():
    return render_template('result.html')

@app.route('/about')
def biz_about():
    return render_template('about.html')


@app.route('/query/<urlquery>', methods=['POST'])
def query(urlquery):
    urlquery = urlquery.lower()
    data = request.get_json()

    if data == '':
        val = json.dumps("No data posted")
    if urlquery == 'competition':
        val = json.dumps(competition.get_competition(data.industry, data.sa_code))
    elif urlquery == "avgperson":
        val = json.dumps(average_person.average_person(data.postcode))
    elif urlquery == "labouravail":
        val = json.dumps(labour_availability.labour_availability(data.postcode))
    else:
        val = "Error"

    return val


@app.route('/test/query/<urlquery>', methods=['GET'])
def query_test(urlquery):
    urlquery = urlquery.lower()

    if urlquery == "competition":
        val = json.dumps(competition.get_competition("Agriculture, Forestry and Fishing", 101011001))
    elif urlquery == "avgperson":
        val = json.dumps(average_person.average_person(2600))
    elif urlquery == "labouravail":
        val = json.dumps(labour_availability.labour_availability(5052))
    else:
        val = "Error"
    return val


if __name__ == '__main__':
    app.run(debug=True)
