from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  users = [ 'Raquel','Deyse','Israely' ]
  return render_template('templatefor.html', title='Welcome', members=users)

app.run(host='0.0.0.0', port=3333)