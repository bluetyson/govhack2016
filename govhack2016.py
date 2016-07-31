from flask import Flask, render_template,request
import json
from datalogic import competition, average_person, labour_availability, survivability, postcode_converter, industry_converter


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
    data = request.get_json(force=True)

    if data == '':
        val = json.dumps({"Error": "No data sent"})
    if urlquery == 'competition':
        # returns json {Year: [TotalNumOfBusiness, EmployeesInIndustryBySaCode], ...}
        val = json.dumps(competition.get_competition(data['industry'],
                                                     postcode_converter.postcode_converter(data['postcode'])
                                                     ))
    elif urlquery == "avgperson":
        # returns:
        # {
        #     "cars": Long,
        #     "marital_status": String,
        #     "internet": String,
        #     "education": String,
        #     "Median Income": Int,
        #     "rent": String,
        #     "dependent_children": Long,
        #     "Median Age": Int
        # }
        val = json.dumps(average_person.average_person(data['postcode']))
    elif urlquery == "labouravail":
        # returns json {DateOfCount: LaborAvailNum, ...}
        val = json.dumps(labour_availability.labour_availability(data['postcode']))

    elif urlquery == "survivability":
        # returns
        #      {"survival_by_employee":
        #          SurvivalYears: SurvivalPercent,
        #             .....
        #       "business_survival":
        #             YearsInBusiness: PercentageStillInBusiness,
        #             ....
        #       }
        #
        val = json.dumps(survivability.survivability(industry_converter.industry_converter(data['industry']),
                                                     data['state'],
                                                     data['employees'],
                                                     data['turnover']))
    else:
        val = json.dumps({"Error": "Not a valid url query"})

    return val


@app.route('/test/query/<urlquery>', methods=['GET'])
def query_test(urlquery):
    urlquery = urlquery.lower()

    if urlquery == '':
        val = json.dumps({"Error": "Not a valid url query"})
    if urlquery == "competition":
        val = json.dumps(competition.get_competition("Mining", 2000, 20))

    elif urlquery == "avgperson":
        val = json.dumps(average_person.average_person(2600))
    elif urlquery == "labouravail":
        val = json.dumps(labour_availability.labour_availability(2600))
    elif urlquery == "survivability":
        val = json.dumps(survivability.survivability('Agriculture, Forestry and Fishing', 'ACT', 23, 898))
    else:
        val = json.dumps({"Error": "No data sent"})
    return val

    # Valid Industries;
    # Agriculture, Forestry and Fishing
    # Mining
    # Manufacturing
    # Electricity, Gas, Water and Waste Services
    # Construction
    # Wholesale Trade
    # Retail Trade
    # Accommodation and Food Services
    # Transport, Postal and Warehousing
    # Information Media and Telecommunications
    # Financial and Insurance Services
    # Rental, Hiring and Real Estate Services
    # Professional, Scientific and Technical Services
    # Administrative and Support Services
    # Public Administration and Safety
    # Education and Training
    # Health Care and Social Assistance
    # Arts and Recreation Services
    # Other Services
    # Unknown
@app.route("/test/postcode/<urlquery>", methods=['GET'])
def postcode_conv(urlquery):
    return json.dumps(postcode_converter.postcode_converter(urlquery, 2, "num"))

@app.route("/test/industryconv/<urlquery>", methods=['GET'])
def industry_conv(urlquery):
    return json.dumps(industry_converter.industry_converter(urlquery))

if __name__ == '__main__':
    app.run(debug=True)



