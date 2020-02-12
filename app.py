from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('app_config.py')
from views import *

# sexta feira - deletar uma numeracao*--condições!

if __name__ == "__main__":
    app.run(debug=True, host='10.75.19.181', port='8086')
