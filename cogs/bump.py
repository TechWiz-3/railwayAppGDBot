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
PROD_GUILD = 867597533458202644

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

class Bump(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    bump = SlashCommandGroup("bumper", "Bumping commands", guild_ids = [PROD_GUILD])

    @bump.command(guild_ids=[PROD_GUILD])
    async def leaderboard(self, ctx):
        await ctx.respond("Right now, local genius Zac the Wise can't figure out a way to sort database entries into a proper leaderboard so for now, the leaderboard is not available")

    @bump.command()
    async def level(self, ctx):
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
            else:
                await ctx.respond("Sorry, can't find your entry")
            
        except Exception as error: 
            print(error)
            await ctx.respond(f"Sorry error occured :(\n{error}")


def setup(bot):
    bot.add_cog(Bump(Bot))
