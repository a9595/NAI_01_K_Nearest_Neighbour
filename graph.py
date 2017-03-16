import numpy as np
from plotly import plotly as py
from plotly.graph_objs import Scatter, Marker

from calulateWithK import calculateWithK
from dataReader import get_training_set


def createGraph():
    dataX = []
    dataY = []
    trainingSet = get_training_set()
    for x in range(1, len(trainingSet)):
        dataX.append(x)
        dataY.append(calculateWithK(x))

    trace1 = Scatter(
        x=dataX,
        y=dataY,
        mode='markers',
        name="Actual Value"
    )

    z = np.polyfit(dataX, dataY, 3)
    f = np.poly1d(z)

    x_new = np.linspace(dataX[0], dataX[-1], 50)
    y_new = f(x_new)

    trace2 = Scatter(
        x=x_new,
        y=y_new,
        mode='lines',
        marker=Marker(color='rgb(100, 100, 100)'),
        name='Fit'
    )

    data = [trace1, trace2]
    layout = dict(title='Percentage of correctly classified test examples versus K',
                  xaxis=dict(title='K value [1]'),
                  yaxis=dict(title='Accuracy of kNN [%]'),
                  )

    fig = dict(data=data, layout=layout)
    py.plot(fig, filename='kNN correct precentage versus K')
