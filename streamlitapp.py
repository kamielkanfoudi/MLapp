import streamlit as st
import pandas as pd 
import altair as alt
import sklearn 
import pickle



filename = "RFC_model-sv.sv"
model = pickle.load(open(filename,'rb'))

st.title('Predicting Heart Disease')
