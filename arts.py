import __main__
import utils
import logging
import random
from random import randint, choice


async def vjuh(message):
    """Вжух!"""
    text = utils.raw(message.message)
    if not text:
        await message.edit('Нет текста после команды :c')
        return
    else:
        vjuh = ("`.∧＿∧\n"
                "( ･ω･｡)つ━☆・*。\n"
                "⊂  ノ    ・゜ .\n"
                "しーＪ   °。  *´¨)\n"
                "             .· ´¸.·*´¨) ¸.·*¨)\n"
                "                     (¸.·´ (¸.·'* ☆\n\n"
                "Вжух и ты `" + f"`{text}`")
        await message.edit(vjuh)

    if text == "podpiska":
        await message.edit("<`.∧＿∧\n"
                           "( ･ω･｡)つ━☆・*。\n"
                           "⊂  ノ    ・゜ .\n"
                           "しーＪ   °。  *´¨)\n"
                           "             .· ´¸.·*´¨) ¸.·*¨)\n"
                           "                     (¸.·´ (¸.·'* ☆\n\n"
                           "Вжух и ты подпишешься ->` @Popugasha_Arkasha")


async def cowsay(message):
    """Корова говорит"""
    text = utils.raw(message.message)
    if not text:
        await message.edit('Нет текста после команды :c')
        return
    else:
        cowsay = ("`"
                  f"< {text} >\n"
                  "\n"
                  "     \   ^__^\n"
                  "	     \  (oo)\_______\n"
                  "         (__)\       )\/\n"
                  "             ||----w||\n"
                  "	            ||     ||`")
        await message.edit(cowsay)


async def padayu(message):
    """Падаем!"""
    text = ("ПАДАЮ")
    paday = ("┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             f"┛┗┛┗┛┃ {text}!\n"
             "┓┏┓┏┓┃ ＼○／\n"
             "┛┗┛┗┛┃ /\n"
             "┓┏┓┏┓┃ノ)\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n"
             "┓┏┓┏┓┃\n"
             "┛┗┛┗┛┃\n")
    await message.edit(paday)


async def priletel(message):
    """Вертолёт прилетел..."""
    text = ("ТЫ ЗАБАНЕН")
    prilitel = ("▬▬▬.◙.▬▬▬\n"
                "  ═▂▄▄▓▄▄▂\n"
                "◢◤ █▀▀████▄▄▄▄◢◤\n"
                "█▄ █ █▄ ███▀▀▀▀▀▀▀╬\n"
                "◥█████◤ прилетел сказать что-то важное...\n"
                "══╩══╩═\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                "╬═╬\n"
                f"╬═╬☻/ - {text}\n"
                "╬═╬/▌\n"
                "╬═╬/ \ ")
    await message.edit(prilitel)


async def lol(message):
    """LOL"""
    lolm = ("┏━┓┈┈╭━━━━╮┏━┓┈┈\n"
            "┃╱┃┈┈┃╱╭╮╱┃┃╱┃┈┈\n"
            "┃╱┗━┓┃╱┃┃╱┃┃╱┗━┓\n"
            "┃╱╱╱┃┃╱╰╯╱┃┃╱╱╱┃\n"
            "┗━━━┛╰━━━━╯┗━━━┛\n")
    await message.edit(lolm)


async def fuckyou(message):
    """Средний палец"""
    fuckyou = ("┏━┳┳┳━┳┳┓\n"
               "┃━┫┃┃┏┫━┫┏┓\n"
               "┃┏┫┃┃┗┫┃┃┃┃\n"
               "┗┛┗━┻━┻┻┛┃┃\n"
               "┏┳┳━┳┳┳┓┏┫┣┳┓\n"
               "┣┓┃┃┃┃┣┫┃┏┻┻┫\n"
               "┃┃┃┃┃┃┃┃┣┻┫┃┃\n"
               "┗━┻━┻━┻┛┗━━━┛\n")
    await message.edit(fuckyou)


async def house(message):
    """Домик"""
    house = ("╯▅╰╱▔▔▔▔▔▔▔╲╯╯\n"
             "▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭\n"
             "▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭\n"
             "╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲\n"
             "▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔\n"
             "▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏\n"
             "▕┓▔┗┓▔┏▏▕┗▏ ┓▔┏\n")
    await message.edit(house)


async def hello(message):
    """Привет!"""
    hello = ("┈┏┓┏┳━┳┓┏┓┏━━┓┈\n"
             "┈┃┃┃┃┏┛┃┃┃┃┏┓┃┈\n"
             "┈┃┗┛┃┗┓┃┃┃┃┃┃┃┈\n"
             "┈┃┏┓┃┏┛┃┃┃┃┃┃┃┈\n"
             "┈┃┃┃┃┗┓┗┫┗┫╰╯┃┈\n"
             "┈┗┛┗┻━┻━┻━┻━━┛┈\n")
    await message.edit(hello)


