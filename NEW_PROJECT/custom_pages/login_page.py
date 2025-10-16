import streamlit as st
import json

def load_users():
    with open("C:\\Users\\aayut\\OneDrive\\Desktop\\NEW_PROJECT\\user.json",'r') as f:
        return json.load(f)
    
def log():
    st.markdown("<h2 style= 'text-align: center;'>Login Page</h2>",unsafe_allow_html=True)

    username = st.text_input('Enter your username')
    password = st.text_input('enter you password',type = 'password')

    if st.button('Login') :
        user = load_users()
        if username in user and user[username]['password']==password:
            st.session_state.auth = True
            st.session_state.username = username
            st.session_state.role = user[username]['role']
            st.session_state.page = 'dashboard'
        else:
            st.error('Invalid username or password')