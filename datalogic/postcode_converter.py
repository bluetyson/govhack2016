import psycopg2

# inputs:
#       postcode: 4-digit postcode in string or number
#       SA_number: an int, either 2, 3 or 4, specifying which SA output is required
#       num_or_name: a string, either "num" or "name", specifying the type of output required
# output: either an int containing the SA number or a string containing the SA name, as requested


def postcode_converter(postcode, SA_number, num_or_name="num"):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    if num_or_name == "num":
        query = "SELECT sa" \
                + str(SA_number) \
                + "_code FROM postcode_sa" \
                + str(SA_number) \
                + " WHERE postcode='" \
                + str(postcode) + "'"
    else:
        query = "SELECT sa" \
                + str(SA_number) \
                + "_name FROM postcode_sa" \
                + str(SA_number) \
                + " WHERE postcode='" \
                + str(postcode) + "'"
    cur.execute(query)
    for line in cur.fetchall():
        return line[0]
