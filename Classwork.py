import streamlit as st

st.text_input("What is your name")
st.write("Explore our library and choose your next read by selecting you genres")

G1,G2,G3,G4,G5 = st.columns(5)


with G1:
  
     if st.checkbox("Nonfiction"):
        Nonfictionbutton=st.button("Nonfiction")
        if Nonfictionbutton: 
             st.success("You chose Non fiction✅")

        
             st.image ("https://m.media-amazon.com/images/I/917tD-Bs6mL._AC_UY327_FMwebp_QL65_.jpg")
             st.write("The Finest Hours:$7.69")

     
             st.image ("https://m.media-amazon.com/images/I/61NDeqVUI1L._AC_UY327_FMwebp_QL65_.jpg")
             st.write("Beyond the Ark:$15.29")
        
  
             st.image ("https://m.media-amazon.com/images/I/81THR0uhcrL._AC_UY327_FMwebp_QL65_.jpg")
             st.write("The 57 Bus:$8.06")

     
             st.image ("https://m.media-amazon.com/images/I/61V-V38FCKL._AC_UY327_FMwebp_QL65_.jpg")
             st.write("Shoot Your Shot:$13.01")

    

with G2:

    if st.checkbox("Fiction"):
        Fictionbutton=st.button("Fiction")
        if Fictionbutton:
           st.success("You chose Fiction✅")

           st.image ("https://m.media-amazon.com/images/I/A1hpFZpYrfL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Escape Room:$8.50")

           st.image ("https://m.media-amazon.com/images/I/715exPJO5AL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("47 Days:$6.99")
           
           st.image ("https://m.media-amazon.com/images/I/51CE0FddcBL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Girl in The Blue Coat:$9.81")
           
           st.image ("https://m.media-amazon.com/images/I/81laL9p9foL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Game Change:$9.04")

with G3:
      
     if st.checkbox("Mystery"):
        Mysterybutton=st.button("Mystery")
        if Mysterybutton:
           st.success("You chose Mystery✅")

           st.image ("https://m.media-amazon.com/images/I/81cOaGbJ87L._AC_UY327_FMwebp_QL65_.jpg")
           if st.checkbox("One of us is Lying:$9.74"):

           st.image ("https://m.media-amazon.com/images/I/61bk97wG2-L._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Girl in Black:$7.99")
           
           st.image ("https://m.media-amazon.com/images/I/8128U7-gY9L._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Lake:$8.99")
           
           st.image ("https://m.media-amazon.com/images/I/61-eg9kdgiL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Shadow Jumper:$7.99")


with G4:
     
     if st.checkbox("Fantasy"):
        Fantasybutton=st.button("Fantasy")
        if Fantasybutton:
           st.success("FYou chose Fantasy✅")

           st.image ("https://m.media-amazon.com/images/I/71zoeYwqvtL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Girl who Looked Beyond the Stars:$9.24")

           st.image ("https://m.media-amazon.com/images/I/91z2qkJKyIL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Six of Crows:$17.48")
           
           st.image ("https://m.media-amazon.com/images/I/81knCJ7POzL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Vampire Academy:$38.06")
           
           st.image ("https://m.media-amazon.com/images/I/71WXdyJncPL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Darkest Minds:$24.81")

with G5:
     
     if st.checkbox("Sci-fi"):
         Scifibutton=st.button("Sci-fi")
         if Scifibutton:
           st.success("You chose Sci-fi✅")

           st.image ("https://m.media-amazon.com/images/I/61d-axe5vfL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Knowledge Seeker:$13.49")

           st.image ("https://m.media-amazon.com/images/I/81c-YM5CHyL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("The Shadow and Bone Trilogy:$17.29")
           
           st.image ("https://m.media-amazon.com/images/I/71-1WBgjGoL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Dune:$9.99")
           
           st.image ("https://m.media-amazon.com/images/I/81xxSRsPPuL._AC_UY327_FMwebp_QL65_.jpg")
           st.write("Scythe:$10.99")








        

