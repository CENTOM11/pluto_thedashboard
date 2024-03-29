import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from base import app
import pandas as pd
from datetime import datetime as dt
from functions import get_data

print("started cp")

df1=get_data()

layout_cp=html.Div(
	[
		dcc.Tabs(
			[
				dcc.Tab(label='Revenue generated from each carepartner', value="cp1"),
				dcc.Tab(label="Count of Rides of Each carepartner", value="cp2")
			],
			id="tabs_cp",
			value="cp1"
		),
		html.Div(id="cp_content",
			# style={
			#     'float':'right'
			# }
				 )
	]
)

# dates dropdown list
dates=list(df1['m&y'].unique())
dates.append("All")

#location dropdown list
loc=list(df1['job_loc'].unique())
loc.append("All Locations")

# job type dropdown list
jobt=list(df1['job_type'].unique())
jobt.append('Both')


#layout for graph1
cp1 = html.Div([
	 html.Div([
		 dcc.Dropdown(id='loc_cp1',options=[{'label': i,'value': i} for i in loc],value=loc[0],style={'height': '30px', 'width': '60%'},placeholder="Select the location")
		 ]),
	html.Div([

        dcc.DatePickerRange(
            id='date_cp1',
            min_date_allowed=dt(2017, 11, 1),
            max_date_allowed=dt(2019, 8, 21),
            initial_visible_month=dt(2018, 11, 1),
            end_date=dt(2019, 8, 21)
        )
        ]),
	# html.Div([
	# 	dcc.Dropdown(id='date_cp1',options=[{'label': i,'value': i} for i in dates],value=loc[0],style={'height': '30px', 'width': '60%'},placeholder="Select the month and year")
	# 	]),

dcc.Graph(id='cp_graph1')
	],
	className="graph")
#callback for graph1
@app.callback(Output('cp_graph1','figure'),
				[Input("loc_cp1","value"),Input('date_cp1','start_date'),Input('date_cp1','end_date')])
				#[Input('date_cp1','value')])
def update_graph1(location,start_date,end_date):
	if location=="All Locations":
		df=df1
	else:
		df=df1[df1['job_loc'] == location]

	if start_date is not None:
		dat = pd.to_datetime(start_date)
		start_date = dt.strftime(dat, '%Y-%m-%d')

	if end_date is not None:
		dat1 = pd.to_datetime(end_date)
		end_date = dt.strftime(dat1, '%Y-%m-%d')

	i = next(iter(df[df['new_date'] == start_date].index), 'no match')
	j = next(iter(df[df['new_date'] == end_date].index), 'no match')

	if (i == "no match"):
		i = 0

	if (j == "no match"):
		j = len(df) - 3

	df2 = df[i:j + 1]
	grouped_revenue = df2.groupby(["driver_name"])["Revenue_generated"].sum()
	return {
			  'data': [{'x': grouped_revenue.index,
					   'y': grouped_revenue.values,'type': 'bar'}],
					 'layout': {
			  'title': 'Revenue generated by each Driver'
					}}

#layout for graph2
cp2 = html.Div([
    # html.Div([
    #     dcc.Dropdown(id='count_cp1',options=[{'label': i,'value': i} for i in list1], style={'height': '30px', 'width': '60%'},value=list1[0],placeholder="Select the no of carepartners to be displayed")
    #     ]),
    html.Div([
        dcc.Dropdown(id='loc_cp2',options=[{'label': i,'value': i} for i in loc],style={'height': '30px', 'width': '60%'},value=loc[0],placeholder="Select the location")
        ]),
    html.Div([

        dcc.DatePickerRange(
            id='date_cp2',
            min_date_allowed=dt(2017, 11, 1),
            max_date_allowed=dt(2019, 8, 21),
            initial_visible_month=dt(2018, 11, 1),
            end_date=dt(2019, 8, 21)
        )
        ]),
    dcc.Graph(id='cp_graph2')
    ]
)

#callback functions for graph2
@app.callback(Output('cp_graph2','figure'),
                [Input("loc_cp2","value"),Input('date_cp2', 'start_date'),
                 Input('date_cp2','end_date')])
def update_graph1(loc_cp1,st_date,en_date):
    if loc_cp1 == 'All Locations':
        c1=df1
    else:
        c1=df1[df1['job_loc'] == loc_cp1]

    c1.dropna(subset=["new_date"], inplace=True)
    c1.reset_index(drop=True, inplace=True)

    if st_date is not None:
        dat = pd.to_datetime(st_date)
        st_date = dt.strftime(dat, '%Y-%m-%d')

    if en_date is not None:
        dat1 = pd.to_datetime(en_date)
        en_date = dt.strftime(dat1, '%Y-%m-%d')

    i = next(iter(c1[c1['new_date'] == st_date].index), 'no match')
    j = next(iter(c1[c1['new_date'] == en_date].index), 'no match')

    if (i == "no match"):
        i = 0

    if (j == "no match"):
        j = len(df1) - 3


    df2 = c1[i:j + 1]
    return {
        'data': [{'x': df2['driver_name'].value_counts().index,
                  'y': df2['driver_name'].value_counts().values, 'type': 'bar'}],
        'layout': {
            'title': 'Count of Rides by each Driver'
        }}


cp3 = html.Div("Graph3")

cp4 = html.Div("Graph4")

@app.callback(Output("cp_content", "children"),[Input("tabs_cp", "value")])
def switch_tab(at):
	if at == "cp1":
		return cp1
	elif at == "cp2":
		return cp2
	elif at == "cp3":
		return cp3
	elif at == "cp4":
		return cp4
	else:
		return html.P("This shouldn't ever be displayed...")


print("end cp")