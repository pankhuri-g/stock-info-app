from flask import Flask, render_template, request, redirect
#import appLogic

app = Flask(__name__)
app.symbol = "NONE"


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  if request.method == 'GET':
     return render_template('index.html')

@app.route('/graph',methods=['POST'])
def graph():
  app.symbol=request.form['symbol']                                                                                             
  return render_template('graph.html',ticker=app.symbol, mydata=5)#appLogic.build_graph(app.symbol))

if __name__ == '__main__':
  app.run(port=33507)
