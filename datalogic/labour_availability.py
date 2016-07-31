import psycopg2
from datalogic import postcode_converter

# returns {'DATE': COUNT, 'DATE': COUNT, ...}
# where DATE is in format Sep-14
# and count is an int


def labour_availability(postcode):

    query = "SELECT * FROM looking_for_work WHERE postcode LIKE '%" + str(postcode) + "%'"
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()
    cur.execute(query)

    val = None

    for line in cur.fetchall():
        val = {"Looking for full-time work": line[1], "Looking for part-time work": line[2]}

    cur.close()
    conn.close()
    return val