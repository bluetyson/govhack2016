from flask import Flask, render_template

app = Flask(__name__)


# TODO: change hello world route
# @app.route('/')
# def hello_world():
#     return render_template('frontpage.html')

@app.route('/')
@app.route('/form')
def biz_form():
    return render_template('form.html')


@app.route('/result')
def biz_result():
    return render_template('result.html')

if __name__ == '__main__':
    app.run(app.run(host='0.0.0.0'))
