import plotly.express as px
import pandas as pd
import plotly as pl

df = px.data.gapminder().query("continent == 'Europe' and year == 2007 and pop > 2.e6")
df = df.sort_values('pop', ascending=False,)
fig = px.bar(df, y='pop', x='country', text_auto='.2s',
            title="Controlled text sizes, positions and angles", color_continuous_scale='purp')
fig.update_traces(textfont_size=12, textangle=45, textposition="outside", cliponaxis=False)
fig.show()
fig.write_image('graf.svg')