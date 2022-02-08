# make bumping reward system
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
from discord import AllowedMentions

load_dotenv()
token = os.getenv("token")
password = os.getenv("password")

mydb = mysql.connector.connect(
  host="containers-us-west-23.railway.app",
  user="root",
  password=password, # sus person, why are you reading this line??
  database="railway",
  port="6499"
)
mycursor = mydb.cursor()

# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣶⣿⣿⣷⣶⣄⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣾⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⢀⣾⣿⣿⡟⠁⣰⣿⣿⣿⡿⠿⠻⠿⣿⣿⣿⣿⣧⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠏⠀⣴⣿⣿⣿⠉⠀⠀⠀⠀⠀⠈⢻⣿⣿⣇⠀⠀⠀
# ⠀⠀⠀⠀⢀⣠⣼⣿⣿⡏⠀⢠⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠈⣿⣿⣿⡀⠀⠀
# ⠀⠀⠀⣰⣿⣿⣿⣿⣿⡇⠀⢸⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡇⠀⠀
# ⠀⠀⢰⣿⣿⡿⣿⣿⣿⡇⠀⠘⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⢀⣸⣿⣿⣿⠁⠀⠀
# ⠀⠀⣿⣿⣿⠁⣿⣿⣿⡇⠀⠀⠻⣿⣿⣿⣷⣶⣶⣶⣶⣶⣿⣿⣿⣿⠃⠀⠀⠀
# ⠀⢰⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀
# ⠀⢸⣿⣿⡇⠀⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠉⠛⠛⠛⠉⢉⣿⣿⠀⠀⠀⠀⠀⠀
# ⠀⢸⣿⣿⣇⠀⣿⣿⣿⠀s⠀⠀ ⢀u⣤⣤⡀ s⢸⣿⣿⣿⣷⣦⠀⠀⠀
# ⠀⠀⢻⣿⣿⣶⣿⣿⣿⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣦⡀⠀⠉⠉⠻⣿⣿⡇⠀⠀
# ⠀⠀⠀⠛⠿⣿⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⠈⠹⣿⣿⣇⣀⠀⣠⣾⣿⣿⡇⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣦⣤⣤⣤⣤⣾⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⣿⣿⣿⣿⣿⠿⠋⠉⠛⠋⠉⠉⠁⠀⠀⠀⠀
# ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠁

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=".", intents = intents)

@bot.slash_command(guild_ids=[867597533458202644])  # create a slash command for the supplied guilds
async def hello(ctx):
    """Say hello to the bot"""  # the command description can be supplied as the docstring
    decide = random.randint(1,4)
    if decide == 1:
        await ctx.respond(f"HEY BOI {ctx.author}!")
    elif decide == 2:
        await ctx.respond(f"Hellooo {ctx.author}!")
    elif decide == 3:
        await ctx.respond(f"**PING** {ctx.author}!")
    else:
        await ctx.respond(f"Sup cali boii :)) {ctx.author}")

