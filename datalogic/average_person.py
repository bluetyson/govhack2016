import psycopg2
from datalogic import postcode_converter

#inputs:
#       postcode: 4-digit int
#output: dictionary specifying median age, median income and data for income quartiles, as follows...
# Q1: less than $21,400; Q2: $21400-$44940; Q3: $44941-$74999; Q4: $75000+

def average_person(postcode):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    SA_code = postcode_converter.postcode_converter(postcode, 2)

    query = "SELECT * FROM personalincome_sa2 WHERE field1='" + str(SA_code) + "'"


    cur.execute(query)
    for line in cur.fetchall():
        return {"Median Age": line[4], "Median Income": line[6], "Q1": line[16], "Q2": line[17], "Q3": line[18], "Q4": line[19]}

    cur.close()
    conn.close()