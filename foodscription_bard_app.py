from bardapi import Bard
import os
import streamlit as st
from streamlit_chat import message
import json
# import re


os.environ["_BARD_API_KEY"] = "YwhglmGAiBMVRJuUFhOCDEfVRVTG2_5EQcGfjYU42EvoyAlu-Jq_nL-ODfQauMRzN56pXA."

# message = input("Ask: ")
# print(Bard().get_answer(str(message))['content'])
# cache = memory.Memory()

st.title("Foodscription - with Google Bard")

def response_api(prompt):
    message = Bard().get_answer(str(prompt))['content']
    # cache[prompt] = message
    return message

def user_input():
    input_text = st.text_input("Paste Ingredients: ")
    return input_text

# def extract_substring(string):
#   """Extracts a substring from a given string that starts with '{' and ends with '}'.

#   Args:
#     string: The string to extract the substring from.

#   Returns:
#     The extracted substring.
#   """

#   pattern = r"{*}"
#   match = re.search(pattern, string)

#   if match is None:
#     return None

#   return match

# if 'generate' not in st.session_state:
#     st.session_state['generate'] = []

# if 'past' not in st.session_state:
#     st.session_state['past'] = []

ingredient = user_input()
# ingredient = input('Enter ingredient: ')
engineered_prompt = "You are a json only output machine give me ingredient and its corresponding foodgroup in the format {ingredient:foodgroup} where given ingredient is key and foodgroup is value: " + ingredient
output = ''
if ingredient:
    output = response_api(engineered_prompt)
    start = output.find('{')
    end = output.find('}')
    json_ = output[start:end+1]
    st.write(output)
    st.write('OK')
    st.write(json_)
   
    # json_ = json.loads(json_)
    # output = str(output)
    # for line in output:
    #     json_expr = "{"+line.partition("{")[2]
    #     output = json.loads(json_expr)
    
    # st.session_state.generate.append(output)
    # st.session_state.past.append(ingredient)

    # print(type(output))


# print(json_)
# print(type(json_))
# print(json_)

# if st.session_state['generate']:
#     for i in range(len(st.session_state['generate'])-1,-1,-1):
#         message(st.session_state["past"][i], is_user=True, key=str(i) + '_user')
#         message(st.session_state["generate"][i], key = str(i))
