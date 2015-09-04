from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html
from bokeh.util.string import encode_utf8
import requests                                                                                                                    
import simplejson                                                                                                                  
from datetime import datetime                                                                                                      
                                                
app = Flask(__name__)                                                                                                              
app.symbol = "NONE" 

def build_graph(ticker):                                                                                   
  url = 'https://www.quandl.com/api/v3/datasets/WIKI/'+ ticker.upper() +'.json?column_index=4&start_date=2015-08-01&end_date=2015-08-31&order=asc' 
  data = requests.get(url).text                                                                                                    
  data = simplejson.loads(data)

  #pick out useful list from json                                                                                                 
  stock_data = data['dataset']['data']
  stock_value = [ member[1] for member in stock_data ]                                                                        
  stock_date = [ datetime.strptime(str(member[0]), '%Y-%m-%d') for member in stock_data ] 

  #use lists generated as x and y axes
  plot = figure(x_axis_type = "datetime")
  plot.line(stock_date, stock_value, legend=ticker.upper()+': Close')
  plot.title = ticker.upper() + ": Aug-2015 Data from Quandl WIKI"
  plot.xaxis.axis_label = 'Date'
  plot.yaxis.axis_label = 'Price'
  plot.circle(stock_date, stock_value)
  html = file_html(plot, CDN, ticker.upper()+" Closing Price plot")
  return html

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
    graph_html = build_graph(str(app.symbol))
    return encode_utf8(graph_html)   
 

if __name__ == '__main__':
  app.run(port=33507)
