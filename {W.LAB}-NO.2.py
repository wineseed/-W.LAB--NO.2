import discord
import random
import os
d = discord.Client()
async def on_ready():
    print("login.....")



@d.event

async def on_message(message):
    if message.content.startswith("!등업"):

         msg = message.content[3:]
    if message.is_private and message.author != '602093599877890048':
        await d.send_message(discord.utills.get(d.get_all_members(), id='540416346962264073'), message.author.name+msg)

         

         

    

access_token = os.inviron["BOT_TOKEN"]
d.run(access_token)

