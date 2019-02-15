from bs4 import BeautifulSoup
import requests
import numpy as np
import pandas as pd

if __name__ == '__main__':
    outFile = open("result.txt", "w")
    url = 'http://www.fi-aeroweb.com/Top-100-US-Airports.html#PAX'
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'lxml')
    airports = soup.find_all('p', class_='style5')
    airports = airports[0].text.replace(',','').replace('\n','',1).split('\n')
    # airports = pd.DataFrame(airports,columns=[])
    for k in soup.find_all('div', class_='style4028', )[0:5]:
        data = k.text.replace(',','').replace('\n\n','').split('\n')
        for i in range(len(airports)):
            airports[i]=airports[i]+','+data[i]
    APS = "Airports,Passengers(PAX),Domestic(PAX),Intl(PAX),Departures,Seats per Aircraft"+'\n'
    for i in range(len(airports)):
        APS = APS+airports[i]+'\n'
    outFile.write("%s\n\n"%APS)
    outFile.close()
