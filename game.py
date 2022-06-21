

         ############
        ######by######
        #####dd64#####
         ############ 
         
import discord, random, asyncio
from discord.ext import commands

def setup(bot):
    bot.add_cog(gameBot(bot))

class gameBot(commands.Cog):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    def __init__(self, bot):
        self.bot=bot
        
    def Word(self):
        with open('Bot_Discord/wordList', 'r') as file:
            word=file.readlines()
            file.close()
        return word[random.randint(0,len(word)-1)].strip()
    
    def printWord(self, word, letter):
        str=''
        for i in word:
            if i in letter:
                str+=i+' '
            else:
                str+='- '
        return str
                
    @commands.command()
    async def pendu(self,ctx):
        def check(message):
            return message.channel == ctx.message.channel
        
        Life = 10
        Letter = []
        notGoodLetter = []
        await ctx.send('Jouons tous ensemble à un petit jeux !')
        await ctx.send("C'est bon j'ai trouver !\nPreparez vous !")
        WORD=self.Word()
        print(WORD)
        Letter.append(WORD[0])
        await ctx.send(f'Le mot à trouver est : {self.printWord(WORD, Letter)}\nIl vous reste {Life} vies')
        while Life != 0:
            try :
                msg = await self.bot.wait_for('message', check=check, timeout=60)
            except :
                await ctx.send('Plus personne ne veux jouer :(\ntanpis!')
                return
            if len(msg.content) == 1 and msg.content.lower() in gameBot.alphabet:
                if msg.content.lower() in Letter or msg.content.lower() in notGoodLetter:
                    await ctx.send('Cette lettre a deja été dite')
                elif msg.content.lower() in WORD:
                    Letter.append(msg.content.lower())
                    if '-' not in self.printWord(WORD, Letter):
                        await ctx.send(f'Bravo ! Vous avez gagné !\nLe mot était bien : {WORD}')
                        return
                    else :
                        await ctx.send(f'Bien joué !\nLe mot à trouver est : {self.printWord(WORD, Letter)}\nIl vous reste {Life} vies\nLettre mauvaise dite : {notGoodLetter}')
                else:
                    Life-=1
                    notGoodLetter.append(msg.content.lower())
                    if Life == 0 :
                        pass
                    else :
                        await ctx.send(f'Dommage !\nLe mot à trouver est : {self.printWord(WORD, Letter)}\nIl vous reste {Life} vies\nLettre mauvaise dite : {notGoodLetter}')
        await ctx.send(f"Vous n'avez plus de vies :(\nLe mot à trouver était : {WORD}")
        return
    
    @commands.command()
    async def pfc(self,ctx):
        def check(message):
            return message.channel == ctx.message.channel and message.author == ctx.message.author
        
        choose = ['pierre', 'feuille', 'ciseaux']
        myAnswer = random.choice(choose)
        await ctx.send('Jouons tous ensemble à un petit jeux !\nChoisi entre ***pierre***, ***feuille*** ou ***ciseaux***\nMoi j\'ai deja choisi')
        try:
            msg = await self.bot.wait_for('message', check=check, timeout=60)
            msg = msg.content.lower()
        except:
            await ctx.send('Plus personne ne veux jouer :(\ntanpis!')
            return
        if msg == myAnswer:
            await ctx.send(f'J\'ai aussi choisi **{myAnswer}**\nEgalité !')
        elif msg not in choose:
            await ctx.send('Ce n\'est pas un choix valide\nTu dois choisir entre pierre, feuille ou ciseaux\nRefait **\*pfc** pour recommencer*')
        elif msg == choose[0]:
            if myAnswer == choose[1]:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as perdu !')
            else:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as gagné !')
        elif msg == choose[1]:
            if myAnswer == choose[2]:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as perdu !')
            else:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as gagné !')
        elif msg == choose[2]:
            if myAnswer == choose[0]:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as perdu !')
            else:
                await ctx.send(f'J\'ai choisi **{myAnswer}**\nTu as gagné !')
        return
    
'''    
with open('Achanger', 'r', encoding='latin2') as file:
    word=file.readlines()
    file.close()
with open('wordList', 'w') as file:
    for i in word:
        N=0
        mot=(i.strip()).lower()
        for j in mot:
            if j not in gameBot.alphabet:
                N+=1
        if N==0:
            file.write(mot+'\n')
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