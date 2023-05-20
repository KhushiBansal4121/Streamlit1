!pip install --upgrade pip
import streamlit as st 


st.set_page_config(
    page_title = "Stock Price Prediction Model " , 
    page_icon = "📈"

)

def view() :
    #Image
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.xxl.thumbs.canstockphoto.com/colorful-waves-abstract-background-blue-dark-image_csp28093770.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True )
    
    #Sidebar
    st.markdown("""
    <style>
    [data-testid=stSidebar] {
        background-color: MidNightBlue;
        background-image: url("https://www.rockwelltrading.com/wp-content/uploads/blank-downside.jpg");
    }
    </style>
    """, unsafe_allow_html=True)
    
    #Content 
    title1 = '<h2 style = "text-align:left;font-family:sans-serif;color:White;font-size:40px;">Stock Market</h2>'
    st.markdown(title1,unsafe_allow_html=True)
    title2 = '<p style = "text-align:left;font-family:sans-serif;color:White;font-size:30px;">A stock market is a public market where you can buy and sell shares for publicly listed companies.</p>'
    st.markdown(title2,unsafe_allow_html=True)

    title3 = '<h2 style = "text-align:left;font-family:sans-serif;color:White;font-size:40px;">Stock Price Prediction Model</h2>'
    st.markdown(title3,unsafe_allow_html=True)
    title4 = '<p style = "text-align:left;font-family:sans-serif;color:White;font-size:30px;">Stock Price Prediction using machine learning helps you discover the future value of company stock and other financial assets traded on an exchange. The entire idea of predicting stock prices is to gain significant profits.</p>'
    st.markdown(title4,unsafe_allow_html=True)


   


if __name__ == "__main__" :
    view()
