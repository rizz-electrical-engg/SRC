# devgaganin
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "21857983"))
API_HASH = getenv("API_HASH", "e469e84c943ce3b8b056eb6a296f2c67")
BOT_TOKEN = getenv("BOT_TOKEN", "7486614085:AAHTzaa8KK3bJjI6dBGJQjpwPZwtaSKu8v4")
OWNER_ID = int(getenv("OWNER_ID", "833465134"))
MONGODB_CONNECTION_STRING = getenv("MONGO_DB", "mongodb+srv://dhimanrajat:Y8IAGI0lVrMhjvkU@cluster0.mytkgu6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = int(getenv("LOG_GROUP", "-1002164681451"))
FORCESUB = getenv("FORCESUB", "-1002482084911")
DEFAULT_SESSION = getenv("DEFAULT_SESSION", "") # this is jkust to help if you dont want to force your bot user to login or if they not interested
