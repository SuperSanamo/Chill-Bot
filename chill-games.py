import discord
from discord.ext import commands
import random
import logging
import asyncio
import time
import subprocess

Client = discord.client
client = commands.Bot(command_prefix = '?')
Clientdiscord = discord.Client()
bot = commands.Bot(command_prefix="?")

@client.event
async def on_ready():
    print("Bot 'Chill-Games' is online and connected to Discord")
    print("----------------------------------------------------")
    game = discord.Game("CosmicPvP On Spirit Planet")
    await client.change_presence(status=discord.Status.idle, activity=game)

@client.event
async def on_message(message):
    if "!help games" in message.content.lower():
        emb = (discord.Embed(description="Proper Command Usage: ```!(game[listed below])```", coulour=0x3DF270))
        emb.set_author(name="Help For 'Chill Games'", icon_url='https://cdn.discordapp.com/avatars/506969842264571904/9c54e14ec42c67f34c5531c04943c20d.png?size=256&quot')
        emb.add_field(name='!8ball (question)', value='Asks The 8 Ball A Question. All Answers Are Genuine.')
        emb.add_field(name='!ping', value="The Bot Replies With 'pong'")
        emb.add_field(name='!coinflip(heads or tails)', value= 'Flips A Coin. Lands On Heads Or Tails. ')
        await message.channel.send(embed=emb)
        print("'!help games' Command Was Triggered")
        print("----------------------------------------------------")

    if "!ping" in message.content.lower():
        emb = (discord.Embed(description="", coulour=0x3DF270))
        emb.set_author(name="Pong!", icon_url='https://cdn.discordapp.com/avatars/506969842264571904/9c54e14ec42c67f34c5531c04943c20d.png?size=256&quot')
        await message.channel.send(embed=emb)
        print("'!ping' Command Was Triggered")
        print("----------------------------------------------------")
        
    if "!8ball" in message.content.lower():
        userID = message.author.name
        variable = [":8ball: | It is certain, **%s**" % (userID),
                    ":8ball: | It is decidedly so, **%s**" % (userID),
                    ":8ball: | Without a doubt, **%s**" % (userID),
                    ":8ball: | Yes, definitely, **%s**" % (userID),
                    ":8ball: | You may rely on it, **%s**" % (userID),
                    ":8ball: | As I see it, yes, **%s**" % (userID),
                    ":8ball: | Most likely, **%s**" % (userID),
                    ":8ball: | Outlook good, **%s**" % (userID),
                    ":8ball: | Yes, **%s**" % (userID),
                    ":8ball: | Signs point to yes, **%s**" % (userID),
                    ":8ball: | Reply hazy try again, **%s**" % (userID),
                    ":8ball: | Ask again later, **%s**" % (userID),
                    ":8ball: | Better not tell you now, **%s**" % (userID),
                    ":8ball: | Cannot predict now, **%s**" % (userID),
                    ":8ball: | Concentrate and ask again, **%s**" % (userID),
                    ":8ball: | Don't count on it, **%s**" % (userID),
                    ":8ball: | My reply is no, **%s**" % (userID),
                    ":8ball: | My sources say no, **%s**" % (userID),
                    ":8ball: | Outlook not so good, **%s**" % (userID),
                    ":8ball: | Very doubtful, **%s**" % (userID)]
        await message.channel.send(random.choice(variable))
        print("'!8ball' Command Was Triggered"),
        print("----------------------------------------------------")

    if "!coinflip" in message.content.lower():
        userID = message.author.name

        variable = [":diamond_shape_with_a_dot_inside:  | It is **Heads!**, **%s**" % (userID),
                    ":diamond_shape_with_a_dot_inside:  | It is **Tails**, **%s**" % (userID),]
        await message.channel.send(random.choice(variable))
        print("'!coinflip' Command Was Triggered"),
        print("----------------------------------------------------")

    if "!help " in message.content.lower():
        emb = (discord.Embed(description="```Currently The Songs Available Are...```", coulour=0x3DF270))
        emb.set_author(name="Please Specify A Song", icon_url='https://cdn.discordapp.com/avatars/506969842264571904/9c54e14ec42c67f34c5531c04943c20d.png?size=256&quot')
        emb.add_field(name='Pysco', value='By Post Malone')
        emb.add_field(name='Dark Night Dummo', value="By Travis Scott")
        emb.add_field(name='Betrayed', value= 'By Lil Xan')
        await message.channel.send(embed=emb)
        print("'!lyrics' Command Was Triggered")
        print("----------------------------------------------------")

client.run('NTI0MzcyMDk3NjkxMDI1NDA4.DvnH8g.5qqQzIRTKSpfyMw1JdBHr0R9dLc')

