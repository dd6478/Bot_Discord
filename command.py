

         ############
        ######by######
        #####dd64#####
         ############ 

from calendar import c
from email import message
from fnmatch import translate
from pydoc import describe
import discord, random, asyncio
from discord.ext import commands
import requests, deepl

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
    **\*trad** : translate a word or a sentence
    **\*flip** : flip a coin
    **\*love** : show the love between 2 people :3 (use *\*love help* for more information)
    **\*mercimek** : for say thanks to a person 
    **\*hehehehaw** : hehehehaw
    **\*cat , \*dog or \*rabbit** : show a random picture of a cat, dog or rabbit  

**GAME** :
    **\*pendu** : play a game of pendu
    **\*pfc** : it's Rock-Paper-Scissors game (use *\*pfc help* for more information)
    **\*bataille** : play to the battleship game (for 2 players)

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
        await ctx.channel.send('Ok je lance la piece !!')
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
        #embed = discord.Embed(title="Dog", description="Here is a random dog", color=0x06F7E9)
        try:
            url = 'https://random.dog/woof.json'
            r = requests.get(url)
            data = r.json()
        #    embed.set_image(url=data['url'])
            await ctx.send(data['url'])
        except:
            await ctx.channel.send("Une erreur est survenue")
            
    @commands.command()
    async def rabbit(self,ctx):
        embed = discord.Embed(title="Rabbit", description='Here is a random rabbit', color=0x00ff00) #creates embed
        file = discord.File(f'rabbit/rabbit-{random.randint(1,69)}', filename="image.png")
        embed.set_image(url="attachment://image.png")
        await ctx.send(file=file, embed=embed)

    @commands.command()
    async def trad(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        def checkEmoji(reaction, user):
            return ctx.message.author == user and message.id == reaction.message.id and (str(reaction.emoji) == "🇫🇷" or str(reaction.emoji) == "🇬🇧" or str(reaction.emoji) == "🇺🇸" or str(reaction.emoji) == "🇪🇸" or str(reaction.emoji) == "🇯🇵" or str(reaction.emoji) == "🇷🇺" )
        
        with open('DeeplAPI', 'r') as file:
            auth_key = file.read().strip()
            file.close()
        Deepl = deepl.Translator(auth_key)
        await ctx.send("Veuillez entrer votre texte et cliqué sur la langue désirée")
        try:
            message = await self.bot.wait_for('message', check=check, timeout=60)
            await message.add_reaction('🇫🇷')
            await message.add_reaction('🇺🇸')
            await message.add_reaction('🇬🇧')
            await message.add_reaction('🇪🇸')
            await message.add_reaction('🇯🇵')
            await message.add_reaction('🇷🇺')
            await asyncio.sleep(0.5)
            reaction, user = await self.bot.wait_for('reaction_add', timeout=60, check=checkEmoji)
        except:
            await ctx.send("**ERROR** : Timeout")
        else:
            if reaction.emoji == "🇫🇷":
                language = 'FR'
            elif str(reaction.emoji) == "🇺🇸":
                language = 'EN-US'
            elif str(reaction.emoji) == "🇬🇧":
                language = 'EN-GB'
            elif str(reaction.emoji) == "🇪🇸":
                language = 'ES'
            elif str(reaction.emoji) == "🇯🇵":
                language = 'JA'
            elif str(reaction.emoji) == "🇷🇺":
                language = 'RU'
            else:
                print(reaction.emoji)
            trad = Deepl.translate_text(message.content, target_lang=language)
            await ctx.send(f'Langue de depart : {trad.detected_source_lang}\nLangue désirée : {language}\n\n{trad.text}')
            

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