import plotly.express as px
import plotly.graph_objects as go
fig = go.Figure()
hodnota=input("jaky typ pie grafu by jsi chtel videt? [1=klasicky, 2=s opakovanema nazvama, 3=donut, 4=sunburst]")

if(hodnota=='1'):
    df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
    df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries
    fig = px.pie(df, values='pop', names='country', title='Population of European continent')
    fig.show()
    
elif(hodnota=='2'):
    df = px.data.tips()
    fig = px.pie(df, values='tip', names='day')
    fig.show()
    
elif(hodnota=='3'):
    labels = ['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen']
    values = [4500, 2500, 1053, 500]
    fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
    fig.show()

elif(hodnota=='4'):
    fig = go.Figure()
    fig = go.Figure(go.Sunburst(
    labels=["Eve", "Cain", "Seth", "Enos", "Noam", "Abel", "Awan", "Enoch", "Azura"],
    parents=["", "Eve", "Eve", "Seth", "Seth", "Eve", "Eve", "Awan", "Eve" ],
    values=[10, 14, 12, 10, 2, 6, 6, 4, 4],
))
fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

fig.show()