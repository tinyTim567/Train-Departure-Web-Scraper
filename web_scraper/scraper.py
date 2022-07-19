from bs4 import BeautifulSoup
import requests
import re


def get_web_page():
    url = "https://realtime.nationalrail.co.uk/ldbcis/departures.aspx?u=039B1CD1-14D4-4CB9-83B1-A84CC3AEDF83&crs=HUL&H=1080"

    result = requests.get(url)
    return BeautifulSoup(result.text, "html.parser")


def main():
    doc = get_web_page()

    # print(doc.prettify())

    departures = doc.find_all(["tr"], id=re.compile("trainStation.*"))
    for departure in departures:
        for item in departure.contents:
            print(item.text)



