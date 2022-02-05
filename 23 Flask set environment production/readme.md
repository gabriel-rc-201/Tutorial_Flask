# Flask set environment production

O arquivo que coordena os ambientes de do projeto é o `config/init.py`, que se segue:

```python
# coding: UTF-8
import os
def load_config(mode=os.environ.get('MODE')):
    """Load config."""
    try:
        if mode == 'PRODUCTION':
            from .production import ProductionConfig
            return ProductionConfig
        elif mode == 'TESTING':
            from .testing import TestingConfig
            return TestingConfig
        else:
            from .development import DevelopmentConfig
            return DevelopmentConfig
    except ImportError:
        from .default import Config
        return Config
```

Por padrão, se você iniciar um servidor Flask, ele será definido para um determinado modo de ambiente.

Isso é exibido quando você executa o comando flask `example.py`.

> \* Serving Flask app "example" (lazy loading)  
> \* Environment: production  
> WARNING: This is a development server. Do not use it in a production deployment.
> Use a production WSGI server instead.  
> \* Debug mode: off  
> \* Running on http://0.0.0.0:5000/ (Press CTRL+C to quit)

nesse caso

> \* Environment: production

você pode rodar o seguinte comando de shell:

> export FLASK_ENV=development

isso vai mudar o ambite para:

> \* Environment: production
