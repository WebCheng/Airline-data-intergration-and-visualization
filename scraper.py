import requests
from bs4 import BeautifulSoup

# url = "https://www.airlineratings.com/safety-rating-tool/"
htmlTxt = ""
with open("tmp", 'r', encoding="utf-8") as f:
    for line in f:
        htmlTxt += line

with open("airlineRating.csv", "a") as f:
    soup = BeautifulSoup(htmlTxt, 'html.parser')
    for x in soup.find("table", {"class": "safetyRatingTable"}).findAll("tr", {"class": "safetyRatingsTableRowBody"}):
        name = x.find("td", {"class", "safetyRatingsTableRowAirline"}).find("label", {"class", "text"}).text

        if name == "JetSmart":
            continue

        country = x.find("td", {"class", "safetyRatingsTableRowCountry"}).text

        rank = len(x.find("td", {"class", "safetyRatingsTableRowIOSA"}).findAll("i", {"class", "fa fa-check"}))

        euAllow = "Y" if x.find("td", {"class", "safetyRatingsTableRowEUAllowed"}).find("i", {"class",
                                                                                              "fa fa-check"}) is not None else "N"
        fatalityFee = "Y" if x.find("td", {"class", "safetyRatingsTableRowFatalityFree"}).find("i", {"class",
                                                                                                     "fa fa-check"}) is not None else "N"
        faaEndorsed = "Y" if x.find("td", {"class", "safetyRatingsTableRowFAAEndorsed"}).find("i", {"class",
                                                                                                    "fa fa-check"}) is not None else "N"
        ICAO_CA = "Y" if x.find("td", {"class", "safetyRatingsTableRowICAOCountry"}).find("i", {"class",
                                                                                                "fa fa-check"}) is not None else "N"

        rate = \
            x.find("td", {"class", "safetyRatingsTableRowRatingsStars"}).find("div", {"class", "rating"}).attrs[
                "style"].split(":")[1].replace("%", " ")
        f.write(",".join([name, country, str(rank), euAllow, fatalityFee, faaEndorsed, ICAO_CA, rate]) + "\n")
