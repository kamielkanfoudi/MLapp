import streamlit as st
import pandas as pd 
import altair as alt
import pickle
import sklearn as sk



filename = "RFC_model-sv.sv"
model = pickle.load(open(filename,'rb'))

st.title('Predicting Heart Disease')
