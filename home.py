import streamlit as st

tab1,tab2,tab3 = st.tabs(["About","Hobbies","Contact"])

with tab1:
    
    col1,col2 = st.columns([0.3,0.7])
    
    with col1:
        st.subheader("Pranav :sunglasses:")
    
    with col2:
        st.write("Hello, I am Pranav, a Junior Junior Developer. My parents find it challenging to manage and track their expenses. So, I created a website  to help them in tracking and managing their expenses. You can use this website to manage and track your expenses as well. I hope you all love it.")

with tab2:
     st.write("I love solving math problems and watching documentaries to learn about different things. Also, I'm into Soccer, enjoying the intensity and skills of the players.")

with tab3:
    st.write("Email : pranav.santhebennur@gmail.com@gmail.com")
    st.write("Website : https://harishmaths.home.blog/")
