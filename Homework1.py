#Timilehin visited a Fruitstore, 
#she wants to buy 2 apples, 5 bananas, 
#10 watermelons, 2 oranges, and 15 pawapaws.
#The price for annapple is $5, banana is $5,
# melon is $20, orange is $5 and pawpaw is $10. 
# Using streamlit show or display total amount that timilehin would spend.
import streamlit as st
st.title ("My Homework")
st.write ("WELCOME TO FRESH FRUITSTORE")
Name= st.text_input ("Kindly input your name")
Apples1=st.number_input ("How many apples do you want to buy",1)
Bananas1= st.number_input ("How many bananas do you want to buy",1)
Watermelons1= st.number_input ("How many watermelons do you want to buy",1)
Oranges1= st.number_input ("How many oranges do you want to buy",1)
Pawpaws1=st.number_input ("How many pawpaws do you want to buy",1)
st.write ("Prices of Items bought")
Apples2= 5
Bananas2= 5
Watermelons2= 20
Oranges2= 5
Pawpaws2= 10
Total= Apples1*Apples2 + Bananas1*Bananas2 + Watermelons1*Watermelons2 + Oranges1*Oranges2 +Pawpaws1*Pawpaws2
Totalamountbutton= st.button ("Display total amount")
if Totalamountbutton:
 st.write ('The total amount is''$',Total,)
st.write ('THANK YOU FOR YOUR PATRONAGE!!😁',Name,)
st.write ('COME AGAIN!!☺️',Name,)