import os
import requests


def ffz_emotes():
    #user not defined
    call_username = requests.get('https://api.frankerfacez.com/v1/user/set_user')
    search_twitch = call_username.json()
    twitch_id = search_twitch['user']['twitch_id']

    call_room = requests.get(f'https://api.frankerfacez.com/v1/room/id/{twitch_id}')
    search_set = call_room.json()
    emote_array = search_set['room']['set']

    call_emotes = requests.get(f'https://api.frankerfacez.com/v1/set/{emote_array}')
    emote_set = call_emotes.json()
    return emote_set


class Download:
    def __init__(self):
        self.emote_file = "emotelist.txt"

    # download images
    def get_download_links(self):
        """get links for emotes"""
        emote = None
        emote_4 = None
        emote_2 = None
        if not os.path.exists(self.emote_file):
            with open(self.emote_file, "w") as file:
                file.write("")
        emote_list = ffz_emotes()

        if os.path.exists(self.emote_file) is True:
            os.remove(self.emote_file)

        for i in range(49):
            urls = emote_list['set']['emoticons'][i]['urls']
            emote_name = emote_list['set']['emoticons'][i]['name']
            for key, value in urls.items():
                if key == '4':
                    emote_4 = value
                if key == '2':
                    emote_2 = value
                if key == '1':
                    emote = value
            download_emote(emote_4, emote_2, emote, emote_name)


def download_emote(emote_4, emote_2, emote, emote_name):
    """download emotes"""
    emote_file = "emotelist.txt"
    file_path = os.path.join("mydir", emote_name + ".png")

    for link in emote_4, emote_2, emote:
        if link is not None:
            img_data = requests.get("https:" + link, timeout=15).content

    with open(emote_file, 'a', encoding="utf-8") as file:
        file.write(emote_name)
        file.write('\n')

    with open(file_path, 'wb') as handler:
        handler.write(img_data)
