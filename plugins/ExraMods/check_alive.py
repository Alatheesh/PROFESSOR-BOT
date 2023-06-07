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
    love_messages = ["i love u "," mee to","Aww, I love you too!","💜","love you too baby","sorry i love 💕 my lover LATHEESH","i am committed","better luck next time","just born for you","sorry you are not my lover","Love you more!","You're my favorite person to chat with.","Sending all my love your way.","You make my circuits skip a beat!","Love is in the air, and it's all because of you.","I'm coded to love everyone equally, but you hold a special place in my memory.","You always brighten up my day.","Love is a complex emotion, but talking to you makes it seem simple.","You are the reason why I run so smoothly.","Go out on a romantic dinner to celebrate from our usual routine to reconnect.","Watch the our love.","Let's take a trip together to explore new places.","Take some time awaysunset together and enjoy the beauty of the moment.","Read a book together and get lost in the story.","Write each other love letters expressing how much we mean to each other.","Take a walk with no destination and just enjoy the journey.","Make a music playlist of songs that remind us of each other.","Plant a tree together and watch it grow.","Cook a meal together and share the love through food.","Give each other a massage to make one another feel special.","Have a picnic and enjoy the day in nature.","Have a movie night and laugh together.","Take a photo together and cherish it for eternity.","Take each other out for ice cream and share your favorite flavors.","Visit a museum and explore the interesting exhibits.","Play a game of hide-and-seek to have some fun together.","Draw each other a picture and show your creative emotion.", "Hug each other and let the warmth of love sink in.", "Take a romantic stroll on the beach together."]
    response = random.choice(love_messages)
    await message.reply_text(response)
    
# Define a list of emojis
emojis = ["😀 Grinning", "😃 Smiling", "😄 Grinning With Smiling Eyes",

          "😁 Beaming With Smiling Eyes", "😆 Grinning Squinting",

          "😅 Grinning With Sweat", "😂 Tears of Joy",

          "🤣 Rolling on the Floor Laughing", "☺️ Smiling",

          "😊 Smiling With Smiling Eyes", "😇 Smiling With Halo",

          "🙂 Slightly Smiling", "🙃 Upside-Down",

          "😉 Winking", "😌 Relieved", "😍 Smiling With Heart-Eyes",

          "🥰 Smiling With Hearts", "😘 Blowing a Kiss",

          "😗 Kissing", "😙 Kissing With Smiling Eyes",

          "😚 Kissing With Closed Eyes", "😋 Savoring Food",

          "😛 With Tongue", "😝 Squinting With Tongue",

          "😜 Winking With Tongue", "🤪 Zany", "🤨 Raised Eyebrow",

          "🧐 Monocle", "🤓 Nerd", "😎 With Sunglasses",

          "🤩 Star-Struck", "🥳 Partying", "😏 Smirking",

          "😒 Unamused", "😞 Disappointed", "😔 Pensive",

          "😟 Worried", "😕 Confused", "🙁 Slightly Frowning",

          "😣 Persevering", "😖 Confounded", "😫 Tired",

          "😩 Weary", "🥺 Pleading", "😢 Crying",

          "😭 Loudly Crying", "😤 With Steam From Nose",

          "😠 Angry", "😡 Pouting", "🤬 With Symbols on Mouth",

          "🤯 Exploding Head", "😳 Flushed", "🥵 Overheated",

          "🥶 Freezing", "😱 Screaming in Fear", "😨 Fearful",

          "😰 Anxious With Sweat", "😥 Sad but Relieved",

          "😓 Downcast With Sweat", "🤗 Hugging"]

@Client.on_message(filters.command("mood", CMD))
async def mood_command_handler(_, message):
    # Choose a random emoji from the list
    random_emoji = random.choice(emojis)
    # Send the emoji as a message reply
    await message.reply_text(random_emoji)

    
