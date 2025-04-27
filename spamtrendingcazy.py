import scratchattach
import threading
import requests
import queue

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36",
    "referer": "https://scratch.mit.edu/",
    "accept": "*/*",
    "origin": "https://scratch.mit.edu"
}

mylist = []

for i in range(20):
    req = requests.get(f"https://api.scratch.mit.edu/explore/projects?limit=16&offset={i * 16}&language=en&mode=trending&q=*", headers=headers).json()
    for ii in req:
        mylist.append(ii["id"])
    print(f"sigma {i}")


print(len(mylist))

with open("accounts.txt") as f:
    data = f.readlines()
    realdata = []
    for i in data:
        realdata.append(i.strip())

queueofprojectid = []
for i in realdata:
    queueofprojectid.append(queue.Queue())
    for i in mylist:
        queueofprojectid[-1].put(i)

sessions = []
for i in realdata:
    sessions.append(scratchattach.login(i, "123456"))
    print(f"logined {i}")

counter = 0

def create_remix(myid):
    global counter
    global queueofprojectid
    mysession = sessions[myid]
    sigma = queueofprojectid[myid]
    while not sigma.empty():
        projectid = sigma.get()
        try:
            mysession.connect_project(projectid).create_remix().share()
            counter = counter + 1
            print(f"created! project: {projectid} {counter}")
        except:
            pass

for iiii in range(len(sessions)):
    for _ in range(20):
        threading.Thread(target=create_remix,args=(iiii,)).start()