helperResponseA = ["Alright, Gravity Destroyers, sending help for you now", "Help? Someone needs help? Right away bois.", "I was sleeping, did you have to wake me up with this help request? Send help now.", "Help? Only God can help you!!", "Aww, you need help fam. Dw I'm here for you", "Help request that's noice", "HELP??? SURE MATE", "K alerting the martian embassy help is required"]
helperResponseB = "**Help request**\n> Please react with <:agreentick:875244017833639956> below this message to enable this ping request, 3 votes excluding me are required unless a moderator approves the request."
helperResponseC = ["Alrightyyyy, we have authorisation to continue", "Nice bruh, stars have aligned, helper ping APPROVED", "Helper ping incoming", "Martian embassy has responded, we're gonna ping the helpers"]
helperResponseD = ["Mighty moderators have bypassed the regular authorisation and progressed this help request at the quantum leap speed", "Ohh nice, mods approved this help request.", "Kids, we got mod chads helpin us out", "Mods have approved this help request, now I'm heading back to bed"]
randomReminders = ["**Community service reminder**\nStop looking at the screen with a dry throat you lazy people :rolling_eyes:", "Stop fidgetting mate, it's annoying", "Right right", "k", "Stop sitting on the computer while you need to go to the bathroom, you know better", "thonking...", "Mind rephrasing that from crazy to english??", "you da man ay", "Public service announcement, SIT PROPERLY PEOPLE\nYall look like monkeys in front of that screen brah", "aww", "You done your workout yet today brah? No time like the present", "Mate seriously I love your enthusiasm but you really need a haircut", "you done your workout toda- oh I see you have looking fire💯", "Be not afraid of greatness. Some are born great, some achieve greatness, and others have greatness thrust upon them.", "All the world's a stage,\nAnd all the men and women merely players;\nThey have their exits and their entrances;\nAnd one man in his time plays many parts,\nHis acts being seven ages.", "Fine sir, you speak an infinite deal of nothing.", "I like that :)", "Cool", "*In a majestical voice*\nThe meaning of life is not simply to exist, to survive, but to move ahead, to go up, to conquer.", "*“Success is not final, failure is not fatal: it is the courage to continue that counts.”* Winston Churchill", "High tech shoes, low tech feet - Ido PortaL", "Success is not a good orientation, awareness however, that is far more valuable", "*What cannot be changed, must be endured.*", "Don’t let yesterday take up too much of today brother", "*“Live in the present, remember the past, and fear not the future, for it doesn’t exist and never shall. There is only now.”*", "Yea fs", ":)", "Das cool tho", "Hmm I like it, what else?", "Wow you stronk", "xD",  "All the best G", "Does this dude always talk like that? :sweat_smile:", "Ah, I see now", "Cool", "huh?\noh got it now, go ahead", "Hmm, not convinced of that fine sir"]
randomResponseChannels = [867597533458202647, 867600399879372820, 867600420246913054, 867601016006770718, 867605832401289247, 868447164999815229, 874471834370850826, 910012458943533057, 887197847240446004]
zacResponses = ["Yes, my man, my king, my owner", "Shut up Zac ok? I'm busy doin stuff", ":heart:", "You da best Zackie", ":rolling_eyes:", "Eh don't mind him guys that's just Zac", "Don't worry about him guys", "How may I be of service fine owner?", "Mate you really gotta fix my coding NOW, there's something that's annoying me in there OK????", "I wuv Gravity Destroyers :star_struck:", "You da man"]
mentionResponses = ["Hello :) I see you've mentioned me, thanks for doing that but I'm not chat bot so I can't really help there", "Hallo", "Me not chatbot sorry :(", "You talkin trash over there brotha?", ":)", "I'm not a chatbot fine sir, however I assure you there are plenty of Gravity Destroyers willing to talk", ":thinking:", "https://cdn.discordapp.com/emojis/802845187088973834.webp?size=240&quality=lossless", "PING", "bruh...", "wow, ok", "long time no see :blush:", "man i told you to stop pinging me", "https://cdn.discordapp.com/emojis/802845187088973834.webp?size=240&quality=lossless", "STOP PINGING ME OR ELSE", "<3", "hehe", "...", "kk", "xD np man", "oh anytimme", "yes yes yes", "meh", "huh, ohh wait", "bruh...", ":joy:", "wow this dude doesn't stop doea he"]
meanWords = ["stfu", "shut up", "shut the fuck up", "fuck you", "hate you", "shut your", "shush", "shsh", "piss off", "buzz off", "shutup"]
rowanMotivation = ["https://www.youtube.com/watch?v=T2zLJW9l-Qw&", "DISCIPLINE, INTERNAL MOTIVATION > external motivation", "HUH? YOU WANT MOTIVATION???\nIt's simple mate, you want to get somewhere? What do you need to do to get there? Now do it.", "**You wanna workout? How about, just do it. Or maybe rethink your training if you're not enjoying it**", "Ay you want motivation, how about thinking about what you want, why you want it and then it'll be easy to go and do what you need to do.\nJust remember, we're here for you :blush:", "It's in you man, I know it is, you just gotta push yourself a little and you'll get it", "*Ay gut naw excooses*\nJust go for it brah", "*I'm tired today, idk if i want to teach at the school today :weary:*\nI think you agree that sounds pretty lame. It's ok to feel tired but it isn't ok to give up. Lets go now man", "SHUT UP AND WORKOUT", ":rolling_eyes: you have everything you need internally **SCHOOL ADJOURNED**", "Not sayin your lazy but... my magic 8ball like intuition says you can use this https://www.youtube.com/watch?v=lj5SzG4XHJo", "Unkown source, wait huh? https://cdn.discordapp.com/attachments/926312175943962674/927406438886801529/v09044g40000c7937ijc77ub2at7lpmg.mp4", "https://pbs.twimg.com/media/BmIY5ptIMAAjRWE.jpg", "**Rise Above**\nhttps://www.youtube.com/watch?v=8VGI7PX8mic", "**Your Call to Workout**\nhttps://www.youtube.com/watch?v=LFWBYqe-GiA", "https://i.imgur.com/OPdGqUy.png", "https://cdn.discordapp.com/attachments/926312175943962674/932831810717626448/v09044g40000c7ed5vjc77u7187vb7l0.mp4", "https://cdn.discordapp.com/attachments/925106780831350784/936863287860142130/encouraging-quotes10-1607057437.jpg", "https://media.discordapp.net/attachments/789069071718678548/812031951505588234/image0.jpg?width=430&height=430"]
onCoolDownResponse = ["Why yall so impatient huh", "Hey matey, command on cooldown, sowwy", ":moyai:", "Patience human, patience", "Patience is a virtue :moyai:", ":rolling_eyes: :rolling_eyes:", "Your impatience is enough to outlast empires", "*Dear human the impatience of your deeds make leopards slow as snails*"]
reminderFunnyResponse = ["Forever more ", "Man something is really bothering me, *why do they call it rush hour... when NOBODY MOVES???", "Always my brother, my captain, my king", "Hehe alright, no guarantees tho", "Monica just invited me to her birthday party, did you HAVE to ask me to do this now????\n*sighs*\nConsider it done", "Yessir", "What sort of a reminder is that, huh", ":D", "*mischevious grin* Well, we'll see about *that* one"]
whatsUpResponse = ["Umm. The sky?", "What's up? THE SKY MATE", "The sky :), or in your case the roof", "Da roof", "The roof is up, but if you mean how am I, I've very well thanks how are you?"]
caribbean_response = ["https://www.youtube.com/watch?v=6zTc2hD2npA", "https://caribbeanpot.com", "Yeah I'll have some of that free fruit thx :))", "DOES THE SUN EVER GO DOWN THERE???"]
british_response = ["ALL HE DOES IS TALK ABOUT THE WEATHER", "Tea, tea, tea, WHAT ABOUT COFFEE?"]
russian_response = ["wwwwaht? im outta here boi", "russian?? RUN\n||vietnam flashbacks||", "https://tenor.com/view/putin-dance-gif-9909272"]
canadian_response = ["I hope he's in the maple syrup cartel *hopeful face*", "Is she always this polite?", "oh one of *those* i get it"]
random_vid = ["https://www.youtube.com/watch?v=Cm15bg1LlAI", "https://www.youtube.com/watch?v=N_7A4Z2zubQ", "https://www.youtube.com/watch?v=WULYEegtTGc", "https://www.youtube.com/watch?v=X3BJYAOIcrM", "https://www.youtube.com/watch?v=4705RoBc21M", "https://www.youtube.com/watch?v=8EEP_pQySEc", "https://tenor.com/view/flavortown-monkey-review-dose-monki-monke-gif-21419037", "https://www.youtube.com/watch?v=JgGfj2r024I", "https://www.youtube.com/watch?v=t_YyrMV7SuE", "https://www.youtube.com/watch?v=PeT2gEj84d4", "https://www.youtube.com/watch?v=YQHE2lT5RP8", "https://www.youtube.com/watch?v=3Lyex2tSUyA", "https://www.youtube.com/watch?v=CIMmK86vNYo", "https://www.youtube.com/watch?v=GyRIk99toRE", "https://www.youtube.com/watch?v=YdydNoqbBmI", "https://www.youtube.com/watch?v=Db9_xsDr5PM", "https://www.youtube.com/watch?v=srD4Rxm2IK0&", "https://www.youtube.com/watch?v=Cxqca4RQd_M", "https://www.youtube.com/watch?v=l7K3y4EPq10", "https://www.youtube.com/watch?v=ahvrHrPGi1k", "https://www.youtube.com/watch?v=5j9mY95zjUc", "https://www.youtube.com/watch?v=t_YyrMV7SuE", "https://www.youtube.com/watch?v=W0_Tt0En7v4", "https://www.youtube.com/watch?v=ReHdQsB5rI8", "https://www.youtube.com/watch?v=-vZXgApsPCQ", "https://www.youtube.com/watch?v=d-0vbvy2ip4", "**Warning: inappropriate language, do not watch if underage:**\nhttps://www.youtube.com/watch?v=8TtXhpd9yAg", "https://www.youtube.com/watch?v=BLB2Mrvh44A", "https://www.youtube.com/watch?v=zkFZWqB4zic", "https://www.youtube.com/watch?v=CFdZWgiAj8I", "https://www.youtube.com/watch?v=NTjjrymeavU", "https://www.youtube.com/watch?v=iwZkHC9KNGM", "https://www.youtube.com/watch?v=YU8aai27vk0", "https://www.youtube.com/watch?v=gXbNoqYNDXM", "https://www.youtube.com/watch?v=QsUYXjcV5h0", "https://www.youtube.com/watch?v=Qw556WICRS4", "https://www.youtube.com/watch?v=0WqO8PHQpEo", "https://www.youtube.com/watch?v=a5xGxkg07FQ", "https://www.youtube.com/watch?v=HFMSGMPrMHY", "https://www.youtube.com/watch?v=eqq5gmHFe5k&", "https://www.youtube.com/watch?v=q9ijfnlF_24", "https://www.youtube.com/watch?v=wCS2x3NtAjA", "https://www.youtube.com/watch?v=OElX_Ta7dpg"]
funny_about_me = ["Global warming hoax? Call that ice CAP"]
random_yt_vid_msg = ["Here ya go mate", "Boredom DESTROYED", "I never said it would be good but here:", "Here it is", "Well well well, if it isn't another bored human", "Bored human incoming", "Have a laff", "Oh i hate this one man \*vomitting face\*", "lmao", "Sure", "Alr, no guarantees tho", "Imma bet this gonna be a Kitty Flanagan vid\nOh HAHAHA"]
bumper_message = ["Ayo bro, thanks a lot for bumping <3", "I like it :)", "Thanks for bumping mate", "Oh YEAH, thanks for bumping", "Bumping hero is BACK", "<3", "Bump bump bump, I wonder 'how is trump?'", "Tysm for the bump man", "I gave that a thump, he gave it a bump, thank you very much, now may I ask, are you Dutch?", "Shut up Grumpbot, why don't you thank the bumper for once", ":)))", "That's the wayyy, thanks :grin:", ":grin:", "ooo yeaaa boiii", "Bump to the top and never stop, ty sir", ":laughing: :pray:", "ty ty man"]


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
    await ctx.send("SURE mate")
    await asyncio.sleep(5)
    async with ctx.typing():
        await asyncio.sleep(7)
    await ctx.send("```---```\n*Ladies and Gentlemen, skinny and stout,*\n*I’ll tell you a tale I know nothing about*\n*The Admission is free, so pay at the door,*\n*Now pull up a chair and sit on the floor*", delete_after = 25)
    await asyncio.sleep(5)
    async with ctx.typing():
        await asyncio.sleep(7)
    await ctx.send("*On a bright day in the middle of the night*\n*Two dead boys got up to fight*\n*Back to back they faced eachother*\n*Drew their swords and shot eachother*\n*The deaf policeman heard the noise*\n*And saved the lives of the two dead boys*\n*If you don't believe my story is true*\n*Ask the blind man, he saw it too*", delete_after = 20)
    await asyncio.sleep(3)
    async with ctx.typing():
        await asyncio.sleep(3)    
    await ctx.send("*Now you've heard the truth in my fable*\n*Have a laugh and cry on the table*", delete_after = 14)
    await asyncio.sleep(2)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("HAHAHA, did you really think I'd give you an answer?!!", delete_after = 12)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("WELL, ||you'd be right|| just after a little wild ride ;) ;)", delete_after = 10)
    async with ctx.typing():
        await asyncio.sleep(5)
    await ctx.send("> I'm the Gravity Destroyers Bot :)\n> I help you guys do your stuff lol\n> I'm usually friendly and sometimes impatient (crazy humans :rolling_eyes:)\n> I'm not a chat bot, I just have clever coding\n> As you would now know, I love pranks <:yeahboi:880034464447754280>")

                        
