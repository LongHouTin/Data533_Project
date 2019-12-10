#!/usr/bin/env python
# coding: utf-8

# In[15]:


def webcrawl():
    import urllib.request
    from bs4 import BeautifulSoup as bs
    import lxml, html5lib
    import time
    from xlrd import open_workbook
    from xlutils.copy import copy
    import xlrd,xlrd,xlwt

    varname=["FEDPURCHASE","FEDSALE","CBOE_VIX","NASDAQ"]
    linkname=["https://alfred.stlouisfed.org/series?seid=RPONTTLD","https://alfred.stlouisfed.org/series?seid=RRPONTTLD","https://alfred.stlouisfed.org/series?seid=VIXCLS","https://alfred.stlouisfed.org/series?seid=NASDAQCOM"]
    toadd=[]
    i=0
    for i in range(len(linkname)):
        st=urllib.request.urlopen(linkname[i])
        ct = st.read().decode('utf-8')
        soup=bs(ct)
        soup.prettify()
        cc=soup.find_all('td') ##找到全部的日期和数值, cc是个list
        date=cc[0].string[0:10]
        if i==3:
            value=float(cc[1].string[0]+cc[1].string[2:]) ##when it is thousand, there is a comma, be careful
        else:
            value=float(cc[1].string)
        toadd.append(value)
        time.sleep(0.1)




    rb = open_workbook("packagedata.xls",formatting_info=True)  # copy, cannot directly writes original file
    wb = copy(rb)
    book=xlrd.open_workbook("packagedata.xls",formatting_info=True)
    sheet=book.sheet_by_index(0)
    s = wb.get_sheet(0)# 选取表单
    # writes
    for i in range(len(linkname)):
        style = xlwt.easyxf(num_format_str='YYYY-MM-DD')
        s.write(sheet.nrows,i+1,toadd[i])
    s.write(sheet.nrows,0,date)
    wb.save('packagedata2.xls')
    print("successfully crawling data from Fed! The most recent date is:{0}".format(date))
    return None

