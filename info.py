import re
from os import environ
import asyncio
import json
from collections import defaultdict
from typing import Dict, List, Union
from pyrogram import Client
from time import time

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if str(value).strip().lower() in ["on", "true", "yes", "1", "enable", "y"]:
        return True
    elif str(value).strip().lower() in ["off", "false", "no", "0", "disable", "n"]:
        return False
    else:
        return default


# Bot information
PORT = environ.get("PORT", "8080")
WEBHOOK = is_enabled(environ.get("WEBHOOK", "True"), True) # Consistent boolean handling
SESSION = environ.get('SESSION', 'Media_search')

# If you want to set API_ID manually in the code:
API_ID = 18019745  # Replace with your actual API ID
# Otherwise, to fetch from environment with a default:
# API_ID = int(environ.get('API_ID', '1234567'))

API_HASH = environ.get('API_HASH', '59f97cf6abf6201b862551f66eae0762') # Provide a default if not always env var
BOT_TOKEN = environ.get('BOT_TOKEN', '6176065465:AAF3Bvumshvfjllw8m9PhpCDavFldl5zFzg') # Provide a default if not always env var

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = is_enabled(environ.get('USE_CAPTION_FILTER', "True"), True)
# If you want to set PICS manually:
PICS = ["https://example.com/pic1.jpg", "https://example.com/pic2.png"]
# Otherwise, to fetch from environment:
# PICS = (environ.get('PICS' ,'https://graph.org/file/01ddfcb1e8203879a63d7.jpg https://graph.org/file/d69995d9846fd4ad632b8.jpg ...')).split()
BOT_START_TIME = time()

# Admins, Channels & Users
# To manually add admins directly in the code (in addition to or instead of environment variables):
MANUAL_ADMINS = [12345, 67890]
ADMINS_ENV = [int(admin) if id_pattern.search(admin) else admin for admin in environ.get('ADMINS', '').split()]
ADMINS = list(set(MANUAL_ADMINS + ADMINS_ENV))

# To manually add channels:
MANUAL_CHANNELS = [-1001234567890, -1000987654321]
CHANNELS_ENV = [int(ch) if id_pattern.search(ch) else ch for ch in environ.get('CHANNELS', '0').split()]
CHANNELS = list(set(MANUAL_CHANNELS + CHANNELS_ENV))

# To manually add authorized users:
MANUAL_AUTH_USERS = [112233, 445566]
auth_users_env = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]
auth_users = list(set(MANUAL_AUTH_USERS + auth_users_env))
AUTH_USERS = (auth_users + [admin for admin in ADMINS if isinstance(admin, int)]) if auth_users else [admin for admin in ADMINS if isinstance(admin, int)]
auth_channel = environ.get('AUTH_CHANNEL')
auth_grp = environ.get('AUTH_GROUP')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None

# To manually add authorized groups:
MANUAL_AUTH_GROUPS = [-100111222333, -100444555666]
AUTH_GROUPS_ENV = [int(ch) for ch in environ.get('AUTH_GROUP', '').split()] if environ.get('AUTH_GROUP') else []
AUTH_GROUPS = list(set(MANUAL_AUTH_GROUPS + AUTH_GROUPS_ENV)) if MANUAL_AUTH_GROUPS or AUTH_GROUPS_ENV else None

