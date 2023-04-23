import os
from dotenv import load_dotenv
load_dotenv()

TG_BOT = os.getenv('TG_BOT_TOKEN')
TG_USER= int(os.getenv('TG_API_ID'))
TG_USER_HASH= os.getenv('TG_API_HASH')
