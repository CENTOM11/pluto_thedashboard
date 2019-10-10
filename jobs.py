import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
from base import app
print("started jobs")

layout_jobs=html.Div(
    [
        dcc.Tabs(
            [
                dcc.Tab(label="Graph 1", value="jobs1"),
                dcc.Tab(label="Graph 2", value="jobs2"),
                dcc.Tab(label="Graph 3", value="jobs3"),
                dcc.Tab(label="Graph 4", value="jobs4"),
            ],
            id="tabs_jobs",
            value="jobs1"
        ),
        html.Div(id="content_jobs",
            # style={
            #     'float':'right'
            # }
                 ),
    ]
)
jobs1 = html.Div('Graph1')

jobs2 = html.Div("Graph2")

jobs3 = html.Div("Graph3")

jobs4 = html.Div("Graph4")

#layout = html.Div([tabs])
print("end jobs")
@app.callback(Output("content_jobs", "children"),[Input("tabs_jobs", "value")])
def switch_tab(at):
    if at == "jobs1":
        return jobs1
    elif at == "jobs2":
        return jobs2
    elif at == "jobs3":
        return jobs3
    elif at == "jobs4":
        return jobs4
    else:
        return html.P("This shouldn't ever be displayed...")