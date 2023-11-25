#@KUSHALHK Thank me later "please don't remove my credits".
from pyrogram import Client, filters
from plugins.helper.engine import ask_ai


@Client.on_message(filters.command('chatgpt'))
async def openai_ask(client, message):
    if len(message.command) == 1:
       return await message.reply_text("Give me a prompt to Search ✨")
    m = await message.reply_text("👀")
    await ask_ai(client, m, message)
