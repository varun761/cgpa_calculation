import numpy as np
import pandas as pd
#import matplotlib.pyplot as plt
from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px

app = Dash(__name__)

xValues, yValues = [], []
scatteredness = 0.1
m = 2
c = 3
for i in range(40):
    for j in range(40 - i):
        xValues.append(i + i * np.random.normal(0, scatteredness))
        yValues.append(m*i + i*np.random.normal(0, scatteredness) + c)
print(len(xValues))
print(len(yValues))
# plt.scatter(xValues, yValues)
# plt.show()
fig = px.scatter(xValues,yValues, x='x-axis', y='y-axis')
# fig.show()

app.layout = html.Div([
    html.H1(children='Title of Dash App', style={'textAlign':'center'}),
    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])
    

if __name__ == '__main__':
    app.run(debug=True)