# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''import datetime as dt
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

#stocks = ["AARTIIND.NS",'ABB.NS','ACC.NS','ADANIENT.NS','ADANIPORTS.NS','ABCAPITAL.NS','ABFRL.NS','APLLTD.NS','AMARAJABAT.NS','AMBUJACEM.NS','APOLLOHOSP.NS','APOLLOTYRE.NS','ASHOKLEY.NS','ASIANPAINT.NS','ASTRAL.NS','ATUL.NS','AUROPHARMA.NS','AUBANK.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJAJFINSV.NS','BALKRISIND.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKBARODA.NS','BATAINDIA.NS','BERGEPAINT.NS','BEL.NS','BHARATFORG.NS','BPCL.NS','BHARTIARTL.NS','BHEL.NS','BIOCON.NS','BSOFT.NS','BRITANNIA.NS','INDUSTOWER.NS','BIL.NS','CANBK.NS','CANFINHOME.NS','CHAMBLFERT.NS','CHOLAFIN.NS','CIPLA.NS','CUB.NS','COALINDIA.NS','COFORGE.NS','COLPAL.NS','CONCORD.BO','COROMANDEL.NS','CROMPTON.NS','CUMMINSIND.BO','GAIL.NS','GMRINFRA.NS','GODREJCP.NS','GRANULES.NS','GUJGASLTD.NS','GLENMARK.NS','GNFC.NS','GODREJPROP.NS','GRASIM.NS','GSPL.NS','HAL.NS','HCLTECH.NS','HDFCBANK.NS','HCLTECH.NS','HDFCBANK.NS','HDFC.NS','HINDALCO.NS','HINDPETRO.NS','HAVELLS.NS','HDFCAMC.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDCOPPER.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIGOLD.NS','IDFCFIRSTB.NS','IDFC.NS','IBULHSGFIN.NS','INDIACEM.NS','IEX.NS','IOC.NS','IGL.NS','INFY.NS','IPCALAB.NS','ITC.NS','INDIAMART.NS','INDHOTEL.NS','INDIGO.NS','INDUSINDBK.NS','INTELLECT.NS','IRCTC.NS','JINDALSTEL.NS','JKCEMENT.NS','JSWSTEEL.NS','JUBLFOOD.NS','LAURUSLABS.NS','L&TFH.NS','LT.NS','LUPIN.NS','LICHSGFIN.NS','MGL.NS','M&M.NS','MARICO.NS','MFSL.NS','MPHASIS.NS','MCX.NS','M&MFIN.NS','MANAPPURAM.NS','METROPOLIS.NS','MSUMI.NS','MUTHOOTFIN.NS','NATIONALUM.NS','NAVINFLUOR.NS','NMDC.NS','NAUKRI.NS','NBCC.NS','NTPC.NS','OBEROIRLTY.NS','ONGC.NS','OFSS.NS','PETRONET.NS','PIDILITIND.NS','PEL.NS','PFC.NS','PNB.NS','PERSISTENT.NS','PFIZER.NS','PIIND.NS','POLYCAB.NS','POWERGRID.NS','PVRINOX.NS','SBICARD.NS','SBIN.NS','SUNPHARMA.NS','SYNGENE.NS','SBILIFE.NS','SRF.NS','SAIL.NS','SUNTV.NS','SHRIRAMFIN.NS','SIEMENS.NS','STAR.NS','TATACHEM.NS','TATACONSUM.NS','TATAPOWER.NS','TORNTPOWER.NS','TVSMOTOR.NS','TATACOMM.NS','TATAMOTORS.NS','TATASTEEL.NS','DABUR.NS','DALMIASUG.NS','DEEPAKNTR.NS','DELTACORP.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','EICHERMOT.NS','ESCORTS.NS','EXIDEIND.NS','FEDERALBNK.NS','FSL.NS','ZEEL.NS','WHIRLPOOL.NS','WIPRO.NS','VOLTAS.NS','VEDL.NS','KOTAKBANK.NS','LTIM.NS','LTTS.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','RAIN.NS','RBL.NS','RAMCOCEM.NS','RELIANCE.NS','TCS.NS','TITAN.NS','TECHM.NS','TRENT.NS','TORNTPHARM.NS','ABBOTINDIA.NS','BOSCHLTD.NS','HONAUT.NS','MARUTI.NS','MRF.NS','NESTLEIND.NS']
#stocks = ["AARTIIND.NS",'ABB.NS','ACC.NS','ADANIENT.NS','ADANIPORTS.NS','ABCAPITAL.NS','ABFRL.NS','APLLTD.NS','AMARAJABAT.NS','AMBUJACEM.NS','APOLLOHOSP.NS','APOLLOTYRE.NS','ASHOKLEY.NS','ASIANPAINT.NS','ASTRAL.NS','ATUL.NS','AUROPHARMA.NS','AUBANK.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJAJFINSV.NS','BALKRISIND.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKBARODA.NS','BATAINDIA.NS','BERGEPAINT.NS','BEL.NS','BHARATFORG.NS','BPCL.NS','BHARTIARTL.NS','BHEL.NS','BIOCON.NS','BSOFT.NS','BRITANNIA.NS','INDUSTOWER.NS','BIL.NS','CANBK.NS','CANFINHOME.NS','CHAMBLFERT.NS','CHOLAFIN.NS','CIPLA.NS','CUB.NS','COALINDIA.NS','COFORGE.NS','COLPAL.NS','CONCORD.BO','COROMANDEL.NS','CROMPTON.NS','CUMMINSIND.BO']
#stocks = ['GAIL.NS','GMRINFRA.NS','GODREJCP.NS','GRANULES.NS','GUJGASLTD.NS','GLENMARK.NS','GNFC.NS','GODREJPROP.NS','GRASIM.NS','GSPL.NS','HAL.NS','HCLTECH.NS','HDFCBANK.NS','HCLTECH.NS','HDFCBANK.NS','HDFC.NS','HINDALCO.NS','HINDPETRO.NS','HAVELLS.NS','HDFCAMC.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDCOPPER.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIGOLD.NS','IDFCFIRSTB.NS','IDFC.NS','IBULHSGFIN.NS','INDIACEM.NS','IEX.NS','IOC.NS','IGL.NS','INFY.NS','IPCALAB.NS','ITC.NS','INDIAMART.NS','INDHOTEL.NS','INDIGO.NS','INDUSINDBK.NS','INTELLECT.NS','IRCTC.NS','JINDALSTEL.NS','JKCEMENT.NS','JSWSTEEL.NS','JUBLFOOD.NS','LAURUSLABS.NS','L&TFH.NS','LT.NS','LUPIN.NS','LICHSGFIN.NS']
#stocks = ['MGL.NS','M&M.NS','MARICO.NS','MFSL.NS','MPHASIS.NS','MCX.NS','M&MFIN.NS','MANAPPURAM.NS','METROPOLIS.NS','MSUMI.NS','MUTHOOTFIN.NS','NATIONALUM.NS','NAVINFLUOR.NS','NMDC.NS','NAUKRI.NS','NBCC.NS','NTPC.NS','OBEROIRLTY.NS','ONGC.NS','OFSS.NS','PETRONET.NS','PIDILITIND.NS','PEL.NS','PFC.NS','PNB.NS','PERSISTENT.NS','PFIZER.NS','PIIND.NS','POLYCAB.NS','POWERGRID.NS','PVRINOX.NS','SBICARD.NS','SBIN.NS','SUNPHARMA.NS','SYNGENE.NS','SBILIFE.NS','SRF.NS','SAIL.NS','SUNTV.NS','SHRIRAMFIN.NS','SIEMENS.NS','STAR.NS','TATACHEM.NS','TATACONSUM.NS','TATAPOWER.NS','TORNTPOWER.NS','TVSMOTOR.NS','TATACOMM.NS','TATAMOTORS.NS','TATASTEEL.NS']
stocks = ['DABUR.NS','DALMIASUG.NS','DEEPAKNTR.NS','DELTACORP.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','EICHERMOT.NS','ESCORTS.NS','EXIDEIND.NS','FEDERALBNK.NS','FSL.NS','ZEEL.NS','WHIRLPOOL.NS','WIPRO.NS','VOLTAS.NS','VEDL.NS','KOTAKBANK.NS','LTIM.NS','LTTS.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','RAIN.NS','RBL.NS','RAMCOCEM.NS','RELIANCE.NS','TCS.NS','TITAN.NS','TECHM.NS','TRENT.NS','TORNTPHARM.NS','ABBOTINDIA.NS','BOSCHLTD.NS','HONAUT.NS','MARUTI.NS','MRF.NS','NESTLEIND.NS']
start = dt.datetime.today()-dt.timedelta(409)
end = dt.datetime.today()-dt.timedelta(44)
cl_price = pd.DataFrame()
final_list = pd.DataFrame()
proceed = pd.DataFrame()
ohlcv_data ={}

