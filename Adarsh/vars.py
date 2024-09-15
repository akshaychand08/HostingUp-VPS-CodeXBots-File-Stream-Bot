# @AmRobots_Bots www.hostingup.in
import os
from os import getenv, environ
from dotenv import load_dotenv



load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(getenv('API_ID', '22301351'))
    API_HASH = str(getenv('API_HASH', '3035f2bbd92a9c5174d174d92b52b25b'))
    PICS = (environ.get('PICS','https://graph.org/file/d2c20ed467fd8a101409f.jpg')).split()
    BOT_TOKEN = str(getenv('BOT_TOKEN', '6391607401:AAEO7NGOJxJvNArDoXwmWViyEtLY6LwdLxw'))
    name = str(getenv('name', 'ShrdiskBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '-1002222888781'))
    PORT = int(getenv('PORT', '9003')) #(Here, enter the hosting port you received from HostingUp, which should start From 9000)
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')) #(DO NOT CHANGE IF U DEPLOY YOUR BOT ON HOSTINGUP VPS)
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "5721673207").split())  
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME', 'AkshayChand08'))
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME'))
    
    else:
        ON_HEROKU = False
    FQDN = str(getenv('FQDN', BIND_ADRESS)) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL', False))
    HAS_SSL = False
    FQDN = 'bots.hostingup.icu:9003' #(Here, enter the domain and hosting port you received from HostingUp. If you're using your own, enter that, but make sure to use the domain name, not the IP address, and include the port as well.)
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL', 'mongodb+srv://akshaychand:akshaychand@cluster0.3gwaqm0.mongodb.net/?retryWrites=true&w=majority'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', 'A_K_Update'))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split())
