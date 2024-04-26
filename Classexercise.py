#Timilehin visited a bookstore, 
#she wants to buy 2 exercise books, 5 pens, 10 erasers,
#two Oxford dictionaries, and 15 drawing books.
#The price for an exercise book is $10, pen is $5,
#eraser is $2, dictionary is $25 and drawing book is $10.
#Using streamlit show or display total amount that timilehin would spend.
import streamlit as st
st.title ("My Class Exercise")
st.write ("WELCOME TO BURJ KHALIFA")
Name= st.text_input ("Kindly input your name")
Books1=st.number_input ("How many books do you want to buy",1)
Pens1= st.number_input ("How many pens do you want to buy",1)
Erasers1= st.number_input ("How many erasers do you want to buy",1)
Dictionaries1= st.number_input ("How many dictionaries do you want to buy",1)
Drawingbooks1=st.number_input ("How many drawing books do you want to buy",1)
st.write ("Prices of Items bought")
Books2= 10
Pens2= 5
Erasers2= 2
Dictionaries2= 25
Drawingbooks2= 10
Total= Books1*Books2 + Pens1*Pens2 + Erasers1*Erasers2 + Dictionaries1*Dictionaries2 +Drawingbooks1*Drawingbooks2
Totalamountbutton= st.button ("Display total amount")
if Totalamountbutton:
 st.write ('The total amount is''$',Total,)
st.write ('Thank you for your patronage',Name,)