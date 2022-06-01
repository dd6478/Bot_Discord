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

        ###### COG ######
@dodoBot.command()
async def load(ctx, extension):
    try:
        dodoBot.load_extension(extension)
        await ctx.send(f'{extension} loaded')
    except Exception as error:
        await ctx.send(f'{extension} can\'t be loaded. [{error}]')

@dodoBot.command()
async def unload(ctx, extension):
    try:
        dodoBot.unload_extension(extension)
        await ctx.send(f'{extension} unloaded')
    except Exception as error:
        await ctx.send(f'{extension} can\'t be unloaded. [{error}]')
        #################



dodoBot.run(Token)





'''
                             (%.                         
                             ((((((                     
                             ((  . ,(((,                 
                             ((          ((%             
                             ((               ((         
                             ((                    /,    
                             ((                         .
                             ((                          
                             ((                          
                         ,(( ((                          
                     %(((((( ((                          
                .(((/     (( ((                         #
            *((,          (( ((                    (,    
        %(                (( ((               ((         
    (                     (( ((         .((%             
                          (( ((  . /(((,                 
                          (( ((((((                      
                          (( (%                          
                          ((                            
                          ((                            
                          ((                            
    %*                    ((                            
        *((               ((                            
             (((          ((                            
               . %(((. .  ((                            
                     *((((((                            
                          ((                  
'''