import __main__
import python
import utils
import text
import terminal
# import notes
import arts
import fl

modules = {
    "terminal": {"terminal": terminal.terminal},
    "text": {
        "sarcasm": text.sarcasm,
        "shout": text.shout,
        "rev": text.reverse,
        "shuffle": text.shuffle,
    },
    "fl": {"fl": fl.fakeload},
    "arts": {
        "bruh": arts.bruh,
        "coffee": arts.coffee,
        "cowsay": arts.cowsay,
        "fuckyou": arts.fuckyou,
        "gren": arts.gren,
        "hello": arts.hello,
        "house": arts.house,
        "imps": arts.imps,
        "lol": arts.lol,
        "padayu": arts.padayu,
        "priletel": arts.priletel,
        "tv": arts.tv,
        "vjuh": arts.vjuh,
        "uno": arts.uno,
        "yoda": arts.yoda,
    },
    "python": {"eval": python.ev},
    # "notes:": {
    #     "save": notes.save,
    #     "note": notes.note,
    #     "delnote": notes.delnote,
    #     "allnotes": notes.all,
    #     "execnote": notes.ex,
    # }
}


async def stop(message):
    """Exit the bot"""
    await message.edit("**Bye!**")
    exit(0)


async def help(message):
    """Get help for PUB"""
    text = "**Help fo PopugUserBot:**\n"
    for cm in __main__.commands.keys():
        func = __main__.commands[cm].__doc__
        text += f"`.{cm}` - __{func}__\n"
    await message.edit(text)


async def _activate_from_db():
    d = __main__.db
    if not await d.keys("Modules"):
        return
    for mod in await d.keys("Modules"):
        if await d.get("Modules", mod) is True:
            __main__.commands.update(modules[mod])


async def activate(event):
    mod = utils.raw(event.message)
    if not mod:
        await event.edit("__Provide a module to activate!__")
        return
    try:
        __main__.commands.update(modules[mod])
        await __main__.db.set("Modules", mod, True)
        await event.edit("**Module activated! Try using `.help`**")
    except KeyError:
        text = "**No such module. Available modules:**\n"
        for i in modules.keys():
            text += f"`{i}`\n"
        await event.edit(text)


async def deactivate(event):
    mod = utils.raw(event.message)
    if not mod:
        await event.edit("__Provide a module to deactivate!__")
        return
    try:
        md = modules[mod]
        for i in md:
            __main__.commands.pop(i)
        await __main__.db.set("Modules", mod, False)
        await event.edit("**Module deactivated!**")
    except KeyError:
        await event.edit("__No such module__")


async def ping(message):
    """Test the bot"""
    await message.edit("**Pong!**")


async def titles(message):
    """Bot developer"""
    bot_developers = ("**Автор - `@Creep7r`\n"
                      "Проект приготовлен по телеграм-канала @Popugasha_Arkasha**")
    await message.edit(bot_developers)


async def sovet(message):
    """Лучший совет в твоей жизни"""
    await message.edit("**Подпишись на @Popugasha_Arkasha!**")
