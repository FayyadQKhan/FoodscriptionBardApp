import streamlit as st
import bard

def get_bard_response(query):
  response = bard.query(query)
  return response

st.title("Bard in Streamlit")

query = st.text_input("Enter a query:")

response = get_bard_response(query)

st.write(response)
