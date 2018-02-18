import pandas_datareader.data as web
import numpy as np
import pandas as pd
 
stock = 'AAPL'
 
data = web.DataReader(stock,data_source="google",start='01/01/2010')['High']
 
data.sort_index(inplace=True)
 
returns = data.pct_change()
 
mean_return = returns.mean()
return_stdev = returns.std()
 
annualised_return = round(mean_return * 252,2)
annualised_stdev = round(return_stdev * np.sqrt(252),2)
 
print ('The annualised mean return of stock {} is {}, and the annualised volatility is {}').format(stock,annualised_return,annualised_stdev)
