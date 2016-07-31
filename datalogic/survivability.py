import psycopg2

#inputs:
#       industry: string containing string matched to one of the industry fields in survival_rates_employee
#       employees: int describing number of employees in the business
#       state: three-letter string denoting state the business operates in
#outputs: dictionary with survivability %s for 1, 2, 3 and 4 years


def survivability_by_employees(industry, employees, state):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    states = {'NSW': 0, 'VIC': 1, 'QLD': 2, 'SA': 3, 'WA': 4, 'TAS': 5, 'NT': 6, 'ACT': 7, 'UKN': 8}

    if employees == 0:
        cols = [8, 18, 28, 38]
    elif employees in range(1, 20):
        cols = [10, 20, 30, 40]
    elif employees in range(20, 200):
        cols = [12, 22, 32, 42]
    elif employees > 200:
        cols = [14, 24, 34, 44]

    query = "SELECT * FROM survival_rates_employee WHERE field_1='" + industry + "'"
    cur.execute(query)

    if not cur.fetchall():
        return None

    line = cur.fetchall()[states[state]]
    return {"1 year": line[cols[0]], "2 years": line[cols[1]], "3 years": line[cols[2]], "4 years": line[cols[3]]}

    cur.close()
    conn.close()

#inputs:
#       industry: string containing string matched to one of the industry fields in survival_rates_employee
#       turnover: int describing amount earned by business per year
#       state: three-letter string denoting state the business operates in
#outputs: dictionary with survivability %s for 1, 2, 3 and 4 years


def survivability_by_turnover(industry, turnover, state):
    conn = psycopg2.connect(dbname="govhack", user="govhack", password="govhack", host="107.155.108.51")
    cur = conn.cursor()

    states = {'NSW': 0, 'VIC': 1, 'QLD': 2, 'SA': 3, 'WA': 4, 'TAS': 5, 'NT': 6, 'ACT': 7, 'UKN': 8}

    if turnover in range(0, 50000):
        cols = [8, 18, 28, 38]
    elif turnover in range(50000, 200000):
        cols = [10, 20, 30, 40]
    elif turnover in range(200000, 2000000):
        cols = [12, 22, 32, 42]
    elif turnover > 2000000:
        cols = [14, 24, 34, 44]

    query = "SELECT * FROM survival_rates_turnover WHERE field_1='" + industry + "'"
    cur.execute(query)
    if not cur.fetchall():
        return None
    line = cur.fetchall()[states[state]]

    return {"1 year": line[cols[0]], "2 years": line[cols[1]], "3 years": line[cols[2]], "4 years": line[cols[3]]}

    cur.close()
    conn.close()


#inputs: [see inputs for survivability sub-functions]
#outputs: dictionary containing survival data by employee number and by annual turnover,
#in format {
#    survival_by_employee: {After 1 year: x%, After 2 years: x%, After 3 years: x%, After 4 years: x%}
#    survival_by_turnover: {After 1 year: x%, After 2 years: x%, After 3 years: x%, After 4 years: x%}


def survivability(industry, state, employees, turnover):
    by_employee = survivability_by_employees(industry, employees, state)
    by_turnover = survivability_by_turnover(industry, turnover, state)

    return {"survival_by_employee": by_employee, "business_survival": by_turnover}
