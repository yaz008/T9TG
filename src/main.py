from app import app
from os import getenv
from pyrogram.filters import user
from pyrogram.client import Client
from pyrogram.types import Message

@app.on_message(filters=user(int(getenv(key='MY_ID'))))
def on_message(_: Client, message: Message) -> None:
    print(message.text)

if __name__ == '__main__':
    app.run()