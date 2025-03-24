# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "23294809")
    API_HASH = environ.get("API_HASH", "fbe5152195458e6aa8ec4298c96fb274")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7545122233:AAGlDCqGFJJRL75T8UYXERUQlMwzAgkBb3A") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '1226915127').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://graph.org/file/e223aea8aca83e99162bb.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://sagnikgraviton847:AutoForward@autoforward.iwsux.mongodb.net/?retryWrites=true&w=majority&appName=AutoForward")
    DATABASE_NAME = environ.get("DATABASE_NAME", "AutoForward")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', ''))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
