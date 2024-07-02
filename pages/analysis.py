import time
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
from sqlalchemy import create_engine,text,inspect


st.session_state.is_trending = False
engine = create_engine("postgresql://postgres:V$QGmNWmGEx5Kzti@realtimetruckdata.cvg4iicuqk12.ap-south-1.rds.amazonaws.com:5432/postgres") #Postgresql connection - dbname://userid:password@hostname:portnumber/databasename

Truck_data_columns = st.sidebar.selectbox("Select the Data_column",
                                       pd.read_sql("SELECT column_name FROM information_schema.columns WHERE table_name = 'truck_data'"
                                                   ,engine))

placeholder =st.empty()
def fetch_data(engine): 

        Truck_data = pd.read_sql('select * from truck_data;',engine) #where "truck_id" = %(name)s;', 
                         #engine,params={'name' :Truck })
        return(Truck_data)

st.subheader("Truck data Analysis")
#while st.session_state.is_trending:
Sql = fetch_data(engine)
    #print("Fetching data every one tw")
time.sleep(1) 
    
cross_tb_app =pd.crosstab(Sql[Truck_data_columns],Sql['truck_id'])
with placeholder:
    fig = px.scatter(y =Sql[Truck_data_columns], x=Sql['truck_id'],color = Sql['truck_id'] )       # Plot!
    st.plotly_chart(fig, use_container_width=True, height = 200)










engine1 = create_engine("postgresql://postgres:V$QGmNWmGEx5Kzti@clickstream.cvg4iicuqk12.ap-south-1.rds.amazonaws.com:5432/postgres") #Postgresql connection - dbname://userid:password@hostname:portnumber/databasename


placeholder =st.empty()
def fetch_data1(engine1): 

        Click_data = pd.read_sql('select * from click_counts;',engine1) #where "truck_id" = %(name)s;', 
                         #engine,params={'name' :Truck })
        return(Click_data)

st.subheader("Click Stream")
#while st.session_state.is_trending:
Sql = fetch_data1(engine1)
    #print("Fetching data every one tw")
time.sleep(1) 
    
#cross_tb_app =pd.crosstab(Sql['clickcount'],Sql['itemid'])
with placeholder:
    fig = px.bar(y =Sql['clickcount'], x=Sql['itemid'],color = Sql['itemid'] )       # Plot!
    st.plotly_chart(fig, use_container_width=True, height = 200)
     
              
 


                                 