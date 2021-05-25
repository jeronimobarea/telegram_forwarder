from telethon import events, TelegramClient
from src.utils.constants import Constants
from src.utils.message import Message

client = TelegramClient(
    Constants.CHAT_NAME.value[1],
    Constants.API_ID.value,
    Constants.API_HASH.value,
)


@client.on(events.NewMessage())
async def handler(event) -> None:
    chat = await event.get_chat()
    if not chat:
        return
    if Message.chat_title_matches(chat.title):
        print(chat)
        event.message.text = Message.format_message(chat.title, event.message.text)
        try:
            await client.send_message(Constants.CHAT_NAME.value[0], event.message)
        except:
            await client.send_message(Constants.CHAT_NAME.value[1], event.message)


if __name__ == "__main__":
    print("Running!")
    client.start()
    client.run_until_disconnected()
