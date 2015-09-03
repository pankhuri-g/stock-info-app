from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.resources import CDN
from bokeh.embed import file_html

"""
plot = figure()
plot.circle([1,2], [3,4])
html = file_html(plot, CDN, "my plot")
"""

app = Flask(__name__)
app.symbol = "NONE"


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
    return render_template('graph.html',ticker=app.symbol, mydata=5)#appLogic.build_graph(app.symbol))
    #return render_template(html)    


if __name__ == '__main__':
  app.run(port=33507)
