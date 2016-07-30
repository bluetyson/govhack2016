from flask import Flask, render_template
import os
from os import path

app = Flask(__name__)


#TODO: change hello world route
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



# additional files to check for reloader
extra_dirs = ['templates','static']
extra_files = extra_dirs[:]
for extra_dir in extra_dirs:
    for dirname, dirs, files in os.walk(extra_dir):
        for filename in files:
            filename = path.join(dirname, filename)
            if path.isfile(filename):
                extra_files.append(filename)


if __name__ == '__main__':
    app.run(use_reloader=True,extra_files=extra_files)
