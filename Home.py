import streamlit as st
import os
#cd "C:\Users\oisin\Documents\TURCAST Website"
#streamlit run Home.py

#The following code is used to modify the style of the website, the normal streamlit wesbsite is quite bland and repetitive. This code aims to change that, this code uses a small mix of CSS and HTML. I did not learn how to properly use these languages as I learned what I could add from the streamlit gallery.
st.markdown(
    """
    <style>
    .stApp {background-color: #dddddd;}

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

    [data-testid="stSidebar"] {background-color: #003366;}
    [data-testid="stSidebar"] * {color: white !important;}
    </style>
    """,
    unsafe_allow_html=True
)

#Customising the top banner, earlier code put this onto a blue background. The blue theme of the website is tied to the blue seen alot with rain, turloughs and weather forecasting.
st.markdown(
    """
    <div class="top-banner"> TURCAST </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#00509e; color:white; padding:6px; text-align:center;"> Home</div>
    """, unsafe_allow_html=True
)
#The sidebar menu looked quite empty, this simple stock image makes it look more eye-catching and full.
st.sidebar.image(os.path.join(os.getcwd(), "static", "rain.jpg"), width='content')

#The website design has been set up, this section deals with the actual content of the page.
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px;">
        <h1 style="text-align: center; color: #0073e6;">TURCAST</h1>
        <h3 style="text-align: center; color: #444;">~Real Time Turlough Depth Forecasting~</h3>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:15px;">
        <p style="color:#333; font-size:16px;">
        TURCAST is a turlough depth forecaster that gives accurate forecasts up to 24 hours ahead in time. Through machine learning it uses weather and soil to provide these accurate and reliable forecasts to help communities,  and farmers better prepare for seasonal flooding in turlough floodplains.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

st.image(os.path.join(os.getcwd(), "static", "turlough_example.jpg"))
st.caption("A turlough in flood, photo credit: Galway County Council")

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:15px;">
    <h3 style="text-align:center;">What is a turlough?</h3>
    </div>
    """,
    unsafe_allow_html=True
)
#Columns are a nice way to split up the format of the page and make it feel different and interesting.
colu1, colu2 = st.columns(2)
with colu1:
    st.markdown(
        '<div style="background-color:#e5ecf2; padding:15px; border-radius:8px; text-align:center;">'
        '<p>Turloughs are one of Irelands many unique geological features, meaning "dry lake" in Irish, turloughs are lakes that appear and disapear seasonally, filling up when rainfall is high and emptying when rainfall is low. They can only be found in limestone regions of Ireland, with the majority of them being found in the west. This is due to the west being home to many more karst regions, which have plenty of underground cave systems which are what drain turloughs.</p>'
        '<p>As climate change worsens and global warming increases, rainfall patterns intensifiy. For turloughs this means they are drier for longer but are more prone to flood the surrounding area. TURCAST aims to tackle this problem with its forecasts</p></div>',
        unsafe_allow_html=True
    )
with colu2:
    st.image(os.path.join(os.getcwd(), "static", "turlough-wmi-2016_med-155.webp"))
    st.caption("The spread of wetland habitat across Ireland, image credit: wetlandsurvey.ie")
    
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:15px;">
        <h4 style="text-align:center;">📊 TURCAST at a Glance</h4> </div>
    """,
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        '<div style="background-color:#e5ecf2; padding:15px; border-radius:8px; text-align:center;">'
        '<h3>0.949</h3><p>R² Accuracy</p></div>',
        unsafe_allow_html=True
    )
with col2:
    st.markdown(
        '<div style="background-color:#e5ecf2; padding:15px; border-radius:8px; text-align:center;">'
        '<h3>3-24 Hours</h3><p>Forecast Range</p></div>',
        unsafe_allow_html=True
    )
with col3:
    st.markdown(
        '<div style="background-color:#e5ecf2; padding:15px; border-radius:8px; text-align:center;">'
        '<h3>Met Éireann + GSI</h3><p>Data Sources</p></div>',
        unsafe_allow_html=True
    )

#Another way to get people to go to other pages on the website, this sections gives a slight description of what each pages function is
st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:20px;">
        <h3 style="text-align:center;">Other Pages</h3></div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:20px;">
        <h3 style="text-align:center;">💻Forecast</h3>
        <p style="text-align:center;">The forecast page shows the details of the current forecast for turloughs that TURCAST works with. The forecasts currently range from between 3-24 hours ahead. 
        <p style="text-align:center;"><a href="./Forecast">Go to Forecast Page ➡️</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:20px;">
        <h3 style="text-align:center;">🛠️Update Logs</h3>
        <p style="text-align:center;">The update logs page shows any new updates to TURCAST and the TURCAST website, detailing what is changed and any progress made.
        <p style="text-align:center;"><a href="./UpdateLogs">Go to the Update Logs Page ➡️</a></p>
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div style="background-color:#e5ecf2; padding:15px; border-radius:8px; margin-top:20px;">
        <h3 style="text-align:center;">👋About</h3>
        <p style="text-align:center;">The about page is a more detailed explanation of TURCAST, how it functions, the backstory behind it and the people who helped create it<p style="text-align:center;"><a href="./About">Go to the About Page ➡️</a></p>
    </div>
    """,
    unsafe_allow_html=True
)
st.divider()
#The page ends abrupdtly and briefly, what I notice on websites is that the bottom of the page generally has thin text that gives credit and signifies the end of the page.
st.markdown(
    """
    <div style="padding:15px; border-radius:8px; margin-top:100px;">
        <h7 style="text-align:center;">Made by Oisin Jackson, <a href="./Contact">Contact</a>  </h7>
      
    </div>
    """,
    unsafe_allow_html=True
)
