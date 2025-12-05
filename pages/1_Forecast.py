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
        TURCAST ~ Real-Time Turlough Forecasting
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#00509e; color:white; padding:6px; text-align:center;">
        Forecast
    </div>
    """,
    unsafe_allow_html=True
)


#The sidebar menu looked quite empty, this simple stock image makes it look more eye-catching and full.
st.sidebar.image(os.path.join(os.getcwd(), "static", "rain.jpg"), width='content')

#The website design has been set up, this section deals with the actual content of the page.
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h1 style="text-align: center; color: #FF4D00;">FORECAST</h1>
      
    </div>
    """,
    unsafe_allow_html=True
)
#When other turloughs are added to the system, I will add a dropdown menu here to select which turlough you want the forecast for.
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h4 style="text-align: center;">Current forecast for Lough Aleenaun </h1>
      
    </div>
    """,
    unsafe_allow_html=True
)
st.image(os.path.join(os.getcwd(), "static", "Forecast 10th august.png"), width="stretch")

#The page would be rather empty with just the image, so every forecast will have a small discussion with any comments on the forecast.
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h4 style="text-align: center;">Diccussion of forecast</h4>
      
    </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
       The current depths of the turlough will remain stable over the next six hours, little rainfall is expected to occur which is resulting in this stability.</p>
    """, unsafe_allow_html=True
)

