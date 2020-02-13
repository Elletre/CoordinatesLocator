import requests
import json

f = open('data.txt', 'r')
line = f.readline()
resultLines = []
while line:
    result = line.split(",")[4] + line.split(",")[5] + line.split(",")[6]
    r = requests.get(url="http://search.maps.sputnik.ru/search?q="+result)
    y = json.loads(r.text)
    lat = (y["result"][0]["position"]["lat"])
    lon = (y["result"][0]["position"]["lon"])
    line = line.replace("NULL", str(lat), 1)
    line = line.replace("NULL", str(lon), 1)
    resultLines.append(line)
    line = f.readline()
f.close()
f = open('data.txt', 'w')
f.writelines(resultLines)
f.close()
