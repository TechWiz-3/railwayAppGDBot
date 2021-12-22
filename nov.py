import discord
import asyncio
import random
import aiohttp
import json
from discord.utils import get
import requests
from discord.ext import commands
from dotenv import load_dotenv
import os
import mysql.connector
mydb = mysql.connector.connect(
  host="containers-us-west-23.railway.app",
  user="root",
  password="yUWgeMOav9HmGFDqUIXo",
  database="railway",
  port="6499"
)
mycursor = mydb.cursor()

bot = commands.Bot(command_prefix=".")

@bot.slash_command(guild_ids=[867597533458202644])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    await ctx.respond(f"Hello {ctx.author}!")

# @slashBot.command()
# async def hello(ctx):
#     await ctx.respond(f"Hello {ctx.author}!")

load_dotenv()
token = os.getenv("token")

helperResponseA = ["Alright, Gravity Destroyers, sending help for you now", "Help? Someone needs help? Right away bois.", "I was sleeping, did you have to wake me up with this help request? Send help now.", "Help? Only God can help you!!", "Aww, you need help fam. Dw I'm here for you", "Help request that's noice", "HELP??? SURE MATE", "K alerting the martian embassy help is required"]
helperResponseB = "**Help request**\n> Please react with <:agreentick:875244017833639956> below this message to enable this ping request, 3 votes excluding me are required unless a moderator approves the request."
helperResponseC = ["Alrightyyyy, we have authorisation to continue", "Nice bruh, stars have aligned, helper ping APPROVED", "Helper ping incoming", "Martian embassy has responded, we're gonna ping the helpers"]
helperResponseD = ["Mighty moderators have bypassed the regular authorisation and progressed this help request at the quantum leap speed", "Ohh nice, mods approved this help request.", "Kids, we got mod chads helpin us out", "Mods have approved this help request, now I'm heading back to bed"]
randomReminders = ["**Community service reminder**\nStop looking at the screen with a dry throat you lazy people :rolling_eyes:", "Stop fidgetting mate, it's annoying", "Right right", "k", "Stop sitting on the computer while you need to go to the bathroom, you know better", "thonking...", "Mind rephrasing that from crazy to english??", "you da man ay", "Public service announcement, SIT PROPERLY PEOPLE\nYall look like monkeys in front of that screen brah", "aww", "You done your workout yet today brah? No time like the present", "Mate seriously I love your enthusiasm but you really need a haircut", "you done your workout toda- oh I see you have looking fire💯", "Be not afraid of greatness. Some are born great, some achieve greatness, and others have greatness thrust upon them.", "All the world's a stage,\nAnd all the men and women merely players;\nThey have their exits and their entrances;\nAnd one man in his time plays many parts,\nHis acts being seven ages.", "Fine sir, you speak an infinite deal of nothing.", "I like that :)", "Cool", "*In a majestical voice*\nThe meaning of life is not simply to exist, to survive, but to move ahead, to go up, to conquer.", "*“Success is not final, failure is not fatal: it is the courage to continue that counts.”* Winston Churchill", "High tech shoes, low tech feet - Ido PortaL", "Success is not a good orientation, awareness however, that is far more valuable", "*What cannot be changed, must be endured.*" "Don’t let yesterday take up too much of today brother"]
randomResponseChannels = [867597533458202647, 867600399879372820, 867600420246913054, 867601016006770718, 867605832401289247, 868447164999815229, 874471834370850826, 910012458943533057, 887197847240446004]
zacResponses = ["Yes, my man, my king, my owner", "Shut up Zac ok? I'm busy doin stuff", ":heart:", "You da best Zackie", ":rolling_eyes:", "Eh don't mind him guys that's just Zac", "Don't worry about him guys", "How may I be of service fine owner?", "Mate you really gotta fix my coding NOW, there's something that's annoying me in there OK????", "I wuv Gravity Destroyers :star_struck:", "You da man"]
mentionResponses = ["Hello :) I see you've mentioned me, thanks for doing that but I'm not chat bot so I can't really help there", "Hallo", "Me not chatbot sorry :(", "You talkin trash over there brtoha?", ":)", "I'm not chatbot fine sir, however I assure you there are plenty of Gravity Destroyers willing to talk", ":thinking:"]
meanWords = ["stfu", "shut up", "shut the fuck up", "fuck you", "hate you"]

