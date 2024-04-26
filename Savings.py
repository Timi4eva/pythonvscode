#Savings App
#Create a python program to ask how much a user wants to save on Monday, Tuesday, up to sunday  
#Add up all his savings
#Show him the total savings for the week
import streamlit as st
st.title ("My Savings App")
name= st.text_input ("What is your name")
Monday= st.number_input ("How much do you want to save on Monday",1)
Tuesday= st.number_input ("How much do you want save on Tuesday",1)
Wednesday= st.number_input ("How much do you want to save on Wednesday",1)
Thursday= st.number_input ("How much do you want to save on Thursday",1)
Friday= st.number_input ("How much do you want to save on Friday",1)
Saturday= st.number_input ("How much do you want to save on Saturday",1)
Sunday= st.number_input ("How much do you want to save on Sunday",1)
total= Monday+Tuesday+Wednesday+Thursday+Friday+Saturday+Sunday

savingsbutton = st.button("Show my saving")

if savingsbutton:
    st.write ('Your total savings for the week is',total,'dollars')