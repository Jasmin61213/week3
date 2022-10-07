import ssl
from types import coroutine
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response)
clist=data["result"]["results"]
with open("week3.csv","w",encoding="utf-8") as file:
    for scene in clist:
        year=int(scene["xpostDate"].split("/")[0])
        if year>=2015:
            address=scene["address"].split()[1]
            address=address.split("區")[0]+"區"
            jpg="https"+scene["file"].split("https")[1]
            file.write(scene["stitle"]+","+address+","+scene["longitude"]+","+scene["latitude"]+","+jpg+"\n")