for ticker in stocks:
    temp = yf.download(ticker,start,end)
    ohlcv_data[ticker]=temp
# extracting stock data (historical close price) for the stocks identified

def Volume(DR, a=10):
    dr=DR.copy()
    dr['signal']=dr['Volume'].ewm(span=a, min_periods=a).mean()
    return dr.loc[:,['signal']]
def Averages(DX):
    dx=DX.copy()
    dx['buy']=dx['Volume']-dx['WV']
    return dx.loc[:,['buy']]
    
    
for ticker in ohlcv_data:
    ohlcv_data[ticker]['WV']=Volume(ohlcv_data[ticker])
for ticker in ohlcv_data:
    ohlcv_data[ticker]['Proceed']=Averages(ohlcv_data[ticker])
for ticker in ohlcv_data:
    cl_price[ticker]=ohlcv_data[ticker]['Proceed']

final_list = cl_price.iloc[-1]
proceed = final_list[(final_list >= 0)]
#print(final_list[(final_list >= 0)])'''




'''import requests
from bs4 import BeautifulSoup

historical_data = {}

url = "https://finance.yahoo.com/quote/INFY.NS/history?p=INFY.NS"

headers = {"User-Agent" : "Brave/v1.52.122"}
page = requests.get(url, headers=headers)
page_content = page.content
soup = BeautifulSoup(page_content,"html.parser")
tabl = soup.find_all("div" , {"class" : "Pb(10px) Ovx(a) W(100%)"})

for t in tabl:
    rows = t.find_all("tr" , {"class": "BdT Bdc($seperatorColor) Ta(end) Fz(s) Whs(nw)"})
    for row in rows:
        print(row.get_text(separator="|"))'''



