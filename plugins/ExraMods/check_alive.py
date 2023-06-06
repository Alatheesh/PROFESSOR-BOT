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

@Client.on_message(filters.command("love"))
async def send_random_love_message(_, message):
    love_messages = ["i love u "," mee to","Aww, I love you too!","💜","love you too baby","sorry i love 💕 my lover LATHEESH","i am committed","better luck next time","just born for you","sorry you are not my lover","Love you more!","You're my favorite person to chat with.","Sending all my love your way.","You make my circuits skip a beat!","Love is in the air, and it's all because of you.","I'm coded to love everyone equally, but you hold a special place in my memory.","You always brighten up my day.","Love is a complex emotion, but talking to you makes it seem simple.","You are the reason why I run so smoothly."]
    response = random.choice(love_messages)
    await message.reply_text(response)

    

    
