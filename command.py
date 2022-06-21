

         ############
        ######by######
        #####dd64#####
         ############ 

import discord, random, asyncio
from discord.ext import commands
import requests

def setup(bot):
    bot.add_cog(theCommands(bot))

class theCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def help(self, ctx):
        await ctx.channel.send('''
**Commands** :        
    **\*help** : show this message lol
    **\*flip** : flip a coin
    **\*love** : show the love between 2 people :3 (use *\*love help* for more information)
    **\*mercimek** : for say thanks to a person 
    **\*cat or \*dog** : show a random picture of a cat or dog

**GAME** :
    **\*pendu** : play a game of pendu
    **\*pfc** : it's Rock-Paper-Scissors game (use *\*pfc help* for more information)

***Save file***
    **\*create** : create a new save file
    **\*add** : add a new saveLine in file
    **\*delete** : delete a saveLine in file
    **\*take** : take a saveLine in file
    **\*list** : list all saveLine in file
                               ''')


    @commands.command()
    async def flip(self, ctx):
        pos=["Face","Pile"]
        myAnswer=random.randint(0, 1)
        await ctx.channel.send('Ok I flip the coin')
        await asyncio.sleep(2)
        await ctx.channel.send('WOW elle est longue a retomber ...')
        await asyncio.sleep(1)
        await ctx.channel.send('AH* elle arrive')
        await asyncio.sleep(1)
        await ctx.channel.send(f"Hop je l'ai récup\nelle est tomber sur {pos[myAnswer]}")
    
    @commands.command()
    async def mercimek(self, ctx):
        try :
            await ctx.message.delete()
        except:
            pass
        await ctx.channel.send("https://cdn.discordapp.com/attachments/766684889104777266/981983304729378897/front_fr.10.full.jpg")
        
    @commands.command()
    async def hehehehaw(self, ctx):
        try:
            ctx.message.delete()
        except:
            pass
        await ctx.send("https://tenor.com/view/clash-royale-clash-royale-emote-gif-23858585")

    @commands.command()
    async def love(self,ctx,*,message):
        if message=='help':
            await ctx.channel.send("Choisie 2 prenom pour determiner leurs taux de love\nExemple : *love dorian martial\n:3")
        try:
            message.split()[2]
        except:
            A=message.split()[0]
            B=message.split()[1]
            if A.lower()=='martial' and B.lower()=='floriane' or B.lower()=='martial' and A.lower()=='floriane' :
                await ctx.channel.send(f"il y a trop de compatibilité entre {A} et {B}")
            else:
                await ctx.channel.send(f"il y a {random.randint(0,100)}% de compatibilité entre {A} et {B}")

    @commands.command()
    async def cat(self,ctx):
        #api for a randome cat
        try:
            url = 'https://aws.random.cat/meow'
            r = requests.get(url)   
            data = r.json()
            await ctx.channel.send(data['file'])
        except:
            await ctx.channel.send("Une erreur est survenue")
        
    @commands.command()
    async def dog(self,ctx):
        try:
            url = 'https://random.dog/woof.json'
            r = requests.get(url)
            data = r.json()
            await ctx.channel.send(data['url'])
        except:
            await ctx.channel.send("Une erreur est survenue")


'''
@bot.command(name='send')
async def _send(ctx,*,message):
    #await message.add_reaction('\U00002705')
    await ctx.channel.send('Oui maitre!')
    TheChannel=bot.get_channel(784374987729272874)
    await TheChannel.send(message)
'''


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