@bot.event
async def on_ready():
    print('Bot is ready!')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Gravity Destroyers"))

@bot.slash_command(guild_ids=[867597533458202644])
async def newyeargoal(ctx,*,goal):
    await ctx.respond(f"Yessir\nYour goal is `{goal}`")
    person = ctx.author
    finalValues = (person, goal)
    sql = "INSERT INTO test_goals_2002 (user, goals) VALUES (%s, %s)"
    mycursor.execute(sql, finalValues)
    mydb.commit()

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
    await ctx.send("SURE mate")
    await asyncio.sleep(5)
    async with ctx.typing():
        await asyncio.sleep(7)
    await ctx.send("```---```\n*Ladies and Gentlemen, skinny and stout,*\n*I’ll tell you a tale I know nothing about*\n*The Admission is free, so pay at the door,*\n*Now pull up a chair and sit on the floor*")
    await asyncio.sleep(5)
    async with ctx.typing():
        await asyncio.sleep(7)
    await ctx.send("*On a bright day in the middle of the night*\n*Two dead boys got up to fight*\n*Back to back they faced eachother*\n*Drew their swords and shot eachother*\n*The deaf policeman heard the noise*\n*And saved the lives of the two dead boys*\n*If you don't believe my story is true*\n*Ask the blind man, he saw it too*")
    await asyncio.sleep(3)
    async with ctx.typing():
        await asyncio.sleep(3)    
    await ctx.send("*Now you've heard the truth in my fable*\n*Have a laugh and cry on the table*")
    await asyncio.sleep(2)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("HAHAHA, did you really think I'd give you an answer?!!")
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("WELL, ||you'd be right|| just after a little wild ride ;) ;)")
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("> I'm the Gravity Destroyers Bot :)\n> I help you guys do your stuff lol\n> I'm usually friendly and sometimes impatient (crazy humans :rolling_eyes:)\n> I'm not a chat bot, I just have clever coding\n> As you would now know, I love pranks <:yeahboi:880034464447754280>")

server = "Gravity Destroyers SW"
@bot.command()
async def testing(ctx):
    for guild in bot.guilds:
        if str(guild) == "Gravity Destroyers SW":
            for role in guild.roles:
                print(role)
                if str(role.name) == "He/Him":
                    print("if was triggered")
                    for member in str(role.members):
                        print(member)
                        # print(member.name)
                        # await ctx.send(member.name)
                    break
                #help me
                        
            

reddit = 867599777743372299

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    meanResponse = False
    if message.channel.id in randomResponseChannels:
        chanceTriggerFunnyTimer = random.randint(1,100)
        if chanceTriggerFunnyTimer == 20 or chanceTriggerFunnyTimer == 21 or chanceTriggerFunnyTimer == 23:
            await message.channel.send(random.choice(randomReminders))

    #print(message)
    if message.author.id == 889042207544340511:
        if message.content == helperResponseB:
            await message.add_reaction("<:agreentick:875244017833639956>")
            # if message.reactions.count == 4:
            #     await message.channel.send(helperResponseC)
    if message.content == "yeah boi":
        await message.channel.send("yeah BOIII")
    if "nice" in message.content.lower():
        chance = random.randint(1, 3)
        if chance == 1:
            emoji = discord.utils.get(bot.emojis, name='GESvibing')
            await message.channel.send(str(emoji))
    for mention in message.mentions:
        if mention.id == 889042207544340511:
            for meanWord in meanWords:
                if meanWord in message.content.lower():
                    await message.reply("NO NO NO and NO\nALSO.... NO")
                    meanResponse=True
            if message.author.id == 760345587802964010 and meanResponse == False:
                await message.channel.send(random.choice(zacResponses))
            elif meanResponse == False:
                await message.channel.send(random.choice(mentionResponses))
    if message.channel.id == reddit and message.author.id != 889042207544340511:
        await message.channel.send("<@&870509092974759946> New reddit post :)")
        

    

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
 

                    
            
# bot.add_command(testing)
bot.add_command(helperping)
bot.add_command(compliment)
bot.add_command(about)
bot.run(token)

# def count(message):
#     for reaction in message.reactions:
#         if reaction.emoji == '✅':
#             return reaction.count
#     return 0