import streamlit as st
import xlrd
import yfinance as yf
import math
from plotly import graph_objs as go 
import datetime 
from datetime import datetime as date 
import pandas as pd
from sklearn.linear_model import LinearRegression

 

st.set_page_config(
    page_title = "Start" , 
    page_icon = "☑️" , 
    
)  

xls = xlrd.open_workbook("Company_Names.xls")
sh = xls.sheet_by_index(0)

companies = {}

for i in range(498) :
    cell_value_class = sh.cell(i,0).value
    cell_value_id = sh.cell(i,1).value
    companies[cell_value_class] = cell_value_id

company = st.sidebar.selectbox("#### Select The Company Name ", list(companies.keys()), 0)


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
if st.sidebar.button("Logout") :
 st.success(" Thank You . ")
 st.stop()

def tab() :

    Company_Information , Latest_stocks , Data_Analysis , Prediction = st.tabs(['#### Company ' , '#### Latest Stocks' , '#### Data Analysis' , '#### Prediction'])

    with Company_Information :
        company_information()

    with Latest_stocks :
        latest_stocks()

    with Data_Analysis :
        data_analysis()   
    
    with Prediction :
        st.header("Prediction")
        prediction()




def company_information() :

    st.header(company)
    data_ticker = yf.Ticker(companies[company])                                                  
    st.write("Symbol :- \n ",data_ticker.info["symbol"])
    open_data = data_ticker.history(period = '1d')
    st.write("Open : \n",str(round(open_data['Open'][0],2)),"USD"," ")    
    st.write("About :- \n ",data_ticker.info['longBusinessSummary'])

def latest_stocks() :

    ticker = yf.Ticker(companies[company])
    todays_data = ticker.history(period = '1d')
    yesterday_data = ticker.history(period = '2d')
   

    if todays_data['Close'][0] < yesterday_data['Close'][0] :
        yesterday_data['Close'][0] = -yesterday_data['Close'][0]


    st.metric(label='#### USD',value=todays_data['Close'][0],delta=yesterday_data['Close'][0])

    df = yf.download(tickers=companies[company], period='100d' , interval = '1d') 

    st.line_chart(data = df,x = None , y = "Close")

    st.dataframe(df[::-1] , width = 1000 , height = 1000)
    
