import streamlit as st
import os 
#cd "C:\Users\oisin\Documents\TURCAST Website"
#streamlit run Home.py

#The following code is used to modify the style of the website, the normal streamlit wesbsite is quite bland and repetitive. This code aims to change that, this code uses a small mix of CSS and HTML. I did not learn how to properly use these languages as I learned what I could add from the streamlit gallery.
st.markdown(
    """
    <style>
    .stApp {
        background-color: #dddddd;
    }

    #MainMenu {visibility: hidden;} 
    footer {visibility: hidden;}
    .block-container {padding-top: 0rem;}

    .top-banner {
        background-color: #003366;  
        color: white;
        padding: 12px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        letter-spacing: 1px;
        margin-bottom: 10px;
    }

    [data-testid="stSidebar"] {
        background-color: #003366;
    }

    [data-testid="stSidebar"] * {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

#Customising the top banner, earlier code put this onto a blue background. The blue theme of the website is tied to the blue seen alot with rain, turloughs and weather forecasting.
st.markdown(
    """
    <div class="top-banner">
        TURCAST ~ Real-Time Turlough Forecasting </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#00509e; color:white; padding:6px; text-align:center;">
        Update Logs </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.image(os.path.join(os.getcwd(), "static", "rain.jpg"), width='content')

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h1 style="text-align: center; color: #4B0076;">UPDATE LOGS</h1> </div>
    """,
    unsafe_allow_html=True
)

with st.expander(" Update Log Details"):
    st.write("""
    31/08/2025: TURCAST Website starts development on version 1.0, the Home, About and Update Log pages have been finished
    """)
    st.write("""
    25/11/2025: The forecast method of the TURCAST system has been finalised.
             """)
    st.write("""
    27/11/2025: The forecast page has been finished meaning TURCAST and the website are complete with plans to launch to the public in the next few weeks
             """)
