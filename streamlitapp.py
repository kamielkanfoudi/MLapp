import streamlit as st
import pandas as pd 
import altair as alt
import pickle


st.set_page_config(page_title="Predicting Heat Disease with Ensemble Models")
overview = st.container()
left, right = st.columns(2)
prediction = st.container()

