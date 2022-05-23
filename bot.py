#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 25 15:31:44 2022

@author: baby-ghost
"""
Token = 'OTY4MTM5OTAwMjc0NzQ5NDUy.Ymagiw.Mc3hrzANeECE030VZy-Wd4afRWM'
import discord
import random
import os
from discord.ext import commands
import time
bot = commands.Bot(command_prefix='!', description='Bot by dd64')
bot.game = discord.Game(name='Spam le plus possible :3')
bot.remove_command('help')

@bot.event
async def on_ready():
    print(f"The bot is ready and the PID is {os.getpid()}")
    with open('PID','w') as PidFile:
        PidFile.write(f'###################\nmy PID is : {os.getpid()}\n###################\n')
        PidFile.close()
    print(str(bot.game))
    await bot.change_presence(activity=bot.game)
    
@bot.command(name='ping')
async def _ping(ctx):
	await ctx.channel.send("pong")
    
@bot.command(name='help')
async def _help(ctx):
    await ctx.channel.send("Il y a 2 commande disponible :\n\t-!PFC\n\t-!flip\n\t-!love\nAmuse toi bien")

@bot.command(name='send')
async def _send(ctx,*,message):
    #await message.add_reaction('\U00002705')
    await ctx.channel.send('Oui maitre!')
    TheChannel=bot.get_channel(784374987729272874)
    await TheChannel.send(message)

@bot.command(name='PFC')
async def _PFC(ctx,*,message='none'):
    pos=["pierre","feuille","ciseaux"]
    myAnswer=random.randint(0, 2)
    if message=='none':
        await ctx.channel.send("Tu na rien mis apres la commande.\nSi tu a besoin d'aide tape !PFC help.")
    elif message=='help':
        await ctx.channel.send("Hey\nTu a 3 possibilité soit pierre soit feuille soit ciseaux.\nExemple : !PFC ciseaux")
        
    elif message.lower()=='ciseaux':
        await ctx.channel.send(f"Moi je dit {pos[myAnswer]}")
        if myAnswer==1:
            await ctx.channel.send("Mince j'ai perdu")
        elif myAnswer==0:
            await ctx.channel.send("YES j'ai gagné")
        else:
            await ctx.channel.send("Bon bas egalité")
            
    elif message.lower()=='feuille':
        await ctx.channel.send(f"Moi je dit {pos[myAnswer]}")
        if myAnswer==0:
            await ctx.channel.send("Mince j'ai perdu")
        elif myAnswer==2:
            await ctx.channel.send("YES j'ai gagné")
        else:
            await ctx.channel.send("Bon bas egalité")
            
    elif message.lower()=='pierre':
        await ctx.channel.send(f"Moi je dit {pos[myAnswer]}")
        if myAnswer==2:
            await ctx.channel.send("Mince j'ai perdu")
        elif myAnswer==1:
            await ctx.channel.send("YES j'ai gagné")
        else:
            await ctx.channel.send("Bon bas egalité")
            
@bot.command(name='love')
async def _love(ctx,*,message):
    if message=='help':
        await ctx.channel.send("Choisie 2 prenom pour determiner leurs taux de love\nExemple : !love dorian martial\n:3")
    try:
        message.split()[2]
    except:
        A=message.split()[0]
        B=message.split()[1]
        if A.lower()=='martial' and B.lower()=='floriane' or B.lower()=='martial' and A.lower()=='floriane' :
            await ctx.channel.send(f"il y a trop de compatibilité entre {A} et {B}")
        else:
            await ctx.channel.send(f"il y a {random.randint(0,100)}% de compatibilité entre {A} et {B}")
            
@bot.command(name='flip')
async def _flip(ctx):
    pos=["Face","Pile"]
    myAnswer=random.randint(0, 1)
    await ctx.channel.send('Ok I flip the coin')
    time.sleep(2)
    await ctx.channel.send('WOW elle est longue a retomber ...')
    time.sleep(1)
    await ctx.channel.send('AH! elle arrive')
    time.sleep(1)
    await ctx.channel.send(f"Hop je l'ai récup\nelle est tomber sur {pos[myAnswer]}")
            
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    print(message.author)
    if str(message.author) == "dodo's BOT#2997":
        pass
    else:
        List=message.content.lower().split()
        if message.content.lower()=="je t'aime petit bot":
            await message.reply(f"moi aussi petit.e {message.author} :heart:")
            await message.add_reaction('\u2764\uFE0F')
            await message.add_reaction('\U0001F449')
            await message.add_reaction('\U0001F448')
            await message.add_reaction('\U0001F49D')
        elif 'martial' in List:
            await message.channel.send('Laisse martial trankil il ne ta rien demander !\nEn plus il est a moi :3 (et a floriane)')
        elif 'quoi' in List or 'quoi?' in List:
            if random.randint(0,100)<=30:
                await message.reply("FEUR lol")
        elif "dm" in List:
            await message.author.send("Alors comme sa tu veux des message dans t'es DM ;)")
        elif message.content.lower()[0:3]=='mia':
            await message.channel.send('Miaaaaa \nhttps://tenor.com/view/kawaii-cute-peach-cat-gif-23743858')
        
'''
@bot.event
async def on_reaction_add(reaction, user):
    print("ok")
    await reaction.remove(user)
'''  
    
@bot.event
async def on_message_edit(before,after):
    if str(before.author) == "dodo's BOT#2997":
        print("lol c moi")
    else:
        await after.channel.send(f'''Notre petit {after.author} a modifier son message :scream:
        Ancien message ==> {before.content.lower()} <==Ancien message''')
    


bot.run(Token)
