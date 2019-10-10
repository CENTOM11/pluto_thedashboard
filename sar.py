print("started sar")

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
from base import app
import jobs
from bus import layout_bus
from cp import layout_cp

app.layout = html.Div([
    html.Div([
        html.Div(
                html.Img(src='/assets/logo_pluto_white.png', height="110%"),
                 style={"float": "right", "height": "100%"}, className='logo_pluto'),

        html.Div(
                html.Img(src='/assets/icon.png',height="100%"),
                style={"float": "left","height":"100%"},
            className='logo_main')
],
        className="header",id='sar'),
    html.Div([
		dcc.Tabs(
            children=[
            dcc.Tab(label='Home',value='4'),
	        dcc.Tab(label='Clients',value='1'),
            dcc.Tab(label='Drivers',value='2'),
            dcc.Tab(label='Rides',value='3')

        ],id='tabs'),
   ] ),
        html.Div(id="tab_content", className="row", style={"margin": "2% 3%"})
    ]
)

home_page = html.Div([
  html.Img(src='/assets/bg_new.png', id='img11')
    ],
    className="home")

@app.callback(Output("tab_content", "children"), [Input("tabs", "value")])
def render_content(value):
    if value == '1':
        return layout_bus
    elif value == '2':
        return layout_cp
    elif value == '3':
        return jobs.layout_jobs
    else:
        return home_page

print("end sar")
if __name__ == '__main__':
    app.run_server(debug=True)
