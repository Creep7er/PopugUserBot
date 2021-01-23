import utils
import traceback
import sys
import meval
import __main__ as bot


async def ev(message):
    """evaluate python expression(s)"""
    try:
        ret = str(await meval.meval(utils.raw(message.message), globals(), **{"message": message, "client": bot.client, "reply": await message.get_reply_message(), "db": bot.db}))
        await message.edit(f"**Evaluated expression:**\n`{utils.raw(message.message)}`\n**Result:**\n`{ret}`")
    except:
        exc = sys.exc_info()
        exc = "".join(traceback.format_exception(exc[0], exc[1], exc[2].tb_next.tb_next.tb_next))
        await message.edit(f"__Expression__:\n`{utils.raw(message.message)}`\n**rose error**:\n`{exc}`")