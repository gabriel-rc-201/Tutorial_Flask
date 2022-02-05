Como o Flask é um microframework, ele permite que você decida sobre muitas coisas. A estrutura do código Flask é uma visão pessoal (ou visão da empresa).  
A estrutura de diretórios que eu recomendo é:

> ├── README.md
> ├── application
> │ ├── **init**.py
> │ ├── controllers
> │ │ └── **init**.py
> │ ├── forms
> │ │ └── **init**.py
> │ ├── models
> │ │ └── **init**.py
> │ ├── services
> │ │ └── **init**.py
> │ ├── static
> │ │ └── **init**.py
> │ ├── templates
> │ │ └── **init**.py
> │ └── utils
> │ └── **init**.py
> ├── config
> │ ├── **init**.py
> │ ├── default.py
> │ ├── development.py
> │ ├── development_sample.py
> │ ├── production.py
> │ ├── production_sample.py
> │ └── testing.py
> ├── deploy
> │ ├── flask_env.sh
> │ ├── gunicorn.conf
> │ ├── nginx.conf
> │ └── supervisor.conf
> ├── manage.py
> ├── pylintrc
> ├── requirements.txt
> ├── tests
> │ └── **init**.py
> └── wsgi.py

Uma breve introdução aqui:

- aplicação: Todos os códigos lógicos para um projeto são colocados aqui
- config: o arquivo de configuração do projeto
- deploy: arquivos relacionados à implementação
- testes: o arquivo de diretório no qual o código do teste de unidade está localizado:
- `manage.py`: arquivo de execução do Flask-Script
- pylintrc: padrão pylint
- requirements.txt: lista de bibliotecas dependentes do projeto
- `wsgi.py`: wsgi executar

segue exemplos de alguns arquivos do tutorial
