import psycopg2
from datalogic import postcode_converter

#inputs:
#       postcode: 4-digit int
#output: dictionary specifying median age, median income, dependent children, education level, marital status, weekly rent, # cars, and internet connection type
# for the average citizen in that postcode


def average_person(postcode):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    output = {}

    SA_code = postcode_converter.postcode_converter(postcode, 2)
    income_query = "SELECT * FROM personalincome_sa2 WHERE field1='" + str(SA_code) + "'"
    cur.execute(income_query)
    for line in cur.fetchall():
        output["Median Age"] = int(line[4])
        output["Median Income"] = int(line[6])

    dependent_children_query = "SELECT * FROM dependend_kids_pcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(dependent_children_query)
    for line in cur.fetchall():
        output["dependent_children"] = (int(line[3]) + 2*int(line[4]) + 3*int(line[5]) + 4*int(line[6]) + 5*int(line[7]) + 6*int(line[8]) + int(line[9]) + 2*int(line[10]) + 3*int(line[11]) + 4*int(line[12]) + 5*int(line[13]) + 6*int(line[14])) / (int(line[-1]) - int(line[-2]))

    education_query = "SELECT * FROM education_postcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(education_query)
    for line in cur.fetchall():
        highest = line.index(str(max(list(map(int, line[4:9])))))
        if highest == 4:
            output["education"] = "Postgraduate Degree"
        elif highest == 5:
            output["education"] = "Graduate Diploma"
        elif highest == 6:
            output["education"] = "Bachelor Degree"
        elif highest == 7:
            output["education"] = "Diploma/Advanced Diploma"
        elif highest == 8:
            output["education"] = "Non-tertiary"

    marital_status_query = "SELECT * FROM marital_status_pcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(marital_status_query)
    for line in cur.fetchall():
        highest = line.index(str(max(list(map(int, line[2:-2])))))
        if highest == 2:
            output["marital_status"] = "Never married"
        elif highest == 3:
            output["marital_status"] = "Widowed"
        elif highest == 4:
            output["marital_status"] = "Divorced"
        elif highest == 5:
            output["marital_status"] = "Separated"
        elif highest == 6:
            output["marital_status"] = "Married"

    rent_query = "SELECT * FROM wkrent_pcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(rent_query)
    for line in cur.fetchall():
        highest = line.index(str(max(list(map(int, line[2:-3])))))
        if highest == 2:
            output["rent"] = "$0"
        elif highest == 3:
            output["rent"] = "$1-$74"
        else:
            output["rent"] = '$' + str(highest*25 - 25) + ' to $' + str(highest*25 - 1)

    cars_query = "SELECT * FROM ncars_pcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(cars_query)
    for line in cur.fetchall():
        output["cars"] = (int(line[3]) + 2*int(line[4]) + 3*int(line[5]) + 4*int(line[6])) / (int(line[-1]) - int(line[-2]) - int(line[-3]))

    internet_query = "SELECT * FROM marital_status_pcode WHERE postcode LIKE '%" + str(postcode) + "%'"
    cur.execute(internet_query)
    for line in cur.fetchall():
        highest = line.index(str(max(list(map(int, line[2:-3])))))
        if highest == 2:
            output["internet"] = "No Internet connection"
        elif highest == 3:
            output["internet"] = "Broadband connection"
        elif highest == 4:
            output["internet"] = "Dial-up connection"
        elif highest == 5:
            output["internet"] = "Other connection"

    cur.close()
    conn.close()

    return output
