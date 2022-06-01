#!/usr/bin/env python3

         ############
        ######by######
        #####dd64#####
         ############ 

import discord, random, os, time, command, event
from discord.ext import commands

        ##### TOKEN #####
with open('/home/baby-ghost/Bureau/BotDiscord/TOKEN', 'r') as file:
    Token=file.read()
    file.close()
        #################

dodoBot=commands.Bot(command_prefix='!', description='Bot by dd64')
dodoBot.game=discord.Game(name="Spam :3")
dodoBot.remove_command('help')

        ##### Ready #####
@dodoBot.event
async def on_ready():
    with open('/home/baby-ghost/Bureau/BotDiscord/PID','w') as pidFile:
        pidFile.write(f'##### my PID is {os.getpid()} #####')
        pidFile.close()
    await dodoBot.change_presence(activity=dodoBot.game)
        #################




dodoBot.add_cog(command.theCommands(dodoBot))
dodoBot.add_cog(event.theEvent(dodoBot))


dodoBot.run(Token)

