import os
from config import Config

class Translation(object):
  START_TXT = """<b>Hᴇʏ {},{}</b>

◈ I Aᴍ Aɴ Aᴅᴠᴀɴᴄᴇᴅ Aᴜᴛᴏ Fᴏʀᴡᴀʀᴅ Bᴏᴛ.
◈ I Cᴀɴ Fᴏʀᴡᴀʀᴅ Aʟʟ Mᴇꜱꜱᴀɢᴇꜱ Fʀᴏᴍ Oɴᴇ Cʜᴀɴɴᴇʟ Tᴏ Aɴᴏᴛʜᴇʀ Cʜᴀɴɴᴇʟ.
◈ Cʟɪᴄᴋ Hᴇʟᴘ Bᴜᴛᴛᴏɴ Tᴏ Kɴᴏᴡ Mᴏʀᴇ Aʙᴏᴜᴛ Mᴇ.

<blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ: <a href='https://t.me/Filmdom_Updates'>𝐅𝐈𝐋𝐌𝐃𝐎𝐌</a></blockquote></b>"""


  HELP_TXT = """<b><u>🛠️ HELP</b></u>

<u>**📚 Available commands:**</u>
<b>⏣ __/start - Check if I'm alive__ 
⏣ __/forward - Forward messages__
⏣ __/unequify - Delete duplicate messages in channels__
⏣ __/settings - Configure your settings__
⏣ __/reset - Reset your settings__</b>

<b><u>💢 Features:</b></u>
<b>► __Forward message from public channel to your channel without admin permission. Ff the channel is private, admin permission is needed__
► __Forward message from private channel to your channel by using userbot(user must be member in there)__
► __Custom Caption__
► __Custom Button__
► __Supports Restricted Chats__
► __Skips Duplicate Messages__
► __Filters type of messages__
► __Skips messages based on extensions, keywords & size__</b>
"""
  
  HOW_USE_TXT = """<b><u>⚠️ Before Forwarding:</b></u>
  
<b>► __Add A Bot Or Userbot__
► __Add Atleast One To Channel (Your Bot/Userbot Must Be Admin In There)
► __You Can Add Chats Or Bots By Using /settings__
► __if the **From Channel** is private your userbot must be member in there or your bot must need admin permission in there__
► __Then use /forward to forward messages__</b>"""
  
  ABOUT_TXT = """<b>
╭───────────⍟
├◈ ᴍy ɴᴀᴍᴇ : <a href=https://t.me/FilmdomForwardBot>Auto Forward Bot</a>
├◈ Dᴇᴠᴇʟᴏᴩᴇʀꜱ : <a href=https://t.me/EccentricExplorerBot>Eccentric Explorer</a> 
├◈ Uᴘᴅᴀᴛᴇs Cʜᴀɴɴᴇʟ: <a href=https://t.me/Filmdom_Updates>𝐅𝐈𝐋𝐌𝐃𝐎𝐌</a>   
├◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>
├◈ Lᴀɴɢᴜᴀɢᴇ: <a href=https://www.python.org/>Pʏᴛʜᴏɴ𝟹</a>
├◈ Dᴀᴛᴀ Bᴀꜱᴇ: <a href=https://cloud.mongodb.com/>MᴏɴɢᴏDB</a>
├◈ Bot Vᴇʀꜱɪᴏɴ: <a href=https://t.me/Filmdom_Bot>V-2.4.1
╰───────────────⍟</b>"""
  
  STATUS_TXT = """<b><u>Bot Status</u>

👨 ᴜsᴇʀs  : {}

🤖 ʙᴏᴛs : {}

📣 ᴄʜᴀɴɴᴇʟ  : {} 
</b>""" 
  
  FROM_MSG = "<b>❪ SET SOURCE CHAT ❫\n\nForward the last message or last message link of source chat.\n/cancel - Cancel this process</b>"
  TO_MSG = "<b>❪ CHOOSE TARGET CHAT ❫\n\nChoose your target chat from the given buttons.\n/cancel - Cancel this process</b>"
  SKIP_MSG = "<b>❪ SET MESSAGE SKIPPING NUMBER ❫</b>\n\n<b>Skip messages, as many as you enter the number, and the rest of the messages will be forwarded\nDefault Skip Number =</b> <code>0</code>\n<code>eg: You enter 0 = 0 message skipped\n You enter 5 = 5 messages skipped</code>\n/cancel <b>- Cancel this process</b>"
  CANCEL = "<b>Process Cancelled Succefully !</b>"
  BOT_DETAILS = "<b><u>📄 BOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ BOT ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"
  USER_DETAILS = "<b><u>📄 USERBOT DETAILS</b></u>\n\n<b>➣ NAME:</b> <code>{}</code>\n<b>➣ USER ID:</b> <code>{}</code>\n<b>➣ USERNAME:</b> @{}"  
         
  TEXT = """<b>╭────❰ <u>Forwarded Status</u> ❱────❍
┃
┣⊸<b>🕵 ғᴇᴛᴄʜᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :</b> <code>{}</code>
┣⊸<b>👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :</b> <code>{}</code>
┣⊸<b>📊 sᴛᴀᴛᴜs  :</b> <code>{}</code>
┣⊸<b>⏳ ᴘʀᴏɢʀᴇss  :</b> <code>{}</code> %
┣⊸<b>⏰ ᴇᴛᴀ :</b> <code>{}</code>
┃
╰────⌊ <b>{}</b> ⌉───❍</b>"""

  TEXT1 = """
╔════❰ ғᴏʀᴡᴀʀᴅ sᴛᴀᴛᴜs ❱➠
║╭━━━━━━━━━━━━━━━➣
║┃
║┣⪼**🕵 ғᴇᴛᴄʜᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**✅ sᴜᴄᴄᴇғᴜʟʟʏ ғᴡᴅ :** `{}`
║┃
║┣⪼**👥 ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴍsɢ :** `{}`
║┃
║┣⪼**🗑️ ᴅᴇʟᴇᴛᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**🪆 sᴋɪᴘᴘᴇᴅ ᴍsɢ :** `{}`
║┃
║┣⪼**📊 sᴛᴀᴛᴜs  :** `{}`
║┃
║┣⪼**⏳ ᴘʀᴏɢʀᴇss :** `{}`
║┃
║┣⪼**⏰ ᴇᴛᴀ :** `{}`
║┃
║╰━━━━━━━━━━━━━━━➣ 
╚════❰ **{}** ❱➠ """

  DUPLICATE_TEXT = """
╔════❰ ᴜɴᴇǫᴜɪғʏ sᴛᴀᴛᴜs ❱
║╭━━━━━━━━━━━━━━━➣
║┣⪼ <b>ғᴇᴛᴄʜᴇᴅ ғɪʟᴇs:</b> <code>{}</code>
║┃
║┣⪼ <b>ᴅᴜᴘʟɪᴄᴀᴛᴇ ᴅᴇʟᴇᴛᴇᴅ:</b> <code>{}</code> 
║╰━━━━━━━━━━━━━━━➣
╚════❰ ❱
"""
  DOUBLE_CHECK = """<b><u>DOUBLE CHECKING ⚠️</b></u>
<code>Before forwarding the messages Click the Yes button only after checking the following</code>

<b>★ YOUR BOT:</b> [{botname}](t.me/{botuname})
<b>★ FROM CHANNEL:</b> `{from_chat}`
<b>★ TO CHANNEL:</b> `{to_chat}`
<b>★ SKIP MESSAGES:</b> `{skip}`

<i>° [{botname}](t.me/{botuname}) must be admin in **TARGET CHAT**</i> (`{to_chat}`)
<i>° If the **SOURCE CHAT** is private your userbot must be member or your bot must be admin in there</b></i>

<b>If the above is checked then the yes button can be clicked</b>"""
