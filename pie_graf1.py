import plotly.express as px
import plotly.graph_objects as go
import numpy as np
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

np.random.seed(1)

N = 100
random_x = np.linspace(0, 1, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Create traces
fig = go.Figure()
fig.add_trace(go.Scatter(x=random_x, y=random_y0,
                    mode='lines',
                    name='lines',
                    line_shape='spline')) # Add this line
fig.add_trace(go.Scatter(x=random_x, y=random_y1,
                    mode='lines+markers',
                    name='lines+markers',
                    line_shape='spline')) # And this line
fig.add_trace(go.Scatter(x=random_x, y=random_y2,
                    mode='markers', name='markers'))

fig.show()