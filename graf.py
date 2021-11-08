import pandas as pd
import plotly.express as px
import requests

url = 'https://raw.githubusercontent.com/Institut-Zdravotnych-Analyz/covid19-data/main/DailyStats/OpenData_Slovakia_Covid_DailyStats.csv'
r = requests.get(url, allow_redirects=True)
open('korona.csv', 'wb').write(r.content)

df = pd.read_csv('./korona.csv', delimiter=';')
fig = px.line(df, x = 'Datum', y = ['Dennych.PCR.testov', 'Dennych.PCR.prirastkov', 'Pocet.umrti'], title='SLOVAK korona data')
fig.write_html('./index.html')
