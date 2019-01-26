import requests
import json

with open("details.json") as jfile:
    details = json.load(jfile)[0]

s = requests.Session()
site_url = "https://osu.ppy.sh/session"
s.post(site_url, data = details)
maplinks =  open("maplist.txt", "r") 
counter = 1

for x in maplinks:
    bm = s.get(x.rstrip())
    mapsetid = bm.url.split("/")[4].split('#')[0]
    link = "https://osu.ppy.sh/beatmapsets/"+mapsetid+"/download"
    downloaded_file = s.get(link)
    with open(str(counter)+".osz", "wb") as wf:
        wf.write(downloaded_file.content)
    print(counter)
    counter += 1
    
