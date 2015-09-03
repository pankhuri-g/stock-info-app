import Quandl
import pandas

def build_graph(ticker):

  mydata = Quandl.get("WIKI/"+ticker.upper()+".4", trim_start="2015-08-01", trim_end="2015-08-31")
  return float(mydata.ix[2,'Close'])
