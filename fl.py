from asyncio import sleep
import __main__

async def fakeload(e):
	"""Фейковая загрузка. Срёт в логи"""
	load = [" ","▏","▎","▍","▌","▋","▊","▉"]
	bar = ""
	count = 0
	await e.edit("`[Инициализация]`")
	await sleep(3)
	for i in range(13):
		for division in load:
			space = " " * (12 - i)
			await e.edit(f"`{bar}{division}{space}[{count}%]`")
			count += 1
			await sleep(0.3)
			if count == 101:
				break
		bar += "█"
	await sleep(2)
	done = "Загрузка завершена!"
	await e.edit(f"`{done}`")