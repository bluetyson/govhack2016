import psycopg2

#inputs:
#   industry: str containing one of the 19 authorotative industry categories
#output: str containing industry category for use in the survivability functions


def industry_converter(industry):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    query = "SELECT * FROM classificationdictionary2 WHERE app='" + str(industry) + "'"
    cur.execute(query)
    for line in cur.fetchall():
        return line[0]

    cur.close()
    conn.close()