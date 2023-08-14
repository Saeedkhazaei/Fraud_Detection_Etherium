import streamlit as st
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer , make_column_transformer
import numpy as np
import pandas as pd
import joblib
from PIL import Image
import time

model = joblib.load('LGBMCpipe.joblib')
col1,col2 = st.columns([2,1])
col1.header('*Whether the transaction of Etherum is fraud or Not*') 
col1.write("Learn More >> [link](https://github.com/Saeedkhazaei)")
#photo = Image.open("Churn.jpg")
#photo.resize((800,600))
#col2.image(photo)
st.write("---")



Avg_min_between_sent_tnx= st.slider("Average time between sent transactions for account in minutes",0,430000)	
Avg_min_between_received_tnx = st.slider("verage time between received transactions for account in minutes",0,485000)
Time_Diff_between_first_and_last =st.slider("Time difference between the first and last transaction",0,2000000)
Sent_tnx = st.slider("Total number of sent normal transactions ?",0,10000)
Received_Tnx= st.slider("Total number of received normal transactions",0,10000)	
Number_of_Created_Contracts =st.slider("Total Number of created contract transactions",0,10000)
max_value_received= st.slider("Maximum value in Ether ever received",0,800000)
avg_val_received =st.slider("verage value in Ether ever received",0,285000)	
avg_val_sent= st.slider ("Average value of Ether ever sent",0,12000)		
total_Ether_sent = st.slider("Total Ether sent for account address",0,30000000)	
total_ether_balance = st.slider("Total Ether Balance following enacted transactions",-15000000,15000000)
ERC20_total_Ether_received = st.slider("Total ERC20 token received transactions in Ether",0,1000000000000)	
ERC20_total_ether_sent = st.slider("Total ERC20token sent transactions in Ether",0,112000000000)
ERC20_total_Ether_sent_contract	= st.slider("Total ERC20 token transfer to other contracts in Ether",0,415000)
ERC20_uniq_sent_addr = st.slider("Number of ERC20 token transactions sent to Unique account addresses",0,10000)
ERC20_uniq_rec_token_name = st.slider("Number of Unique ERC20 tokens received",0,1000)

row=[Avg_min_between_sent_tnx,Avg_min_between_received_tnx,Time_Diff_between_first_and_last,Sent_tnx,
    Received_Tnx, Number_of_Created_Contracts, max_value_received, avg_val_received,avg_val_sent,
    total_Ether_sent,total_ether_balance, ERC20_total_Ether_received, ERC20_total_ether_sent,
    ERC20_total_Ether_sent_contract,ERC20_uniq_sent_addr,ERC20_uniq_rec_token_name]
def predict(): 
    columns=['Avg min between sent tnx', 'Avg min between received tnx',
       'Time Diff between first and last (Mins)', 'Sent tnx', 'Received Tnx',
       'Number of Created Contracts', 'max value received ',
       'avg val received', 'avg val sent', 'total Ether sent',
       'total ether balance', ' ERC20 total Ether received',
       ' ERC20 total ether sent', ' ERC20 total Ether sent contract',
       ' ERC20 uniq sent addr', ' ERC20 uniq rec token name']
    X = pd.DataFrame([row], columns = columns)
    scaler=StandardScaler()
    X=scaler.fit_transform(X)
    prediction = model.predict(X)
    progress_bar = col1.progress(0)
    for perdiction_complited in range(100):
        time.sleep(0.05)
        progress_bar.progress(perdiction_complited+1)

    if prediction[0] == 1: 
        st.error('The transaction is fraud :thumbsdown:')
    else: 
        st.success('The transaction is non fraud :thumbsup:') 

trigger = st.button('Predict', on_click=predict) 
st.write("---")

    
