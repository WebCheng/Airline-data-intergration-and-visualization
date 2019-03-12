import csv
from numpy import genfromtxt
import pandas
import numpy as np


def setAirportName(names, airportSet):
    rt = []
    for i, n in enumerate(names[1:]):
        apName = " ".join(n.lower().split(" ")[:-1])
        df = airportSet.str.contains(apName, regex=False)
        df = df.index[df == True].tolist()
        if len(df) > 0:
            rt.append([apName, i, df[0]])
    rt = np.array(rt)
    return rt


finalSet, nameList = np.array([np.zeros(5)]), None
apSet = pandas.read_csv('./DATASET/AIRPORT.csv', delimiter=':', encoding="utf-8")
years = [1993, 1994, 1995, 1996, 1997, 1998,
         1999, 2000, 2001, 2002, 2003, 2004,
         2005, 2006, 2007, 2008, 2009, 2010,
         2011, 2012, 2013, 2014, 2015, 2016,
         2017]
airSet = []
with open("./DATASET/airline-traffic-data-by-main-air.csv", "r")as f:
    spamreader = csv.reader(f, delimiter=',', quotechar='|')
    for idx, row in enumerate(spamreader):
        if idx == 0:
            nameList = setAirportName(row, apSet["NAME"].str.lower())
            cList = apSet[["IATA", "ICAO"]].ix[nameList.T[2].astype(np.int)]

            airSet.append(nameList.T[0])
            airSet.append(np.array(cList["IATA"]))
            airSet.append(np.array(cList["ICAO"]))
        else:
            tt = []
            tt.append(np.array(row)[(nameList.T[1].astype(np.int))])
            tt.insert(0, [years[idx - 1] for i in range(len(tt[0]))])
            finalSet = np.concatenate(
                (
                    finalSet,
                    np.concatenate((np.array([[years[idx - 1] for i in range(len(tt[0]))]]).T,
                                    np.array(airSet).T,
                                    np.array([np.array(row)[(nameList.T[1].astype(np.int))]]).T)
                                   , axis=1)
                )
                , axis=0
            )

ft = np.array(finalSet[1:])
with open("./DATASET/AIRLINE_TRAFFIC.csv", "w") as f:
    f.write("YEAR,AIRPORT_NAME,IATA_CODE,ICAO_CODE,TRAFFIC\n")
    for row in ft:
        tmp = "\"{0}\",\"{1}\",\"{2}\",\"{3}\",\"{4}\"".format(
            row[0], row[1], row[2],
            row[3], row[4])
        f.write(tmp + "\n")

print("Done!!")
