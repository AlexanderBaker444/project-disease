#!/usr/bin/env python
# coding: utf-8

# In[14]:


import pandas as pd
import os
from pathlib import Path


# In[15]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


# In[16]:


tabtitle = 'Disease'
myheading='Analysis of Fever Cases'
neighborhood='Placeholder'
color1='red'
color2='blue'
sourceurl = 'https://www.drivendata.org/competitions/44/dengai-predicting-disease-spread/'
githublink = 'https://github.com/AlexanderBaker444/dash-scatterplot-disease'


# In[17]:


current=Path.cwd()
data_path=Path.joinpath(current,'data')
full_path_X=Path.joinpath(data_path,'dengue_labels_train.csv')
full_path_Y=Path.joinpath(data_path,'dengue_features_train.csv')
df_X=pd.read_csv(full_path_X)
df_Y=pd.read_csv(full_path_Y)


# In[18]:


full_set=pd.merge(df_X,df_Y)
full_set.columns


# In[19]:


full_set.head()


# In[20]:


san_juan=full_set[full_set.city=='sj']
san_juan.head()


# In[21]:


iquitos=full_set[full_set.city=='iq']
iquitos.head()


# In[22]:


full_set['city_color']=full_set.city.map({'sj':5,'iq':10})


# In[23]:


full_set['city'].value_counts()


# In[31]:


trace = go.Scatter(
    x = full_set['reanalysis_air_temp_k'],
    y = full_set['reanalysis_relative_humidity_percent'],
    mode='markers',
    name='weather relations',
     marker=dict(
        color = full_set['city_color'], # set color equal to a third variable
        colorscale=[color1, color2],
        #colorbar=dict(title='Citys'),
        #showscale=True
    )
    
)

trace1=go.Scatter(
    y = san_juan['total_cases'],
    x = san_juan['reanalysis_dew_point_temp_k'],
    mode='markers',
    name='san juan'
)

trace2=go.Scatter(
    y = iquitos['total_cases'],
    x = iquitos['reanalysis_dew_point_temp_k'],
    mode='markers',
    name='iquitos'
)


# In[35]:


from plotly.subplots import make_subplots
import plotly.graph_objects as go


data = [trace]
data2 =[trace1]
data3 =[trace2]
layout = go.Layout(
    title = f'Larger homes cost more in {neighborhood}!', # Graph title
    xaxis = dict(title = 'Temp of Dew'), # x-axis label
    yaxis = dict(title = 'Disease Cases'), # y-axis label
    hovermode ='closest' # handles multiple points landing on the same vertical
)
fig=make_subplots(rows=3, cols=1,subplot_titles=("Comparing the Weather in Iquitos(Blue) and San Juan(Red)","Cases and Dew Temp in Iquitos", "Cases and Dew Temp in San Juan"))
fig.add_trace(
    trace,
    row=1, col=1
)

fig.add_trace(
    trace1,
    row=2, col=1
)

fig.add_trace(
    trace2,
    row=3, col=1
)


fig.update_xaxes(title_text="air temp", row=1, col=1)
fig.update_xaxes(title_text="dew temp", row=2, col=1)
fig.update_xaxes(title_text="dew temp", row=3, col=1)

# Update yaxis properties
fig.update_yaxes(title_text="humidity percentage", row=1, col=1)
fig.update_yaxes(title_text="total cases", row=2, col=1)
fig.update_yaxes(title_text="total cases", row=3, col=1)

fig.update_layout(height=1000, width=800, title_text="Subplots")
fig.show()


# In[34]:


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





# In[ ]:





# In[ ]:





# In[ ]:




