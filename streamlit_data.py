#!/usr/bin/env python
# coding: utf-8

# In[3]:


import streamlit as st
import pandas as pd
import numpy as np


# In[7]:


st.title('This is my first app!')
st.write('This is a table')
dataframe = pd.DataFrame(np.random.randn(10, 20),
  columns = ('col %d' % i
    for i in range(20)))
st.write(dataframe)
st.write('This is a line_chart.')
st.line_chart(dataframe)


# In[6]:


st.write('This is a area_chart.')
st.area_chart(dataframe)
st.write('This is a bar_chart.')
st.bar_chart(dataframe)


# In[8]:


st.write('Map data')
data_of_map = pd.DataFrame(
  np.random.randn(1000, 2) / [60, 60] + [36.66, -121.6],
  columns = ['latitude', 'longitude'])
st.map(data_of_map)


# In[ ]:




