import logging
from src.config import Config
from imports import Flask, routes, examples_ui

app = Flask(__name__, static_url_path="/assets", static_folder='assets')
app.secret_key = Config.get('server_secret_key')

app.register_blueprint(routes)
app.register_blueprint(examples_ui) 

log_state = bool(Config.get('server_logging'))
log = logging.getLogger('werkzeug')
if log_state == True:
    log.disabled = False
elif log_state == False:
    log.disabled = True
       
if __name__ == '__main__':
    app.run(host=Config.get('server_host'), port=int(Config.get('server_port')), debug=bool(Config.get('server_debug')))