import os

class Config(object):
    API_ID = int(os.environ.get("API_ID", "21013168"))
    API_HASH = os.environ.get("API_HASH", "8ce3522bd21cc937eee4c68813d501d5")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", 6607142340:AAHrS-Nn4B2Oy_OkQ240lsHwrNxYTReNoF8)
    STRING_SESSION = os.environ.get("STRING_SESSION", 1BVtsOL4BuwRthWvMMSsvXnOceAZ0wbVCEeviqmx64yU6xm0B8QyDtCZw6juPZs12G3wwOBAb1jwOJ28wtgDxABDmIn8GWthvPru-L0DiVzVwKTuHVUXcm2riKUZ71xJT4WRcQxDgkxWxD3hxcT7kKg5PS3WKKrEd4doNY2K1pn3vs7ERqTSXnrWOy24I4A2vVutHOn-rBlxzRMgidCkgCcRqSNkASRHPL5GpkmCBYcyCiJbzxi-obJXDEoDTlXyfddu_z1G38o8yyv91l_6CJeIF8p3SetaHrshqntlIRE0T_2rdR3PnCRPRS_UX_Lomi-5twoCTtEeDjP8GJtOX_ueP0hh25oc=)
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