'''import datetime as dt
import requests
from bs4 import BeautifulSoup
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt


#tickers = ['DABUR.NS','DALMIASUG.NS','DEEPAKNTR.NS','DELTACORP.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','EICHERMOT.NS','ESCORTS.NS','EXIDEIND.NS','FEDERALBNK.NS','FSL.NS','ZEEL.NS','WHIRLPOOL.NS','WIPRO.NS','VOLTAS.NS','VEDL.NS','KOTAKBANK.NS','LTIM.NS','LTTS.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','RAIN.NS','RBL.NS','RAMCOCEM.NS','RELIANCE.NS','TCS.NS','TITAN.NS','TECHM.NS','TRENT.NS','TORNTPHARM.NS','ABBOTINDIA.NS','BOSCHLTD.NS','HONAUT.NS','MARUTI.NS','MRF.NS','NESTLEIND.NS']
tickers = ['INFY.NS']
historical_data_dict ={}

start = dt.datetime.today()-dt.timedelta(366)
end = dt.datetime.today()-dt.timedelta(1)

for ticker in tickers:
    #scraping income statement
    url = " https://finance.yahoo.com/quote/{}/history?p={}".format(ticker,ticker)
   
    historical_data = {}
    table_title = {}
    
    headers = {"User-Agent" : "Brave/v1.52.122"}
    page = requests.get(url, headers=headers)
    page_content = page.content
    soup = BeautifulSoup(page_content,"html.parser")
    
    for a in soup.find_all("div", {"class": "D(ib) Mend(20px)"}):
        ltp=a.find('span', {'class':'e3b14781 f5a023e1'})
        ltp=ltp.str.replace(r",","").astype('float')
        print(ltp)
        #if ltp>open:
        
        
    
    tabl = soup.find_all("div" , {"class" : "M(0) Whs(n) BdEnd Bdc($seperatorColor) D(itb)"})
    for t in tabl:
        heading = t.find_all("div" , {"class": "D(tbr) C($primaryColor)"})
        for top_row in heading:
            table_title[top_row.get_text(separator="|").split("|")[0]] = top_row.get_text(separator="|").split("|")[1:]
        rows = t.find_all("div" , {"class": "D(tbr) fi-row Bgc($hoverBgColor):h"})
        for row in rows:
            income_statement[row.get_text(separator="|").split("|")[0]] = row.get_text(separator="|").split("|")[1:]

    temp = pd.DataFrame(income_statement).T
    temp.columns = table_title["Breakdown"]
    income_statatement_dict[ticker] = temp'''


