#1 chicken is sold for 15 dollars
#create a chicken app to ask users how many chicken users want to get
#show them the total amount
import streamlit as st
st.title ("CHICKEN HAVNEN")
st.image ("https://i.pinimg.com/736x/30/7c/d3/307cd3bdca76ed65cf5307973a5f3f3e.jpg", width=200)
st.write ("1 CHICKEN IS SOLD FOR 15 DOLLARS")
Original= 15
Chickens= st.number_input ("How many Chickens do you want to buy",1)
total= Original * Chickens
Totalamountbutton= st.button ("Show the total amount")
if Totalamountbutton:
  st. write ('The total amount is',total,'dollars')