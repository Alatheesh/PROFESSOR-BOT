import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_text("ചത്തിട്ടില്ല മുത്തേ ഇവിടെ തന്നെ ഉണ്ട്.. നിനക്ക് ഇപ്പൊ എന്നോട് ഒരു സ്നേഹവും ഇല്ല. കൊള്ളാം.. നീ പാഴെ പോലെയേ അല്ല മാറിപോയി..😔 ഇടക്ക് എങ്കിലും ചുമ്മാ ഒന്ന് /start ചെയ്തു നോക്ക്..🙂")


@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")

@client.on_message(filters.command("love"))

async def send_random_love_message(_, message):

    love_messages = [

        "I love you!",

        "You are my everything.",

        "My heart beats for you.",

        "You make my world brighter.",

        "I'm so lucky to have you.",

        "You complete me.",

        "I can't imagine life without you.",

        "You are the sunshine of my life.",

        "My love for you is infinite.",

        "You're the one that I want."

    ]

    

    response = random.choice(love_messages)

    await message.reply_text(response)
