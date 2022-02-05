#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify, request
from flask_mongoengine import MongoEngine

app = Flask(__name__)

# cofigura os dados para acessar o banco de dados
app.config['MONGODB_SETTINGS'] = {
  'db': 'your_database',
  'host': 'localhost',
  'port': 27017
}
db = MongoEngine()
db.init_app(app)

# cria o modelo do objeto que vai ser armazenado no banco de dados
class User(db.Document):
  name = db.StringField()
  email = db.StringField()
  def to_json(self):
    return {"name": self.name,
            "email": self.email}

# adiciona/salva um dado no banco de dados
@app.route('/', methods=['POST'])
def create_record():
    record = json.loads(request.data)
    user = User(name=record['name'],
                email=record['email'])
    user.save()
    return jsonify(user.to_json())

# atualiza um linha no banco de dados
@app.route('/', methods=['PUT'])
def update_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.update(email=record['email'])
    return jsonify(user.to_json())

# deleta um dado do banco de dados
@app.route('/', methods=['DELETE'])
def delete_record():
    record = json.loads(request.data)
    user = User.objects(name=record['name']).first()
    if not user:
        return jsonify({'error': 'data not found'})
    else:
        user.delete()
    return jsonify(user.to_json())

if __name__ == "__main__":
  app.run(debug=True)