@bot.command()
@commands.cooldown(1,60,commands.BucketType.user)
async def motivation(ctx):
    async with ctx.typing():
        await asyncio.sleep(3)
    await ctx.send(content = "Welcome to Rowan's School of Motivation\nhttps://thumbs.gfycat.com/ZestyPowerlessDaddylonglegs-size_restricted.gif", delete_after=5)
    async with ctx.typing():
        await asyncio.sleep(3)
    await ctx.send(random.choice(rowanMotivation))

@bot.command()
async def bump_rewards(ctx):
    await ctx.send(
        "<@&929992167949209601> 5 bumps\n<@&929992275302432808> 15 bumps\n<@&929992208826892298> 30 bumps\n<@&929992243270537256> 50 bumps\n<@&929992377706369034> 75 bumps\n<@&929992347876479006> 105 bumps\n<@&929992418915405875> 140 bumps",
        allowed_mentions=AllowedMentions.none()
            )

@bot.slash_command(guild_ids=[867597533458202644])
async def bumping_rewards(ctx):
    """Shows the role rewards for each number of bumps"""
    await ctx.respond(
        "<@&929992167949209601> 5 bumps\n<@&929992275302432808> 15 bumps\n<@&929992208826892298> 30 bumps\n<@&929992243270537256> 50 bumps\n<@&929992377706369034> 75 bumps\n<@&929992347876479006> 105 bumps\n<@&929992418915405875> 140 bumps"
            )
