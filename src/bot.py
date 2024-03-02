import requests # these are our modules imported. if the application doesnt open make sure to run setup.bat and install python then add to PATH
from requests import *
import discord
from discord.ext import commands
import colorama
from colorama import *
import ctypes
import os
import time
import datetime
import sys

plus = f"{Fore.MAGENTA}[{Fore.RESET}+{Fore.MAGENTA}]{Fore.RESET} "
tme = (Back.BLACK + Fore.LIGHTMAGENTA_EX + time.strftime("%H:%M:%S ", time.gmtime()) + Back.RESET + Fore.WHITE + Style.BRIGHT)

intents=discord.Intents.all() #turn all of them on for the bot in https://discord.com/developers/applications
nuker = commands.Bot(command_prefix='.', intents=intents) # command prefix is used for the commands of your bot, .nuke .help etc


@nuker.event
async def on_ready():
    print(plus  +  tme + "Logged In As " + Fore.RED + nuker.user.name)


@nuker.command()
async def nuke(ctx): # this command creates the channels
        
       for i in range(50): # the 50 inside the parenthesis/brackets are how many channels are created. please make sure if u do lots then you could get ratelimited!!!
             try:
                  await ctx.guild.create_text_channel(name="Nuked")
             except:
                   pass

           
             

      

nuker.run('YOUR BOT TOKEN HERE') # bot token here