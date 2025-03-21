import streamlit as st
import pandas

col1, col2 = st.columns(2)

with col1:
  st.image("Images/profile.png")

with col2:
  st.title("Sima Dhimal")
  content = """Hi There!, I am a python Programmer, living in Hannover, Germany.
               I am Studying Computer Science and I am excited to build some cool Python Apps. 
               """

  st.write(content)

content = """Below is the Projects I have Build. Feel free to contact me!"""

st.write(content)

df = pandas.read_csv("data.csv", sep=";")
col3, col4 = st.columns(2)
with col3:
  for index, row in df[10:].iterrows():
    st.header(row["title"])
    st.write(row["description"])
    st.image("images/" + row["image"])
    st.write(f"[Source Code]({row['url']})")

with col4:
  for index, row in df[:10].iterrows():
    st.header(row["title"])
    st.write(row["description"])
    st.image("images/" + row["image"])
    st.write(f"[Source Code]({row['url']})")