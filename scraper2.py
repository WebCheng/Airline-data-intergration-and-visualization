import requests
from bs4 import BeautifulSoup

hostUrl = "https://www.airlinequality.com"
r = requests.get('https://www.airlinequality.com/review-pages/a-z-airline-reviews/')
soup = BeautifulSoup(r.text, 'html.parser')

dic = {}
for tar in list("QWERTYUIOPASDFGHJKLZXCVBNM"):
    try:
        for x in soup.find("div", {"id": "a2z-ldr-{0}".format(tar)}).findAll("a"):
            link, airline = x.attrs['href'], x.text
            next_soup = BeautifulSoup(requests.get(url=hostUrl + link).text, 'html.parser')
            tableContent = next_soup.find("section", {"class", "layout-section layout-1"}) \
                .find("table", {"class", "review-ratings"})

            rateArr = []
            for td in tableContent.findAll("td", {"class", "review-rating-stars"}):
                rateArr.append(len(td.findAll("span", {"class", "star fill"})))
            dic.setdefault(airline, rateArr)
    except:
        print(tar)

print("AIRLINE_NAME,FOOD_RATE,ENTERTAINMENT_RATE,SEAT_RATE,SERVICE_RATE,MONEY_RATE")
for key, val in dic.items():
    print("{0},{1},{2},{3},{4},{5}".format(key, val[0], val[1], val[2], val[3], val[4]))

print("Done")
