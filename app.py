import logging
from imports import Flask, routes, examples_ui, getConfigurate

cfg = getConfigurate()
app = Flask(__name__, static_url_path="/assets", static_folder='assets')
app.secret_key = cfg['server_secret_key']

app.register_blueprint(routes)
app.register_blueprint(examples_ui) 

log_state = bool(cfg['server_logging'])
log = logging.getLogger('werkzeug')
if log_state == True:
    log.disabled = False
elif log_state == False:
    log.disabled = True
    
    
if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))