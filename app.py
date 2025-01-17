from flask import Flask, request, jsonify
import yaml
from sync import sync
from web import web

app = Flask(__name__)

with open('./config.yml', 'r', encoding='utf-8') as f:
  config = yaml.load(f.read(), Loader=yaml.FullLoader)

app.register_blueprint(sync, url_prefix='/sync')
app.register_blueprint(web, url_prefix='/')

if __name__ == '__main__':
  appPort = config["host"]["port"]
  if appPort:
    print(f"Host will run on port {appPort} sosu!")
  else:
    print(f"No specific port. Host will run on default 14514 sosu.")
    appPort = 14514
  app.run(port=appPort,debug=True)