@bot.command()
@commands.cooldown(1,60,commands.BucketType.user)
async def motivation_quote(ctx):
    async with ctx.typing():
        await asyncio.sleep(3)
        raw_quote = requests.get('https://zenquotes.io/?api=random&key=2b03ca0a25fce4fcb2bc9a77d7302d3a11263a23')
        quote_content = raw_quote.content
        loaded_quote = json.loads(quote_content)
        unlisted_quote = loaded_quote[0]
        finished_quote = unlisted_quote["q"]
        await ctx.send(f"{finished_quote}")

@bot.slash_command(guild_ids=[867597533458202644])
async def motivational_quote(ctx):
    """Hits you with some great motivational quotes"""
    raw_quote = requests.get('https://zenquotes.io/?api=random&key=2b03ca0a25fce4fcb2bc9a77d7302d3a11263a23')
    quote_content = raw_quote.content
    loaded_quote = json.loads(quote_content)
    unlisted_quote = loaded_quote[0]
    finished_quote = unlisted_quote["q"]
    await ctx.respond(f"{finished_quote}")

@bot.slash_command(guild_ids=[867597533458202644])
async def random_words(ctx):
    """Gives your bored self 10 random words"""
    finalWords = ""
    raw_get = requests.get('https://random-word-api.herokuapp.com/word?number=10')
    word_content = raw_get.content
    loaded_words = json.loads(word_content)
    for word in loaded_words:
        finalWords = finalWords + word + " "
    await ctx.respond(f"{finalWords.capitalize()}")

