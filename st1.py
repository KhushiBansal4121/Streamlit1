import streamlit as st
import yfinance as yf 

#Image
def image() :
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://static.vecteezy.com/system/resources/previews/000/186/072/original/vector-digital-candle-stick-graph-design-for-stock-market.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True )

#Title
def title() :
    title = '<h1 style = "text-align:center;font-family:sans-serif;color:White;font-size:60px;">\nStock Price Prediction Model </h1>'
    st.markdown(title,unsafe_allow_html=True)

#Content
def content() :
    title1 = '<h2 style = "text-align:left;font-family:sans-serif;color:White;font-size:40px;">Stock Market</h2>'
    st.markdown(title1,unsafe_allow_html=True)
    title2 = '<p style = "text-align:left;font-family:sans-serif;color:White;font-size:30px;">A stock market is a public market where you can buy and sell shares for publicly listed companies.</p>'
    st.markdown(title2,unsafe_allow_html=True)

    title3 = '<h2 style = "text-align:left;font-family:sans-serif;color:White;font-size:40px;">Stock Price Prediction Model</h2>'
    st.markdown(title3,unsafe_allow_html=True)
    title4 = '<p style = "text-align:left;font-family:sans-serif;color:White;font-size:30px;">Stock Price Prediction using machine learning helps you discover the future value of company stock and other financial assets traded on an exchange. The entire idea of predicting stock prices is to gain significant profits.</p>'
    st.markdown(title4,unsafe_allow_html=True)

#Sidebar
def sidebar() :
    st.markdown("""
    <style>
    [data-testid=stSidebar] {
        background-color: MidNightBlue;
        background-image: url("https://th.bing.com/th/id/R.3f009dcf6b318dedf9b7b2cb22be9b2a?rik=7FUFGVWqDNXf%2fw&riu=http%3a%2f%2fgetwallpapers.com%2fwallpaper%2ffull%2fa%2f8%2fc%2f687843.jpg&ehk=ltZNkB7YuNMHeaczzQL7q67tDdirMVJ7moSjB3w1V7Q%3d&risl=&pid=ImgRaw&r=0");
    }
    </style>
    """, unsafe_allow_html=True)



    title_sidebar = '<h2 style = "text-align:left;font-family:sans-serif;color:White;font-size:40px;">Welcome </h2>'
    st.sidebar.markdown(title_sidebar,unsafe_allow_html=True)
    if st.sidebar.button("Login") :
        st.sidebar.success('Login Successful ',icon="✅")
        option()
    elif st.sidebar.button("Create Account") :
        st.sidebar.success('Account Created Successfully ',icon="✅")
        st.balloons()
        option()

#Company Options
def option() :
    Sub_title_sidebar = '<h2 style = "text-align:left ; font-family:sans:serif ; color:White ; font-size:20px ;">Company</h2>'
    st.sidebar.markdown(Sub_title_sidebar , unsafe_allow_html=True)
    op = st.sidebar.selectbox("",(" ","Apple","Microsoft","Google","Facebook"))
    st.sidebar.write(op)
    return op

image()
title()
content()
sidebar()




