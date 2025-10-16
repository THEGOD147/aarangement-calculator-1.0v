import streamlit as st
from custom_pages import login_page as login
from custom_pages import dashboard
import time
import base64
"""
gif_path = "intro.gif"
if "intro"not in st.session_state:
    st.session_state.intro = False
    st.session_state.intro_st_time = time.time()

if not st.session_state.intro:
    passed_time = time.time() - st.session_state.intro_st_time
     
    if passed_time < 3:
        with open(gif_path,"rb") as f:
            gif_bytes =f.read()
            gif_base64 = base64.b64encode(gif_bytes).decode()

        html=       f"""
                    <style>
                    .fullcreeen{{
                    position: fixed;
                    top=0; left=0;
                    width:100vw;
                    height:100vh;
                    display:flex:
                    justify-content: center;
                    align-items: center;
                    background-colour: black;
                    z-index:9999;
                    }}
                    .fullscreen img{{
                    width:100vw;
                    height;100vh;
                    object-fit: cover;
                    }}
                    </style>
                    <div class="fullscreen">
                      <img src="data:image/gif;base64,{gif_base64}"/>
                    </div>
                    """
        st.components.v1.html(html , height=800)
        time.sleep(3)
        st.session_state.intro = True
        st.rerun()
        """
    
if 'auth' not in st.session_state:
    st.session_state.auth = False
if 'page' not in st.session_state:
    st.session_state.page = 'login'

if not st.session_state.auth:
    login.log()
else:
    if st.session_state.page == 'dashboard':

         dashboard.show()
