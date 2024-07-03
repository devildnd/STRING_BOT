from os import getenv
from dotenv import load_dotenv

load_dotenv()

#❖________①_______❖_______#
API_ID = int(getenv("API_ID", 18688563))

#❖________②_______❖_______#
API_HASH = getenv("API_HASH", 48315c25585c23eee6b1f346aad17a68)

#❖________③_______❖_______#
BOT_TOKEN = getenv("BOT_TOKEN", 5935941442:AAEIZGT8QgfVBY35eX4znwSag0uN9sniskk)

#❖________④_______❖_______#
OWNER_ID = int(getenv("OWNER_ID", 5562877717))

#❖________⑤_______❖_______#
MONGO_DB_URI = getenv("MONGO_DB_URI", mongodb+srv://lnkgeevr:lnkgeevr@cluster0.bp33u5p.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)

#❖________⑥_______❖_______#
MUST_JOIN = getenv("MUST_JOIN", rockstar_remix)
