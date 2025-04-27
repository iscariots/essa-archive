import requests
import re
import json

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    "x-csrftoken": "a",
    "x-requested-with": "XMLHttpRequest",
    "referer": "https://scratch.mit.edu/",
}

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
        self.password = None
        self._cookies = {
            "scratchsessionsid" : self.session_id,
            "scratchcsrftoken" : "a",
            "scratchlanguage" : "en",
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
        global loginsuccess
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
            raise Exception("error processing proxy")
        if itssucess == True:
            try:
                self.session_id = re.search('"(.*)"', request.headers["Set-Cookie"]).group()
                self.token = request.json()[0]["token"]
                self._cookies["scratchsessionsid"] = self.session_id
                self._headers["x-token"] = self.token
                self.password = password
                self.get_csrf_token()
                loginsuccess = True
                #print(self._cookies)
            except AttributeError:
                loginsuccess = False
                raise Exception("username or password its invalid")
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
        #print(self._headers)
        #print(self._cookies)
        #print(self._headers["x-csrftoken"])
    
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
        #print(self._headers["x-csrftoken"])
        return self.csrf_token
    
def get_csrf_tokenn():
        headers = {
            "x-requested-with": "XMLHttpRequest",
            "Cookie": "scratchlanguage=en;permissions=;",
            "referer": "https://scratch.mit.edu",
        }

        request = requests.get("https://scratch.mit.edu/csrf_token/", headers=headers, timeout=5)
        csrf_token = re.search(
            "scratchcsrftoken=(.*?);", request.headers["Set-Cookie"]
        ).group(1)
        #print(self.csrf_token)

        #print(self._headers)
        #print(self._cookies)
        #print(self._headers["x-csrftoken"])
        return csrf_token