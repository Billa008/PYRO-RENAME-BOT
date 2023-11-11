"""
Apache License 2.0
Copyright (c) 2022 @PYRO_BOTZ
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Telegram Link : https://t.me/PYRO_BOTZ 
Repo Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT
License Link : https://github.com/TEAM-PYRO-BOTZ/PYRO-RENAME-BOT/blob/main/LICENSE
"""

import re, os, time

id_pattern = re.compile(r'^.\d+$') 

class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "")
    API_HASH  = os.environ.get("API_HASH", "")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "") 
   
    # database config
    DB_NAME = os.environ.get("DB_NAME","pyro-botz")     
    DB_URL  = os.environ.get("DB_URL","")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "")
    ADMIN       = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]
    FORCE_SUB   = os.environ.get("FORCE_SUB", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", None))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))



class Txt(object):
    # part of text configuration
    START_TXT = """<b>👋 Hᴀɪ {} ,
I'ᴍ A Sɪᴍᴘʟᴇ 𝟸GB Fɪʟᴇ  Rᴇɴᴀᴍᴇ+Fɪʟᴇ Tᴏ Vɪᴅᴇᴏ Cᴏɴᴠᴇɴᴛᴏʀ Bᴏᴛ Wɪᴛʜ Tʜᴜᴍʙɴᴀɪʟ & Cᴜsᴛᴏᴍ Cᴀᴘᴛɪᴏɴ Sᴜᴘᴘᴏʀᴛ 🚀
Tʜɪs Bᴏᴛ Wᴀs Cʀᴇᴀᴛᴇᴅ Bʏ : @Doremon_Botz 🛠</b>"""

    ABOUT_TXT = """<b>╭───────────⍟
├✯ Mʏ Nᴀᴍᴇ : {}
✯ Cʀᴇᴀᴛᴏʀ : <a href=https://t.me/Praxxsh>A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ</a>
✯ Dᴀᴛᴀ Bᴀsᴇ : Mᴏɴɢᴏ-ᴅʙ
✯ Bᴏᴛ Sᴇʀᴠᴇʀ : Aɴʏᴡʜᴇʀᴇ
✯ Bᴜɪʟᴅ Vᴇʀsɪᴏɴ : Billa Rᴇɴᴀᴍᴇʀ V3.0.0</a></b>     
╰───────────────⍟ """

    THUMBNAIL_TXT = """
🌌 <b><u>Hᴏᴡ Tᴏ Sᴇᴛ Tʜᴜᴍʙɴɪʟᴇ</u></b>
  
•> /start a bot and send any picture to automatically set thumbnile.
•> /delthumb use this command and delete your old thumbnile.
•> /viewthumb use this command view your current thumbnile."""

     CUSTOM_TXT ="""
•> /set_caption - set a custom caption
•> /see_caption - see your custom caption
•> /del_caption - delete custom caption."""

     HELP_TXT ="""

<code>{prefix}</code>  = new name with your prefix
<code>{filename}</code>  = new name  
<code>{filesize}</code>  = original file size (⚠️ ± 10% not accurate)
<code>{duration}</code>  = original file duration time 

✏️ HOW TO RENAME A FILE
•> send any file and click rename option and type new file name and 
 send select [ document, video, audio ]👈 choice this.
<b>•></b> Sᴇɴᴅ Aɴy Fɪʟᴇ Aɴᴅ Tyᴩᴇ Nᴇᴡ Fɪʟᴇ Nɴᴀᴍᴇ \nAɴᴅ Aᴇʟᴇᴄᴛ Tʜᴇ Fᴏʀᴍᴀᴛ [ document, video, audio ].           
ℹ️ 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/+5xScmjemXiI4Yjll>Doremon - Botz🛠</a>
"""

#⚠️ Dᴏɴ'ᴛ Rᴇᴍᴏᴠᴇ Oᴜʀ Cʀᴇᴅɪᴛꜱ @ᴩyʀᴏ_ʙᴏᴛᴢ🙏🥲
    DEV_TXT = """<b><u>Sᴏʀʀʏ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ Oғ Tʜɪs Bᴏᴛ ɪs Pʀɪᴠᴀᴛᴇ</b></u>
» 𝗔𝗻𝘆 𝗢𝘁𝗵𝗲𝗿 𝗛𝗲𝗹𝗽 𝗖𝗼𝗻𝘁𝗮𝗰𝘁 :- <a href=https://t.me/Praxxsh>A ᴅ ᴏ ʟ ғ 🔰 R ᴀ ᴍ</a>"""

    PROGRESS_BAR = """<b>\n
╭━━━━❰ᴘʀᴏɢʀᴇss ʙᴀʀ❱━➣
┣•> 🗃️ Sɪᴢᴇ: {1} | {2}
┣⪼ ⏳️ Dᴏɴᴇ : {0}%
┣•> 🚀 Sᴩᴇᴇᴅ: {3}/s
┣⪼ ⏰️ Eᴛᴀ: {4}
╰━━━━━━━━━━━━━━━➣ </b>"""


