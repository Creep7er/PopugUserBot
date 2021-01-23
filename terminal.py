import subprocess
import utils


async def terminal(event):
    """Execute stuff in your os terminal"""
    command = utils.raw(event.message)
    await event.edit(f"**Running command:**\n`{command}`")
    result = subprocess.getoutput(command)
    await event.edit(f"**Running command:**\n`{command}`\n**Result:**\n`{result}`")
