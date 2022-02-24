# imports
import dash
from dash import html


# setup
app = dash.Dash(__name__, title='My First Dash Deployment')
server = app.server

# Layout
app.layout = html.Div([
    html.H3('My First Deployment!!!', style={
        'color': 'aliceblue',
        'padding-top': '50px',
        'text-align': 'center'
    }),
    html.P('Congratulations, you have successfully deployed your first dash app', style={
        'color': 'red',
        'text-align': 'center',
        'padding-top': '50px'
    })
])


# run
if __name__ == '__main__':
    app.run_server(debug=True)
