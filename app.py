from flask import Flask
import yaml
from sync import sync
from web import web

try:
  with open('config.yml', 'r', encoding='utf-8') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
except:
  print("Failed to read config file.")
  exit()

theme = config['web']['theme']
if theme is None:
  theme = 'default'

app = Flask(__name__,static_url_path='/static', static_folder=f'static/{theme}/', template_folder=f'templates/{theme}')

app.register_blueprint(sync)
app.register_blueprint(web)

if __name__ == '__main__':
  appPort = config["host"]["port"]
  debug = config["host"]["debug"]
  if debug is None:
    debug = False
  if appPort:
    print(f"Host will run on port {appPort} sosu!")
  else:
    print(f"No specific port. Host will run on default 14514 sosu.")
    appPort = 14514
  app.run(port=appPort,debug=debug)