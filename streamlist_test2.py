#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

# Sample data
data = {
    'Date': pd.date_range(start='2022-01-01', end='2022-01-10'),
    'Value1': np.random.randn(10).cumsum(),
    'Value2': np.random.randn(10).cumsum(),
    'Category': ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A']
}
df = pd.DataFrame(data)

# Streamlit app
st.title('Dynamic Dashboard with Streamlit')

# Sidebar for user input
selected_visualization = st.sidebar.selectbox('Select Visualization', ['Line Chart', 'Bar Chart', 'Scatter Plot', 'Box Plot', 'Histogram'])

# Filter data based on user selection
if selected_visualization == 'Line Chart':
    st.subheader('Line Chart')
    fig, ax = plt.subplots()
    for category in df['Category'].unique():
        subset = df[df['Category'] == category]
        ax.plot(subset['Date'], subset['Value1'], label=f'Category {category}')
    ax.legend()
    st.pyplot(fig)

elif selected_visualization == 'Bar Chart':
    st.subheader('Bar Chart')
    fig, ax = plt.subplots()
    for category in df['Category'].unique():
        subset = df[df['Category'] == category]
        ax.bar(subset['Date'], subset['Value1'], label=f'Category {category}')
    ax.legend()
    st.pyplot(fig)

elif selected_visualization == 'Scatter Plot':
    st.subheader('Scatter Plot')
    fig = px.scatter(df, x='Date', y='Value1', color='Category')
    st.plotly_chart(fig)

elif selected_visualization == 'Box Plot':
    st.subheader('Box Plot')
    fig = px.box(df, x='Category', y='Value1', points='all')
    st.plotly_chart(fig)

elif selected_visualization == 'Histogram':
    st.subheader('Histogram')
    fig, ax = plt.subplots()
    for category in df['Category'].unique():
        subset = df[df['Category'] == category]
        ax.hist(subset['Value1'], bins=20, alpha=0.5, label=f'Category {category}')
    ax.legend()
    st.pyplot(fig)

