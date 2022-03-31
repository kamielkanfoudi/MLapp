import streamlit as st
import pandas as pd 
import altair as alt
import pickle


st.set_page_config(page_title="Predicting Heat Disease with Ensemble Models")
overview = st.container()
left, right = st.columns(2)
prediction = st.container()

sex_d = {0:"Female",1:"Male"}
alc_d = {0:"No",1:"Yes"}
race_d = {0:"White", 1:"Black", 2:"Asian", 3:"Hispanic", 4:"American Indian/Alaskan Native", 5: "Other"}


