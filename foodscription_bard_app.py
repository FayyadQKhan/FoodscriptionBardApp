from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message

os.environ["_BARD_API_KEY"] = "YwhglmGAiBMVRJuUFhOCDEfVRVTG2_5EQcGfjYU42EvoyAlu-Jq_nL-ODfQauMRzN56pXA."

# message = input("Ask: ")
# print(Bard().get_answer(str(message))['content'])

st.title("Foodscription - with Google Bard")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    return message

def user_input():
    input_text = st.text_input("Provide the image URL only: ")
    return input_text

if 'generate' not in st.session_state:
    st.session_state['generate'] = []

if 'past' not in st.session_state:
    st.session_state['past'] = []

user_text = user_input()
engineered_prompt = "identify the image in the link and give ingredients, foodgroup and portion size for each ingredient in table format: " + user_text

if user_text:
    output = response_api(engineered_prompt)
    st.session_state.generate.append(output)
    st.session_state.past.append(user_text)

if st.session_state['generate']:
    for i in range(len(st.session_state['generate'])-1,-1,-1):
        message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generate"][i], key = str(i))
