import emoji

EMOJI_UNICODE = {

    ":grinning_face_with_big_eyes:": "\U0001F603",

    ":beaming_face_with_smiling_eyes:": "\U0001F601",

    ":face_with_tears_of_joy:": "\U0001F602",

    ":rolling_on_the_floor_laughing:": "\U0001F923",

    # Add more emoji here

}
# Generate a list of all available emojis
all_emojis = [emoji.emojize(e) for e in emoji.emojis()]

# Generate the code for the emoji dictionary
code = "emoji_dict = {\n"
for e in all_emojis:
    # Extract the mood description from the shortcode
    mood_desc = e.split("_face")[0][1:]
    # Escape any special characters in the emoji string
    emoji_str = repr(e)[1:-1].replace("'", r"\'")
    code += f"    '{mood_desc}': '{emoji_str}',\n"
code += "}\n"

# Print the resulting code
print(code)
