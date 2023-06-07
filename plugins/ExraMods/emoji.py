import emoji

EMOJI_UNICODE = [

    ':grinning_face_with_big_eyes:': '\U0001F603',

    ':beaming_face_with_smiling_eyes:': '\U0001F601',

    ':rolling_on_the_floor_laughing:': '\U0001F923',

    ':face_with_tears_of_joy:': '\U0001F602',

    ':smiling_face_with_open_mouth:': '\U0001F604',

    ':smiling_face_with_open_mouth_and_smiling_eyes:': '\U0001F605',

    ':smiling_face_with_open_mouth_and_cold_sweat:': '\U0001F605',

    ':smiling_face_with_open_mouth_and_tightly_closed_eyes:': '\U0001F606',

    ':smiling_face_with_halo:': '\U0001F607',

    ':smiling_face_with_horns:': '\U0001F608',

    ':winking_face:': '\U0001F609',

    ':smiling_face_with_smiling_eyes:': '\U0001F60A',

    ':face_savouring_delicious_food:': '\U0001F60B',

    ':relieved_face:': '\U0001F60C',

    ':smiling_face_with_heart-eyes:': '\U0001F60D',

    ':smiling_face_with_sunglasses:': '\U0001F60E',

    ':smirk:': '\U0001F60F',

    ':neutral_face:': '\U0001F610',

    ':expressionless_face:': '\U0001F611',

    ':unamused_face:': '\U0001F612',

    ':face_with_cold_sweat:': '\U0001F613',

    ':pensive_face:': '\U0001F614',

    ':confused_face:': '\U0001F615',

    ':confounded_face:': '\U0001F616',

    ':kissing_face:': '\U0001F617',

    ':face_throwing_a_kiss:': '\U0001F618',

    ':kissing_face_with_smiling_eyes:': '\U0001F619',

    ':kissing_face_with_closed_eyes:': '\U0001F61A',

    ':face_with_stuck-out_tongue:': '\U0001F61B',

    ':face_with_stuck-out_tongue_and_winking_eye:': '\U0001F61C',

    ':face_with_stuck-out_tongue_and_tightly_closed_eyes:': '\U0001F61D',

    ':disappointed_face:': '\U0001F61E',

    ':worried_face:': '\U0001F61F',

    ':angry_face:': '\U0001F620',

    ':pouting_face:': '\U0001F621',

    ':crying_face:': '\U0001F622',

    ':persevering_face:': '\U0001F623',

    ':face_with_look_of_triumph:': '\U0001F624',

    ':disappointed_but_relieved_face:': '\U0001F625',

    ':frowning_face_with_open_mouth:': '\U0001F626',

    ':anguished_face:': '\U0001F627',

    ':fearful_face:': '\U0001F628',

    ':weary_face:': '\U0001F629',

    ':sleepy_face:': '\U0001F62A',

    ':tired_face:': '\U0001F62B',

    ':grimacing_face:': '\U0001F62C',

    ':loudly_crying_face:': '\U0001F62D',

    ':face_with_open_mouth:': '\U0001F62E',

    ':hushed_face:': '\U0001F62F',

    ':face_screaming_in_fear:': '\U0001F630',

    ':astonished_face:': '\U0001F632',

    ':flushed_face:': '\U0001F633',

    ':sleeping_face:': '\U0001F634',

    ':dizzy_face:': '\U0001F635',

    ':face_without_mouth:': '\U0001F636',

    ':face_with_medical_mask:': '\U0001F637',

    ':grinning_cat_face_with_smiling_eyes:': '\U0001F638',

    ':cat_face_with_wry_smile:': '\U0001F63C',

    ':kissing_cat_face:': '\U0001F63D',

    ':weary_cat_face:': '\U0001F640',

    ':crying_cat_face:': '\U0001F63F',

    ':pouting_cat_face:': '\U0001F63E',

    ':see-no-evil_monkey:': '\U0001F648',

    ':hear-no-evil_monkey:': '\U0001F649',

    ':speak-no-evil_monkey:': '\U0001F64A',

    ':smiling_face_with_halo:': '\U0001F607',

    ':raised_hands:': '\U0001F64C',

    ':folded_hands:': '\U0001F64F',

    ':man_and_woman_holding_hands:': '\U0001F46B',

    ':two_men_holding_hands:': '\U0001F46C',

    ':two_women_holding_hands:': '\U0001F46D',

    ':baby_angel:': '\U0001F47C',

    ':face_with_cowboy_hat:': '\U0001F920',

    ':clown_face:': '\U0001F921',

    ':nauseated_face:': '\U0001F922',

    ':nerd_face:': '\U0001F913',

    ':smiling_face_with_horns:': '\U0001F608',

    ':ogre:': '\U0001F479',

    ':goblin:': '\U0001F47A',

    ':ghost:': '\U0001F47B',

    ':alien:': '\U0001F47D',

    ':robot_face:': '\U0001F916',

    ':pile_of_poo:': '\U0001F4A9',

    ':fire:': '\U0001F525',

    ':sparkles:': '\U00002728',

    ':star:': '\U00002B50',

    ':star2:': '\U0001F31F',

    ':dizzy:': '\U0001F4AB',

    ':boom:': '\U0001F4A5',

    ':collision:': '\U0001F4A5',

    ':anger_symbol:': '\U0001F4A2',

    ':sweat_droplets:': '\U0001F4A6',

    ':dash_symbol:': '\U0001F4A8',

    ':dollar_banknote:': '\U0001F4B5',

    ':money_with_wings:': '\U0001F4B8',

    ':credit_card:': '\U0001F4B3',

    ':chart_increasing_with_yen:': '\U0001F4B9',

    ':chart_decreasing_with_yen:': '\U0001F4B9',

    ':envelope:': '\U00002709',

    ':e-mail_symbol:': '\U0001F4E7',

    ':incoming_envelope:': '\U0001F4E8',

    ':envelope_with_downwards_arrow_above:': '\U0001F4E9',

    ':outgoing_envelope:': '\U0001F4E4',

    ':envelope_with_upwards_arrow_above:': '\U0001F4E5',

    ':closed_mailbox_with_raised_flag:': '\U0001F4EB',

    ':closed_mailbox_with_lowered_flag:': '\U0001F4EA',

    ':open_mailbox_with_raised_flag:': '\U0001F4EC',

    ':open_mailbox_with_lowered_flag:': '\U0001F4ED',

    ':postbox:': '\U0001F4EE',

    ':ballot_box_with_ballot:': '\U0001F5F3',

    ':pencil:': '\U0000270F',

    ':black_nib:': '\U00002712',

    ':memo:': '\U0001F4DD',

    ':briefcase:': '\U0001F4BC',

    ':file_folder:': '\U0001F4C1',

    ':open_file_folder:': '\U0001F4C2',

    ':card_index_dividers:': '\U0001F5C2',

    ':calendar:': '\U0001F4C5',

':tear-off_calendar:': '\U0001F4C6',

':spiral_note_pad:': '\U0001F5D2',

':spiral_calendar_pad:': '\U0001F5D3',

':clipboard:': '\U0001F4CB',

':file_cabinet:': '\U0001F5C4',

':wastebasket:': '\U0001F5D1',

':locked:': '\U0001F512',

':unlocked:': '\U0001F513',

':locked_with_key:': '\U0001F510',

':key:': '\U0001F511',

':old_key:': '\U0001F5DD',

':hammer:': '\U0001F528',

':pick:': '\U000026CF',

':hammer_and_pick:': '\U00002692',

':hammer_and_wrench:': '\U0001F6E0',

':dagger_knife:': '\U0001F5E1',

':crossed_swords:': '\U00002694',

':gun:': '\U0001F52B',

':bomb:': '\U0001F4A3',

':hocho:': '\U0001F52A',

':shield:': '\U0001F6E1',

':smoking_symbol:': '\U0001F6AC',

':skull_and_crossbones:': '\U00002620',

':coffin:': '\U000026B0',

':funeral_urn:': '\U000026B1',

':amphora:': '\U0001F3FA',

':crystal_ball:': '\U0001F52E',

':prayer_beads:': '\U0001F4FF',

':barber_pole:': '\U0001F488',

':alembic:': '\U00002697',

':telescope:': '\U0001F52D',

':microscope:': '\U0001F52C',

':hole:': '\U0001F573',

':pill:': '\U0001F48A',

':syringe:': '\U0001F489',

':thermometer:': '\U0001F321',

':label:': '\U0001F3F7',

':bookmark:': '\U0001F516',

':toilet:': '\U0001F6BD',

':shower:': '\U0001F6BF',

':bathtub:': '\U0001F6C1',

':sewing_needle:': '\U0001FAA1',

':thread:': '\U0001F9F5',

':yarn:': '\U0001F9F6',

':knot:': '\U0001FAA2',

':glasses:': '\U0001F453',

':sunglasses:': '\U0001F576',

':goggles:': '\U0001F97D',

':lab_coat:': '\U0001F97C',

':safety_vest:': '\U0001F9BA',

':necktie:': '\U0001F454',

':t-shirt:': '\U0001F455',

':jeans:': '\U0001F456',

':scarf:': '\U0001F9E3',

':gloves:': '\U0001F9E4',

':coat:': '\U0001F9E5',

':socks:': '\U0001F9E6',

':dress:': '\U0001F457',

':kimono:': '\U0001F458',

':sari:': '\U0001F97B',

':one-piece_swimsuit:': '\U0001FA71',

':briefs:': '\U0001FA72',

':shorts:': '\U0001FA73',

':bikini:': '\U0001F459',

':woman’s_clothes:': '\U0001F45A',

':purse:': '\U0001F45B',

':handbag:': '\U0001F45C',

':clutch_bag:': '\U0001F45D',

':shopping_bags:': '\U0001F6CD',

:school_satchel:': '\U0001F392',

':mans_shoe:': '\U0001F45E',

':running_shoe:': '\U0001F45F',

':high-heeled_shoe:': '\U0001F460',

':woman’s_sandal:': '\U0001F461',

':woman’s_boot:': '\U0001F462',

':crown:': '\U0001F451',

':womans_hat:': '\U0001F452',

':top_hat:': '\U0001F3A9',

':graduation_cap:': '\U0001F393',

':billed_cap:': '\U0001F9E2',

':military_helmet:': '\U0001FA96',

':rescue_worker’s_helmet:': '\U000026D1',

':prayer_beads:': '\U0001F4FF',

':lipstick:': '\U0001F484',

':ring:': '\U0001F48D',

':gem_stone:': '\U0001F48E',

':mute_speaker:': '\U0001F507',

':speaker_low_volume:': '\U0001F508',

':speaker_medium_volume:': '\U0001F509',

':speaker_high_volume:': '\U0001F50A',

':loudspeaker:': '\U0001F4E2',

':megaphone:': '\U0001F4E3',

':postal_horn:': '\U0001F4EF',

':bell:': '\U0001F514',

':bell_with_slash:': '\U0001F515',

':musical_note:': '\U0001F3B5',

':musical_notes:': '\U0001F3B6',

':studio_microphone:': '\U0001F399',

':level_slider:': '\U0001F39A',

':control_knobs:': '\U0001F39B',

':microphone:': '\U0001F4E2',

':headphone:': '\U0001F3A7',

':radio:': '\U0001F4FB',

':saxophone:': '\U0001F3B7',

':guitar:': '\U0001F3B8',

':musical_keyboard:': '\U0001F3B9',

':trumpet:': '\U0001F3BA',

':violin:': '\U0001F3BB',

':drum:': '\U0001F941',

':mobile_phone:': '\U0001F4F1',

':mobile_phone_with_arrow:': '\U0001F4F2',

':telephone:': '\U0000260E',

':telephone_receiver:': '\U0001F4DE',

':pager:': '\U0001F4DF',

':fax_machine:': '\U0001F4E0',

':battery:': '\U0001F50B',

':electric_plug:': '\U0001F50C',

':laptop_computer:': '\U0001F4BB',

':desktop_computer:': '\U0001F5A5',

':printer:': '\U0001F5A8',

':keyboard:': '\U00002328',

':computer_mouse:': '\U0001F5B1',

':trackball:': '\U0001F5B2',

':film_frames:': '\U0001F39E',

':film_projector:': '\U0001F4FD',

':clapper_board:': '\U0001F3AC',

':television:': '\U0001F4FA',

':camera:': '\U0001F4F7',

':camera_with_flash:': '\U0001F4F8',

':video_camera:': '\U0001F4F9',

':movie_camera:': '\U0001F3A5',

':videocassette:': '\U0001F4FC',

':optical_disc:': '\U0001F4BF',

':dvd:': '\U0001F4C0'
    
]

# Generate a list of all available emojis
all_emojis = list(emoji.EMOJI_UNICODE.values())

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
