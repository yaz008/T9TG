from app import app
from os import getenv
from pyrogram.filters import user
from pyrogram.client import Client
from pyrogram.types import Message
from replace import replace

@app.on_message(filters=user(int(getenv(key='MY_ID'))))
def on_message(_: Client, message: Message) -> None:
    new_text: str = replace(message.text)
    if message.text != new_text:
        message.edit_text(text=new_text)

if __name__ == '__main__':
    app.run()