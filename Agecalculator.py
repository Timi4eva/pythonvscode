import streamlit as st #this is used to build a page for my python project
st.title("My Age Calculator")
name= st.text_input("What is your name")
yob= st.number_input("What is your year of birth",1)
current=st.number_input("What is the current year",1)
age= current-yob
st.write('Your age is',age,'years old')