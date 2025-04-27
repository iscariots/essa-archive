import scratchattach
import threading
import requests
import random
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

queueofprojectid = queue.Queue()
for i in mylist:
    queueofprojectid.put(i)

mysession = scratchattach.login("chaotic_legend", "qwerty")

print("successfully login now create remix!")

counter = 0

def create_remix():
    global counter
    global queueofprojectid
    while not queueofprojectid.empty():
        projectid = queueofprojectid.get()
        try:
            mysession.connect_project(projectid).create_remix().share()
            counter = counter + 1
            print(f"created! project: {projectid} {counter}")
        except:
            pass

for _ in range(30):
    threading.Thread(target=create_remix).start()