

         ############
        ######by######
        #####dd64#####
         ############ 

import discord, time, random
from discord.ext import commands

class theCommands(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def flip(self, ctx):
        pos=["Face","Pile"]
        myAnswer=random.randint(0, 1)
        await ctx.channel.send('Ok I flip the coin')
        time.sleep(2)
        await ctx.channel.send('WOW elle est longue a retomber ...')
        time.sleep(1)
        await ctx.channel.send('AH! elle arrive')
        time.sleep(1)
        await ctx.channel.send(f"Hop je l'ai récup\nelle est tomber sur {pos[myAnswer]}")