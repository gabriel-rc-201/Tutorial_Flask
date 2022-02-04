para retor arquivos .json através do flask nós utilizamos a seguinte função: jsonify,  
segue exemplo de código:

```python
#!/usr/bin/env python
# encoding: utf-8
import json
from flask import Flask, jsonify
app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'name': 'alice',
                    'email': 'alice@outlook.com'})

app.run()
```

para uma API Rest nós comumente utilizamos os seguintes métodos HTTP:

- GET\* (pegar dados do banco)
- POST\* (cadastrar dados no banco)
- PUT\* (atualizar dados no banco)
- DELETE\* (deletar dados no banco)
- PATCH (atualizações mais pontuais no banco)
- HEAD (pega os cabeçalhos do banco)

\*-> são os mais utilizados

para utilizar esses métodos nós fazemos alterações no corpo da rota, como se segue:

```python
@app.route('/', methods=['GET'])
@app.route('/', methods=['PUT'])
@app.route('/', methods=['POST'])
@app.route('/', methods=['DELETE'])
```
