from telethon import events, TelegramClient
from src.constants import Constants
from src.utils import Utils

with TelegramClient(
        Constants.CHAT_NAME.value,
        Constants.API_ID.value,
        Constants.API_HASH.value,
) as client:
    @client.on(events.NewMessage())
    async def handler(event) -> None:
        if not event.chat:
            return
        if Utils.chat_title_matches(event.chat.title):
            event.message.text = Utils.format_message(event.chat.title, event.message.text)
            await client.send_message(Constants.CHAT_NAME.value, event.message)


    client.run_until_disconnected()
