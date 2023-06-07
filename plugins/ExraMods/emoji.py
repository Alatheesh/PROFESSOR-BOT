import re

import emoji

def get_emoji(shortcode):

    unicode_char = emoji.emojize(f':{shortcode}:')

    name = emoji.UNICODE_EMOJI.get(unicode_char, None)

    if name is not None:

        name = name.replace('_', ' ').capitalize()

    return name

shortcode_to_mood = {

    '😃': 'grinning_face_with_big_eyes',

    '😊': 'smiling_face_with_smiling_eyes',

    '😌': 'relieved_face',

    '😍': 'smiling_face_with_heart_eyes',

    '😇': 'smiling_face_with_halo',

    '🤔': 'thinking_face',

    '😢': 'crying_face',

    '😠': 'angry_face',

    '😴': 'sleeping_face',

    '😷': 'face_with_medical_mask',

    '🥰': 'smiling_face_with_three_hearts',

    '🤩': 'star-struck',

    '🙄': 'face_with_rolling_eyes',

    '🤕': 'face_with_head-bandage',

    '🧐': 'face_with_monocle',

    '😖': 'confounded_face',

    '🤬': 'face_with_symbols_on_mouth',

    '🤗': 'hugging_face',

    '🤢': 'nauseated_face',

    '😱': 'face_screaming_in_fear',

}

emoji_dict = {}

for shortcode, mood_desc in shortcode_to_mood.items():

    emoji_dict[mood_desc] = get_emoji(shortcode)

print(emoji_dict) 
