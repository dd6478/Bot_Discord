

         ############
        ######by######
        #####dd64#####
         ############ 

import re
import discord, random, asyncio
from discord.ext import commands
from pathlib import Path

def setup(bot):
    bot.add_cog(saveBot(bot))

class saveBot(commands.Cog):
    def __init__(self, bot):
        self.bot=bot
    
    def author(self, ctx):
        return ctx.author.id, ctx.author.name
    
    @commands.command()
    async def create(self, ctx): # Create a new save file
        authorID, authorName = self.author(ctx) 
        if Path(f'Player/{authorID}').is_file(): 
            await ctx.send('**ERROR** : you already have a save file\nIf you want to add save, use ***\*add (Name of your save) (the thing you want to save)***') 
        else:
            with open(f'Player/{authorID}', 'w') as file: 
                file.write(f'Save file for {authorName} - ID : {authorID}\n')
                file.close()
            await ctx.send(f'Save file created\nIf you want to add a save, use the command ***\*add (Name of your save) (the thing you want to save)***')           

    @commands.command()
    async def add(self, ctx): # Add a new saveLine in file
        try:
            await ctx.message.delete()
        except:
            pass
        authorID, authorName = self.author(ctx)
        if Path(f'Player/{authorID}').is_file(): 
            if len(ctx.message.content.split(' ')) != 3:
                await ctx.send('**ERROR** : you need to specify the name of the save and the thing you want to save')
            else:
                with open(f'Player/{authorID}', 'r') as file: 
                    Len=len(file.readlines())
                    file.close()
                with open(f'Player/{authorID}', 'a') as file: 
                    file.write(f'{Len-1} : {ctx.message.content[5:]}\n')
                    file.close()
                await ctx.send(f'\'*{ctx.message.content[5:]}*\' added to your save file')
        else:
            await ctx.send('**ERROR** : you don\'t have a save file yet\nIf you want to create a save file, use ***\*create***')
            
    @commands.command()
    async def take(self, ctx):
        #send the line to the user
        authorID, authorName = self.author(ctx)
        if Path(f'Player/{authorID}').is_file():
            if len(ctx.message.content.split(' ')) != 2:
                await ctx.send('**ERROR** : you need to specify the number of the save you want to take\nExample : ***\*take 4***')
            else:
                with open(f'Player/{authorID}', 'r') as file: 
                    Read=file.readlines()
                    file.close()
                try:
                    Len=int(ctx.message.content.split(' ')[1])
                except:
                    ctx.send('**ERROR** : you need to specify the number of the save you want to take\nExample : ***\*take 4***')
                try:
                    Read=Read[Len+1]
                    await ctx.send(f"This is your saveLine\n{Read[4:]}")
                except:
                    await ctx.send('**ERROR** : you need to specify a valid number\nYou can make ***\*list*** to see the list of your save')
        else:
            await ctx.send('**ERROR** : you don\'t have a save file yet\nIf you want to create a save file, use ***\*create***')
          
    @commands.command()            
    async def delete(self,ctx): # Delete a saveLine in file
        authorID, authorName = self.author(ctx)
        if Path(f'Player/{authorID}').is_file():
            await ctx.send('**ERROR** : this feature is not available yet')
        else:
            await ctx.send('**ERROR** : you don\'t have a save file yet\nIf you want to create a save file, use ***\*create***')

    @commands.command()
    async def list(self, ctx): # List all saveLine in file
        authorID, authorName = self.author(ctx)
        if Path(f'Player/{authorID}').is_file(): 
            with open(f'Player/{authorID}', 'r') as file:
                readFile = file.read()
                file.close()
            await ctx.send(f'Your save file :\n```{readFile}```')
        else:
            await ctx.send('**ERROR** : you don\'t have a save file yet\nIf you want to create a save file, use ***\*create***')


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