import requests
import datetime
from requests_html import HTML
import pandas as pd


url = 'https://www.boxofficemojo.com/year/world/'
now = datetime.datetime.now()
year = now.year


def url_to_file(url, filename='world.html'):
    r = requests.get(url)
    if r.status_code == 200:
        html_text = r.text
        with open(f'world-{year}.html', 'w') as f:
            f.write(html_text)
        return html_text


# region Store HTML contents in file and a variable
html_text = url_to_file(url)
# endregion

# Use requests-html to parse HTML
r_html = HTML(html=html_text)
# Find the element (table) that we are interested in
table_class = '.imdb-scroll-table'

# find the data in the table
r_table_data = r_html.find(table_class)
# Now that we have found the table element, print out the text from the table (cell values)
# r_table_data[0].text

# Let's try and look at the table rows
rows = r_table_data[0].find('tr')  # [0] = 1st element - in this case in a list
#  rows now contains a single list containing each row - a list of elements

header_row = rows[0]
header_columns = header_row.find('th')
header_row_names = [x.text for x in header_columns]
table_data = []  # empty list to contain each row

for row in rows[1:]:  # for each row ignoring to header row
    columns = row.find('td')  # find the columns
    row_data = []  # empty list to store row values
    for index, column in enumerate(columns):  # for each column element
        row_data.append(column.text)  # sdd the column value to a list
    table_data.append(row_data)  # then add the list to the table_data list which will contain all rows

#  use Pandas to export to csv
df = pd.DataFrame(table_data, columns=header_row_names)
df.to_csv('world-2021.csv', index=False)
