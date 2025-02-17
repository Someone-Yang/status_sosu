from flask import Blueprint, json, render_template
import yaml,datetime
 
try:
  with open('config.yml', 'r', encoding='utf-8') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
except:
  print("Failed to read config file.")
  exit()

theme = config['web']['theme']
if theme is None:
  theme = 'default'
web = Blueprint('web', __name__)

@web.route('/', methods=['GET'])
def index():
  datas = []
  for client in config["client"].keys():
    try:
      with open(f'sync/{client}.json', 'r', encoding='utf-8') as sf:
        data = json.loads(sf.read())
        current_time = int(datetime.datetime.now().timestamp())
        data["clientname"] = client
        data["timed"] = current_time - data['lastrecord']
        datas.append(data)
    except:
      print(f"Could not read saved file for clientname {client}, skip.")
      continue
  return render_template('index.html', client=config['client'], datas=datas, web=config['web'])