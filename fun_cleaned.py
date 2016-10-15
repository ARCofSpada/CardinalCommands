import discord
from discord.ext import commands
from random import randint
from random import choice, shuffle
import json
import urllib.request
import requests

class Fun:
    """Fun commands!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fight(self, name1, unused, name2):
        """random fights."""

        # Code goes here
        x = randint(0, 5000)
        y = randint(0, 5000)
        #str = " ".join(args)
        #str1 = str.split("vs")
        #name1 = str1[0]
        #name2 = str1[1]
        name1 = name1.replace("\"", "") #horrible coding? Pfft, who cares
        name2 = name2.replace("\"", "")
        if name1.lower() == 'chuck norris' or name2.lower() == 'chuck norris':
            await self.bot.say('NOBODY CAN BEAT CHUCK NORRIS.')
            #yield from event.conv.send_message(text_to_segments('NOBODY CAN BEAT CHUCK NORRIS.'))
        elif x > y:
            await self.bot.say(name1 + ' beats ' + name2 + ' ' + str(x) + ' to ' + str(y) + '!')
        elif x < y:
            await self.bot.say(name2 + ' beats ' + name1 + ' ' + str(y) + ' to ' + str(x) + '!')
            # await self.bot.say("I can do stuff!")
    
    @commands.command()
    async def chance(self, *args):
        """random percentage chance."""
        x = randint(0,100)
        text = args+': There is a ' + str(x) + '% chance.'
        await self.bot.say(text)
    
    @commands.command()
    async def pixiv(self, arg):
        """link to pixiv"""
        id = "http://www.pixiv.net/member_illust.php?illust_id=" + arg + "&mode=medium"
        await self.bot.say(id)

    @commands.command()
    async def coinflip(self):
        """Flip a coin."""
        
        x = randint(0, 1)
        if (x == 0):
            await self.bot.say('The coin landed on heads.')
        else:
            await self.bot.say('The coin landed on tails.')

    @commands.command()
    async def mokou(self):
        """Random Mokou images"""
        mokouArray = ["http://dailycap.s-ul.eu/ypuuRv3U.jpg","http://dailycap.s-ul.eu/rO1UMQwf.jpg","http://dailycap.s-ul.eu/wKEQC2RU.jpg","http://dailycap.s-ul.eu/YZ0cSHCm.jpg","http://dailycap.s-ul.eu/jEROBACx.jpg","http://dailycap.s-ul.eu/cD8Dg7Sj.jpg","http://dailycap.s-ul.eu/xDO8E6ed.jpg","http://dailycap.s-ul.eu/zQ4xBha9.jpg","http://dailycap.s-ul.eu/vIHneLhG.jpg","http://dailycap.s-ul.eu/WFAtTs75.jpg","http://dailycap.s-ul.eu/pXD5NJUb.jpg","http://dailycap.s-ul.eu/4cZIjeVP.jpg","http://dailycap.s-ul.eu/8N9UgXFC.jpg","http://dailycap.s-ul.eu/d3Z3LWkA.jpg","http://dailycap.s-ul.eu/NbHWYw8X.jpg","http://dailycap.s-ul.eu/dYdyC0AQ.jpg","http://dailycap.s-ul.eu/6fImnAFW.jpg","http://dailycap.s-ul.eu/TZHMoE8x.jpg","http://dailycap.s-ul.eu/CvekcbZs.jpg","http://dailycap.s-ul.eu/Uo2Lcf6y.jpg","http://dailycap.s-ul.eu/lNulVN7r.jpg","http://dailycap.s-ul.eu/icPuYkLv.jpg","http://dailycap.s-ul.eu/UKlAQ1rd.jpg","http://dailycap.s-ul.eu/98Q4N5mJ.jpg","http://dailycap.s-ul.eu/GnO6cupx.jpg","http://dailycap.s-ul.eu/UAIvnX20.jpg","http://dailycap.s-ul.eu/mbp61ibW.jpg","http://dailycap.s-ul.eu/iTSdH0EC.jpg","http://dailycap.s-ul.eu/K4JikDp2.jpg","http://dailycap.s-ul.eu/EzX5KXIM.jpg","http://dailycap.s-ul.eu/IL68Mqzt.jpg","http://dailycap.s-ul.eu/TmVvnwmG.jpg","http://dailycap.s-ul.eu/2dpUrHVA.jpg","http://dailycap.s-ul.eu/JbaIwVdq.jpg","http://dailycap.s-ul.eu/fxLxmhcf.jpg","http://dailycap.s-ul.eu/mNvn5HjO.jpg","http://dailycap.s-ul.eu/sqWfQvIT.jpg","http://dailycap.s-ul.eu/KZcA1EOb.jpg","http://dailycap.s-ul.eu/MFfzLBjs.jpg","http://dailycap.s-ul.eu/Z8ycDYJV.jpg","http://dailycap.s-ul.eu/F9sZNS1r.jpg","http://dailycap.s-ul.eu/rZxbWfYT.jpg","http://dailycap.s-ul.eu/iL6SwDWV.jpg","http://dailycap.s-ul.eu/sS8xCauN.jpg","http://dailycap.s-ul.eu/2uLnVPR0.jpg","http://dailycap.s-ul.eu/xBD5NQgt.jpg","http://dailycap.s-ul.eu/3As4ZLuY.jpg","http://dailycap.s-ul.eu/G5kOthIg.jpg","http://dailycap.s-ul.eu/wIa2m6Yo.jpg","http://dailycap.s-ul.eu/YY5hpCvP.jpg","http://dailycap.s-ul.eu/AJMvzDvD.jpg","http://dailycap.s-ul.eu/yPoQWSfQ.jpg","http://dailycap.s-ul.eu/aOABp0L4.jpg","http://dailycap.s-ul.eu/eYIeJccl.jpg","http://dailycap.s-ul.eu/jDxocZiL.jpg","http://dailycap.s-ul.eu/shBdNpcm.jpg","http://dailycap.s-ul.eu/Gc8vEysu.jpg","http://dailycap.s-ul.eu/5gxIWmbD.jpg","http://dailycap.s-ul.eu/RCVhvlPZ.jpg","http://dailycap.s-ul.eu/aUCBkuLh.jpg","http://dailycap.s-ul.eu/2J8xbHMv.jpg","http://dailycap.s-ul.eu/ZVVsLVay.jpg","http://dailycap.s-ul.eu/LMPvkoUb.jpg","http://dailycap.s-ul.eu/9MtJpxPc.jpg","http://dailycap.s-ul.eu/KAXfiBeO.jpg","http://dailycap.s-ul.eu/1jzyzz2w.jpg","http://dailycap.s-ul.eu/oXsEGaNR.jpg","http://dailycap.s-ul.eu/bpYs1wNt.jpg","http://dailycap.s-ul.eu/4pspUeG3.jpg","http://dailycap.s-ul.eu/19NrHCDr.jpg","http://dailycap.s-ul.eu/kjTxibin.jpg","http://dailycap.s-ul.eu/TYlokann.jpg","http://dailycap.s-ul.eu/NoHBNUXu.jpg","http://dailycap.s-ul.eu/UwU6dGBx.jpg","http://dailycap.s-ul.eu/UgdKWMKH.jpg","http://dailycap.s-ul.eu/PCfvIOlI.jpg","http://dailycap.s-ul.eu/0v4iGnG9.jpg","http://dailycap.s-ul.eu/66ZKEseJ.jpg","http://dailycap.s-ul.eu/lcPaYjoT.jpg","http://dailycap.s-ul.eu/yPTCF36R.jpg","http://dailycap.s-ul.eu/dMyp4BtX.jpg","http://dailycap.s-ul.eu/s4juB6Yo.jpg","http://dailycap.s-ul.eu/Vd4W98XU.jpg","http://dailycap.s-ul.eu/1sKKg6s1.jpg","http://dailycap.s-ul.eu/gb0tSB1S.jpg","http://dailycap.s-ul.eu/mDwyZAck.jpg","http://dailycap.s-ul.eu/bhpM73HR.jpg","http://dailycap.s-ul.eu/vGZiAXMG.jpg","http://dailycap.s-ul.eu/W9bDy9jV.jpg","http://dailycap.s-ul.eu/VNqgbkrc.jpg","http://dailycap.s-ul.eu/0KJEUx6n.jpg","http://dailycap.s-ul.eu/iBgzyjO8.jpg","http://dailycap.s-ul.eu/mRXywy8I.jpg","http://dailycap.s-ul.eu/HWDD6fxi.jpg","http://dailycap.s-ul.eu/20MTOuLh.jpg","http://dailycap.s-ul.eu/QxvXBcPf.jpg","http://dailycap.s-ul.eu/yDH9Qg8G.jpg","http://dailycap.s-ul.eu/Wb3RMLVo.jpg","http://dailycap.s-ul.eu/iAxzJTSM.jpg","http://dailycap.s-ul.eu/959CKzIu.jpg","http://dailycap.s-ul.eu/4yU0aQhy.jpg","http://dailycap.s-ul.eu/t3S0hUYA.jpg","http://dailycap.s-ul.eu/IPuK1UGM.jpg","http://dailycap.s-ul.eu/SIVCXKAs.jpg","http://dailycap.s-ul.eu/furSB6UW.jpg","http://dailycap.s-ul.eu/huLUB0h5.jpg","http://dailycap.s-ul.eu/kYBccYNq.jpg","http://dailycap.s-ul.eu/kW7M3r7q.jpg","http://dailycap.s-ul.eu/GGbPuc9T.jpg","http://dailycap.s-ul.eu/LnEVXcsh.jpg","http://dailycap.s-ul.eu/hIyugCSj.jpg","http://dailycap.s-ul.eu/ddQ8ehDZ.jpg","http://dailycap.s-ul.eu/n0AIkMSV.jpg","http://dailycap.s-ul.eu/LNZjNTfQ.jpg","http://dailycap.s-ul.eu/iRjv9LVr.jpg","http://dailycap.s-ul.eu/EBtQsSnF.jpg","http://dailycap.s-ul.eu/c549hwrA.jpg","http://dailycap.s-ul.eu/RBSmO2f5.jpg","http://dailycap.s-ul.eu/oK6xv2ZG.jpg","http://dailycap.s-ul.eu/KOA0rskE.jpg","http://dailycap.s-ul.eu/8q3Uqqz6.jpg","http://dailycap.s-ul.eu/mt2EpKMQ.jpg","http://dailycap.s-ul.eu/pudREGAQ.jpg","http://dailycap.s-ul.eu/cp2DzR4X.jpg","http://dailycap.s-ul.eu/GaNVsrVU.jpg","http://dailycap.s-ul.eu/sUckwm9C.jpg","http://dailycap.s-ul.eu/iwEHYCPu.jpg","http://dailycap.s-ul.eu/SEFcqx7c.jpg","http://dailycap.s-ul.eu/l6v80LYq.jpg","http://dailycap.s-ul.eu/aUB3xc3X.jpg","http://dailycap.s-ul.eu/fm5SsLJg.jpg","http://dailycap.s-ul.eu/lCnK0k0i.jpg","http://dailycap.s-ul.eu/s88RbGOM.jpg","http://dailycap.s-ul.eu/u3eaH45Y.jpg","http://dailycap.s-ul.eu/M36SuP9b.jpg","http://dailycap.s-ul.eu/BZa0KXRd.jpg","http://dailycap.s-ul.eu/CeMbzPsN.jpg","http://dailycap.s-ul.eu/WE0bAD45.jpg","http://dailycap.s-ul.eu/hKDcGB30.jpg","http://dailycap.s-ul.eu/1XinBfru.jpg","http://dailycap.s-ul.eu/0uJN4Kdu.jpg","http://dailycap.s-ul.eu/NdLKuIDZ.jpg","http://dailycap.s-ul.eu/y6YLCFPt.jpg","http://dailycap.s-ul.eu/ZYASN4E3.jpg","http://dailycap.s-ul.eu/J4tNdUNN.jpg","http://dailycap.s-ul.eu/a3tRNEe0.jpg","http://dailycap.s-ul.eu/uHU8urze.jpg","http://dailycap.s-ul.eu/fTAyueE6.jpg","http://dailycap.s-ul.eu/9Tn5tP0H.jpg","http://dailycap.s-ul.eu/MvPAJPEi.jpg","http://dailycap.s-ul.eu/vMJEgIH9.jpg","http://dailycap.s-ul.eu/p8MZQGy0.jpg","http://dailycap.s-ul.eu/qmfugCxl.jpg","http://dailycap.s-ul.eu/Oak14cjK.jpg","http://dailycap.s-ul.eu/YOklxrpM.jpg","http://dailycap.s-ul.eu/9NSLvRPy.jpg","http://dailycap.s-ul.eu/98MSOpFE.jpg","http://dailycap.s-ul.eu/Pe2KurJB.jpg","http://dailycap.s-ul.eu/OPPBgyii.jpg","http://dailycap.s-ul.eu/wQ5LAqo1.jpg","http://dailycap.s-ul.eu/9wY0DJq7.jpg","http://dailycap.s-ul.eu/8Z13bRpx.jpg","http://dailycap.s-ul.eu/gCpJ9BVl.jpg","http://dailycap.s-ul.eu/na3kkh4f.jpg","http://dailycap.s-ul.eu/MVq5GG4W.jpg","http://dailycap.s-ul.eu/bvPcr9Oq.jpg","","http://dailycap.s-ul.eu/2tY4l065.jpg","http://dailycap.s-ul.eu/poHFiTmS.jpg","http://dailycap.s-ul.eu/6gmupgwb.jpg","http://dailycap.s-ul.eu/8hNXSvC0.png","http://dailycap.s-ul.eu/V8pUSBr5.jpg","http://dailycap.s-ul.eu/jaaSfRa2.jpg","http://dailycap.s-ul.eu/UPYN3YMr.jpg","http://dailycap.s-ul.eu/LWGrPMQh.jpg","http://dailycap.s-ul.eu/Tu6Ekyhh.jpg","http://dailycap.s-ul.eu/C9OzzHaC.jpg","http://dailycap.s-ul.eu/kLbIZ9pn.jpg","http://dailycap.s-ul.eu/hLD2ZgUk.jpg","http://dailycap.s-ul.eu/WXdrGXlx.jpg","http://dailycap.s-ul.eu/eWw1BdSW.jpg"]
        shuffle(mokouArray)
        await self.bot.say(choice(mokouArray))

    @commands.command()
    async def askhelix(self, question):
        """Ask the helix fossil a question."""

        if not question:
            await self.bot.say('What is your question?')
            return

        answers = [
            "It is certain",
            "It is decidedly so",
            "Without a doubt",
            "Yes, definitely",
            "You may rely on it",
            "As I see it, yes",
            "Most likely",
            "Outlook good",
            "Yes",
            "Signs point to yes",
            "Reply hazy, try again",
            "Ask again later",
            "Better not tell you now",
            "Cannot predict now",
            "Concentrate and ask again",
            "Don't count on it",
            "My reply is no",
            "My sources say no",
            "Outlook not so good",
            "Very doubtful"
        ]

        shuffle(answers)

        await self.bot.say("**The Helix Fossil answers:** "+choice(answers))
        


    @commands.command()
    async def osu(self):
        """post images from Music Game Hell."""

        images = [
            "https://arcofswords.s-ul.eu/2CV33oOi",
            "https://arcofswords.s-ul.eu/w0s7FqS0",
            "https://arcofswords.s-ul.eu/1YV2bAik",
            "https://arcofswords.s-ul.eu/EHdFXJY9",
            "https://arcofswords.s-ul.eu/ZDSfF0jd",
            "https://arcofswords.s-ul.eu/ag3eObpA",
            "https://arcofswords.s-ul.eu/eNP2hRGl",
            "http://i.imgur.com/BDC3KrZ.jpg"
        ]
        
        shuffle(images)
        await self.bot.say(choice(images))
        
        
    @commands.command(no_pm=True, pass_context=False)
    async def psychopass(self, user: discord.Member):
        """Find a user's crime coefficient"""
        
        
        #The letter a starts at 97, so subtract 97 from the character to get 0
        char_array = [ord(char) - 97 for char in user.name.lower()]
        cc = sum(char_array) #crime coefficient
        max_cc_possible = len(char_array) * 26
        cc_percentage = int(round(cc/max_cc_possible*100, 2))
        
        text =  "**" + user.name + "**'s crime coefficient: " + str(cc_percentage) + "%\n"
        if cc_percentage <= 50:
            text += "This person is not a target for enforcement action. The trigger of The Dominator will be locked."
        elif cc_percentage > 50 and cc_percentage < 75:
            text += "Classified as a latent criminal and is a target for enforcement action. The Dominator is set to Non-Lethal Paralyzer mode."
        elif cc_percentage >= 75 and cc_percentage < 100:
            text += "Poses a dangerous threat to society. Lethal force is authorized. The Dominator will automatically switch to Lethal Eliminatior."
        elif cc_percentage >= 100:
            text += "***BZZT*** Error!"
        #text += "\n__DEBUG:__\ncc: " + str(cc) + "\nmax cc: " + str(max_cc_possible)
        
        await self.bot.say(text)
        
def setup(bot):
    bot.add_cog(Fun(bot))
