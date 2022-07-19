from bs4 import BeautifulSoup
import requests
import re


def get_web_page(url):
    result = requests.get(url)
    return BeautifulSoup(result.text, "html.parser")


def get_train_times(station_code):
    url = "https://realtime.nationalrail.co.uk/ldbcis/departures.aspx?u=039B1CD1-14D4-4CB9-83B1-A84CC3AEDF83&crs=" + station_code + "&H=1080"
    soup = get_web_page(url)

    s = soup.find("div", class_="contents")
    departures = s.find_all("tr", id=re.compile("trainStation.*"))

    station_departures = []
    i = 0
    for d in departures:
        # departure = {"destination", "via", "platform", "departs", "expected", "header", "stops", "late_reason",
        #             "cancelled_reason", "not_calling_list"}

        departure = {}
        tag_list = []
        for tag in d:
            if tag.text != "\n":
                tag_list.append(tag.text)

        departure["destination"] = tag_list[0]
        departure["platform"] = tag_list[1]
        departure["departs"] = tag_list[2]
        departure["expected"] = tag_list[3]

        # Get calling points for departure
        c = s.find("tr", id=("callingPoints" + str(i)))
        calling_points_tags = c.find_all("span")

        calling_points = []
        for calling_point_tag in calling_points_tags:
            calling_points.append(calling_point_tag.text)

        departure["header"] = calling_points[0]
        calling_points.pop(0)

        # Gets cancellation reason
        try:
            departure["cancellation_reason"] = (c.find("div", class_="canc_reason")).text
        except AttributeError:
            ()

        # Gets late reason
        try:
            departure["late_reason"] = (c.find("span", class_="late_reason")).text
            calling_points.remove((c.find("span", class_="late_reason")).text)
        except AttributeError:
            ()

        # Gets last report
        try:
            departure["last_report_label"] = (c.find("span", class_="LastReportLabel")).text
            calling_points.remove((c.find("span", class_="LastReportLabel")).text)
        except AttributeError:
            ()
        try:
            departure["last_report_status"] = (c.find("span", class_="LastReportStatus")).text
            calling_points.remove((c.find("span", class_="LastReportStatus")).text)
        except AttributeError:
            ()
        try:
            departure["last_report_station"] = (c.find("span", class_="LastReportStation")).text
            calling_points.remove((c.find("span", class_="LastReportStation")).text)
        except AttributeError:
            ()
        try:
            departure["last_report_time"] = (c.find("span", class_="LastReportTime")).text
            calling_points.remove((c.find("span", class_="LastReportTime")).text)
        except AttributeError:
            ()

        # Gets not calling list

        try:
            departure["not_calling_list"] = (c.find("span", class_="not_calling_list")).text
            calling_points.remove((c.find("span", class_="not_calling_list")).text)
        except AttributeError:
            ()

        departure["calling_points"] = calling_points
        station_departures.append(departure)
        i = i + 1

    return station_departures
