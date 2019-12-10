#!/usr/bin/env python
# coding: utf-8

# In[39]:


def linechart():
    import pygal
    import pandas as pd

    data=pd.read_excel("packagedata2.xls")
    buy=list(data.iloc[-10:,1])
    sell=list(data.iloc[-10:,2])
    date=list(data.iloc[-10:,0])
    date=[str(date[i])[:10] for i in range(len(date))]

    # str(date[2])[:10]
    # bar_chart = pygal.Bar()
    # bar_chart.add('FedPurchase', buy)
    # bar_chart.add('FedSale',sell)


    # from IPython.display import SVG, display
    # display(SVG(bar_chart.render(disable_xml_declaration = True)))
    # # operation()  


    line_chart = pygal.Line()

    line_chart.title = 'Last 10 Days US Federal Reserve Open Market Operation'

    line_chart.x_labels = date
    line_chart.add('OvernightPurchase',buy)
    line_chart.add('OvernightSale',sell)
    


    from IPython.display import SVG, display
    display(SVG(line_chart.render(disable_xml_declaration = True)))
    


    
def barchart30days():
    import pygal 
    import pandas as pd
    
    ct=-30
    data=pd.read_excel("packagedata2.xls")
    buy=list(data.iloc[ct:,1])
    sell=list(data.iloc[ct:,2])
    net=list(map(lambda x,y:x-y, buy,sell))
    date=list(data.iloc[ct:,0])

    date=[str(date[i])[:10] for i in range(len(date))]


    # line_chart = pygal.Line()

    bar_chart = pygal.Bar(x_label_rotation=270)
    bar_chart.add('Fed Net Purchase', net)
    bar_chart.x_labels = date

    from IPython.display import SVG, display
    display(SVG(bar_chart.render(disable_xml_declaration = True)))
    

    
    
    

def barchartyrs():
    import pygal 
    import pandas as pd

    ct=-504
    data=pd.read_excel("packagedata2.xls")
    buy=list(data.iloc[ct:,1])
    sell=list(data.iloc[ct:,2])
    net=list(map(lambda x,y:x-y, buy,sell))
    date=list(data.iloc[ct:,0])

    date=[str(date[i])[:10] for i in range(len(date))]


    # line_chart = pygal.Line()

    bar_chart = pygal.Bar(x_label_rotation=90)
    bar_chart.add('Fed Net Purchase', net)
    bar_chart.x_labels = date

    from IPython.display import SVG, display
    display(SVG(bar_chart.render(disable_xml_declaration = True)))
