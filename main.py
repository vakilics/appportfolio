import streamlit as st

#3rd party library to use csv data..
import pandas
#Note: if not use pandas, then will have to do like:
#with open("data.csv") as file:
#    content = file.read()
#    print(content)

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

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
Bellow you can find some cool projects to click start coding ....
"""
st.write(content2)

#col3, col4 = st.columns(2)
#To make empty space between two columns:
col3 , empty_col, col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():  #first 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"], width=200)
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows(): #last 10 rows
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"]) # generates the path to image: eg: images/1.png
