import os
import json
from termcolor import colored

class AConfig():
    def __init__(self):
        self.maxMemory = {}
        self.quantization = None
        self.openaiGPTKey = None
        self.temperature = 0.0
        self.flashAttention2 = False
        self.speechOn = False
        self.localExecution = False
        self.contextWindowRatio = 0.6
        return

    def Initialize(self, needOpenaiGPTKey = False):
        oldDict = self.Load("config.json")
        needUpdate = (set(oldDict.keys()) != set(self.__dict__))
        self.__dict__ = {k: oldDict[k] if k in oldDict else v for k,v in self.__dict__.items()}
        
        needUpdate = needUpdate or (needOpenaiGPTKey and (self.openaiGPTKey is None))
        
        if needUpdate:
            print("config.json need to be updated.")
            print(colored("********************** Initialize *****************************", "yellow"))
            if self.openaiGPTKey is None:
                key = input(colored("Your openai chatgpt key (press Enter if not): ", "green"))
                self.openaiGPTKey = key if 1 < len(key) else None
            self.Store("config.json")
            print(colored("********************** End of Initialization *****************************", "yellow"))
        return

    def Load(self, configFile: str = "config.json") -> dict:
        if os.path.exists(configFile):
            with open(configFile, "r") as f:
                return json.load(f)
        else:
            return dict()
    
    def Store(self, configFile: str = "config.json"):
        with open(configFile, "w") as f:
            json.dump(self.__dict__, f)
        return
    
    
config = AConfig()