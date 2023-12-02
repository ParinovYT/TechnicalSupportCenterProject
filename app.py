from flask import Flask
from src.config import load_configurate
from routes import routes
from src.examples_ui import examples_ui

cfg = load_configurate('src/config.json')
app = Flask(__name__, static_url_path="/assets", static_folder='assets')

app.register_blueprint(routes)
app.register_blueprint(examples_ui) 

if __name__ == '__main__':
    app.run(host=cfg['server_host'], port=int(cfg['server_port']), debug=bool(cfg['server_debug']))