async def coffee(message):
    """Чашечка кофи"""
    text = ("Это тебе :з")
    coffeem = ("─▄▀─▄▀\n"
              "──▀──▀\n"
              "█▀▀▀▀▀█▄\n"
              "█░░░░░█─█\n"
              "▀▄▄▄▄▄▀▀\n\n"
              f"{text}\n")
    await message.edit(coffeem)


async def tv(message):
    """ОЧЕНЬ ВАЖНО!"""
    text = ("ОЧЕНЬ ВАЖНАЯ НОВОСТЬ!")
    tv = ("░▀▄░░▄▀\n"
          "▄▄▄██▄▄▄▄▄░▀█▀▐░▌\n"
          "█▒░▒░▒░█▀█░░█░▐░▌\n"
          "█░▒░▒░▒█▀█░░█░░█\n"
          "█▄▄▄▄▄▄███══════\n\n"
          f"{text}")
    await message.edit(tv)


async def gren(message):
    """ВЗРЫВ!"""
    text = ("ВЗРЫВАЮ ТЕБЯ НАХУЙ!")
    gren = ("─▄▀▀███═◯\n"
            "▐▌▄▀▀█▀▀▄\n"
            "█▐▌─────▐▌\n"
            "█▐█▄───▄█▌\n"
            "▀─▀██▄██▀\n\n"
            f"{text}")
    await message.edit(gren)


async def bruh(message):
    """Just bruh"""
    bruh = ("╭━━╮╱╱╱╱╱╭╮\n"
            "┃╭╮┃╱╱╱╱╱┃┃\n"
            "┃╰╯╰┳━┳╮╭┫╰━╮\n"
            "┃╭━╮┃╭┫┃┃┃╭╮┃\n"
            "┃╰━╯┃┃┃╰╯┃┃┃┃\n"
            "╰━━━┻╯╰━━┻╯╰╯\n")
    await message.edit(bruh)


async def uno(message):
    """НА ТЕБЯ!"""
    uno = ("⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⡟⡴⠛⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⡏⠴⠞⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⡏⠩⣭⣭⢹⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⠟⣵⣾⠟⠟⣼⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⠿⠀⢛⣵⡆⣶⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⡏⢸⣶⡿⢋⣴⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣇⣈⣉⣉⣼⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢣⠞⢺⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⡴⣣⣿⣿⡇\n"
           "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣿⣿⣿⡇")
    await message.edit(uno)


async def imps(message):
    """Используй .imps <@ или реплай>. Может быть он импостер?"""
    reply = await message.get_reply_message()
    args = utils.raw(message.message)
    if not args and not reply:
        user = await message.client.get_me()
    if reply:
        user = await utils.get_user(await message.get_reply_message())
    if args:
        user = await message.client.get_entity(args)
    imps = ['wasn`t the impostor', 'was the impostor']
    imp = ("`.      　。　　　　•　    　ﾟ　　.      .     。\n"
           "　　.　　　.　　　  .　　　.　　　　　。　　   。　   .\n"
           "　.　　      。        ඞ   。　    .     　.　      •      .\n"
           f"•     {user.first_name} {choice(imps)} 。　   .\n"
           f"　 。     {randint(1, 5)} impostor(s) remains.　　　.　 　.\n"
           ",　　　　.　 .　　       .        •   •    。.\n"
           "。  •　   .   　ﾟ 　  •  　ﾟ .        .    　.`")
    await message.edit(imp)


async def yoda(message):
    """Магистр Йода"""
    text = ("Чувствую дебила в тебе я")
    yoda = ("＿\n"
            "\ー . _ ,´”. : : .“._ .ー´/\n"
            ". ＼>＇_._: :_._' <´／\n"
            "． ‘-: 'ㅎ'/..\'ㅎ'-´\n"
            "  ,.二＼_ ‘,ー、/_\n"
            "'／-＼\ ー¯´/／＼\n"
            "(   ＼ )/   )\n"
            ") ＼ ＿ \)（( ＿ ／（\n"
            "＼  ／Ξ)(Ξ＼ ／\n"
            f"{text}\n")
    await message.edit(yoda)


async def rip(message):
    """Помянем..."""
    text = ("Любим, помним, скорбим...")
    rip = ("⁠      _\n"
           "    __| |__ \n"
           "   |_R.I.P_|\n"
           "      | |   \n"
           "      | |   \n"
           "      | |   \n"
           "      |_|\n"
           f"{text}\n")
    await message.edit(rip)
