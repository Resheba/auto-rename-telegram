import json
from bot import Bot

with open('config.json', 'r') as config:
    config_py = json.loads(config.read())
    BOTS = [Bot(**bot) for bot in config_py.get('bots')]
    CHANNELS = config_py.get('channels')


#JSON Structure

{
    "channels":
        [
            -1001978319159,
            -1001760896418
        ],
    "bots":
        [
            {
                "API_ID": 12345678, 
                "API_HASH": "25tt4t2fbawda66bf3beb43d7476d5f", 
                "PHONE": "8913333999", 
                "PASSWORD": "password"
            }
        ]
}