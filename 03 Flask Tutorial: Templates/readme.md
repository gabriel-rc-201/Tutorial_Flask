o flask tem um método para renderizar arquivos html

```python
from flask import render_template
render_template('templatefor.html', title='Welcome', members=users)
```

para renderizar esses arquivos eles têm de estar localizados em uma pasta chamada `templates`
