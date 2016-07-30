import psycopg2
from datalogic import postcode_converter

# returns {'DATE': COUNT, 'DATE': COUNT, ...}
# where DATE is in format Sep-14
# and count is an int


def labour_availability(postcode):

    SA_code = postcode_converter.postcode_converter(postcode, 3, "name")

    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    query = "SELECT * FROM job_services WHERE field_1='" + str(SA_code) + "'"

    print(query)
    cur.execute(query)
    count_by_date = {}
    for line in cur.fetchall():
        if line[3] in count_by_date.keys():
            count_by_date[line[3]] += int(line[-1])
        else:
            count_by_date[line[3]] = int(line[-1])

    cur.close()
    conn.close()

    return str(count_by_date)