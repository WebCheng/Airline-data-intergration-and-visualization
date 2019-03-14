

import plotly
import pymysql
pymysql.install_as_MySQLdb()
from plotly.offline import  plot
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='yzwanm', api_key='kUo1iUJh9qAMkVVsxJiD')
mapbox_access_token = 'pk.eyJ1IjoieXp3YW5tIiwiYSI6ImNqc2w1bm5lZDFxNXg0M241dnhreGlvaTUifQ.w0V9xH-zUjVBiFQyCpJRkw'

db = pymysql.connect("localhost","root","123456","aitport")

cursor = db.cursor()
cursor.execute("""SELECT  DISTINCT Origin, LATITUDE, LONGITUDE FROM aitport.AIRPORT, aitport.ALLYEARS_SCHEDULE where IATA_CODE = Origin;""")
info1 = cursor.fetchall()
List=[]
List2=[]
List3=[]
for row in info1:
 List.append(row[1])
 List2.append(row[2])
 List3.append(row[0])

List=','.join(map(str,List))
List2=','.join(map(str,List2))
List3=',,'.join(map(str,List3))

cursor1 = db.cursor()

cursor1.execute("""SELECT  DISTINCT Dest, LATITUDE, LONGITUDE FROM aitport.AIRPORT, aitport.ALLYEARS_SCHEDULE where IATA_CODE = Dest;""")
info2 = cursor1.fetchall()
List4=[]
List5=[]
List6=[]
for r in info2:
 List4.append(r[1])
 List5.append(r[2])
 List6.append(r[0])

List4=','.join(map(str,List4))
List5=','.join(map(str,List5))
List6=',,'.join(map(str,List6))



airports = [go.Scattermapbox(
    lat=List.split(','),
    lon=List2.split(','),
    text=List3.split(',,'),

    mode = 'markers',
    marker = go.scattermapbox.Marker(
        size = 5,
        color = 'blue',



    ))]
flight_paths = []
for i in range(len(List.split(','))):
    flight_paths.append(
        go.Scattermapbox(
            lat = [List.split(',')[i], List4.split(',')[i]],
            lon = [List2.split(',')[i], List5.split(',')[i]],
            mode = 'lines',

            line=dict(
                width=1,
                color='red',

            ),

        )
    )




layout = go.Layout(
    autosize=True,
    hovermode='closest',

    mapbox=dict(
        accesstoken=mapbox_access_token,
        style='dark',
        bearing=0,
        center=dict(
            lat=45.58869934000000,
            lon=-122.59799960000000
        ),
        pitch=0,
        zoom=10
    ),
)

db.close()
fig = dict(data=flight_paths + airports, layout=layout)
plot(fig, filename = 'd3-flight-paths.html')
