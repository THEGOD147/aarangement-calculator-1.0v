import streamlit as st


def show():
     
     

     col1, col2 = st.columns([6, 1])
     with col1:
          st.write("")
     with col2:
               if st.button('Logout'):
                    st.session_state.auth = False
                    st.session_state.page = 'login'
                    st.rerun()

     username = st.session_state.get('username', '')
     st.markdown("<h2 style='text-align:center;'>Dashboard</h2>", unsafe_allow_html=True)
     st.markdown('---')
     st.markdown(
          f"<h2 style='text-align:center;font-size:28px;'>welcome, <strong>{username}</strong></h2>",
          unsafe_allow_html=True,
     )

     st.markdown("<br>",unsafe_allow_html=True)
     
     for label, key, colour in [
           ('Add Members','Add members','LightBlue'),
           ('Generate Arrangement time table','Generate','lightgreen'),
           ('Members Attendence','Attendence','lightpurple')
           ]:
              left, centre, right = st.columns([1, 2, 1])
              with centre:
                     if st.button(label,key=key):
                         st.markdown("<div style='text-align:center;'>", unsafe_allow_html = True)
                         st.toast(f"{label} feature coming soon!", icon='🔜')
                         st.markdown("</div>", unsafe_allow_html = True)
              st.markdown("<br>", unsafe_allow_html =True)
              


     