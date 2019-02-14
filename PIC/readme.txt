**************
TABLE routes
**************
airline: 2-letter (IATA) or 3-letter (ICAO) code of the airline.
airline_id: Unique OpenFlights identifier for airline (see Airline).
source_airport: 3-letter (IATA) or 4-letter (ICAO) code of the source airport.
source_airport_id: Unique OpenFlights identifier for source airport (see Airport)
destination_airport: 3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
destination_airport_id: Unique OpenFlights identifier for destination airport (see Airport)
codeshare: “Y” if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
stops: Number of stops on this flight (“0” for direct)
equipment: 3-letter codes for plane type(s) generally used on this flight, separated by spaces

**************
TABLE airlines
**************
airline_id: Unique OpenFlights identifier for this airline.
name: Name of the airline.
alias: Alias of the airline. For example, All Nippon Airways is commonly known as “ANA”.
IATA: 2-letter IATA code, if available.
ICAO: 3-letter ICAO code, if available.
callsign: Airline callsign.
country: Country or territory where airline is incorporated.
active: “Y” if the airline is or has until recently been operational, “N” if it is defunct.
This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as “Y”.

************************
TABLE allyears(airlines)
************************
Year	1987-2008
Month	1-12
DayofMonth	1-31
DayOfWeek	1 (Monday) - 7 (Sunday)
DepTime	actual departure time (local, hhmm)
CRSDepTime	scheduled departure time (local, hhmm)
ArrTime	actual arrival time (local, hhmm)
CRSArrTime	scheduled arrival time (local, hhmm)
UniqueCarrier	unique carrier code
FlightNum	flight number
TailNum	plane tail number
ActualElapsedTime	in minutes
CRSElapsedTime	in minutes
AirTime	in minutes
ArrDelay	arrival delay, in minutes
DepDelay	departure delay, in minutes
Origin	origin IATA airport code
Dest	destination IATA airport code
Distance	in miles
TaxiIn	taxi in time, in minutes
TaxiOut	taxi out time in minutes
Cancelled	was the flight cancelled?
CancellationCode	reason for cancellation (A = carrier, B = weather, C = NAS, D = security)
Diverted	1 = yes, 0 = no
CarrierDelay	in minutes
WeatherDelay	in minutes
NASDelay	in minutes
SecurityDelay	in minutes
LateAircraftDelay	in minutes


**************
TABLE carriers
**************
Code: Abbreviation of Airline name
Description: Airline name