import yfinance as yf
import pandas as pd
import numpy as np
from matplotlib.pyplot import title
import requests
import json
import mplfinance as mpl 
#import xlsxwriter

hist = {}
cl_price = pd.DataFrame()
final_list = pd.DataFrame()
stock1 = pd.DataFrame()
today = {}
BULL = {}
Green = {}
Red = {}
BEAR = {}
PLOTG = {}
PLOTR = {}

# get historical market data
#stocks = ["AARTIIND.NS",'ABB.NS','ACC.NS','ADANIENT.NS','ADANIPORTS.NS','ABCAPITAL.NS','ABFRL.NS','APLLTD.NS','AMARAJABAT.NS','AMBUJACEM.NS','APOLLOHOSP.NS','APOLLOTYRE.NS','ASHOKLEY.NS','ASIANPAINT.NS','ASTRAL.NS','ATUL.NS','AUROPHARMA.NS','AUBANK.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJAJFINSV.NS','BALKRISIND.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKBARODA.NS','BATAINDIA.NS','BERGEPAINT.NS','BEL.NS','BHARATFORG.NS','BPCL.NS','BHARTIARTL.NS','BHEL.NS','BIOCON.NS','BSOFT.NS','BRITANNIA.NS','INDUSTOWER.NS','BIL.NS','CANBK.NS','CANFINHOME.NS','CHAMBLFERT.NS','CHOLAFIN.NS','CIPLA.NS','CUB.NS','COALINDIA.NS','COFORGE.NS','COLPAL.NS','CONCORD.BO','COROMANDEL.NS','CROMPTON.NS','CUMMINSIND.BO','GAIL.NS','GMRINFRA.NS','GODREJCP.NS','GRANULES.NS','GUJGASLTD.NS','GLENMARK.NS','GNFC.NS','GODREJPROP.NS','GRASIM.NS','GSPL.NS','HAL.NS','HCLTECH.NS','HDFCBANK.NS','HCLTECH.NS','HDFCBANK.NS','HDFC.NS','HINDALCO.NS','HINDPETRO.NS','HAVELLS.NS','HDFCAMC.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDCOPPER.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIGOLD.NS','IDFCFIRSTB.NS','IDFC.NS','IBULHSGFIN.NS','INDIACEM.NS','IEX.NS','IOC.NS','IGL.NS','INFY.NS','IPCALAB.NS','ITC.NS','INDIAMART.NS','INDHOTEL.NS','INDIGO.NS','INDUSINDBK.NS','INTELLECT.NS','IRCTC.NS','JINDALSTEL.NS','JKCEMENT.NS','JSWSTEEL.NS','JUBLFOOD.NS','LAURUSLABS.NS','L&TFH.NS','LT.NS','LUPIN.NS','LICHSGFIN.NS','MGL.NS','M&M.NS','MARICO.NS','MFSL.NS','MPHASIS.NS','MCX.NS','M&MFIN.NS','MANAPPURAM.NS','METROPOLIS.NS','MSUMI.NS','MUTHOOTFIN.NS','NATIONALUM.NS','NAVINFLUOR.NS','NMDC.NS','NAUKRI.NS','NBCC.NS','NTPC.NS','OBEROIRLTY.NS','ONGC.NS','OFSS.NS','PETRONET.NS','PIDILITIND.NS','PEL.NS','PFC.NS','PNB.NS','PERSISTENT.NS','PFIZER.NS','PIIND.NS','POLYCAB.NS','POWERGRID.NS','PVRINOX.NS','SBICARD.NS','SBIN.NS','SUNPHARMA.NS','SYNGENE.NS','SBILIFE.NS','SRF.NS','SAIL.NS','SUNTV.NS','SHRIRAMFIN.NS','SIEMENS.NS','STAR.NS','TATACHEM.NS','TATACONSUM.NS','TATAPOWER.NS','TORNTPOWER.NS','TVSMOTOR.NS','TATACOMM.NS','TATAMOTORS.NS','TATASTEEL.NS','DABUR.NS','DALMIASUG.NS','DEEPAKNTR.NS','DELTACORP.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','EICHERMOT.NS','ESCORTS.NS','EXIDEIND.NS','FEDERALBNK.NS','FSL.NS','ZEEL.NS','WHIRLPOOL.NS','WIPRO.NS','VOLTAS.NS','VEDL.NS','KOTAKBANK.NS','LTIM.NS','LTTS.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','RAIN.NS','RBL.NS','RAMCOCEM.NS','RELIANCE.NS','TCS.NS','TITAN.NS','TECHM.NS','TRENT.NS','TORNTPHARM.NS','ABBOTINDIA.NS','BOSCHLTD.NS','HONAUT.NS','MARUTI.NS','MRF.NS','NESTLEIND.NS']
#stocks = ["AARTIIND.NS",'ABB.NS','ACC.NS','ADANIENT.NS','ADANIPORTS.NS','ABCAPITAL.NS','ABFRL.NS','APLLTD.NS','AMARAJABAT.NS','AMBUJACEM.NS','APOLLOHOSP.NS','APOLLOTYRE.NS','ASHOKLEY.NS','ASIANPAINT.NS','ASTRAL.NS','ATUL.NS','AUROPHARMA.NS','AUBANK.NS','AXISBANK.NS','BAJAJ-AUTO.NS','BAJAJFINSV.NS','BALKRISIND.NS','BALRAMCHIN.NS','BANDHANBNK.NS','BANKBARODA.NS','BATAINDIA.NS','BERGEPAINT.NS','BEL.NS','BHARATFORG.NS','BPCL.NS','BHARTIARTL.NS','BHEL.NS','BIOCON.NS','BSOFT.NS','BRITANNIA.NS','INDUSTOWER.NS','BIL.NS','CANBK.NS','CANFINHOME.NS','CHAMBLFERT.NS','CHOLAFIN.NS','CIPLA.NS','CUB.NS','COALINDIA.NS','COFORGE.NS','COLPAL.NS','CONCORD.BO','COROMANDEL.NS','CROMPTON.NS','CUMMINSIND.BO']
#stocks = ['GAIL.NS','GMRINFRA.NS','GODREJCP.NS','GRANULES.NS','GUJGASLTD.NS','GLENMARK.NS','GNFC.NS','GODREJPROP.NS','GRASIM.NS','GSPL.NS','HAL.NS','HCLTECH.NS','HDFCBANK.NS','HCLTECH.NS','HDFCBANK.NS','HDFC.NS','HINDALCO.NS','HINDPETRO.NS','HAVELLS.NS','HDFCAMC.NS','HDFCLIFE.NS','HEROMOTOCO.NS','HINDCOPPER.NS','HINDUNILVR.NS','ICICIBANK.NS','ICICIGI.NS','ICICIGOLD.NS','IDFCFIRSTB.NS','IDFC.NS','IBULHSGFIN.NS','INDIACEM.NS','IEX.NS','IOC.NS','IGL.NS','INFY.NS','IPCALAB.NS','ITC.NS','INDIAMART.NS','INDHOTEL.NS','INDIGO.NS','INDUSINDBK.NS','INTELLECT.NS','IRCTC.NS','JINDALSTEL.NS','JKCEMENT.NS','JSWSTEEL.NS','JUBLFOOD.NS','LAURUSLABS.NS','L&TFH.NS','LT.NS','LUPIN.NS','LICHSGFIN.NS']
#stocks = ['MGL.NS','M&M.NS','MARICO.NS','MFSL.NS','MPHASIS.NS','MCX.NS','M&MFIN.NS','MANAPPURAM.NS','METROPOLIS.NS','MSUMI.NS','MUTHOOTFIN.NS','NATIONALUM.NS','NAVINFLUOR.NS','NMDC.NS','NAUKRI.NS','NBCC.NS','NTPC.NS','OBEROIRLTY.NS','ONGC.NS','OFSS.NS','PETRONET.NS','PIDILITIND.NS','PEL.NS','PFC.NS','PNB.NS','PERSISTENT.NS','PFIZER.NS','PIIND.NS','POLYCAB.NS','POWERGRID.NS','PVRINOX.NS','SBICARD.NS','SBIN.NS','SUNPHARMA.NS','SYNGENE.NS','SBILIFE.NS','SRF.NS','SAIL.NS','SUNTV.NS','SHRIRAMFIN.NS','SIEMENS.NS','STAR.NS','TATACHEM.NS','TATACONSUM.NS','TATAPOWER.NS','TORNTPOWER.NS','TVSMOTOR.NS','TATACOMM.NS','TATAMOTORS.NS','TATASTEEL.NS']
stocks = ['DABUR.NS','DALMIASUG.NS','DEEPAKNTR.NS','DELTACORP.NS','DIVISLAB.NS','DIXON.NS','DLF.NS','LALPATHLAB.NS','DRREDDY.NS','EICHERMOT.NS','ESCORTS.NS','EXIDEIND.NS','FEDERALBNK.NS','FSL.NS','ZEEL.NS','WHIRLPOOL.NS','WIPRO.NS','VOLTAS.NS','VEDL.NS','KOTAKBANK.NS','LTIM.NS','LTTS.NS','UBL.NS','MCDOWELL-N.NS','UPL.NS','RAIN.NS','RBL.NS','RAMCOCEM.NS','RELIANCE.NS','TCS.NS','TITAN.NS','TECHM.NS','TRENT.NS','TORNTPHARM.NS','ABBOTINDIA.NS','BOSCHLTD.NS','HONAUT.NS','MARUTI.NS','MRF.NS','NESTLEIND.NS']

