#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import streamlit as st
import plotly.express as px


# In[7]:


merged_df = pd.read_csv("merged.csv")


# In[9]:


st.title("サロンサーチ")
price_limit = st.slider("最低価格の上限", min_value=2000,
max_value=12000, step=200, value=6000)
score_limit = st.slider("人気スコアの下限", min_value=0.0,
max_value=35.0, step=2.0, value=5.0)


# In[11]:


filtered_df = merged_df[
(merged_df['price'] <= price_limit)&
(merged_df['pop_score'] >= score_limit)
]


# In[12]:


fig = px.scatter(
filtered_df,
x='pop_score',
y='price',
hover_data=['name_salon', 'access','star', 'review'],
title='人気スコアと最低カット価格の散布図'
)
st.plotly_chart(fig)


# In[14]:


selected_salon = st.selectbox('気になるサロンを選んで詳細を確認', filtered_df['name_salon'])

if selected_salon:
    url = filtered_df[filtered_df['name_salon'] == selected_salon]['link_detail'].values[0]
    st.markdown(f"[{selected_salon}のページへ移動]({url})", unsafe_allow_html=True)


# In[16]:


sort_key = st.selectbox(
"ランキング基準を選んでください",
("star", "pop_score", "review", "price", "設備")
)
ascending = True if sort_key == "price" else False


# In[17]:


st.subheader(f"{sort_key} によるサロンランキング（上位10件）")
ranking_df = filtered_df.sort_values(by=sort_key, ascending=ascending).head(10)
st.dataframe(ranking_df[["name_salon", "price", "pop_score", "star", "review",
"設備", "access"]])


# In[ ]:




