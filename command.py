

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
    async def _help(ctx):
        await ctx.channel.send("Il y a 3 commande disponible :\n\t-!PFC\n\t-!flip\n\t-!love\nAmuse toi bien")


    @commands.command()
    async def flip(self, ctx):
        pos=["Face","Pile"]
        myAnswer=random.randint(0, 1)
        await ctx.channel.send('Ok I flip the coin')
        await asyncio.sleep(2)
        await ctx.channel.send('WOW elle est longue a retomber ...')
        await asyncio.sleep(1)
        await ctx.channel.send('AH! elle arrive')
        await asyncio.sleep(1)
        await ctx.channel.send(f"Hop je l'ai récup\nelle est tomber sur {pos[myAnswer]}")


    @commands.command()
    async def PFC(self, ctx,*,message='none'):
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

    @commands.command()
    async def love(self,ctx,*,message):
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

    @commands.command()
    async def cat(self,ctx):
        try:
            url = 'https://aws.random.cat/meow'
            r = requests.get(url)
            data = r.json()
            print(f'###### {data["file"]} ######')
            await ctx.channel.send(data['file'])
        except:
            await ctx.channel.send("Une erreur est survenue")
        
    @commands.command()
    async def dog(self,ctx):
        try:
            url = 'https://random.dog/woof.json'
            r = requests.get(url)
            data = r.json()
            print(f'###### {data["url"]} ######')
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