for ticker in stocks:
    temp = yf.Ticker(ticker)
    hist[ticker] = temp.history(period="252d")
    
    
def Volume(DR, a=10):
    dr=DR.copy()
    dr['signal']=dr['Volume'].ewm(span=a, min_periods=a).mean()
    return dr.loc[:,['signal']]
def Averages(DX):
    dx=DX.copy()
    dx['buy']=dx['Volume']-dx['WV']
    return dx.loc[:,['buy']]
#def Long(LG):
 #   lg=LG.copy()
        
    
for ticker in hist:
    hist[ticker]['WV']=Volume(hist[ticker])
for ticker in hist:
    hist[ticker]['Proceed']=Averages(hist[ticker])
for ticker in hist:
    cl_price[ticker]=hist[ticker]['Proceed']
    
final_list = cl_price.iloc[-1]
proceed = final_list[(final_list >= 0)]

for ticker in proceed.index:
    temp = yf.Ticker(ticker)
    today[ticker]=temp.history(period="52d")

#today=+ve_volume

for ticker in today:
    today[ticker]["return"]=today[ticker]["Close"].pct_change()


for ticker in today:
    temp2 = today[ticker].iloc[-1]
    oo = temp2[0]
    cc = temp2[3]
    if cc>oo:
        Green[ticker]=today[ticker]
        PLOTG[ticker]=today[ticker]
    if oo>cc:
        Red[ticker]=today[ticker]
        PLOTR[ticker]=today[ticker]

