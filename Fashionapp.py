#title
#-image
#-categories
#Men's Fashion
#Women's Fashion
#Children's Fashion
#(each category must havedifferent types of unique items and the prices 
#like shirts(long sleeves,short, round nexk, polo etc), boxers, trousers, shoes, bags etc)
#Show the total bill

import streamlit as st
st.set_page_config (layout="wide")
total = 0
st.title("Lalekside Boutique")
st.image("https://www.google.com/imgres?q=boutiques%20logo&imgurl=https%3A%2F%2Fimages.freecreatives.com%2Fwp-content%2Fuploads%2F2016%2F09%2Fboutique-logos.jpg&imgrefurl=https%3A%2F%2Fwww.freecreatives.com%2Flogos%2Fboutique-logo.html&docid=yWvZZtfWxNMCCM&tbnid=mrutWiDA03_FXM&vet=12ahUKEwikpeuDic6FAxXTQ0EAHTbVAJYQM3oFCIEBEAA..i&w=600&h=340&hcb=2&ved=2ahUKEwikpeuDic6FAxXTQ0EAHTbVAJYQM3oFCIEBEAA")
st.subheader("Our varieties are:")
st.title("Men's Fashion")
st.image("")

MF1,MF2,MF3,MF4 = st.columns(4)


with MF1:
    st.image("")
    if st.checkbox("Denim Jeans:30"):
        st.success("You bought Denim Jeans✅")
        total += 30
        
with MF2:
    st.image("")
    if st.checkbox("White Shirts:$10"):
        st.success("You bought White Shirts✅")
        total += 10

with MF3:
    st.image("")
    if st.checkbox("Shorts:$15"):
        st.success("You bought Shorts✅")
        total += 15

with MF4:
    st.image("")
    if st.checkbox("Tuxedo:$100"):
        st.success("You bought Tuxedo✅")
        total += 100
        

st.title("Women's Fashion")
st.image("")

WF1,WF2,WF3,WF4 = st.columns(4)

with WF1:
    st.image("")
    if st.checkbox("Accessories:$10"):
        st.success("You bought Accessories✅")
        total += 10

with WF2:
    st.image("")
    if st.checkbox("Dresses:$20"):
        st.success("You bought Dresses✅")
        total += 20

with WF3:
    st.image("")
    if st.checkbox("T-Shirts:$25"):
       st.success("You bought T-Shirts✅")
       total += 25

with WF4:
    st.image("")
    if st.checkbox("Skirts:$18"):
       st.success("You bought Skirts✅")
       total += 18


st.title("Children's Fashion")
st.image("")

CF1,CF2,CF3,CF4 = st.columns(4)

with CF1:
    st.image("")
    if st.checkbox("Joggers:$10"):
        st.success("You bought Joggers✅")
        total += 10

with CF2:
    st.image("")
    if st.checkbox("Skorts:$10"):
        st.success("You bought Skorts✅")
        total += 10

with CF3:
    st.image("")
    if st.checkbox(" Full body Boy Suit:$50"):
        st.success("You bought Boy Suit✅")
        total += 50

with CF4:
    st.image("")
    if st.checkbox(" Cheerleading Set:$30"):
        st.success("You bought Cheer Set✅")
        total += 30











