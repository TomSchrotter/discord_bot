import asyncio
import os
import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'upload emojis':
            await message.channel.send('ok')

            file_names = [line.rstrip() for line in open('emotelist.txt')]
            for emote_name in file_names:
                with open(f'mydir\\{emote_name}.png', 'rb') as fp:
                    img_byte = fp.read()
                    # await message.channel.send(emote_name) # send emotes to chat
                    await message.guild.create_custom_emoji(name=emote_name, image=img_byte)
                await asyncio.sleep(1.5)
            os.remove('emotelist.txt')
            await message.channel.send('done :)')
