import vk_api
import random

class Knocker:
    def __init__(self):
        self.bot = vk_api.VkApi(token=open("./token", "r").readline())
        self.bot._auth_token()
        
    def SendMsg(self, messageText : str, peerId):
        self.bot.method("messages.send",{"peer_id": 160500068, "random_id" : random.randint(1, 1000),"message": messageText})
