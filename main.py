from pyrogram import Client, filters
from time import sleep
from datetime import datetime
import asyncio

chats = []
MESSAGE_TEXT = "https://t.me/+Kr42Gs5ilbhkMmVi\t\t\t5K ОХВАТА\nhttps://t.me/+GBTNA327484wNzRi\t\t\t2K ОХВАТА\nhttps://t.me/+itgM63j8ZZ8yZDcy\t\t\t5K ОХВАТА\nhttps://t.me/+StJpNMJWySs0YTRi\t\t\t8K ОХВАТА\n\nПривет, продам места в новостях👆, приходом будешь доволен.\nПиши мне - @OXPAHA_AHYCA"

app = Client("my_account")
app.start()

if int(datetime.now().strftime("%H")) >= 0 and int(datetime.now().strftime("%H")) < 10:
	app.send_message('me', 'Бот запущен. Рассылка происходит каждые 60 минут, текст:')
else:
	app.send_message('me', 'Бот запущен. Рассылка происходит каждые 10 минут, текст:')
app.send_message('me', MESSAGE_TEXT, disable_web_page_preview=True)

loop = asyncio.get_event_loop()
async def main():
    while True:
    	@app.on_message(filters.group)
    	def add(client, message):
    		if not message.chat.id in chats:
    			chats.append(message.chat.id)
    			app.send_message('me', 'В базу добавлена 1 группа.', disable_web_page_preview=True)
    	for i in chats:
    		await app.send_message(i, MESSAGE_TEXT, disable_web_page_preview=True)
    		await asyncio.sleep(6)
    	if int(datetime.now().strftime("%H")) >= 0 and int(datetime.now().strftime("%H")) < 10:
    		await asyncio.sleep(3600)
    	else:
    		await asyncio.sleep(600)

loop.run_until_complete(main())

app.run()
