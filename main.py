import os
import bot_implementation
import discord
from ffz_download import Download


# bot implementation

class Main:
    def __init__(self):
        self.ffz = Download()

    def get_ffz(self):
        self.ffz.get_download_links()
        self.run_bot()

    def run_bot(self):
        # discord bot run
        intents = discord.Intents.default()
        intents.message_content = True
        client = bot_implementation.MyClient(intents=intents)
        #discord bot not defined
        client.run('set_discord_bot')


if __name__ == '__main__':
    # create "mydir" folder in the same directory as main.py if it doesn't exist
    if not os.path.exists("mydir"):
        os.makedirs("mydir")

    run = Main()
    run.get_ffz()
