from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
  return 'Web App with Python Flask!'

@app.route('/hello')
def hello_world():
    return "Hello World!"

# route params
@app.route('/product/<name>')
def get_product(name="relogio"):
  return "The product is " + str(name)

@app.route('/sale/<transaction_id>')
def get_sale(transaction_id=0):
  return "The transaction is "+str(transaction_id)

@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name


app.run(host='0.0.0.0', port=3333)