#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd 

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots


# In[2]:


ru_losses_per = pd.read_csv('D:/Dataset/War/russia_losses_personnel.csv')


# In[3]:


ru_losses_eq = pd.read_csv('D:/Dataset/War/russia_losses_equipment.csv')


# In[4]:


ru_losses_per.head()


# In[5]:


ru_losses_eq.head()


# In[6]:


ru_losses_per.info()


# In[7]:


ru_losses_eq.info()


# In[8]:


ru_losses_per.drop('POW',axis=1,inplace=True)


# In[9]:


ru_losses_per.describe()


# In[10]:


ru_losses_eq.describe()


# In[11]:


fig=px.line(ru_losses_eq,x='date',y=['drone','aircraft','helicopter'],template='ggplot2',title='<b>Russia Air Equipment losses')
fig.show()


# In[12]:


names=['aircraft','helicopter','drone']
values=[ru_losses_eq['aircraft'].max(),ru_losses_eq['helicopter'].max(),ru_losses_eq['drone'].max()]
fig=px.pie(names=names,values=values,hole=.7,template='ggplot2')
fig.update_layout(title_x=0.5,legend=dict(orientation='h',yanchor='bottom',y=1.02,xanchor='right',x=1))


# In[13]:


x, y = ru_losses_per['date'], ru_losses_per['personnel']

fig = go.Figure()

fig.add_trace(go.Scatter(x=x, y=y,
                    mode='lines+markers',
                    name='lines+markers'))

fig.show()


# In[14]:


x = ru_losses_eq['date']
y0 = ru_losses_eq['tank']
y1 = ru_losses_eq['field artillery']
y2 = ru_losses_eq['APC']
y3 = ru_losses_eq['military auto']

fig = go.Figure()


# In[15]:


fig.add_trace(go.Scatter(x=x, y=y0,
                    mode='lines+markers',
                    name='Tank'))


# In[16]:


fig.add_trace(go.Scatter(x=x, y=y1,
                    mode='lines+markers',
                    name='Field artillery'))


# In[17]:


fig.add_trace(go.Scatter(x=x, y=y2,
                    mode='lines+markers',
                    name='APC'))


# In[18]:


fig.add_trace(go.Scatter(x=x, y=y3,
                    mode='lines+markers',
                    name='Military auto'))


# In[19]:


fig.update_layout(legend_orientation="h",
                  legend=dict(x=0, y=1, traceorder="normal"),
                  title="Weapons: Ground, Other",
                  xaxis_title="Date",
                  yaxis_title="Weapons ",
                  margin=dict(l=0, r=0, t=30, b=0))
fig.show()

