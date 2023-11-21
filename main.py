import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=600)

with col2:
    st.title("Abdul Rahman, Vakili")
    content = """
    Hi, I am Abdul Rahman Vakili! A Senior IT system engineer. 
    I did my master studies and later Ph.D in network and operating systems. 
    I enjoy software development and doing DevOps !     
    """
    st.info(content)
    #st.write(content)
content2 = """
Bellow you can find some or my works
"""
st.write(content2)
