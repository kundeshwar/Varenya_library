
#-------------------------------------------------------import your labrary here 
import streamlit as st
from deta import Deta
import pandas as pd 
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu
#-------------------------------------------------side bar page 
st.set_page_config(page_title="Varenya", page_icon="📜", initial_sidebar_state="expanded")
#------------------------------------------------user_authencation
DETA_KEY = "d0mihef4jnu_xNrzt7qwxJyeVNX7wQKpP5ZoVuMAKocu"

# Initialize with a project key
deta_base = Deta(DETA_KEY)
config = {'credentials': {'usernames': {'Varenya': {'email': 'Varenya@gmail.com', 'name': 'Varenya', 'password': '$2b$12$AtB2jyQ3meDxVDyjSc6DD.TGnA0vsSch7FlECMe0OORxtrmab8mMy'}, 'Kundeshwar': {'email': 'Kundeshwar@gmail.com', 'name': 'Kundeshwaar', 'password': '$2b$12$beZVqTd/EnB62ORYj7/fCunr6r7Ykk8VHAjnwUG6OS86UExUL5j0e'}}}, 'cookie': {'expiry_days': 30, 'key': 'random_signature_key', 'name': 'random_cookie_name'}, 'preauthorized': {'emails': ['melsby@gmail.com']}}
authenticator = stauth.Authenticate(
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)

name, authentication_status, username = authenticator.login("Login", "main")
if authentication_status == False:
    st.error("Username/Passwords is incorrest")
if authentication_status == None:
    st.warning("Please enter your username and password")
