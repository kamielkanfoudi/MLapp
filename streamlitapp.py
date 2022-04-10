
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

#test

Smoking = {0:"No",1:"Yes"}
AlcoholDrinking = {0:"No",1:"Yes"}
Stroke = {0:"No",1:"Yes"}
DiffWalking = {0:"No",1:"Yes"}
Sex = {0:"Male",1:"Female"}
PhysicalActivity = {0:"No",1:"Yes"}
Asthma = {0:"No",1:"Yes"}
KidneyDisease = {0:"No",1:"Yes"}
SkinCancer = {0:"No",1:"Yes"}
Race = {0:"White", 1:"Black", 2:"Asian", 3:"Hispanic", 4:"American Indian/Alaskan Native", 5:"Other"}
Diabetic = {0:"No",1:"Yes"}
GenHealth = {0:"Poor", 1:"Fair", 2:"Good", 3:"Very good", 4:"Excellent"}
AgeCategory = {0:"18-24", 1:"25-29", 2:"30-34", 3:"35-39", 4:"40-44", 5:"45-49", 6:"50-54", 7:"55-59", 8:"60-64", 9:"65-69", 10:"70-74", 11:"75-79", 12:"80 or older"}

with left:
	Smoking_radio = st.radio( "Have you smoked at least 100 cigarettes in your entire life?", list(Smoking.keys()), format_func=lambda x : Smoking[x] )
	AlcoholDrinking_radio = st.radio( "Do you drink alcohol heavily? (Heavy drinkers (adult men having more than 14 drinks per week and adult women having more than 7 drinks per week)", list(AlcoholDrinking.keys()), format_func=lambda x : AlcoholDrinking[x])
 	Stroke_radio = st.radio( "Did you have a stroke in the past?", list(Stroke.keys()), format_func=lambda x : Stroke[x] )
  	DiffWalking_radio = st.radio( "Do you have serious difficulty walking or climbing stairs?", list(DiffWalking.keys()), format_func=lambda x : DiffWalking[x] )
  	Sex_radio = st.radio( "What is your gender?", list(Sex.keys()), format_func=lambda x : Sex[x] )
  	PhysicalActivity_radio = st.radio( " Have you been engaging in physical activity or exercise during the past 30 days other than your regular job?", list(PhysicalActivity.keys()), format_func=lambda x : PhysicalActivity[x] )
	Age_radio = st.radio( "Age", list(AgeCategory.keys()), format_func=lambda x : AgeCategory[x] )
	GenHealth_radio = st.radio( "Would you say that in general your health is...", list(GenHealth.keys()), format_func=lambda x : GenHealth[x] )
	Diabetic_radio = st.radio( "Diabetic", list(Diabetic.keys()), format_func=lambda x : Diabetic[x] )
	Race_radio = st.radio( "Race", list(Race.keys()), format_func=lambda x : Race[x] )
	SkinCancer_radio = st.radio( "Have you had Skin Cancer?", list(SkinCancer.keys()), format_func=lambda x : SkinCancer[x] )
	KidneyDisease_radio = st.radio( "Have you had a Kidney Disease?", list(KidneyDisease.keys()), format_func=lambda x : KidneyDisease[x] )
	Asthma_radio = st.radio( "Do you have asthma?", list(Asthma.keys()), format_func=lambda x : Asthma[x] )
					 
					 
					 

