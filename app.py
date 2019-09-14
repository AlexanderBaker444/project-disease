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
myheading='Analysis of housing prices in Washington DC'
neighborhood='Placeholder'
color1='#04F9E6'
color2='#1B03B1'
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


full_set['city_color']=full_set.city.map({'sj':0,'iq':1})


# In[15]:


full_set['city'].value_counts()


# In[16]:


trace = go.Scatter(
    x = full_set['reanalysis_dew_point_temp_k'],
    y = full_set['total_cases'],
    mode='markers',
    marker=dict(
        size=8,
        color = full_set['city_color'], # set color equal to a third variable
        colorscale=[color1, color2],
        colorbar=dict(title='city'),
        showscale=True
    )
)


# In[17]:


data = [trace]
layout = go.Layout(
    title = f'Larger homes cost more in {neighborhood}!', # Graph title
    xaxis = dict(title = 'Temp of Dew'), # x-axis label
    yaxis = dict(title = 'Disease Cases'), # y-axis label
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




