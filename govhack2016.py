from flask import Flask, render_template
import json
from datalogic import competition

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


@app.route('/query/<string:querytype>', methods=['POST'])
def query(querytype):
    if querytype == 'competition':
        return {}
    if querytype == 'avgperson':
        return {}

@app.route('/test/query/<string:querytype>', methods=['GET'])
def query_test(querytype):
    querytype = querytype.lower
    # val = None
    if querytype == 'competition':
        val = json.dumps(competition.get_competition("Agriculture, Forestry and Fishing", 101011001))
    elif querytype == 'avgperson':
        val = json.dumps(competition.get_competition("Agriculture, Forestry and Fishing", 101011001))
    elif querytype == 'laboravail':
        val = json.dumps(competition.get_competition("Agriculture, Forestry and Fishing", 101011001))
    else:
        val = "Error"
    return val

if __name__ == '__main__':
    app.run(debug=True)
