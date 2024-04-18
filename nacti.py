import pandas as pd
import plotly as ptl
import plotly.express as px

# Načtení CSV souboru
df = pd.read_csv('OD_SLDB_HD_at.csv')
df.info()
df['rok']
df.columns
df[df.columns[4]]
df[df.columns[4]].unique()
pd.pivot_table(df, values=['hodnota'], index=['rok'], columns=['stapro_txt','kraj_text'])
fig = px.sunburst(df, path=[px.Constant("vse"), 'stapro_txt', 'kraj_text','rok', 'okres_text'  ], values='hodnota') #teemap, sunburst
fig.update_traces(root_color="lightgrey")
fig.update_layout(margin = dict(t=40, l=20, r=20, b=20))
fig.show()