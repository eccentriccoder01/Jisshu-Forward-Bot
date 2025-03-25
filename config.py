from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28264988")
    API_HASH = environ.get("API_HASH", "2eea24560203cd8b2320f075874395e5")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8044956949:AAH8shedzLH-N5AP_D0OdxQKhrpHFGscMSE") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6713601081').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://i.pinimg.com/1200x/b1/23/10/b12310195a44c3ccee8d6b9a4a914a07.jpg'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://sagnikgraviton847:AutoForward@autoforward.iwsux.mongodb.net/?retryWrites=true&w=majority&appName=AutoForward")
    DATABASE_NAME = environ.get("DATABASE_NAME", "AutoForward")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '2493411028'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/filmdom_updates") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