@bot.slash_command(guild_ids=[867597533458202644])
async def landscape_picture(ctx):
    pass


#create remindme command

@bot.command()
async def random_yt(ctx):
    await ctx.send(f"{random.choice(random_yt_vid_msg)}\n{random.choice(random_vid)}")

@bot.slash_command(guild_ids=[867597533458202644])
async def random_yt_vid(ctx):
    """Provides a random yt vid from a list for your enjoyment"""
    await ctx.respond(f"{random.choice(random_yt_vid_msg)}\n{random.choice(random_vid)}")

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        errorMsg = '**Still on cooldown, please try again in {:.2f}s**'.format(error.retry_after)
        rowanMsg = random.choice(onCoolDownResponse)
        async with ctx.typing():
            await asyncio.sleep(3)
        await ctx.send(f'{errorMsg}\n{rowanMsg}')

reddit = 867599777743372299

@bot.event
async def on_message(message):
    if message.author.id != 889042207544340511:
        await bot.process_commands(message)
        meanResponse = False
        if message.channel.id in randomResponseChannels:
            chanceTriggerFunnyTimer = random.randint(1,100)
            if chanceTriggerFunnyTimer == 20:
                # async with message.channel.typing():
                #     await asyncio.sleep(3)
                await message.channel.send(random.choice(randomReminders))
        if message.author.id == 931377734821773413:
            if message.content == ":flushed:":
                await message.channel.send("So um how are you today Adrienne?")
        if "Thank you for bumping our Server! If you haven't already, please go to" in message.content and message.author.id == 735147814878969968:
            bumper = message.mentions
            bumperId = ""
            bumperName = ""
            entryExists = False
            numberOfPoints = 1
            for user in bumper:
                bumperId = user.id
                bumperName = user.name
            findIfEntryExists = "SELECT points FROM bumping WHERE userId = %s"
            values = (bumperId,)
            mycursor.execute(findIfEntryExists, values)
            for entry in mycursor:
                print("true triggered")
                entryExists = True
                numberOfPoints, = entry
            if entryExists == False:
                insertBump = "INSERT INTO bumping (userId, username, points) VALUES (%s, %s, %s)"
                values = (bumperId, bumperName, 1)
                mycursor.execute(insertBump, values)
                mydb.commit()
                await message.channel.send(f"Ayo bro, thanks a lot for bumping <3 you now have 1 point\nRn this is a feature in the works, more soon hopefully :)")
            elif entryExists == True:
                newPoints = int(numberOfPoints) + 1
                updateNumberOfPoints = "UPDATE bumping SET points = %s WHERE userId = %s"
                values = (newPoints, bumperId)
                mycursor.execute(updateNumberOfPoints, values)
                mydb.commit()
                server = bot.get_guild(867597533458202644)
                bumper_object = server.get_member(int(bumperId))
                if newPoints == 5:
                    await bumper_object.add_roles(discord.Object(929992167949209601))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n:trophy: You've also earned the <@&929992167949209601> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 15:
                    await bumper_object.add_roles(discord.Object(929992275302432808))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992275302432808> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 30:
                    await bumper_object.add_roles(discord.Object(929992208826892298))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992208826892298> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 50: #50
                    await bumper_object.add_roles(discord.Object(929992243270537256))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992243270537256> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 75:
                    await bumper_object.add_roles(discord.Object(929992377706369034))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992377706369034> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 105:
                    await bumper_object.add_roles(discord.Object(929992347876479006))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992347876479006> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                elif newPoints == 140:
                    await bumper_object.add_roles(discord.Object(929992418915405875))
                    await message.channel.send(
                        f"Ayo bro, thanks a lot for bumping <3 you now have {newPoints} points\n\n:trophy: You've also earned the <@&929992418915405875> role :)",
                        allowed_mentions = AllowedMentions.none()
                            )
                else:
                    await message.channel.send(
                        f"{random.choice(bumper_message)}\nYou now have {newPoints} points\n`.bump_rewards` `/bumping_rewards`",
                        allowed_mentions = AllowedMentions.none()
                            )

        # if "wrist" in message.content.lower() and ("pain", "injury") in message.content.lower():
        #     await message.channel.send(
        #         'https://cdn.discordapp.com/attachments/867599113825812481/927822953868046336/sign.png'
        #             )
                # if message.reactions.count == 4:
                #     await message.channel.send(helperResponseC)
        if message.content == "yeah boi":
            await message.channel.send("yeah BOIII")
        # if ("sup", "wassup", "whats up", "what's up") in message.content.lower():
        #     await message.channel.send(random.choice(whatsUpResponse))
        if "legs" in message.content.lower() and message.author.id != 889042207544340511:
            number = random.randint(1,5)
            if number == 1:
                await message.channel.send("`l e g s` ??? Did someone say legs?")
            elif number == 2:
                await message.channel.send("Oof xD")
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
    elif message.author.id == 889042207544340511:
        if message.content == helperResponseB:
            await message.add_reaction("<:agreentick:875244017833639956>")



@bot.event
async def on_reaction_add(reaction, user):
    print(reaction.emoji, user.name)
    #create if statement to ensure it isn't a bot
    if reaction.emoji == "🍆" or reaction.emoji == "🍑":
        await reaction.message.channel.send(f"{str(user.mention)} naughty boi, you trying to post bad emojis")
        await reaction.clear()
        try:
            await reaction.message.add_reaction("❤️")
        except:
            pass
        if user.id == 728541505123516447:
            banthonk = discord.utils.get(bot.emojis, name='banthonk')
            await reaction.message.channel.send(f"<@760345587802964010> BB seems like he wants the banner hammer {banthonk}")
    else:
        emoji = reaction.emoji
        #await reaction.message.add_reaction(str(emoji))
        if reaction.message.author.id == 889042207544340511 and reaction.message.content == helperResponseB:

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
bot.run(token)