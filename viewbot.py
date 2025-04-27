import scratchattach as sa
import threading
import time
import requests

ADD_HOW_MANY = 1000000000000000000
MODE = "proxy"
DELAY = 0

files = open("viewbot.txt")
spammer = files.readlines()
listofspamer = []
i = 0

#6446649
#5842709

for iu in range(int(len(spammer) / 2)):
    listofspamer.append(spammer[i].split("\n")[0])
    i = i + 2

print(f"{len(listofspamer)} ignore this")

proxies = []

with open("scannedproxy.txt") as f:
    proxies_raw = f.readlines()
    for i in proxies_raw:
        if not i.split("\n")[0] in proxies:
            proxies.append(i.split("\n")[0])

with open("working_proxy.txt") as f:
    proxies_raw = f.readlines()
    for i in proxies_raw:
        if not i.split("\n")[0] in proxies:
            proxies.append(i.split("\n")[0])

with open("working_proxy_maybe.txt") as f:
    proxies_raw = f.readlines()
    for i in proxies_raw:
        if not i.split("\n")[0] in proxies:
            proxies.append(i.split("\n")[0])

with open("saved_working_proxy.txt") as f:
    proxies_raw = f.readlines()
    for i in proxies_raw:
        if not i.split("\n")[0] in proxies:
            proxies.append(i.split("\n")[0])

with open("working_proxy2.txt") as f:
    proxies_raw = f.readlines()
    for i in proxies_raw:
        if not i.split("\n")[0] in proxies:
            proxies.append(i.split("\n")[0])

#with open("saved_proxy.txt") as f:
 #   proxies_raw = f.readlines()
  #  for i in proxies_raw:
   #     proxies.append(i.split("\n")[0])

#with open("saved_proxy2.txt") as f:
 #   proxies_raw = f.readlines()
  #  for i in proxies_raw:
   #     proxies.append(i.split("\n")[0])

#with open("savedproxy.txt") as f:
 #   proxies_raw = f.readlines()
  #  for i in proxies_raw:
   #     proxies.append(i.split("\n")[0])

#response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
#for i in response.json()["data"]:
 #   proxies.append(str(i["ip"]) + ":" + str(i["port"]))

print(f"{len(proxies)} different proxy found")

#fornow = False

#if fornow == True:
 #   for i in proxies:
  #      with open("sigma_proxy.txt", "a") as f:
   #         f.write(f"{i}\n")

#print(proxies)

#AUTH = {"username": "PragnaAyitha", "password": "1234567890"}

globali = 0
givenprojectid = input("input your project id: ")
response3 = requests.get(f"https://api.scratch.mit.edu/projects/{givenprojectid}").json()
givenuser = response3["author"]["username"]
views = response3["stats"]["views"]
print(f"project you want botted have {views} views")
print("view botting for user " + givenuser)
faileds = 0

time.sleep(1)

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu",
}

def getrealviews():
    global views
    try:
        response3 = requests.get(f"https://api.scratch.mit.edu/projects/{givenprojectid}",
            headers = {
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36",
                "Pragma" : "no-cache",
                "Cache-Control" : "no-cache"
                }
        ).json()
        views = response3["stats"]["views"]
        print("views has been updated")
    except:
        pass

def getviews():
    while True:
        getrealviews()
        time.sleep(10)

def addview(accountid):
    global globali
    #try:
    session = sa.login(listofspamer[accountid], "123456")
    project = sa.get_project(givenprojectid)
    project.post_view()
    project2 = session.connect_project(givenprojectid)
    project2.post_view_auth()
    print(f"sucessfully add view {globali} with account {listofspamer[accountid]}")
    #except:
        #print(f"failed to add view with account {globali} {listofspamer[accountid]}")
    globali = globali + 1

def add_view_proxy(proxy):
    global faileds
    global globali
    global views
    try:
        res = requests.post(
            f"https://api.scratch.mit.edu/users/{givenuser}/projects/{givenprojectid}/views/",
            headers=headers,
            proxies={"http":proxy, "https":proxy}
        )
        if str(res.status_code) == "200":
            print(f"successfully add view {globali} with proxy {proxy} now project have {views} views request code {res.status_code}")
            globali = globali + 1
        #elif str(res.status_code) == "429":
            #print(f"failed to add view and proxy {proxy} is rate limited")
    except:
        faileds = faileds + 1
        #print(f"failed add view {globali} with proxy {proxy}")

idofspammer = 0

threading.Thread(target=getviews).start()

for _ in range(ADD_HOW_MANY):
    if MODE == "account":
        if idofspammer > len(listofspamer) - 1:
            idofspammer = 0
        threading.Thread(target=addview, args=(idofspammer,)).start()
    elif MODE == "proxy":
        if idofspammer > len(proxies) - 1:
            idofspammer = 0
        threading.Thread(target=add_view_proxy, args=(proxies[idofspammer],)).start()
    time.sleep(DELAY)
    idofspammer = idofspammer + 1