### flask extensions:

- **Flask Mail** - providencia uma interface SMTP para as aplicações Flask

- **Flask WTF** - Adiciona validação e renderização do WTForms

- **Flask SQLAlchemy** - Adiciona suporte SQLAlchemy para as aplicações Flask

- **Flask Sijax-Sijax** - biblioteca interface-Python/jQuery para construir requisições AJAX faceis de usar em aplicações web

### Como importar

As extensões Flask são tipicamente nomeadas como flask-foo

A importação é como se segue:

```python
from flask_foo import [class, function]
```

Para as versões do Flask depois da 0.7, você também pode usar a sintax

```python
from flask.ext import foo
```

Às vezes, o módulo de compatibilidade precisa ser ativado. Ele pode ser instalado executando o flaskext_compat.py:

```python
import flaskext_compat
flaskext_compat.activate()
from flask.ext import foo
```
