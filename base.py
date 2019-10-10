import dash
# from flask_caching import Cache
# import pandas as pd

e_stylesheets = ['/assets/css/header1.css']
app = dash.Dash(__name__, external_stylesheets=e_stylesheets)

server = app.server

app.config.suppress_callback_exceptions = True

