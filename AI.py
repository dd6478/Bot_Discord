

         ############
        ######by######
        #####dd64#####
         ############ 
         
import os, openai
import discord, random, asyncio
from discord.ext import commands

with open('OpenAIAPI', 'r') as file:
    API=file.read().strip()
    file.close()
openai.api_key=API

def setup(bot):
    bot.add_cog(AIBot(bot))

class AIBot(commands.Cog):

    def __init__(self, bot):
        self.bot=bot

    @commands.command()
    async def talk(self, ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        
        await ctx.send("**Communication ON** : let's talk with the bot\nYou can stop the conversation by typing `bye`")
        chat = '''Your name is dodo bot and you are a bot discord create by dd64,
Your job is to talk with people and make them happy,
A lot of people love you because you are the best bot in the world
if a people are lost with the command said the '*help' command can help them :

        '''
        while True :
            try :
                message = await self.bot.wait_for('message', check=check, timeout=60)
            except :
                chat+="\nTime out"
                break
            
            if message.content.lower() == 'bye':
                await ctx.send("Bye")
                chat+="\nBye"
                break
            else:
                question = message.content
                chat += f'\n{message.author.name}: ' + question + '\ndodoBot:'
                reponse = openai.Completion.create(
                    engine='text-davinci-002', 
                    prompt=chat, 
                    temperature=0.5, 
                    max_tokens=200, 
                    top_p=1, 
                    frequency_penalty=0.5, 
                    presence_penalty=0, 
                    stop=["dodoBot:"]
                )
                answer = reponse.choices[0].text.strip()
                chat += answer
                await ctx.send(f"{answer}\n")
        with open(f'{message.author.name}.dodoBot', 'a') as file:
            file.write(chat)
            file.write('\n\n####################\n####################\n####################\n\n')
            file.close()
        await ctx.send("**Communication OFF**")


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
