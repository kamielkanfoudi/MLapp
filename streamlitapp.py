
import streamlit as st
import pickle
from datetime import datetime
import sklearn

st.set_page_config(page_title="Predicting Heart Disease")
overview = st.container()
left, right = st.columns(2)
prediction = st.container()

with overview:
	st.title("Predicting Heart Disease")
	st.markdown("Predicting probability of getting heart disease")
filename = "RFC_model-sv.sv"
model = pickle.load(open(filename,'rb'))

#

Smoking = {0:"No",1:"Yes"}
AlcoholDrinking = {0:"No",1:"Yes"}
Stroke = {0:"No",1:"Yes"}
DiffWalking = {0:"No",1:"Yes"}
Sex = {0:"No",1:"Yes"}
PhysicalActivity = {0:"No",1:"Yes"}
Asthma = {0:"No",1:"Yes"}
KidneyDisease = {0:"No",1:"Yes"}
SkinCancer = {0:"No",1:"Yes"}
Race = {0:"White", 1:"Black", 2:"Asian", 3:"Hispanic", 4:"American Indian/Alaskan Native", 5:"Other"}
Diabetic = {0:"No",1:"Yes"}
GenHealth = {0:"Poor", 1:"Fair", 2:"Good", 3:"Very good", 4:"Excellent"}
AgeCategory = {0:"18-24", 1:"25-29", 2:"30-34", 3:"35-39", 4:"40-44", 5:"45-49", 6:"50-54", 7:"55-59", 8:"60-64", 9:"65-69", 10:"70-74", 11:"75-79", 12:"80 or older"}

with left:
	Smoking_radio = st.radio( "Smoking", list(Smoking.keys()), format_func=lambda x : Smoking[x] )
	

