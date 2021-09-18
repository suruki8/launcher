import requests
import json
key = "A9508EC2E9B74E44ABCFD01ADA3FB24E"
id = "76561198052122833"
uri = f"http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key={key}&steamid={id}&format=json&include_appinfo=true"
# uri = "https://steamcommunity.com/id/ZeIED"
responce = requests.get(uri)
games =  responce.json()['response']['games']
# apid= []
# for i in games:
#     apid.append(i['appid'])
apid = list(map(lambda x : x['appid'], games))

print(apid)
# with open('test.json', 'wt') as f:
    # json.dump(games, f)