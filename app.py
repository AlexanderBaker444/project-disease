#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import os
from pathlib import Path


# In[2]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# In[3]:


tabtitle = 'Disease'
myheading='Is Disease Worse in San Juan (Red) or Iquitos  (Blue)?'
neighborhood='San Juan'
color1='red'
color2='blue'
sourceurl = 'https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/'
githublink = 'https://github.com/AlexanderBaker/dash-scatterplot-disease'


# In[4]:


current=Path.cwd()
data_path=Path.joinpath(current,'data')
full_path_X=Path.joinpath(data_path,'dengue_labels_train.csv')
full_path_Y=Path.joinpath(data_path,'dengue_features_train.csv')
df_X=pd.read_csv(full_path_X)
df_Y=pd.read_csv(full_path_Y)


# In[8]:


full_set=pd.merge(df_X,df_Y)
full_set.columns


# In[14]:


full_set['city_color']=full_set.city.map({'sj':2,'iq':4})


# In[15]:


full_set['city'].value_counts()


# In[16]:


trace = go.Scatter(
    x = full_set['reanalysis_dew_point_temp_k'],
    y = full_set['station_precip_mm'],
    mode='markers',
    marker=dict(
        size=full_set['city_color'],
        color = full_set['total_cases'], # set color equal to a third variable
        colorscale=[color1, color2],
        colorbar=dict(title='total cases'),
        showscale=True
    )
)


# In[17]:


data = [trace]
layout = go.Layout(
    title = f'More Fevers are Seen in {neighborhood}!', # Graph title
    xaxis = dict(title = 'Temp of Dew'), # x-axis label
    yaxis = dict(title = 'Percipitation'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig = go.Figure(data=data, layout=layout)


# In[18]:


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.H1(myheading),
    dcc.Graph(
        id='figure-1',
        figure=fig
    ),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)

############ Deploy
if __name__ == '__main__':
    app.run_server()


# In[ ]:




