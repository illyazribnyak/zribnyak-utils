from telethon import TelegramClient
import asyncio

API_ID =API_ID
API_HASH = "Api hash"


PHONE_NUMBER = "phone"

# 🔹 Введіть ID, username або номер телефону користувача, якого шукаємо
TARGET_USER = "target phone"

async def main():

    client = TelegramClient("session_name", API_ID, API_HASH)


    await client.start(PHONE_NUMBER)

    try:

        user = await client.get_entity(TARGET_USER)

        # Виводимо знайдені дані
        print(f" ID: {user.id}")
        print(f" Username: @{user.username}" if user.username else "👤 Username: (відсутній)")
        print(f" Phone: {user.phone}" if user.phone else "📞 Phone: (відсутній)")

    except Exception as e:
        print(f" Помилка: {e}")

    await client.disconnect()

asyncio.run(main())