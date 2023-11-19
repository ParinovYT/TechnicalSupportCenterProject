from flask import Flask, render_template
import json

app = Flask(__name__)

config = 0


@app.route('/')
def index():
    return render_template('index.html')

def load_configurate(file:str):
    global config
    with open(file) as f:
        config = json.load(f)  

if __name__ == '__main__':
    load_configurate('config.json')
    app.run(port=int(config['server_port']), host=str(config['server_host']), debug=bool(config['server_debug']))