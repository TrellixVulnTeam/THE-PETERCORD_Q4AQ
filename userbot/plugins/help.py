import logging


from userbot.Config import Config
from userbot.events import register

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s",
    level=logging.WARNING)


@register(outgoing=True, pattern=r"^\.petercordbothelp")
async def yardim(event):
    try:
            return
    tgbotusername = TG_BOT_TOKEN_BF_HER
        if tgbotusername is not None:
            results = await event.client.inline_query(tgbotusername, "@TEAMSquadUserbotSupport")
            await results[0].click(
                event.chat_id, reply_to=event.reply_to_msg_id, hide_via=True
            )
            await event.delete()
        else:
            await event.edit(
                "`Bot tidak berfungsi! Harap setel Token Bot dan Nama Pengguna dengan benar. Modul telah dihentikan.`"
            )
    except Exception:
        return await event.edit(
            "`Anda tidak dapat mengirim hasil sebaris dalam obrolan ini (disebabkan oleh SendInlineBotResultRequest)`"
        )
