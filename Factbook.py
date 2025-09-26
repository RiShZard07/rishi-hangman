import csv

def load_data(factbook):
    """
    Reads file factbook.csv and creates a dictionary
    factbook of the form:
    {'Afghanistan': {'Area(sq km)': '647500', ...}, ...}
    """
    with open('factbook.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=';')

        rownum = 0
        for row in reader:
            if rownum == 0:
                headers = row  # saves the header names
            elif rownum == 1:
                pass  # skips the data type row
            else:
                if not row or not row[0]:
                    continue  # skips the blank lines

                country = row[0]
                attrs = {}

                for i in range(1, len(headers)):
                    value = row[i] if i < len(row) else ''
                    attrs[headers[i]] = value

                factbook[country] = attrs

            rownum += 1

def main():
    # initializes and loads factbook
    factbook = {}
    load_data(factbook)

    # compare some labor forces
    print('Chilean Labor Force is', int(factbook['Chile']['Labor force']))
    print('Indian Labor Force is', int(factbook['India']['Labor force']))

    # find the largest country by area
    max_country = 'Unknown'
    max_area = -1
    for country in factbook:
        area = int(factbook[country]['Area(sq km)'])
        if area > max_area:
            max_area = area
            max_country = country
    print('Largest Country is', max_country)

    # list number of internet users in Morocco
    print('Morocco has', int(factbook['Morocco']['Internet users']), 'internet users')

    # Add one more query here of your own
    min_country = 'Unknown'
    min_area = float('inf')
    for country in factbook:
        areastr = factbook[country].get('Area(sq km)', '0')
        if areastr and areastr.isdigit():
            area = int(areastr)
            if 0 < area < min_area:
                min_area = area
                min_country = country
    print('Smallest Country is', min_country)

    # call main
main()

"""
/Users/rishikeshavadamarla/PycharmProjects/PythonProject10/.venv/bin/python /Users/rishikeshavadamarla/PycharmProjects/PythonProject10/Factbook.py 
Chilean Labor Force is 6200000
Indian Labor Force is 482200000
Largest Country is Russia
Morocco has 800000 internet users
Smallest Country is Baker Island

Process finished with exit code 0
"""