import psycopg2
from datalogic import postcode_converter

# returns [TOTAL 2014, TOTAL 2013, TOTAL 2012, X Employees 2014, X Employees 2013, X Employees 2012] where X is the stated number of employees, if given
# If employees not specified, will only return [TOTAL 2014, TOTAL 2013, TOTAL 2012]

# requires pre prossesing for SA2 code & industry
def get_competition(industry, postcode, employees=0):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    SA_code = postcode_converter.postcode_converter(postcode, 3)

    if SA_code is None or industry is None:
        return None

    query = "SELECT * FROM business_employee_counts WHERE field_1='" + industry + "' AND field_2='" + str(SA_code) + "'"

    cur.execute(query)
    something = []
    for line in cur.fetchall():
        something.extend(line)

    print(something)

    if not something:
        return None

    num_businesses = [int(line[8])*1000, int(line[14])*1000, int(line[20])*1000]

    if employees == 0:
        columns = [4, 9, 15]
    elif employees in range(1, 5):
        columns = [4, 10, 16]
    elif employees in range(5, 20):
        columns = [5, 11, 17]
    elif employees in range(20, 200):
        columns = [6, 12, 18]
    elif employees > 200:
        columns = [7, 13, 19]

    print(num_businesses)
    query = "SELECT " \
            "field_" + str(columns[0]) + ", "\
            "field_" + str(columns[1]) + ", "\
            "field_" + str(columns[2]) + " "\
            "FROM business_employee_counts WHERE field_1='" + industry + "' AND field_2='" + SA_code + "'"
    cur.execute(query)

    counts = list()
    for line in cur.fetchall():
        counts.extend(line)

    counts = list(map(int, counts))
    aggeragateData = list(zip(num_businesses, counts))

    years = ["2014","2013","2012"]
    x = {}
    i = 0
    for year in years:
        x[year] = aggeragateData[i]
        i += i


    cur.close()
    conn.close()

    return dict(x)




