import discord
import asyncio
import random
import aiohttp
import json
from discord.utils import get
import requests
from discord.ext import commands

bot = commands.Bot(command_prefix=".")

helperResponseA = ["Alright, Gravity Destroyers, sending help for you now", "Help? Someone needs help? Right away bois.", "I was sleeping, did you have to wake me up with this help request? Send help now.", "Help? Only God can help you!!", "Aww, you need help fam. Dw I'm here for you", "Help request that's noice", "HELP??? SURE MATE", "K alerting the martian embassy help is required"]
helperResponseB = "**Help request**\n> Please react with <:agreentick:875244017833639956> below this message to enable this ping request, 3 votes excluding me are required unless a moderator approves the request."
helperResponseC = ["Alrightyyyy, we have authorisation to continue", "Nice bruh, stars have aligned, helper ping APPROVED", "Helper ping incoming", "Martian embassy has responded, we're gonna ping the helpers"]
helperResponseD = ["Mighty moderators have bypassed the regular authorisation and progressed this help request at the quantum leap speed", "Ohh nice, mods approved this help request.", "Kids, we got mod chads helpin us out", "Mods have approved this help request, now I'm heading back to bed"]

@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Gravity Destroyers"))


@commands.command()
async def compliment(ctx, user):
    x = requests.get('https://complimentr.com/api')
    #jsonCompliment = f'\'{x.content}\''
    jsonCompliment = x.content
    compliment = json.loads(jsonCompliment)
    #ctx.send(compliment["compliment"])
    print(compliment["compliment"])
    finalsend = compliment["compliment"]
    await ctx.send(f'{user} {finalsend}')
@commands.command()
async def helperping(ctx, usermention, *,messageid):
    global uusermention
    global mmessageid
    global whorequested
    whorequested = ctx.author.mention
    uusermention = usermention
    mmessageid = messageid
    await ctx.send(random.choice(helperResponseA))
    await asyncio.sleep(2)
    await ctx.send(helperResponseB)#889042207544340511
    
    #await ctx.channel.purge(1)
@commands.command()
async def about(ctx):
    async with ctx.typing():
        # do expensive stuff here
        await asyncio.sleep(3)
    await ctx.send("Oh hey, you wanna know more about me??")
    await ctx.send("SURE I'll do that hahahaha")
    async with ctx.typing():
        await asyncio.sleep(10)
    await ctx.send("Ladies and Gentlemen, skinny and stout,\nI\’ll tell you a tale I know nothing about\nThe Admission is free, so pay at the door,\nNow pull up a chair and sit on the floor")
    async with ctx.typing():
        await asyncio.sleep(10)
    await ctx.send("On a bright day in the middle of the night\nTwo dead boys got up to fight\nBack to back they face eachother\nDrew their swords and shot eachother\nThe deaf policeman heard the noise and saved the lives of the two dead boys\nIf you don't believe my story is true\nAsk the blind man, he saw it too")
    async with ctx.typing():
        await asyncio.sleep(15)
    await ctx.send("HAHAHA, did you really think I'd give you an answer?!!")
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("WELL, ||you'd be right|| just after a little wild ride ;) ;)")
    async with ctx.typing():
        await asyncio.sleep(3)
    await ctx.send("I'm the Gravity Destroyers Bot :)\nI help you guys do your stuff lol\nI'm usually friendly and sometimes impatient (crazy humans :rolling_eyes:)\nI'm not a chat bot, I just have clever coding")

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    #print(message)
    if message.author.id == 889042207544340511:
        if message.content == helperResponseB:
            await message.add_reaction("<:agreentick:875244017833639956>")
            # if message.reactions.count == 4:
            #     await message.channel.send(helperResponseC)
    if message.content == "yeah boi":
        await message.channel.send("yeah BOIII")
    

@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji)
    emoji = reaction.emoji
    await reaction.message.add_reaction(str(emoji))
    if reaction.message.author.id == 889042207544340511 and reaction.message.content == helperResponseB:
        #if reaction.count == 2:
        # if discord.utils.get(reaction.message.reactions, emoji='<:agreentick:913047736876691557>').count == 2:
        #     await reaction.message.channel.send("ayo bois")
        #await reaction.message.channel.send(reaction.emoji)
        #print(str(reaction.emoji))
        #print(user.roles)

        if str(reaction.emoji) == '<:agreentick:875244017833639956>' and reaction.count > 2:
            await reaction.message.channel.send(random.choice(helperResponseC))
        else:
            for role in user.roles:
                #print(role)
                if role.id in (872984654544765028, 910706555496849458, 910701780055228456):
                    await reaction.message.channel.send(random.choice(helperResponseD))
                    await reaction.message.channel.send(f'Alright thanks {whorequested} we got this help request going now')
                    if mmessageid.isnumeric():
                        textchannel = reaction.message.channel
                        originalMessage = await textchannel.fetch_message(int(mmessageid))
                        #await textchannel.send(originalMessage.content)
                        await reaction.message.channel.send(f'(**phantom helper ping, pretend it\'s here)**\n{uusermention} needs help with {originalMessage.content}')#<@&872010951795306496>
                    else:
                        await reaction.message.channel.send(f'(**phantom helper ping, pretend it\'s here)**\n{uusermention} needs help with {mmessageid}')#<@&872010951795306496>
 

                    
            
bot.add_command(helperping)
bot.add_command(compliment)
bot.add_command(about)
bot.run("ODg5MDQyMjA3NTQ0MzQwNTEx.YUbfEw.ZT6JbqB8EPZdoxekpY6GFfMl2F8")

# def count(message):
#     for reaction in message.reactions:
#         if reaction.emoji == '✅':
#             return reaction.count
#     return 0