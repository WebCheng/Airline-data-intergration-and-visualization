
import plotly
import pymysql
pymysql.install_as_MySQLdb()

from plotly.offline import  plot
import plotly.plotly as py
import plotly.graph_objs as go


plotly.tools.set_credentials_file(username='yzwanm', api_key='kUo1iUJh9qAMkVVsxJiD')
#
mapbox_access_token = 'pk.eyJ1IjoieXp3YW5tIiwiYSI6ImNqc2w1bm5lZDFxNXg0M241dnhreGlvaTUifQ.w0V9xH-zUjVBiFQyCpJRkw'
db = pymysql.connect("localhost","root","123456","aitport")

cursor = db.cursor()
cursor.execute("""SELECT * FROM aitport.AIRPORT;""")
info1 = cursor.fetchall()
List=[]
List2=[]
List3=[]
for row in info1:
    List.append(row[6])
    List2.append(row[7])
    List3.append(row[1])

List=','.join(map(str,List))
List2=','.join(map(str,List2))
List3=',,'.join(map(str,List3))
# print(len(info1),len(List.split(',')), len(List2.split(',')), len(List3.split(',,')))

# #
# # #
data = [
    go.Scattermapbox(
        lat = List.split(','),
        lon= List2.split(','),
        mode='markers',
        marker=dict(
            size=9
        ),
        text= List3.split(',,'),
    )
]

layout = go.Layout(
    autosize=True,
    hovermode='closest',
    mapbox=dict(
        accesstoken=mapbox_access_token,
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
fig = dict(data=data, layout=layout)
plot(fig, filename='Montreal Mapbox.html')
