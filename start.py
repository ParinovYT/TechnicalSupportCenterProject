from flask import Flask, render_template
import config

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    config.load_configurate('config.json')
    app.run(port=int(config.data['server_port']), host=str(config.data['server_host']), debug=bool(config.data['server_debug']))