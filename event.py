

         ############
        ######by######
        #####dd64#####
         ############ 

import discord, random
from discord.ext import commands

class theEvent(commands.Cog):
    def __init__(self, bot):
        self.bot=bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await self.bot.process_commands(message)
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