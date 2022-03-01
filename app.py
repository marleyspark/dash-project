# imports
# dash
import dash

from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.express as px
import pandas as pd

mainData = pd.read_csv("data/newdata.csv")

# setup
app = dash.Dash(__name__, title='Branches Dashboard')
server = app.server

# Layout
app.layout = html.Div([
    html.H1('Welcome to the Dashboard!!!',
            style={
                'color': 'black',
                'padding-top': '50px',
                'text-align': 'center'
            }),
    html.P('Use the dropdowns to see the visulisations',
           style={
               'color': 'black',
               'text-align': 'center',
               'padding-top': '50px'
           }),
    html.H2('Products Purchased by City by Region',
            style={
                'color': 'black',
                'padding-top': '50px',
            }),
    html.H3('Top 5'),
    html.P('Select Region'),
    dcc.Dropdown(mainData.region.unique(), id='region-dropdown-Top-5'),
    html.Br(),
    html.Br(),
    html.P('Select City'),
    dcc.Dropdown(mainData.county.unique(), id='city-dropdown-Top-5'),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='top-5-graph'),
    html.Br(),
    html.Br(),
    html.H3('Bottom 5'),
    html.P('Select Region'),
    dcc.Dropdown(mainData.region.unique(), id='region-dropdown-bottom-5'),
    html.Br(),
    html.Br(),
    html.P('Select City'),
    dcc.Dropdown(mainData.county.unique(), id='city-dropdown-bottom-5'),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='bottom-5-graph'),
    html.H2('Best Performing Branches Per City Per Region',
            style={
                'color': 'black',
                'padding-top': '50px',
            }),
    html.H3('Top 10'),
    html.P('Select Region'),
    dcc.Dropdown(mainData.region.unique(),
                 id='best-performing-banches-dropdown-region'),
    html.Br(),
    html.Br(),
    html.P('Select Branch'),
    dcc.Dropdown(mainData.branch_name.unique(),
                 id='best-performing-banches-dropdown-branch'),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='branches-best-graph'),
    html.Br(),
    html.Br(),
    html.H3('Bottom 10'),
    html.P('Select Region'),
    dcc.Dropdown(mainData.region.unique(),
                 id='worst-performing-banches-dropdown-region'),
    html.Br(),
    html.Br(),
    html.P('Select Branch'),
    dcc.Dropdown(mainData.branch_name.unique(),
                 id='worst-performing-banches-dropdown-branch'),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='branches-worst-graph'),
    html.H2('Top 10 Branches Sales per Hour',
            style={
                'color': 'black',
                'padding-top': '50px',
            }),
    html.P('Select Branch'),
    dcc.Dropdown(mainData.branch_name.unique(),
                 id='sales-per-hour-branch-dropdown'),
    html.Br(),
    html.Br(),
    html.P('Select Hour'),
    dcc.Dropdown(mainData.hour.unique(), id='sales-per-hour--time-dropdown'),
    html.Br(),
    html.Br(),
    dcc.Graph(figure={}, id='sales-per-hour-graph'),
    html.H2('Top 10 and Bottom 10 Branches by Profit',
            style={
                'color': 'black',
                'padding-top': '50px',
            }),
    html.Button('Top 10', id='top10-btn'),
    html.Button('Bottom 10', id='bottom10-btn'),
    dcc.Graph(figure={}, id='top-bottom-brances-graph')
])


#Top 5
@app.callback(
    Output(component_id='top-5-graph', component_property='figure'),
    Input(component_id='region-dropdown-Top-5', component_property='value')
    #Input(component_id='city-dropdown-Top-10',component_property='value')
)
def show_viz(dropdown):
    if dropdown is not None:
        my_df = pd.read_csv("data/newdata.csv")
        groupby_df = my_df.groupby(['region','county','item', 'quantity'], as_index=False).sum().sort_values(by='quantity', ascending=False).head(5)
        figure = px.bar(groupby_df, x='item', y=['quantity'])
        return figure
    return {}


#dropdown filter callback for Top 5
@app.callback(
    Output(component_id='city-dropdown-Top-5', component_property='options'),
    Input(component_id='region-dropdown-Top-5', component_property='value'))
def update_option(region):
    if region is not None:
        my_df = pd.read_csv("data/newdata.csv")
        my_df = my_df[my_df['region'] == region]
        return my_df.county.unique()
    return []


#bottom 5
@app.callback(
    Output(component_id='bottom-5-graph', component_property='figure'),
    Input(component_id='region-dropdown-bottom-5', component_property='value')
    #Input(component_id='city-dropdown-Top-10',component_property='value')
)
def show_viz(dropdown):
    if dropdown is not None:
        my_df = pd.read_csv("data/newdata.csv")
        groupby_df = my_df.groupby(['region', 'county', 'item', 'quantity'],
                                   as_index=False).sum().sort_values(
                                       by='quantity', ascending=True).head(5)
        figure = px.bar(groupby_df, x='item', y=['quantity'])
        return figure
    return {}


