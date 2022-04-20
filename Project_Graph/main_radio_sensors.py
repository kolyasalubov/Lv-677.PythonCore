import pymysql as MySQLdb
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import dash
from dash import dcc
from dash import html


conn = MySQLdb.connect(host="localhost", user="root", passwd="", db="sensors_redio")
cursor = conn.cursor()
cursor.execute('select Date, Input_value_ALPHA, Control_level_ALPHA, Input_value_BETA, Control_level_BETA from sensor_alpha_beta');
rows = cursor.fetchall()

df = pd.DataFrame( [[ij for ij in i] for i in rows] )
df.rename(columns={0: 'Date', 1: 'ALPHA_index', 2: 'CL_ALPHA', 3: 'BETA_index', 4: 'CL_BETA'}, inplace=True);
df = df.sort_values(['Date'], ascending=[1]);

fig = make_subplots(
    rows=3, cols=1,
    shared_xaxes=True,
    vertical_spacing=0.15,
    specs=[[{"type": "table"}],
           [{"type": "scatter"}],
           [{"type": "scatter"}]]
)

fig.add_trace(
        go.Scatter(
        x=df.Date,
        y=df['ALPHA_index'],
        text=['ALPHA_index'],
        mode='lines',
        name='ALPHA_index'
    ),
    row=3, col=1
)

fig.add_trace(
        go.Scatter(
            x=df.Date,
            y=df['CL_ALPHA'],
            mode='lines',
            text=['CL_ALPHA'],
            name='CL_ALPHA',
            line_color='red'
     ),
        row=2, col=1
)

fig.add_trace(
        go.Scatter(
            x=df.Date,
            y=df['BETA_index'],
            mode='lines',
            text=['BETA_index'],
            name='BETA_index'
     ),
        row=2, col=1
)

fig.add_trace(
        go.Scatter(
            x=df.Date,
            y=df['CL_BETA'],
            mode='lines',
            text=['CL_BETA'],
            name='CL_BETA',
            line_color='red'
     ),
        row=3, col=1
)

fig.add_trace(
    go.Table(
        header=dict(
            values=['Date', 'ALPHA_index', 'CL_ALPHA', 'BETA_index','CL_BETA'],
            font=dict(size=10),
            align="left"
        ),
        cells=dict(
            values=[df[k].tolist() for k in df.columns[0:]],
            align = "left")
    ),
    row=1, col=1
)

fig.update_layout(
    xaxis=dict(
        rangeselector=dict(
            buttons=list([
                dict(count=1,
                     label="1m",
                     step="month",
                     stepmode="backward"),
                dict(count=6,
                     label="6m",
                     step="month",
                     stepmode="backward"),
                dict(count=1,
                     label="YTD",
                     step="year",
                     stepmode="todate"),
                dict(count=1,
                     label="1y",
                     step="year",
                     stepmode="backward"),
                dict(step="all")
            ])
        ),
        rangeslider=dict(
            visible=False
        ),
        type="date"
    )    
)

fig.layout.yaxis1.update({'title': 'ALPHA_index, mBq/day'})
fig.layout.yaxis2.update({'title': 'BETA_index, mBq/day'})
fig.layout.xaxis2.update({'title': 'Date'})


fig.update_layout(
    height=650,
    showlegend=True, 
    title_text="Indexes of emissions of radioactive substances into the atmosphere - Alpha and Beta particles",
)

fig.show()

app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
 ])

app.run_server(debug=True, use_reloader=False)
