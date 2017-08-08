from flask import Flask
from flask_bootstrap import Bootstrap


app = Flask(__name__)
app.config['SECRET_KEY'] = 'fd8bac171093f571f831ba0e8fd5aaf2314ed27a611e4dbe'

bootstrap = Bootstrap(app)

from . import views
