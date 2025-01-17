from flask import Blueprint, request, json
import yaml
 
sync = Blueprint('sync', __name__)

try:
  with open('./config.yml', 'r', encoding='utf-8') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
except:
  print("Failed to read config file.")
  exit()

global_secret = config['host']['secret']

@sync.route('/', methods=['POST'])
def index():
  postData = request.get_json()
  if (postData['secret'] == global_secret):
    clientname = postData['clientname']
    try:
      with open(f'./sync/{clientname}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(postData['data']))
      return("Sync done.",200)
    except:
      return("Sync received but failed to save.",500)
  else:
    return ("No matched secret.",401)