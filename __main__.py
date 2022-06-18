#!/usr/bin/env python3

         ############
        ######by######
        #####dd64#####
         ############ 

import discord, random, os, time, command, event
from discord.ext import commands

        ##### TOKEN #####
with open('TOKEN', 'r') as file:
    Token=file.read()
    file.close()
        #################

dodoBot=commands.Bot(command_prefix='!', description='Bot by dd64')
dodoBot.game=discord.Game(name="Spam :3")
dodoBot.remove_command('help')

        ##### Ready #####
@dodoBot.event
async def on_ready():
    with open('PID','w') as pidFile:
        pidFile.write(f'##### my PID is {os.getpid()} #####') 
        pidFile.close()
    await dodoBot.change_presence(activity=dodoBot.game)
    dodoBot.load_extension('command')
    dodoBot.load_extension('event')
    dodoBot.load_extension('save')
    dodoBot.load_extension('game')
        #################

def isOwner(ctx):
    return ctx.author.id == 229333437641654272

        ###### COG ######

@dodoBot.command()
async def load(ctx, extension):
    if isOwner(ctx):
        try:
            dodoBot.load_extension(extension)
            await ctx.send(f'{extension} loaded')
        except Exception as error:
            await ctx.send(f'{extension} can\'t be loaded. [{error}]')
    else:
        await ctx.send('You are not the owner of this bot')

    
    
@dodoBot.command()
async def unload(ctx, extension):
    if isOwner(ctx):
        try:
            dodoBot.unload_extension(extension)
            await ctx.send(f'{extension} unloaded')
        except Exception as error:
            await ctx.send(f'{extension} can\'t be unloaded. [{error}]')
    else:
        await ctx.send('You are not the owner of this bot')
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