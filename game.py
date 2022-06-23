

         ############
        ######by######
        #####dd64#####
         ############ 
         
import os
import discord, random, asyncio
from discord.ext import commands
from copy import deepcopy

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
    
    
    
    def createGrille(self):
        grille=[]
        for i in range(5):
            grille.append(['~']*5)
        return grille
    
    def addBoat(self, G, Coo):
        dico = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
        Coo = Coo.split(':')
        try :
            Befor = G[int(Coo[1])-1][dico[Coo[0]]]
            if Befor == '~':
                G[int(Coo[1])-1][dico[Coo[0]]] = '+'
            elif Befor == '+':
                raise KeyError
        except KeyError and IndexError:
            raise ValueError('Coordinate not valid') 
        return G
    
    def addMine(self, G, Coo):
        dico = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4}
        Coo = Coo.split(':')
        try :
            Befor = G[int(Coo[1])-1][dico[Coo[0]]]
            if Befor == '~':
                G[int(Coo[1])-1][dico[Coo[0]]] = '*'
            elif Befor == '+':
                G[int(Coo[1])-1][dico[Coo[0]]] = 'X'
            elif Befor == '*' or Befor == 'X':
                raise OSError('Mine already there')
        except KeyError and IndexError:
            raise ValueError('Coordinate not valid') 
        return G
    
    def afficherGrille(self, G):
        str='```\n\ A B C D E /\n'
        N=1 
        for i in G:
            str+=f'{N} '
            for j in i:
                str+=f'{j} '
            str+=f'{N}\n'
            N+=1
        str+='/ A B C D E \ \n```'
        return str
        
    def afficherGrillePublic(self, Player1, G1, Player2, G2):
        Str='```\n###############\n#\ A B C D E /#\n'
        N=1 
        for i in G1:
            Str+=f'#{N} '
            for j in i:
                Str+=f'{j} '
            if N==3:
                Str+=f'{N}# <=={Player1}\n'
            else:
                Str+=f'{N}#\n'
            N+=1
        Str+='#/ A B C D E \#\n###############\n#\ A B C D E /#\n'
        N=1 
        for i in G2:
            Str+=f'#{N} '
            for j in i:
                Str+=f'{j} '
            if N==3:
                Str+=f'{N}# <=={Player2}\n'
            else:
                Str+=f'{N}#\n'
            N+=1
        Str+='#/ A B C D E \#\n###############\n```'
        return Str
    
    @commands.command()
    async def bataille(self,ctx):
        def check(message):
            return message.channel == ctx.message.channel and message.content.lower() == 'moi'
        def checkPrivate(message):
            return checkPrivateJ1(message) or checkPrivateJ2(message) 
        def checkPrivateJ1(message):
            return message.author == msgJoueur1.author
        def checkPrivateJ2(message):
            return message.author == msgJoueur2.author
        
        privateJ1 = self.createGrille()
        privateJ2 = self.createGrille()
        
        await ctx.send('Jouons tous ensemble à un petit jeux !\nLes 2 prochaine perssonnes a dire "moi" seront les 2 joueurs\nPreparez vous !')
        try :
            msgJoueur1 = await self.bot.wait_for('message', check=check, timeout=60)
            await ctx.send(f'**joueur 1** : {msgJoueur1.author.mention}')
            msgJoueur2 = await self.bot.wait_for('message', check=check, timeout=60)
            await ctx.send(f'**joueur 2** : {msgJoueur2.author.mention}')
        except :
            await ctx.send('Trop long !')
            return
        '''
        if msgJoueur1.author == msgJoueur2.author:
            await ctx.send('Les **2 joueurs** sont identiques !\nTa crue tu allais m\'avoir ?\n***Jeux annulé!!***')
            return
        '''
        await msgJoueur1.author.send(self.afficherGrille(privateJ1))
        await msgJoueur2.author.send(self.afficherGrille(privateJ2))
        N=1
        while N!=4:
            print(N)
            if N==1:
                await msgJoueur1.author.send(f'Le bateaux N°{N} a placé a une taille de **2/1**\nChoisi 2 case cote a cote (*ex : A:1,A:2*)')
                await msgJoueur2.author.send(f'Le bateaux N°{N} a placé a une taille de **2/1**\nChoisi 2 case cote a cote (*ex : A:1,A:2*)')
            else:
                await msgJoueur1.author.send(f'\n\nOk maintenant\nLe bateaux N°{N} a placé a une taille de **1/1**\nChoisi 1 case (*ex : A:1*)')
                await msgJoueur2.author.send(f'\n\nOk maintenant\nLe bateaux N°{N} a placé a une taille de **1/1**\nChoisi 1 case (*ex : A:1*)')
            try :
                coordonate = await self.bot.wait_for('message', check=checkPrivate, timeout=60)
                if coordonate.author == msgJoueur1.author:
                    print("jsuis ici")
                    reponseJ1 = coordonate.content.lower()
                    reponseJ2 = await self.bot.wait_for('message', check=checkPrivateJ2, timeout=60)
                    reponseJ2 = reponseJ2.content.lower()
                elif coordonate.author == msgJoueur2.author:
                    print("jsuis la")
                    reponseJ2 = coordonate.content.lower()
                    reponseJ1 = await self.bot.wait_for('message', check=checkPrivateJ1, timeout=60)
                    reponseJ1 = reponseJ1.content.lower()
            except:
                await msgJoueur1.author.send('Trop long !')
                await msgJoueur2.author.send('Trop long !')
                return
            if N==1:
                reponseJ1 = reponseJ1.split(',')
                reponseJ2 = reponseJ2.split(',')
                try:
                    if (reponseJ1[0].split(':')[0] == reponseJ1[1].split(':')[0] or reponseJ1[0].split(':')[1] == reponseJ1[1].split(':')[1]):
                        if (reponseJ2[0].split(':')[0] == reponseJ2[1].split(':')[0] or reponseJ2[0].split(':')[1] == reponseJ2[1].split(':')[1]):
                            A=deepcopy(privateJ1)
                            B=deepcopy(privateJ2)
                            self.addBoat(A,reponseJ1[0])
                            self.addBoat(A,reponseJ1[1])
                            self.addBoat(B,reponseJ2[0])
                            self.addBoat(B,reponseJ2[1])
                        else :
                            await msgJoueur1.author.send(f'**ERROR** : {msgJoueur2.author.name} a mal placé son bateau\nOn recommence\n\n')
                            await msgJoueur2.author.send(f'**ERROR** : {msgJoueur2.author.name} a mal placé son bateau\nOn recommence\n\n')
                            raise ValueError('ERROR')
                    else :
                        await msgJoueur1.author.send(f'**ERROR** : {msgJoueur1.author.name} a mal placé son bateau\nOn recommence\n\n')
                        await msgJoueur2.author.send(f'**ERROR** : {msgJoueur1.author.name} a mal placé son bateau\nOn recommence\n\n')
                        raise ValueError('ERROR')
                except ValueError:
                    pass
                except:
                    await msgJoueur1.author.send('**ERROR** : Mauvaise coordonnée !!\nOn recommence\n\n')
                    await msgJoueur2.author.send('**ERROR** : Mauvaise coordonnée !!\nOn recommence\n\n')
                    
                else:
                    print(privateJ1)
                    self.addBoat(privateJ1,reponseJ1[0])
                    self.addBoat(privateJ1,reponseJ1[1])
                    self.addBoat(privateJ2,reponseJ2[0])
                    self.addBoat(privateJ2,reponseJ2[1])
                    await msgJoueur1.author.send(self.afficherGrille(privateJ1))
                    await msgJoueur2.author.send(self.afficherGrille(privateJ2))
                    N+=1
                finally :
                    del(A)
                    del(B)
            else:
                try:
                    A=deepcopy(privateJ1)
                    B=deepcopy(privateJ2)
                    self.addBoat(A,reponseJ1)
                    self.addBoat(B,reponseJ2)
                except:
                    await msgJoueur1.author.send('**ERROR** : Mauvaise coordonnée !!\nOn recommence\n\n')
                    await msgJoueur2.author.send('**ERROR** : Mauvaise coordonnée !!\nOn recommence\n\n')
                else:
                    self.addBoat(privateJ1,reponseJ1)
                    self.addBoat(privateJ2,reponseJ2)
                    await msgJoueur1.author.send(self.afficherGrille(privateJ1))
                    await msgJoueur2.author.send(self.afficherGrille(privateJ2))
                    N+=1
                finally:
                    del(A)
                    del(B)
        await msgJoueur1.author.send('Ok les bateaux sont placés')
        await msgJoueur2.author.send('Ok les bateaux sont placés')
        await ctx.send('Les bateaux des deux joueurs sont placés\n\n')
        GrillePb = self.afficherGrillePublic(msgJoueur1.author.name,privateJ1,msgJoueur2.author.name,privateJ2)
        GrillePb = GrillePb.replace('+','~')
        await ctx.send(GrillePb)
    
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