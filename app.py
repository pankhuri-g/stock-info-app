from flask import Flask, render_template, request, redirect
#import appLogi
import flask
from bokeh.embed import components
from bokeh.plotting import figure
from bokeh.resources import INLINE
from bokeh.templates import RESOURCES
from bokeh.util.string import encode_utf8


app = Flask(__name__)
app.symbol = "NONE"


def getitem(obj, item, default):
    if item not in obj:
        return default
    else:
        return obj[item]


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

    """ Very simple embedding of a polynomial chart"""
    # Grab the inputs arguments from the URL
    # This is automated by the button
    args = flask.request.args

    # Get all the form arguments in the url with defaults
    color = colors[getitem(args, 'color', 'Black')]
    _from = int(getitem(args, '_from', 0))
    to = int(getitem(args, 'to', 10))

    # Create a polynomial line graph
    x = list(range(_from, to + 1))
    fig = figure(title="Polynomial")
    fig.line(x, [i ** 2 for i in x], color=color, line_width=2)

    # Configure resources to include BokehJS inline in the document.
    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/reference/resources_embedding.html#module-bokeh.resources
    plot_resources = RESOURCES.render(
        js_raw=INLINE.js_raw,
        css_raw=INLINE.css_raw,
        js_files=INLINE.js_files,
        css_files=INLINE.css_files,
    )

    # For more details see:
    #   http://bokeh.pydata.org/en/latest/docs/user_guide/embedding.html#components
    script, div = components(fig, INLINE)
    html = flask.render_template(
        'graph.html',
        plot_script=script, plot_div=div, plot_resources=plot_resources,
        color=color, _from=_from, to=to
    )
    return encode_utf8(html)
                                                                                      
  #return render_template('graph.html',ticker=app.symbol, mydata=5)#appLogic.build_graph(app.symbol))

if __name__ == '__main__':
  app.run(port=33507)
