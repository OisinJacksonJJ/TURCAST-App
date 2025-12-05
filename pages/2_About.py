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
        TURCAST ~ Real-Time Turlough Forecasting</div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#00509e; color:white; padding:6px; text-align:center;">
        About </div>
    """,
    unsafe_allow_html=True
)

st.sidebar.image(os.path.join(os.getcwd(), "static", "rain.jpg"), width='content')

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h1 style="text-align: center; color: #8bc34a;">ABOUT</h1>
        <h3 style="text-align: center; color: #444;">The story behind TURCAST, and where it is now</h3>
    </div>
    """,
    unsafe_allow_html=True
)

#Most of this page is just me talking about the project. Nothing special to note for the rest of this page.
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
    <p style="color:#333; font-size:16px;">
    The idea of a turlough forecasting system has been in the works since early 2024, the idea came around while a seperate project looking at turlough rainfall interactions was being presented at BT Young Scientist 2024. The idea stemmed from the question "How would you continue this project?".  </p>
        <p style="color:#333; font-size:16px;">
     Since then TURCAST has been in the works since the Summer of 2025, it is a personal project that works with publically available data from sources such as the Geological Survey of Ireland, Met Eireann and ECMWF's ERA5 datasheets.</p>
       <p style="color:#333; font-size:16px;">
     The TURCAST model is ran on python and extreme gradient boosting regression (XGBoost), TURCAST currently has a high accuracy, as it sits at an R² score of 0.9490 and an RMSE of 30cm. The model works off a variety of features such as rainfall, temperature, soil moisture and pressure to achieve this accuracy.</p>
    </div>
    """,
    unsafe_allow_html=True
)
st.image(os.path.join(os.getcwd(), "static", "TURCAST_accuracy.png"))
st.caption("TURCAST prediction graph as of Septmber 1st 2025")

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
     Looking at the graph the current problems with TURCAST are clear. Performance after dry periods is significantly worse then wet periods.

     However it is exceptionally good at capturing the turloughs depth when it is rising and when it should start falling, future versions of TURCAST will be tailored to try improve these flaws. </p>
 
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h3 style="text-align: center; color: #444;">Limitations of TURCAST</h3></div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
     TURCAST, while highly functional has some significant limitations to it being better:
     1. Public data for turloughs and weather data in the area is extremely limited. Hourly turlough depth data can be only be found from the GSI groundwater monitoring project, meaning TURCAST's scope of what turloughs it can work with is extremely limited, unfortunately that is the only available data for turloughs. There is a severe lack of soil and local weather data at the turloughs. At the moment TURCAST is running off of Met Eireann's hourly data at Athenry and Shannon, generally 50km from turloughs monitored by the GSI. </p>
    <p style="color:#333; font-size:16px;">
     2. Each and every turlough is extremely different. Numerous factors go into what makes a turlough drain and flood, this is due to a mix of under-ground cave networks and their capacity to drain and intake water. Other factors include soil content and their ability to absorb water. At the moment TURCAST only works with Lough Aleenaun, located in Carron Co. Clare which drains and floods rapidly multiple times a year, this is in contrast to others turloughs that have been tested such as Lough Ballycar in Shannon Co. Clare which remains in place or remains drained for much longer periods. TURCAST will have to be tuned to each turlough before accurate forecasts can be made. </p>
 
    """,
    unsafe_allow_html=True
)
st.image(os.path.join(os.getcwd(), "static", "Lough Aleenaun.png"))
st.caption("Lough Aleenaun's depth history, source: GSI Groundwater level data viewer")
st.image(os.path.join(os.getcwd(), "static", "Lough Ballycar.png"))
st.caption("Lough Ballycar's depth history, source: GSI Groundwater level data viewer")
st.caption("Note the difference in time between how fast they rise and drain")

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h3 style="text-align: center; color: #444;">The Developer behind TURCAST</h3> </div>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
        Oisín Jackson is the main developer behind TURCAST, and at the moment is the only developer working on this project.</p>
    """, unsafe_allow_html=True
)
st.image(os.path.join(os.getcwd(), "static", "YoungScientist2022.jpg"))
st.caption("Oisín Jackson and his 2022 Young Scientist project, source: Clare Champion")
st.markdown("""
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
        I have been doing Young Scientist projects since 2020 and TURCAST intends to be 6th and final entry to the competition, it is a continuation of the previously mentioned turlough rainfall interaction project titled "An Investigation into the Relationship Between Precipitation and Water Levels in the Burren". Coinicedently that project is a continuation of another project that to do with river depth. Both of these projects won the Met Eireann award at the Young Scientist competition.</p>
        <p style="color:#333; font-size:16px;">
        I have always had an interest in meteorology, it has been the strongest theme across all my Young Scientist projects. So I found it fitting to make my last project about meteorology, while taking it a step above the previous projects.</p>
        """, unsafe_allow_html=True
)
col1, col2 = st.columns(2)
with col1:
  st.image(os.path.join(os.getcwd(), "static", "YoungScientist2023.jpg"))
  st.caption("My BT Young Scientist 2023 Met Eireann award")

with col2:
  st.image(os.path.join(os.getcwd(), "static", "YoungScientist2024.jpg"))
  st.caption("My BT Young Scientist 2024 Met Eireann award")
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:0px;">
        <p style="color:#333; font-size:16px;">
        My ambitions for TURCAST at the moment are to make the model the best version possible but also to improve the quality of this website and improve the long term forecasting accuracy of TURCAST to make it a viable option for turlough forecasting in Ireland. The image below shows the TURCAST's accuracy when it comes to 48h forecasting</p>
    """, unsafe_allow_html=True
)
st.image(os.path.join(os.getcwd(), "static", "Screenshots.png"))
st.caption("The quality of the 48h forecast is noticably worse then the 6h forecast")