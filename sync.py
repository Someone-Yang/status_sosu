from flask import Blueprint, request, json
import yaml,datetime


try:
  with open('config.yml', 'r', encoding='utf-8') as f:
    config = yaml.load(f.read(), Loader=yaml.FullLoader)
except:
  print("Failed to read config file.")
  exit()

sync = Blueprint('sync', __name__)

global_secret = config['host']['secret']

@sync.route('/sync', methods=['POST'])
def index():
  postData = request.get_json()
  if (postData['secret'] == global_secret):
    clientname = postData['clientname']
    current_time = int(datetime.datetime.now().timestamp())
    lastrecord = 0
    lastsent = 0
    lastreceived = 0
    try:
      with open(f'sync/{clientname}.json', 'r', encoding='utf-8') as sf:
        data = json.loads(sf.read())
      lastrecord = data['lastrecord']
      lastsent = data['network']['sent']
      lastreceived = data['network']['received']
    except:
      print(f"Cannot read last record of {clientname}. Skip.")
    nData = postData['data']
    nData['lastrecord'] = current_time
    nData['network']['sentd'] = nData['network']['sent'] - lastsent
    nData['network']['receivedd'] = nData['network']['received'] - lastreceived
    nData['recordd'] = current_time - lastrecord
    try:
      with open(f'sync/{clientname}.json', 'w', encoding='utf-8') as file:
        file.write(json.dumps(nData))
      return("Sync done.",200)
    except:
      return("Sync received but failed to save.",500)
  else:
    return ("No matched secret.",401)