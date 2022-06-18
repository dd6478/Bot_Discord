         ############
        ######by######
        #####dd64#####
         ############ 

import discord
from discord.ext import commands
from pathlib import Path
from wakeonlan import send_magic_packet


def setup(bot):
    bot.add_cog(wakeBot(bot))

class wakeBot(commands.Cog):
    def __init__(self,bot):
        self.bot=bot
    
    @commands.command()
    async def wakeup(self, ctx):
        def check(m):
            return m.author == ctx.message.author and m.channel == ctx.message.channel
        
        if Path(f'Player/{ctx.author.id}.wake').is_file():
            with open(f'Player/{ctx.author.id}.wake', 'r') as file:
                line = file.readlines()
                try:
                    send_magic_packet(line[1].strip(), ip_address=line[2].strip(), port=int(line[3].strip()))
                    await ctx.send('the packet has been sent\nEnjoy')
                except:
                    await ctx.send('**ERROR** : the packet couldn\'t be sent')
        else:
            await ctx.send('specify the mac adress\nYou are 60 seconds to respond')
            try :
                msg = await self.bot.wait_for('message', check=check, timeout=60)
            except :
                await ctx.send('**ERROR** : you are too late')
            macAdress = msg.content
            await ctx.send('specify the IP address\nYou are 60 seconds to respond')
            try :
                msg = await self.bot.wait_for('message', check=check, timeout=60)
            except :
                await ctx.send('**ERROR** : you are too late')
            IPAdress = msg.content
            await ctx.send('specify the port\nYou are 60 seconds to respond')
            try :
                msg = await self.bot.wait_for('message', check=check, timeout=60)
            except :
                await ctx.send('**ERROR** : you are too late')
            Port = msg.content
            with open(f'Player/{ctx.author.id}.wake', 'w') as file:
                file.write(f'{ctx.author.id}-{ctx.author.name}\n{macAdress}\n{IPAdress}\n{Port}')
                file.close()
            await ctx.send(f'Data saved\nMac address : {macAdress}\nIP address : {IPAdress}\nPort : {Port}')


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