# MongoDB information
DATABASE_URI = environ.get('DATABASE_URI', "")
DATABASE_NAME = environ.get('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

#maximum search result buttos count in number#
MAX_RIST_BTNS = int(environ.get('MAX_RIST_BTNS', "10")) # You can directly assign an integer here if needed
START_MESSAGE = environ.get('START_MESSAGE', '👋 𝙷𝙴𝙻𝙾 {user}\n\n𝙼𝚈 𝙽𝙰𝙼𝙴 𝙸𝚂 {bot},\n𝙸 𝙲𝙰𝙽 𝙿𝚁𝙾𝚅𝙸𝙳𝙴 𝙼𝙾𝚅𝙸𝙴𝚂, 𝙹𝚄𝚂𝚃 𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿 𝙰𝙽𝙳 𝙼𝙰𝙺𝙴 𝙼𝙴 𝙰𝙳𝙼𝙸𝙽...')
BUTTON_LOCK_TEXT = environ.get("BUTTON_LOCK_TEXT", "⚠️ 𝙃𝙚𝙮 {query}! 𝙏𝙝𝙖𝙩'𝙨 𝙉𝙤𝙩 𝙁𝙤𝙧 𝙔𝙤𝙪. 𝙋𝙡𝙚𝙖𝙨𝙚 𝙍𝙚𝙦𝙪𝙚𝙨𝙩 𝙔𝙤𝙪𝙧 𝙊𝙬𝙣")
FORCE_SUB_TEXT = environ.get('FORCE_SUB_TEXT', '𝑱𝒐𝒊𝒏 𝑶𝒖𝒓 𝑴𝒐𝒗𝒊𝒆 𝑼𝒑𝒅𝒂𝒕𝒆𝒔 𝑪𝒉𝒂𝒏𝒏𝒆𝒍 𝑻𝒐 𝑼𝒔𝒆 𝑻𝒉𝒊𝒔 𝑩𝒐𝒕!')
RemoveBG_API = environ.get("RemoveBG_API", "")
WELCOM_PIC = environ.get("WELCOM_PIC", "")
WELCOM_TEXT = environ.get("WELCOM_TEXT", "Hai {user}\nwelcome to {chat}")
PMFILTER = environ.get('PMFILTER', "True")
G_FILTER = is_enabled(environ.get("G_FILTER", "True"), True)
BUTTON_LOCK = is_enabled(environ.get("BUTTON_LOCK", "True"), True)

# url shortner
SHORT_URL = environ.get("SHORT_URL")
SHORT_API = environ.get("SHORT_API")

# Others
IMDB_DELET_TIME = int(environ.get('IMDB_DELET_TIME', "300"))
LOG_CHANNEL = int(environ.get('LOG_CHANNEL', 0)) # You can directly assign an integer here
SUPPORT_CHAT = environ.get('SUPPORT_CHAT', 'mkn_bots_updates')
P_TTI_SHOW_OFF = is_enabled((environ.get('P_TTI_SHOW_OFF', "True")), True)
PM_IMDB = is_enabled(environ.get('PM_IMDB', "True"), True)
IMDB = is_enabled((environ.get('IMDB', "True")), True)
SINGLE_BUTTON = is_enabled((environ.get('SINGLE_BUTTON', "True")), True)
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", "{file_name}")
BATCH_FILE_CAPTION = environ.get("BATCH_FILE_CAPTION", None)
IMDB_TEMPLATE = environ.get("IMDB_TEMPLATE", "<b>Query: {query}</b> \n‌IMDb Data:\n\n🏷 Title: <a href={url}>{title}</a>\n🎭 Genres: {genres}\n📆 Year: <a href={url}/releaseinfo>{year}</a>\n🌟 Rating: <a href={url}/ratings>{rating}</a> / 10")
LONG_IMDB_DESCRIPTION = is_enabled(environ.get("LONG_IMDB_DESCRIPTION", "False"), False)
SPELL_CHECK_REPLY = is_enabled(environ.get("SPELL_CHECK_REPLY", "True"), True)
MAX_LIST_ELM = environ.get("MAX_LIST_ELM", None)
INDEX_REQ_CHANNEL = int(environ.get('INDEX_REQ_CHANNEL', LOG_CHANNEL)) # You can directly assign an integer here
# To manually add file store channels:
MANUAL_FILE_STORE_CHANNEL = [-100999888777, -100666555444]
FILE_STORE_CHANNEL_ENV = [int(ch) for ch in (environ.get('FILE_STORE_CHANNEL', '')).split()]
FILE_STORE_CHANNEL = list(set(MANUAL_FILE_STORE_CHANNEL + FILE_STORE_CHANNEL_ENV))

MELCOW_NEW_USERS = is_enabled((environ.get('MELCOW_NEW_USERS', "True")), True)
PROTECT_CONTENT = is_enabled((environ.get('PROTECT_CONTENT', "False")), False)
PUBLIC_FILE_STORE = is_enabled((environ.get('PUBLIC_FILE_STORE', "True")), True)

#request force sub
REQ_SUB = bool(environ.get("REQ_SUB", "True")) # Corrected to string for is_enabled if needed
SESSION_STRING = environ.get("SESSION_STRING", "")
