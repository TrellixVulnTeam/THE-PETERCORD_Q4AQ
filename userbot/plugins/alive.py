# Thanks to Sipak bro and Aryan.. 
# animation Idea by @NOOB_GUY_OP (Sipakisking) 
# Made by @diemmmmmmmmmm...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# Porting in PETERCORD Userbot by @diemmmmmmmmmm

import asyncio
import random
from telethon import events
from userbot.utils import admin_cmd
from userbot import ALIVE_NAME, PETERCORDversion
from PETERCORDBOT.utils import admin_cmd, sudo_cmd
from telethon.tl.types import ChannelParticipantsAdmins

# TENTANG AKU DAN DIA
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "𝕄𝔸𝔽𝕀𝔸𝔹𝕆𝕋"

# Thanks to Sipak bro and Raganork.. 
# animation Idea by @diemmmmmmmmmm (Sipakisking)
# Made by @ROMANTIC_KILLER...and thanks to @Crackexy for the logos...
# Kang with credits else gay...
# alive.py for @diemmmmmmmmmm

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

PETERCORD = bot.uid


edit_time = 16
""" =======================CONSTANTS====================== """
file1 = "https://telegra.ph/file/2408a2877646132ac52fd.mp4"
file2 = "https://telegra.ph/file/e97d640332ce5eadb3f89.mp4"
file3 = "https://telegra.ph/file/0b2862d312a2aeb804b36.mp4"
file4 = "https://telegra.ph/file/866c79e351350a08f2b06.mp4"
""" =======================CONSTANTS====================== """
pm_caption = "  __**⚡⚡𝗣𝗘𝗧𝗘𝗥𝗖𝗢𝗥𝗗 𝐁𝐎𝐓 𝐈𝐒 𝐀𝐋𝐈𝐕𝐄⚡⚡**__\n\n"

pm_caption += f"**━━━━━━━━━━━━━━━━━━━━**\n\n"
pm_caption += (
    f"                 ⚡𝗣𝗘𝗡𝗚𝗚𝗨𝗡𝗔⚡\n  **👾[{DEFAULTUSER}](tg://user?id={PETERCORD})👾**\n\n"
)
pm_caption += f"┏━━━━━━━━━━━━━━━━━━━\n"
pm_caption += f"┣•➳➠ `𝗧𝗘𝗟𝗘𝗧𝗛𝗢𝗡:` `{version.__version__}` \n"
pm_caption += f"┣•➳➠ `𝗩𝗘𝗥𝗦𝗜𝗢𝗡:` `{PETERCORDversion}`\n"
pm_caption += f"┣•➳➠ `𝗦𝗨𝗗𝗢:` `{sudou}`\n"
pm_caption += f"┣•➳➠ `𝗖𝗛𝗔𝗡𝗡𝗘𝗟:` [𝙿𝙴𝚃𝙴𝚁𝙲𝙾𝚁𝙳](https://t.me/TEAMSquadUserbotSupport)\n"
pm_caption += f"┣•➳➠ `𝗖𝗥𝗘𝗔𝗧𝗢𝗥:` [Ilham Mansiez](https://t.me/diemmmmmmmmmm)\n"
pm_caption += f"┣•➳➠ `𝗦𝗨𝗣𝗣𝗢𝗥𝗧:` [PETERCORD](https://t.me/TEAMSquadUserbotSupport)\n"
pm_caption += f"┗━━━━━━━━━━━━━━━━━━━\n"
pm_caption += " [⚡REPO⚡](https://github.com/IlhamMansiez/PETERCORDBOT) 🔸 [📜License📜](https://github.com/IlhamMansiez/PETERCORDBOT/blob/main/LICENSE)"

# @command(outgoing=True, pattern="^.alive$")
@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()   
    
    on = await borg.send_file(alive.chat_id, file=file1,caption=pm_caption)

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(alive.chat_id, on, file=file2) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(alive.chat_id, ok, file=file1)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(alive.chat_id, ok2, file=file2)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(alive.chat_id, ok3, file=file3)
    
    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(alive.chat_id, ok4, file=file2)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(alive.chat_id, ok5, file=file1)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(alive.chat_id, ok6, file=file3)

    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, caption=pm_caption)
    await alive.delete()
    
    