if authentication_status ==True:
        #---------------------------------------------sidebat.button("Click Me 👈")
        authenticator.logout("Logout", "sidebar")
        st.sidebar.title(f"Welcome To")
        with st.sidebar:
            option = " Varenya 📜"
            st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)
            st.markdown("------------------")
            option_m_1 = option_menu("SELECT MODE", options=["View Data", "Add Data"], default_index=1)
            st.markdown("------------------")
            option_m = option_menu("SELECT SUBJECT(Data Storage)", options=["Hindi", "History", "Sanskrit", "Geography", "Other Books"], default_index=0)
            st.markdown("------------------")
        #--------------------------------had 
        # --- HIDE STREAMLIT STYLE ---
        hide_st_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    header {visibility: hidden;}
                    </style>
                    """
        st.markdown(hide_st_style, unsafe_allow_html=True)
            
        #---------------------------------------------headline for app
        option = " Varenya 📚"
        st.markdown(f"<h1 style='text-align: center;'><b>{option}</b></h1>",unsafe_allow_html=True)

        #--------------------------------------------get all infromation from database 
        

        #------------------------------------datafrems created
        
        #---------------------------------------------------------------hindi
        if option_m == "Hindi" and option_m_1 == "Add Data":
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            db_1 = deta_base.Base("Hindi_content")
            st.header("Add a Book")
            with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("Name of book"):
                    link_1_h = st.text_area("write here 🔽", placeholder="Enter name of book here ...")
                with st.expander("Author"):
                    link_2_h = st.text_area("write here 🔽", placeholder="Name of Author here ...")
                with st.expander("Description"):
                    link_3_h = st.text_area("write here 🔽", placeholder="Book Description ...")
                with st.expander("Link (English)"):
                    link_4_h = st.text_area("write here 🔽", placeholder="Link of Book here ...")
                with st.expander("Comments"):
                    link_5_h = st.text_area("write here 🔽", placeholder="Enter a comment here ...")
                with st.expander("other language link"):
                    link_6_h = st.text_area("write here 🔽", placeholder="Enter link of book here ...")
                
                submitted = st.form_submit_button("Save Data")
                if submitted:
                    st.write(f"Name of Book:- ", link_1_h)
                    st.write(f"Author:- ", link_2_h)
                    st.write(f"Description:- ", link_3_h)
                    st.write(f"English Link:- ", link_4_h)
                    st.write(f"Comments:- ", link_5_h)
                    st.write(f"other language link:- ", link_6_h)
                    db_1.put({"Name of Book": link_1_h,  "Author": link_2_h, "Description": link_3_h, "Link(English)": link_4_h, "comments": link_5_h, "other links": link_6_h})
                    st.success("Data saved")
        if option_m == "Hindi" and option_m_1 == "View Data":
            db_1 = deta_base.Base("Hindi_content")
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            st.header("Books")
            with st.dataframe():
                st.dataframe(db_1.fetch().items)
        #------------------------------------------------history
        if option_m == "History" and option_m_1 == "Add Data":
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            db_2 = deta_base.Base("History_content")
            st.header("Add a Book")
            with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("Name of book"):
                    link_1 = st.text_area("write here 🔽", placeholder="Enter name of book here ...")
                with st.expander("Author"):
                    link_2 = st.text_area("write here 🔽", placeholder="Name of Author here ...")
                with st.expander("Description"):
                    link_3 = st.text_area("write here 🔽", placeholder="Book Description ...")
                with st.expander("Link (English)"):
                    link_4 = st.text_area("write here 🔽", placeholder="Link of Book here ...")
                with st.expander("Comments"):
                    link_5 = st.text_area("write here 🔽", placeholder="Enter a comment here ...")
                with st.expander("other language link"):
                    link_6 = st.text_area("write here 🔽", placeholder="Enter link of book here ...")
                
                submitted = st.form_submit_button("Save Data")
                if submitted:
                    st.write(f"Name of Book:- ", link_1)
                    st.write(f"Author:- ", link_2)
                    st.write(f"Description:- ", link_3)
                    st.write(f"English Link:- ", link_4)
                    st.write(f"Comments:- ", link_5)
                    st.write(f"other language link:- ", link_6)
                    #database.insert_period_1(link_1, link_2, link_3, link_4, link_5, link_6)
                    db_2.put({"Name of Book": link_1,  "Author": link_2, "Description": link_3, "Link(English)": link_4, "comments": link_5, "other links": link_6})
                    st.success("Data saved")
        if option_m == "History" and option_m_1 == "View Data":
            db_2 = deta_base.Base("History_content")
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            st.header("Books")
            with st.dataframe():
                st.dataframe(db_2.fetch().items)
        #-----------------------------------------------------Geograpy 
        if option_m == "Geography" and option_m_1 == "Add Data":
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            db_3 = deta_base.Base("Geography")
            st.header("Add a Book")
            with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("Name of book"):
                    link_1_g = st.text_area("write here 🔽", placeholder="Enter name of book here ...")
                with st.expander("Author"):
                    link_2_g = st.text_area("write here 🔽", placeholder="Name of Author here ...")
                with st.expander("Description"):
                    link_3_g = st.text_area("write here 🔽", placeholder="Book Description ...")
                with st.expander("Link (English)"):
                    link_4_g = st.text_area("write here 🔽", placeholder="Link of Book here ...")
                with st.expander("Comments"):
                    link_5_g = st.text_area("write here 🔽", placeholder="Enter a comment here ...")
                with st.expander("other language link"):
                    link_6_g = st.text_area("write here 🔽", placeholder="Enter link of book here ...")
                
                submitted = st.form_submit_button("Save Data")
                if submitted:
                    st.write(f"Name of Book:- ", link_1_g)
                    st.write(f"Author:- ", link_2_g)
                    st.write(f"Description:- ", link_3_g)
                    st.write(f"English Link:- ", link_4_g)
                    st.write(f"Comments:- ", link_5_g)
                    st.write(f"other language link:- ", link_6_g)
                    #database.insert_period_3(link_1_g, link_2_g, link_3_g, link_4_g, link_5_g, link_6_g)
                    db_3.put({"Name of Book": link_1_g,  "Author": link_2_g, "Description": link_3_g, "Link(English)": link_4_g, "comments": link_5_g, "other links": link_6_g})
                    st.success("Data saved")
        if option_m == "Geography" and option_m_1 == "View Data":
            db_3 = deta_base.Base("Geography")
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            st.header("Books")
            with st.dataframe():
                st.dataframe(db_3.fetch().items)
        #---------------------------------------------others 
        if option_m == "Other Books" and option_m_1 == "Add Data":
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            db_4 = deta_base.Base("Other%20Books%20")
            st.header("Add a Book")
            with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("Name of book"):
                    link_1_ot = st.text_area("write here 🔽", placeholder="Enter name of book here ...")
                with st.expander("Author"):
                    link_2_ot = st.text_area("write here 🔽", placeholder="Name of Author here ...")
                with st.expander("Description"):
                    link_3_ot = st.text_area("write here 🔽", placeholder="Book Description ...")
                with st.expander("Link (English)"):
                    link_4_ot = st.text_area("write here 🔽", placeholder="Link of Book here ...")
                with st.expander("Comments"):
                    link_5_ot = st.text_area("write here 🔽", placeholder="Enter a comment here ...")
                with st.expander("other language link"):
                    link_6_ot = st.text_area("write here 🔽", placeholder="Enter link of book here ...")
                
                submitted = st.form_submit_button("Save Data")
                if submitted:
                    st.write(f"Name of Book:- ", link_1_ot)
                    st.write(f"Author:- ", link_2_ot)
                    st.write(f"Description:- ", link_3_ot)
                    st.write(f"English Link:- ", link_4_ot)
                    st.write(f"Comments:- ", link_5_ot)
                    st.write(f"other language link:- ", link_6_ot)
                    #database.insert_period_4(link_1_ot, link_2_ot, link_3_ot, link_4_ot, link_5_ot, link_6_ot)
                    db_4.put({"Name of Book": link_1_ot,  "Author": link_2_ot, "Description": link_3_ot, "Link(English)": link_4_ot, "comments": link_5_ot, "other links": link_6_ot})
                    st.success("Data saved")
        if option_m == "Other Books" and option_m_1 == "View Data":
            db_4 = deta_base.Base("Other%20Books%20")
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            st.header("Books")
            with st.dataframe():
                wata = db_4.fetch()
                st.dataframe(wata.items)
        #---------------------------------------------sankrit
        if option_m == "Sanskrit" and option_m_1 == "Add Data":
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            db_5 = deta_base.Base("Sanskrit")
            st.header("Add a Book")
            with st.form("entry_form", clear_on_submit=True):
                col1, col2 = st.columns(2)
                with st.expander("Name of book"):
                    link_1_s = st.text_area("write here 🔽", placeholder="Enter name of book here ...")
                with st.expander("Author"):
                    link_2_s = st.text_area("write here 🔽", placeholder="Name of Author here ...")
                with st.expander("Description"):
                    link_3_s = st.text_area("write here 🔽", placeholder="Book Description ...")
                with st.expander("Link (English)"):
                    link_4_s = st.text_area("write here 🔽", placeholder="Link of Book here ...")
                with st.expander("Comments"):
                    link_5_s = st.text_area("write here 🔽", placeholder="Enter a comment here ...")
                with st.expander("other language link"):
                    link_6_s = st.text_area("write here 🔽", placeholder="Enter link of book here ...")
                
                submitted = st.form_submit_button("Save Data")
                if submitted:
                    st.write(f"Name of Book:- ", link_1_s)
                    st.write(f"Author:- ", link_2_s)
                    st.write(f"Description:- ", link_3_s)
                    st.write(f"English Link:- ", link_4_s)
                    st.write(f"Comments:- ", link_5_s)
                    st.write(f"other language link:- ", link_6_s)
                    #database.insert_period_5(link_1_s, link_2_s, link_3_s, link_4_s, link_5_s, link_6_s)
                    db_5.put({"Name of Book": link_1_s,  "Author": link_2_s, "Description": link_3_s, "Link(English)": link_4_s, "comments": link_5_s, "other links": link_6_s})
                    st.success("Data saved")
        if option_m == "Sanskrit" and option_m_1 == "View Data":
            db_5 = deta_base.Base("Sanskrit")
            #database.insert_period_2(link_1, link_2, link_3, link_4, link_5, link_6)
            st.header("Books")
            with st.dataframe():
                st.dataframe(db_5.fetch().items)
