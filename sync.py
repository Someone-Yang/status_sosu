from flask import Blueprint, request, json
import yaml
 
sync = Blueprint('sync', __name__)

with open('./config.yml', 'r', encoding='utf-8') as f:
  config = yaml.load(f.read(), Loader=yaml.FullLoader)

global_secret = config['host']['secret']

@sync.route('/', methods=['POST'])
def index():
  postData = request.get_json()
  if (postData['secret'] == global_secret):
    clientname = postData['clientname']
    with open(f'./sync/{clientname}.json', 'w', encoding='utf-8') as file:
      file.write(json.dumps(postData['data']))
    return("Sync done.",200)
  else:
    return ("No matched secret.",401)