def data_analysis() :

    df = yf.download(tickers=companies[company], start = "2015-01-01" , end  = date.today().strftime("%Y-%m-%d") ) 
        

    #company = company_name() 
    st.header("Data Analysis")
    st.header(company)

    st.subheader("Opening Price V/S Time Chart")
    fig_open = go.Figure()
    fig_open.add_trace(go.Scatter(x = df.index , y = df['Open'] , name = 'Stock Open' , marker = {'color' : 'orange'}))
    fig_open.layout.update(title_text = "Time Silder Open Data" , xaxis_rangeslider_visible = True)
    fig_open.update_xaxes(rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    st.plotly_chart(fig_open)

    st.subheader("Closing Price V/S Time Chart")
    fig_close = go.Figure()
    fig_close.add_trace(go.Scatter(x = df.index , y = df['Close'] , name = 'Stock Open' , marker = {'color' : 'violet'}))
    fig_close.layout.update(title_text = "Time Slider Close Data" , xaxis_rangeslider_visible = True)
    fig_close.update_xaxes(rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    st.plotly_chart(fig_close)

    st.subheader("Closing Opening Price V/S Time Chart")
    fig_open_and_close = go.Figure()
    fig_open_and_close.add_trace(go.Scatter(x = df.index , y = df['Open'] , name = 'Stock Open' , marker = {'color' : 'yellow'}))
    fig_open_and_close.add_trace(go.Scatter(x = df.index , y = df['Close'] , name = 'Stock Close' , marker = {'color' : 'blue'}))
    fig_open_and_close.layout.update(title_text = "Time Slider Open And Close Data" , xaxis_rangeslider_visible = True)
    fig_open_and_close.update_xaxes( rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    st.plotly_chart(fig_open_and_close)

    st.subheader("Volume Of Stocks In Millions V/S Time Chart")
    fig_volume_of_stocks = go.Figure()
    fig_volume_of_stocks.add_trace(go.Bar(x = df.index , y = df['Volume'] , name = 'Volume Stocks' , marker = {'color' : 'turquoise'}))
    fig_volume_of_stocks.layout.update(title_text=" Time Slider For The Volume Of The Stock In Millions Of The Company ", xaxis_rangeslider_visible = True)
    fig_volume_of_stocks.update_xaxes(rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    st.plotly_chart(fig_volume_of_stocks)

    st.subheader("Low And High V/S Time Chart Graph               ")
    fig_low_and_high = go.Figure()
    fig_low_and_high.add_trace(go.Scatter(x = df.index , y = df['High'] , name = 'High Price Of Stocks ' , marker = {'color' : 'yellow'}))
    fig_low_and_high.add_trace(go.Scatter(x = df.index , y = df['Low'] , name = 'Low Price Of Stocks ' , marker = {'color' : 'green'}))
    fig_low_and_high.layout.update(title_text = "Time Slider For Low And High Stocks Prices" , xaxis_rangeslider_visible = True)
    fig_low_and_high.update_xaxes(rangeslider_visible = True , 
                                  rangeselector = dict(
                                        buttons = list ( [
                                           dict(count = 30 , label = "30d" , step = "day" , stepmode = "backward") , 
                                           dict(count = 60 , label = "60D" , step = "day" , stepmode = "backward") ,
                                           dict(count = 90 , label = "90D" , step = "day" , stepmode = "backward") , 
                                           dict(count = 180 , label = "180D" , step = "day" , stepmode = "backward") , 
                                           dict(count = 365 , label = "365D" , step = "day" , stepmode = "backward") ,
                                           dict(step = "all")
                                ])
                            ))
    st.plotly_chart(fig_low_and_high)

    st.subheader("Moving Average V/S Time Chart")
    fig_moving_average = go.Figure()    
    
    df['MA_10'] = df.Close.rolling(10).mean()
    fig_moving_average.add_trace(go.Scatter(x = df.index , y = df['MA_10'] , name = 'Moving Average Of 10 Days' , marker = {'color' : 'red'}))    
    df['MA_20'] = df.Close.rolling(20).mean()
    fig_moving_average.add_trace(go.Scatter(x = df.index , y = df['MA_20'] , name = 'Moving Average Of 20 Days' , marker = {'color' : 'purple'}))    
    df['MA_100'] = df.Close.rolling(100).mean()
    fig_moving_average.add_trace(go.Scatter(x = df.index , y = df['MA_100'] , name = 'Moving Average Of 100 Days' , marker = {'color' : 'gold'}))    
    df['MA_200'] = df.Close.rolling(200).mean() 
    fig_moving_average.add_trace(go.Scatter(x = df.index , y = df['MA_200'] , name = 'Moving Average Of 200 Days ' , marker = {'color' : 'silver'}))    
    fig_moving_average.layout.update(title_text = "Time Silder Open Data" , xaxis_rangeslider_visible = True)
    fig_moving_average.update_xaxes(rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    st.plotly_chart(fig_moving_average)

    st.subheader("Profit Margins Bar Graph")    
   
    data_ticker = yf.Ticker(companies[company])
    gross_margin = data_ticker.info['grossMargins']     
    operating_margin = data_ticker.info['operatingMargins']
    ebidta_margin = data_ticker.info['ebitdaMargins']
    net_margin = data_ticker.info['netIncomeToCommon'] / data_ticker.info['totalRevenue']

    fig_margins = go.Figure()
    colors = ['','','',''] # ['blue'] * 4
    colors[0] = 'aqua'
    colors[1] = 'burlywood' 
    colors[2] = 'cornsilk'
    colors[3] = 'darkturquoise'
    fig_margins.add_trace(go.Bar(x = ["Gross Margin" , "Operating Margin" , "Ebidta Margin" , "Net Margin"] , y = [gross_margin , operating_margin , ebidta_margin , net_margin] , marker_color = colors))
    fig_margins.layout.update(title_text = "Profit Margins ")
    st.plotly_chart(fig_margins)    

    st.subheader("Moving Average With Market Price Complete V/S Time Chart")
    fig_moving_average_stocks_graph = go.Figure(data = [ go.Candlestick(
                                                                        x = df.index , 
                                                                        open = df['Open'] ,
                                                                        high = df['High'] , 
                                                                        low = df['Low'] , 
                                                                        close = df['Close'] , 
                                                                        name = 'Moving Average With Market Price ' , 
                                                                        increasing_line_color = 'pink' , 
                                                                        decreasing_line_color = 'purple'
                                                                        ) 
                                                     ]
                                                            
                                                )  
    
    df['MA_100'] = df.Close.rolling(100).mean()
    fig_moving_average_stocks_graph.add_trace(go.Scatter(x = df.index , y = df['MA_100'] , name = 'Moving Average Of 100 Days' , marker = {'color' : 'gold'}))    
    df['MA_200'] = df.Close.rolling(200).mean() 
    fig_moving_average_stocks_graph.add_trace(go.Scatter(x = df.index , y = df['MA_200'] , name = 'Moving Average Of 200 Days ' , marker = {'color' : 'silver'}))    
    fig_moving_average_stocks_graph.layout.update(title_text = "Time Silder Open Data" , xaxis_rangeslider_visible = True)
    fig_moving_average_stocks_graph.update_xaxes(rangeslider_visible=True,
                          rangeselector=dict(
                              buttons=list([
                                  dict(count=30, label="30D", step="day", stepmode="backward"),
                                  dict(count=60, label="60D", step="day", stepmode="backward"),
                                  dict(count=90, label="90D", step="day", stepmode="backward"),
                                  dict(count=180, label="180D", step="day", stepmode="backward"),
                                  dict(count=365, label="365D", step="day", stepmode="backward"),
                                  dict(step="all")
                              ])
                          ))
    #fig_moving_average_stocks_graph.yaxis2.showgrid = False 
    st.plotly_chart(fig_moving_average_stocks_graph)
    #st.plotly_chart(fig_moving_average_stocks_graph)

def prediction() :
    import datetime 
    st.header("Prediction")
    y = date.today().year 
    m = date.today().month
    dd = date.today().day
    prediction_date = st.date_input("#### Select Date For Prediction Of Stock Price Of The Company :- " , datetime.date(y , m , dd) )
    if prediction_date >= date.today() :
        st.title(prediction_date)
        ticker_symbol = companies[company]
        st.write(company)

        if st.button("Prediction Of Stock Price . ") :

    
            # Get the historical data for the stock
            stock_data = yf.download(ticker_symbol)

            # Create a DataFrame with the "Close" prices
            df = pd.DataFrame(stock_data['Close'])

            # Add a column for the target variable, which is the future price (next day's close)
            df['Target'] = df['Close'].shift(-1)

            # Drop rows with missing values
            df.dropna(inplace=True)

            # Split the data into features (X) and target variable (y)
            X = df.iloc[:, :-1]
            y = df['Target']

            # Train a linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Get the last available close price
            last_close_price = df['Close'].iloc[-1]

            # Create a DataFrame with the prediction date
            prediction_df = pd.DataFrame(index=[pd.to_datetime(prediction_date)])

            # Add features to the prediction DataFrame (e.g., previous close price)
            prediction_df['Close'] = last_close_price

            # Make the prediction
            predicted_price = model.predict(prediction_df)

            st.write("The Predicted Price Is :- ")
            st.title(predicted_price[0])
         
    else :
        st.write("Enter The Correct Date :- ")      
    
def start() :
    view()
    tab()
    
if __name__ == "__main__" :
    start()
