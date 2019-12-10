
### Team Member:

Name | StudentID | GithubID
:--- | :--- | :---
Long Hou Tin | 49341431 | LongHouTin
Harry Yuanlong Sun | 77091445 | Harrysun26

> PackageName: fed
>
> Description: obtain online data, update local excel files, manipulation data and visualize.



&nbsp;
### Background Description:

- The goal of the package is to help user conveniently obtain part of US federal Reserve open market operation data and have a basic idea of what is happening in the US open market operation.   

- The US Federal Reserve resume its asset purchase since Oct 15 2019 .  The current balance of US federal reserve is close to US$4000billion, and it is expanding at a rate of 60billion/month, until second quarter next year.
  
- Asset purchase(quantitative easing ) are extreme measures during crisis to shift financial market participant’s expectation on monetary policy, providing support for asset prices, i.e. 2007, The Great Depression in 1930s.  

- By observing this data, it is helpful to understand the market because when equity market at high positions becomes inactive to such easing monetary environment, the easing effects is over, which means there will be collapse following (considering the business profits are decreasing) .  

- In addition to US federal Reserve open market operation data, the package also monitoring on Hang Seng Index. Hang Seng Index is a stock market index consisting of 50 of the largest and most liquid companies listed on the Hong Kong Stock Exchange. This accounts for more than half of its total market capitalization. It is designed to mimic the overall performance of the stock market at any given time, thus providing international investors with a quick glance into the health of Hong Kong's stock market, which can be difficult to see when looking at individual equities. Which this sub-package, user can easily retrieve current and historic quote of Hang Seng Index and its constituents for reference or further analysis.

- Sub-packages of this package (functions to realize):
  - Obtain data(updated daily) from Federal reserve website
  - Data cleaning and saving into “.xls” files; show head and tail
  - Data presentation (i.e. federal reserve operation, purchase and sale, Hang Seng Index and historical price of its consituent stocks)



&nbsp;
### 5 sub-packages in total: 

> Harry Yuanlong Sun: `crawl`, `readfile`, `draw`, `calculate`
>
> Long Hou Tin: `HSI`



### The current structure of the package is as follows:

`Package` | `Sub-package` | `modules(.py)` | `Function Names` | `Explanations on functions`
:---: | :--- | :--- | :--- | :---
Package | Sub-package | modules(.py) | Function Names | Explanations on functions 
fed | crawl | crawl | webcrawl() | Scrape data from US Fed daily: Manually
fed | draw | visualize | linechart() | Show line chart of fed data
fed | craw | visualize | barchart30days() | Bar chart of fed net overnight purchase-30d
fed | craw | visualize | barchartyrs() | Bar chart of fed net overnight purchase-500d
fed | calculate | fmath | netPurchaseChange(date) | Net purchase change compared with previous day (%) 
fed | calculate | fmath | netPurchase(date) | Certain date’s net purchase
fed | calculate | fmath | nasdaq(date) | Return nasdaq index value of certain date
fed | calculate | fmath | vix(date) | Return vix value of certain date
fed | HSI | instant | indices() | Retrieve instant quote of HIS from internet
fed | HSI | instant | stocks() | Retrieve instant of its 50 constituents
fed | HSI | historic | getprices() | Return historic prices of the stocks 
fed | HSI | historic | plotprices() | Plot (multiple) time series of the price
fed | HSI | historic | getreturns() | Return standard daily returns of the price
fed | HSI | historic | getlogreturns() | Return log daily returns of the price
fed | HSI | historic | plotreturns() | Plot histogram of (log) return



&nbsp;
### Package Structure:

> fed/
>
> &nbsp;&nbsp;&nbsp;&nbsp; \_\_init\_\_.py
>
> &nbsp;&nbsp;&nbsp;&nbsp; crawl/
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \_\_init\_\_.py
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `crawl.py`
>
> &nbsp;&nbsp;&nbsp;&nbsp; draw/
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \_\_init\_\_.py
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `visualize.py`
>
> &nbsp;&nbsp;&nbsp;&nbsp; calculate/
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \_\_init\_\_.py
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `fmath.py`
>
> &nbsp;&nbsp;&nbsp;&nbsp; HSI/
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; \_\_init\_\_.py
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `instant.py: this module use inheritance`
>
> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; `historic.py`




&nbsp;
### Appendix：

- Data relevant links: 
  - Overnight Total sales by Fed:
    https://alfred.stlouisfed.org/series?seid=RRPONTTLD
  - Overnight Total purchase by Fed:
    https://alfred.stlouisfed.org/series?seid=RPONTTLD
  - Nasdq Stock Index:
    https://alfred.stlouisfed.org/series?seid=NASDAQCOM
  - Volatility Index:
    https://alfred.stlouisfed.org/series?seid=VIXCLS
  - Hang Seng Index:
    http://www.aastocks.com/en/stocks/market/index/hk-index-con.aspx

&nbsp;
- Project info available at: https://github.com/harrysun26/Data533Labs
