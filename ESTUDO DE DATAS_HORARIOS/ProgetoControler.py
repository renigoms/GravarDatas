import json
import addinfo
import datetime



def gravardados(x,y):
    with open('BdDatas', 'w') as arqjson:
        json.dump(x, arqjson, indent=y)

def lerarqjson():
    with open('BdDatas', 'r+') as arqjson:
        global diciodatas
        diciodatas = json.load(arqjson)



