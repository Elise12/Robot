import telethon
import asyncio
import time
from telethon import TelegramClient, sync
from telethon.sync import TelegramClient, events
# Настройка
# Сюда пишем api_id и api_hash | my.telegram.org
api_id =
api_hash = '' 

# Нужный текст для автоответчика

message = "Maintenant que vous avez affaire à un bot, l'administrateur va bientôt arriver."

# Сам автоответчик

client = TelegramClient('bebra', api_id, api_hash)
client.start()
print(client.get_me().stringify())
print('Le compte est valide')
@client.on(events.NewMessage)
async def handler(event):
    time.sleep(3)
    await event.reply(message)
    time.sleep(10) # Il est nécessaire que le compte ne vole pas aux îles de bananes  
client.run_until_disconnected()