#dropdown filter callback for bttom 5
@app.callback(
    Output(component_id='city-dropdown-bottom-5', component_property='options'),
    Input(component_id='region-dropdown-bottom-5', component_property='value'))
def update_option(region):
    if region is not None:
        my_df = pd.read_csv("data/newdata.csv")
        my_df = my_df[my_df['region'] == region]
        return my_df.county.unique()
    return []

# top 10branches
@app.callback(
    Output(component_id='branches-best-graph', component_property='figure'),
    Input(component_id='best-performing-banches-dropdown-branch',
          component_property='value')
    #Input(component_id='best-performing-banches-dropdown-city', component_property='value')
)
def show_viz(dropdown):
    if dropdown is not None:
        my_df = pd.read_csv("data/newdata.csv")
        groupby_df = my_df.groupby(['branch_name','amount_in_gbp'],
                                   as_index=False).sum().sort_values(
                                       by='amount_in_gbp', ascending=False).head(10)
        figure = px.bar(groupby_df, x='branch_name', y=['amount_in_gbp'])
        return figure
    return {}


#dropdown filder callback to banches top 10
@app.callback(
    Output(component_id='best-performing-banches-dropdown-branch',
           component_property='options'),
    Input(component_id='best-performing-banches-dropdown-region',
          component_property='value'))
def update_option(branch_name):
    if branch_name is not None:
        my_df = pd.read_csv("data/newdata.csv")
        my_df = my_df[my_df['region'] == branch_name]
        return my_df.branch_name.unique()
    return []


# bottom 10branches
@app.callback(
    Output(component_id='branches-worst-graph', component_property='figure'),
    Input(component_id='worst-performing-banches-dropdown-branch',
          component_property='value')
    #Input(component_id='best-performing-banches-dropdown-city', component_property='value')
)
def show_viz(dropdown):
    if dropdown is not None:
        my_df = pd.read_csv("data/newdata.csv")
        groupby_df = my_df.groupby(['branch_name', 'amount_in_gbp'],
                                   as_index=False).sum().sort_values(
                                       by='amount_in_gbp',
                                       ascending=True).head(10)
        figure = px.bar(groupby_df, x='branch_name', y=['amount_in_gbp'])
        return figure
    return {}


#dropdown filder callback to banches top 10
@app.callback(
    Output(component_id='worst-performing-banches-dropdown-branch',
           component_property='options'),
    Input(component_id='worst-performing-banches-dropdown-region',
          component_property='value'))
def update_option(branch_name):
    if branch_name is not None:
        my_df = pd.read_csv("data/newdata.csv")
        my_df = my_df[my_df['region'] == branch_name]
        return my_df.branch_name.unique()
    return []

#SalesPerHour
@app.callback(
    Output(component_id='sales-per-hour-graph', component_property='figure'),
    Input(component_id='sales-per-hour--time-dropdown',
          component_property='value')
    #Input(component_id='sales-per-hour--time-dropdown', component_property='value')
)
def show_viz(dropdown):
    if dropdown is not None:
        data = pd.read_csv("data/newdata.csv")
        #my_df = pd.DataFrame(data=grades)
        figure = px.bar(data, x='branch_name', y=['hour'])
        return figure
    return {}


#dropdown filter callback for sales per hour
@app.callback(
    Output(component_id='sales-per-hour--time-dropdown',
           component_property='options'),
    Input(component_id='sales-per-hour-branch-dropdown',
          component_property='value'))
def update_option(hour):
    if hour is not None:
        my_df = pd.read_csv("data/newdata.csv")
        my_df = my_df[my_df['branch_name'] == hour]
        return my_df.hour.unique()
    return []


#topandbottombranches
@app.callback(
    Output(component_id='top-bottom-brances-graph',
           component_property='figure'),
    Input(component_id='top10-btn', component_property='n_clicks')
    #Input(component_id='bottom10-btn',component_property='n_clicks')
)
def show_viz(buttonPress):
    if buttonPress is not None:
        my_df = pd.read_csv("data/newdata.csv")
        branchdata = pd.read_excel('data/branch_expenses.xlsx')
        grouped_branch = branchdata['(operational_cost + staff_bonuses + misc_expenses + waste_cost)'] = branchdata.sum(axis=1)
        grouped_branch = branchdata.groupby(['branch_name'],as_index=False).sum().sort_values(by='branch_name',ascending=True).head(10)
        grouped_total = my_df['amount_in_gbp'] = my_df.sum(axis=1)
        grouped_total = my_df.groupby(['branch_name'],as_index=False).sum().sort_values(by='branch_name',ascending=True).head(10)
        table_join = pd.merge(grouped_branch,grouped_total,how='left',on=['branch_name'])
        table_join = table_join['final_total'] = table_join['(operational_cost + staff_bonuses + misc_expenses + waste_cost)'] - table_join['amount_in_gbp']
        #my_df = pd.DataFrame(data=grades)
        figure = px.bar(table_join, x='branch_name', y=['final_total']).head(10)
        return figure
    return {}


# run
if __name__ == '__main__':
    app.run_server(debug=True)
