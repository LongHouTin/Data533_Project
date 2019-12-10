#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
def netPurchaseChange(date):
    data= pd.read_excel("packagedata.xls")
    data.FEDPURCHASE[data.DATE==date].values-data.iloc[data[data.DATE==date].index-1,1].values ## calculate change
    a=(data.FEDPURCHASE[data.DATE==date].values-data.iloc[data[data.DATE==date].index-1,1].values)/data.iloc[data[data.DATE==date].index-1,1].values
    b=round(a[0],4) # rounding
    return b

def netPurchase(date):
    data= pd.read_excel("packagedata.xls")
    change=data.FEDPURCHASE[data.DATE==date].values-data.FEDSALE[data.DATE==date].values ## calculate change
    return change[0]

def vix(date): # calculate past 20 days CBOE_VIX standard deviation
    data= pd.read_excel("packagedata.xls")
#     from statistics import stdev
    vix=data.CBOE_VIX[data.DATE==date].values
    return vix

def nasdaq(date):
    data= pd.read_excel("packagedata.xls")
    nas=data.NASDAQ[data.DATE==date].values
    return float(str(nas)[1:8])

    

    
    
# In[ ]:




