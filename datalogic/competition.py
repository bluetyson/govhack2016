import psycopg2

# returns [TOTAL 2014, TOTAL 2013, TOTAL 2012, X Employees 2014, X Employees 2013, X Employees 2012] where X is the stated number of employees, if given
# If employees not specified, will only return [TOTAL 2014, TOTAL 2013, TOTAL 2012]

# requires pre prossesing for SA2 code & industry
def get_competition(industry, SA_code, employees=0):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    SA_code = str(SA_code)

    query = "SELECT * FROM business_employee_counts WHERE field_1='" + industry + "' AND field_2='" + SA_code + "'"
    cur.execute(query)
    for line in cur.fetchall():
        num_businesses = [int(line[8])*1000, int(line[14])*1000, int(line[20])*1000]
        columns = []
        if employees == 0:
            columns = [3, 9, 15]
        elif employees in range(1, 5):
            columns = [4, 10, 16]
        elif employees in range(5, 20):
            columns = [5, 11, 17]
        elif employees in range(20, 200):
            columns = [6, 12, 18]
        elif employees > 200:
            columns = [7, 13, 19]


        return dict(zip(num_businesses, columns))





    cur.close()
    conn.close()

