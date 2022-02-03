from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)
mail = Mail(app)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'your@email.com'
app.config['MAIL_PASSWORD'] = '******'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True


@app.route("/")
def index():
  msg = Message('Hello', sender = 'your@email.com', recipients = ['ganriel201@gmail.com'])
  msg.body = "This is the email body"
  mail.send(msg)
  return "Sent"

if __name__ == '__main__':
   app.run(debug = True)