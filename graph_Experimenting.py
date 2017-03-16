# import plotly.plotly as py
# import plotly.graph_objs as go
# # from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot, offline
#
# # Create random data with numpy
# import numpy as np
#
# py.sign_in('a9595', 'JiSGkDYi671JmrA2oy41')
# # py.sign_in(py.get_credentials())
# # py.get_credentials()
# # py.sign_in()
#
# N = 1000
# random_x = np.random.randn(N)
# random_y = np.random.randn(N)
#
# # Create a trace
# trace = go.Scatter(
#     x = random_x,
#     y = random_y,
#     mode = 'markers'
# )
#
# data = [trace]
#
# # Plot and embed in ipython notebook!
# py.iplot(data, filename='graph')
#
# # or plot with: plot_url = py.plot(data, filename='basic-line')


import urllib2
import numpy as np

import plotly.plotly as py
# py.sign_in('halblooline', 'j90503v8gq')
py.sign_in('a9595', 'JiSGkDYi671JmrA2oy41')

import plotly.graph_objs as go
import numpy as np

N = 1000
random_x = np.random.randn(N)
random_y = np.random.randn(N)

# Create a trace
trace = go.Scatter(
    x = random_x,
    y = random_y,
    mode = 'markers'
)

data = [trace]

# Plot and embed in ipython notebook!
py.plot(data, filename='basic-scatter')

# or plot with: plot_url = py.plot(data, filename='basic-line')