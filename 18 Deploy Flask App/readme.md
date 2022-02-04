podemos colocar a aplicação online tanto atravez do [PythonAnywhere](https://www.pythonanywhere.com/?affiliate_id=00535ced)

mas também podemos fazer através de um servidor proprio utilizando o Apache

para usar ele instalamos o `mod_wsgi`, que é um modulo apache

```sh
pip install mod_wsgi
```

para veirficar se a instalação foi bem sucedidad usamos o seguinte comando:

```sh
mod_wsgi-express start-server
```

ele vai rodar através da porta 8000 do localhost

Configure Apache you need to tell mod_wsgi, where your application is located:
configurando o Apache nós precisamos falar ao mod_wsgi, onde a sua aplicação está localizada:

```html
<VirtualHost *>
  ServerName example.com WSGIScriptAlias / C:\yourdir\yourapp.wsgi

  <Directory C:\yourdir> Order deny,allow Allow from all </Directory>
</VirtualHost>
```
