from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.util.string import encode_utf8


import requests                                                                                                                    
import pandas                                                                                                                      
import simplejson                                                                                                                  
#from collections import OrderedDict                                                                                               
from datetime import datetime                                                                                                      
                                                                                                                                   
url = 'https://www.quandl.com/api/v3/datasets/WIKI/AAPL.json?column_index=4&start_date=2015-08-01&end_date=2015-08-31&order=asc' 
data = requests.get(url).text                                                                                                    
data = simplejson.loads(data)                                                                                                    
stock_data=data['dataset']['data']                                                                                               
  #print type(stock_data[0][1])                                                                                                    
  #stock_dict = OrderedDict()                                                                                                      
  #stock_dict = dict(stock_data)                                                                                                   
  #print type(stock_dict)                                                                                                          
  #print (stock_dict)                                                                                                              
  #return float(mydata.ix[2,'Close'])                                                                                              
stock_value = [member[1] for member in stock_data]                                                                               
stock_date = [datetime.strptime(str(member[0]), '%Y-%m-%d') for member in stock_data] 

"""
plot = figure()
plot.circle([1,2], [3,4])
html = file_html(plot, CDN, "my plot")
"""

app = Flask(__name__)
app.symbol = "NONE"

plot = figure(x_axis_type = "datetime")
#plot.line(x=[1, 2, 3, 4, 5], y=[6, 7, 2, 4, 5])
plot.line(stock_date, stock_value)
plot.title = "Stock Closing Prices"
html = file_html(plot, CDN, "my plot")

@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET'])
def index():
  if request.method == 'GET':
     return render_template('index.html')

@app.route('/graph',methods=['POST'])
def graph():
    app.symbol=request.form['symbol']       
    #return render_template('graph.html',ticker=app.symbol, mydata=5)#appLogic.build_graph(app.symbol))
    return encode_utf8(html)   


if __name__ == '__main__':
  app.run(port=33507)
