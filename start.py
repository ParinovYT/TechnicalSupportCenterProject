import src.config as config 
import src.main as main 

if __name__ == '__main__':
    config.load_configurate('src/config.json')
    main.app.run(port=int(config.data['server_port']), host=str(config.data['server_host']), debug=bool(config.data['server_debug']))
