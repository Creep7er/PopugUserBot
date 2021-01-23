import random
import utils


async def sarcasm(message):
    """gEt a LiTtLe WeIrD"""
    text = list(utils.raw(message.message))
    if not text:
        text = list(utils.raw((await message.get_reply_message()).message))
    text[1::2], text[::2] = map(str.lower, text[1::2]), map(str.upper, text[::2])
    await message.edit("".join(text))


async def shout(message):
    """SHOUT!"""
    await message.edit(utils.raw(message.message).upper())


async def shuffle(message):
    """hsulfses tufsf"""
    a = list(utils.raw(message.message))
    if not a:
        a = list((await message.get_reply_message()).message)
    random.shuffle(a)
    await message.edit("".join(a))


async def reverse(message):
    """Reverses ffuts"""
    if not utils.raw(message.message):
        await message.edit((await message.get_reply_message()).message[::-1])
    await message.edit(utils.raw(message.message)[::-1])


async def arange(count):
    for i in range(count):
        yield(i)