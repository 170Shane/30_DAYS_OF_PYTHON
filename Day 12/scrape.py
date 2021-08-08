import requests
import datetime
from requests_html import HTML

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
# print out the text from the table
print(r_table_data[0].text)


