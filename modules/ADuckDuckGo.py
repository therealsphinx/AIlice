import requests

from common.lightRPC import makeServer
from modules.AScrollablePage import AScrollablePage

class ADuckDuckGo():
    def __init__(self):
        self.baseURL = "https://api.duckduckgo.com/"
        self.page = AScrollablePage(functions={"SCROLLDOWN": "SCROLLDOWNDUCKDUCKGO"})
        return
    
    def ModuleInfo(self):
        return {"NAME": "duckduckgo", "ACTIONS": {"DUCKDUCKGO": {"sig": "DuckDuckGo(keywords:str)->str", "prompt": "Use duckduckgo to search internet content."},
                                                  "SCROLLDOWNDUCKDUCKGO": {"sig": "ScrollDown()->str", "prompt": "Scrolldown the results."}}}
    
    def DuckDuckGo(self, keywords: str) -> str:
        params = {
            'q': keywords,
            'format': 'json',
        }

        try:
            response = requests.get(self.baseURL, params=params)
            ret = str(response.json())
        except requests.RequestException as e:
            print(f"Error during the request: {e}")
            ret = str(e)
        self.page.LoadPage(str(ret), "TOP")
        return self.page()
    
    def ScrollDown(self):
        self.page.ScrollDown()
        return self.page()

duckduckgo = ADuckDuckGo()
makeServer(duckduckgo, "ipc:///tmp/ADuckDuckGo.ipc", ["ModuleInfo", "DuckDuckGo", "ScrollDown"]).Run()