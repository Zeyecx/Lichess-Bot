import requests
import json
import datetime
from configparser import ConfigParser

parser = ConfigParser()
parser.read("parameter.ini")

configObject = parser["PARAMS"]
id_team = configObject["teamID"]
team_name = configObject["teamname"]

url = "https://lichess.org/api/team/" + id_team + "/users"
param = dict()
resp = requests.get(url=url,params=param)
list_resp = resp.text.splitlines()
data = list(map(lambda x: json.loads(x), list_resp))

fault_users = []
for i in data:
    is_faulti = i.get("tosViolation")
    if is_faulti:
        user = i.get("username")
        fault_users.append(user)

now = datetime.datetime.today()
date = now.strftime('%d.%m.%Y')
datei = open('blacklist.txt','a')
datei.write("\n\nIn the Team " + team_name + ", found at: " + date)
for i in fault_users:
    print(i)
    datei.write("\nhttps://lichess.org/@/" + i)