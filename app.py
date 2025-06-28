#!/usr/bin/env python
# coding: utf-8

# In[3]:


import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

# Loading  Data
url = "https://data.cityofnewyork.us/resource/2td3-mfek.json"
df = pd.read_json(url)

# Converting numerical columns
df['unduplicated_clients'] = pd.to_numeric(df['unduplicated_clients'], errors='coerce')
df.dropna(subset=['unduplicated_clients', 'borough'], inplace=True)

# Dash app setup
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server 

app.layout = html.Div([
    html.H1("NYC Senior Services Dashboard (Dash Plotly)", style={"textAlign":"center"}),
    html.Hr(),
    html.P("Choose borough of interest:"),
    html.Div(html.Div([
        dcc.Dropdown(id='borough-dropdown', clearable=False,
                     value="BROOKLYN",
                     options=[{'label': x, 'value': x} for x in
                              df["borough"].dropna().unique()]),
    ],className="two columns"),className="row"),

    html.Div(id="visual-output", children=[]),
])

@app.callback(Output(component_id="visual-output", component_property="children"),
              Input(component_id="borough-dropdown", component_property="value"),
)
def update_graphs(selected_borough):
    filtered_df = df[df["borough"] == selected_borough]

    # BAR: Total Clients by Program Type
    fig_bar = px.bar(filtered_df.groupby("program_type")["unduplicated_clients"].sum().reset_index(),
                     x="program_type", y="unduplicated_clients",
                     title="Total Clients by Program Type")

    # ZIP BAR 
    zip_counts = filtered_df['zip_code'].value_counts().reset_index()
    zip_counts.columns = ['zip_code', 'program_count']
    fig_zip = px.bar(zip_counts, x='zip_code', y='program_count',
                     labels={'zip_code': 'Zip Code', 'program_count': 'Program Count'},
                     title='Programs Count by Zip Code')

    # PIE CHART
    pie_df = filtered_df['program_type'].value_counts().reset_index()
    pie_df.columns = ['program_type', 'count']
    fig_pie = px.pie(pie_df, names='program_type', values='count', title='Program Type Distribution')

    # BOX PLOT
    fig_box = px.box(filtered_df, x='program_type', y='unduplicated_clients',
                     title='Client Distribution by Program Type')

    # GEO SCATTER
    fig_map = px.scatter_mapbox(filtered_df, lat="latitude", lon="longitude",
                                size="unduplicated_clients", color="program_type",
                                hover_name="program_name", zoom=9,
                                mapbox_style="open-street-map", title="Program Locations in Borough")

    return [
        html.Div([
            html.Div([dcc.Graph(figure=fig_bar)], className="six columns"),
            html.Div([dcc.Graph(figure=fig_zip)], className="six columns"),
        ], className="row"),
        html.H2("Program Overview", style={"textAlign":"center"}),
        html.Hr(),
        html.Div([
            html.Div([dcc.Graph(figure=fig_pie)], className="six columns"),
            html.Div([dcc.Graph(figure=fig_box)], className="six columns"),
        ], className="row"),
        html.Div([
            html.Div([dcc.Graph(figure=fig_map)], className="twelve columns"),
        ], className="row"),
    ]

if __name__ == '__main__':
    app.run(debug=False)


# In[ ]:




