**************
TABLE routes
**************
airline: 2-letter (IATA) or 3-letter (ICAO) code of the airline.
airline_id: Unique OpenFlights identifier for airline (see Airline).
source_airport: 3-letter (IATA) or 4-letter (ICAO) code of the source airport.
source_airport_id: Unique OpenFlights identifier for source airport (see Airport)
destination_airport: 3-letter (IATA) or 4-letter (ICAO) code of the destination airport.
destination_airport_id: Unique OpenFlights identifier for destination airport (see Airport)
codeshare: ¡°Y¡± if this flight is a codeshare (that is, not operated by Airline, but another carrier), empty otherwise.
stops: Number of stops on this flight (¡°0¡± for direct)
equipment: 3-letter codes for plane type(s) generally used on this flight, separated by spaces

**************
TABLE airlines
**************
airline_id: Unique OpenFlights identifier for this airline.
name: Name of the airline.
alias: Alias of the airline. For example, All Nippon Airways is commonly known as ¡°ANA¡±.
IATA: 2-letter IATA code, if available.
ICAO: 3-letter ICAO code, if available.
callsign: Airline callsign.
country: Country or territory where airline is incorporated.
active: ¡°Y¡± if the airline is or has until recently been operational, ¡°N¡± if it is defunct.
This field is not reliable: in particular, major airlines that stopped flying long ago, but have not had their IATA code reassigned (eg. Ansett/AN), will incorrectly show as ¡°Y¡±.

