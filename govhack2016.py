from flask import Flask, render_template
import os
from os import path

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


@app.route('/query/<string:type>',methods=['POST'])
def query(type):
    if type == 'competition':
        return 'FRODO BAGGINSSSSS'#competition_algorithm()
    if type == 'avgperson':
        return {}


if __name__ == '__main__':
    app.run(debug=True)