for ticker in PLOTG:
    PLOTG[ticker]=PLOTG[ticker][['Open','High','Low','Close']]
    
for ticker in PLOTR:
    PLOTR[ticker]=PLOTR[ticker][['Open','High','Low','Close']]   
    
for ticker in Green:
    BULL[ticker]=Green[ticker][['Close','return']]
    
for ticker in Red:
    BEAR[ticker]=Red[ticker][['Close','return']]
    
for ticker in PLOTG:
    PLOTG[ticker].head()
    mpl.plot(
    PLOTG[ticker],
    type="candle", 
    title = f"{ticker} BULL",  
    style="yahoo"
    )
    
for ticker in PLOTR:
    PLOTR[ticker].head()
    mpl.plot(
    PLOTR[ticker],
    type="candle", 
    title = f"{ticker} BEAR",  
    style="yahoo",
    )
    
#stock1 = today['ABBOTINDIA.NS']['Close','return']

#for ticker in YES:
 #   YES[ticker].to_excel(writer, sheet_name=ticker, index=False)


    
#stock1 = YES['ABBOTINDIA.NS']
#print(stock1)
#stock1.to_excel('created.xlsx', index=False)

#writer = pd.ExcelWriter('output.xlsx')
# write dataframe to excel
#stock1.to_excel(writer, sheet_name='Sheet1', index=False)
# save the excel



    
    