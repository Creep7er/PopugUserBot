import os
import asyncio


async def main():
    try:
        print("Checking for 'telethon' package...")
        from telethon import TelegramClient
        print("'telethon' found!")
    except ModuleNotFoundError:
        print("'telethon' not found. Installing...")
        os.system("pip install telethon")
        from telethon import TelegramClient
    try:
        print("Checking for 'meval' package...")
        import meval
        print("'meval' found!")
    except ModuleNotFoundError:
        print("'meval' not found. Installing...")
        os.system("pip install meval")
        import meval

    print("You will now be asked for your api development hash and id. To get them, go to my.telegram.org and "
          "authorize.")
    try:
        api_id = int(input("Enter your api id: "))
    except ValueError:
        print("Invalid id - not a number. Run installation again.")
        exit(1)
    api_hash = input("Enter your api hash: ")
    print("Connecting client...")
    client = TelegramClient('anon', api_id, api_hash)
    password = input("If you have 2fa, enter your password. Otherwise just hit 'Enter': ")
    if password:
        await client.start(password=password)
    else:
        await client.start()
    await client.connect()
    db_message = await client.send_message("me", "{}")
    db_id = db_message.id
    print("DO NOT SHARE ANY FILES CREATED BY THE USERBOT! They might contain your account and private data")
    print("Creating config...")
    f = open("config", "w+")
    f.write(f"{api_id}\n{api_hash}\n{db_id}")
    f.close()
    del client
    print("The installation is done and you can start the bot with 'python ub.py'. Note that you should not use '.eval' command unless you "
          "know python, as '.eval' can execute malicious code.")

loop = asyncio.get_event_loop()
asyncio.set_event_loop(loop)
loop.run_until_complete(main())
