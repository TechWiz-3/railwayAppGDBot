import discord
from discord import Bot
from discord import Emoji
from discord.commands import slash_command, SlashCommandGroup
from discord.commands import Option
from discord.ext import commands
from discord.utils import get
import os
import mysql.connector
from dotenv import load_dotenv
from random import choice
from discord import AllowedMentions
from numpy import full
PROD_GUILD = 867597533458202644
import asyncio

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

print("hi")

class Bump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bump = SlashCommandGroup("bumper", "Bumping commands", guild_ids = [PROD_GUILD])

    # @bump.command(guild_ids=[PROD_GUILD])
    # async def leaderboard(self, ctx):
    #     """Shows bumping leaderboard... maybe"""
    #     mydb.commit()
    #     lb_list = []
    #     final_msg = ""
    #     second_page = ""
    #     full = {}
    #     get_lb = "SELECT userId, points FROM bumping"
    #     mycursor.execute(get_lb)
    #     for entry in mycursor:
    #         user_id, points = entry
    #         lb_list.append(int(points))
    #         for point in lb_list:
    #             full[user_id] = point
    #             #final_msg += f"{member}\t{point}" 
    #     sort_orders = sorted(full.items(), key=lambda x: x[1], reverse=True)
    #     counter = 0
    #     for i in sort_orders:
    #         counter += 1
    #         if counter <=10:
    #             final_msg += f"`{i[1]}`\t<@{i[0]}>\n"
    #         else:
    #             second_page += f"<@{i[0]}>\t`{i[1]}`\n"            
    #     await ctx.respond(f"{final_msg}", allowed_mentions = AllowedMentions.none())
        
    #     def check(self, reaction, user):
    #             return user == ctx.author and str(reaction.emoji) == '➡️'
    #     try:
    #         reaction, user = await self.bot.wait_for(event = 'reaction_add', check=check, timeout=60.0)
    #     except asyncio.TimeoutError:
    #         await ctx.channel.send('👎')
    #     else:
    #         await ctx.channel.send('👍')


    @bump.command()
    async def level(self, ctx):
        """Shows you your bump points"""
        entry_exists = False
        points = 0
        try:
            findIfEntryExists = "SELECT points FROM bumping WHERE userId = %s"
            values = (str(ctx.author.id),)
            mycursor.execute(findIfEntryExists, values)
            for entry in mycursor:
                entry_exists = True
                if entry_exists == True:
                    points, = entry
                else:
                    print("for level command, for loop for bump entry did not run")
            if entry_exists == True:
                await ctx.respond(f"You have `{points}` bumps") # add funny response here
                #await ctx.respond(choice([f"You want me to show you how many bump points you got? no way lmao", "ZERO POINTS", "Error :weary: user not found in database", "You have to bump before checking level... lmao human"]))
            else:
                await ctx.respond("Sorry, can't find your entry")
            
        except Exception as error: 
            print(error)
            await ctx.respond(f"Sorry error occured :(\n{error}")

    @commands.command()
    async def bump_rewards(self, ctx):
        await ctx.send(
            "<@&929992167949209601> 5 bumps\n<@&929992275302432808> 15 bumps\n<@&929992208826892298> 30 bumps\n<@&929992243270537256> 50 bumps\n<@&929992377706369034> 75 bumps\n<@&929992347876479006> 105 bumps\n<@&929992418915405875> 140 bumps",
            allowed_mentions = AllowedMentions.none()
                )

    @bump.command()
    async def rewards(self, ctx):
        """Shows the role rewards for each number of bumps"""
        await ctx.respond(
            "<@&929992167949209601> 5 bumps\n<@&929992275302432808> 15 bumps\n<@&929992208826892298> 30 bumps\n<@&929992243270537256> 50 bumps\n<@&929992377706369034> 75 bumps\n<@&929992347876479006> 105 bumps\n<@&929992418915405875> 140 bumps"
                )

def setup(bot):
    bot.add_cog(Bump(Bot))
