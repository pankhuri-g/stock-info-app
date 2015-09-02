from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.symbol = "NONE"


@app.route('/')
def main():
  return redirect('/index')

@app.route('/index', methods=['GET','POST'])
def index():
  if request.method == 'GET':
     return render_template('index.html')
  else:
     app.symbol=request.form['symbol']
     return render_template('graph.html',ticker=app.symbol)

if __name__ == '__main__':
  app.run(port=33507)
