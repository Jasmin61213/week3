import ssl
from types import coroutine
ssl._create_default_https_context = ssl._create_unverified_context
import urllib.request as request
import json
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式
clist=data["result"]["results"]
with open("week3.csv","w",encoding="utf-8") as file:
    for scene in clist:
        year=int(scene["xpostDate"].split("/")[0])
        if year>=2015:
            # print(year)
            address=scene["address"].split()[1]
            address=address.split("區")[0]+"區"
            jpg="https"+scene["file"].split("https")[1]
            file.write(scene["stitle"]+","+address+","+scene["longitude"]+","+scene["latitude"]+","+jpg+"\n")
    # for xpostDate in clist:
    #     year=xpostDate["xpostDate"].split("/")[0]
    #     # file.write(year+"\n")
    # for stitle in clist:
    #     title=stitle["stitle"]
    # # for address in clist:
    # #     print(address["address"])
    # for longitude in clist:
    #     longitude=longitude["longitude"]
    # for latitude in clist:
    #     latitude=latitude["latitude"]
    # for jfile in clist:
    #     # jpg=file["file"].split(".")[0]+"."+file["file"].split(".")[1]+"."+file["file"].split(".")[2]+".jpg"
    #     jpg="https"+jfile["file"].split("https")[1]
    #     file.write(year+","+jpg+"\n")
# title_series=pd.Series(title,name="title")
# result_dataframe = pd.concat([title],axis=1)
# result_dataframe.to_csv('week3.csv', index = None)
# with open("week3.csv","w",encoding="utf-8") as csvfile:
#     writer=csv.writer(csvfile)
#     writer.writerows([])
