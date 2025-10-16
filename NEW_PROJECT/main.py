import streamlit as st
from custom_pages import login_page as login
from custom_pages import dashboard

    
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'page' not in st.session_state:
    st.session_state.page = 'login'

if not st.session_state.auth:
    login.log()
else:
    if st.session_state.page == 'dashboard':

         dashboard.show()


