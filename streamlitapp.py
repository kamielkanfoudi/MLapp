
import streamlit as st
import pickle
from datetime import datetime


filename = "RFC_model-sv.sv"
model = pickle.load(open(filename,'rb'))

st.title('Predicting Heart Disease')
#test
