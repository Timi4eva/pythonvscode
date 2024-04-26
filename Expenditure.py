import streamlit as st
st.title("Diamond Bank App")
st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQPtHPPpwwUunS8EAnBbyi3ABThh1XhsI0cDppsKTaArQ&s",width=1100)
st.subheader("Hello, welcome to the Diamond Bank app")

Name=st.text_input("Input your name")
st.text_input("Input your password")
Loginbutton= st.button("LOG IN")  
if Loginbutton:
    st.success("You are Logged in ✅")

Current=st.number_input("How much do you have currently",1)
Spent=st.number_input("How much have you spent",1)
Total=Current-Spent 
Totalamountleftbutton= st.button("Your total amount:")
if Totalamountleftbutton:
    st.write(f'{Name}, you have {Total} dollars left')
