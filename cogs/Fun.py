import discord
import sys
import os
import io
import asyncio
from discord.ext import commands


class Fun:
    def __init__(self, bot):
       self.bot = bot
       
       
    @commands.command()
    async def hack(self, ctx, user: discord.Member):
        """Hack someone's account! Try it!"""
        msg = await ctx.send(f"Hacking! Target: {user}")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓    ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓   ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files... [▓▓▓▓▓ ]")
        await asyncio.sleep(2)
        await msg.edit(content="Accessing Discord Files COMPLETE! [▓▓▓▓▓▓]")
        await asyncio.sleep(2)
        await msg.edit(content="Retrieving Login Info... [▓▓▓    ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓ ]")
        await asyncio.sleep(3)
        await msg.edit(content="Retrieving Login Info... [▓▓▓▓▓▓ ]")
        await asyncio.sleep(4)
        await msg.edit(content=f"An error has occurred hacking {user}'s account. Please try again later. ❌")   
   
    
    @commands.command(aliases=['animation', 'a'])
    async def anim(self, ctx, Type):
        """Animations! Usage: *anim [type]. For a list, use *anim list."""
        if Type is None:
            await ctx.send('Probably a really cool animation, but we have not added them yet! But hang in there! You never know... For a current list, type *anim list')
        else:
            if Type.lower() == 'wtf':
              msg = await ctx.send("```W```")
              await asyncio.sleep(1)
              await msg.edit(content="```WO```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT D```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA F```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FU```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FUK```")
              await asyncio.sleep(1)
              await msg.edit(content="```WOT DA FUK!```")
              await asyncio.sleep(1)
              await msg.edit(content="WOT DA FUK!")
            elif Type.lower() == 'mom':
              msg = await ctx.send("```Y```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO M```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MO```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MOM```")
              await asyncio.sleep(1)
              await msg.edit(content="```YO MOM!```")
            await asyncio.sleep(1)
              await msg.edit(content="YO MOM!")
            elif Type.lower() == 'gethelp':
              msg = await ctx.send("```STOP!```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! G```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Ge```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get s```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get so```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get som```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some HELP```")
              await asyncio.sleep(1)
              await msg.edit(content="```STOP! Get some HELP!!!```")
              await asyncio.sleep(1)
              await msg.edit(content="STOP! Get some HELP!!!")
            elif Type.lower() == 'sike':
              msg = await ctx.send("```W```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wa```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wai```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait.```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait..```")
              await asyncio.sleep(1)
              await msg.edit(content="```Wait...```")
              await asyncio.sleep(1)
              await msg.edit(content="```SIKE!```")
              await asyncio.sleep(1)
              await msg.edit(content="SIKE!")
            elif Type.lower() == 'gitgud':
              msg = await ctx.send("```G```")
              await asyncio.sleep(1)
              await msg.edit(content="```Gi```")
              await asyncio.sleep(1)
              await msg.edit(content="```Git```")
              await asyncio.sleep(1)
              await msg.edit(content="```Git GUD!```")
              await asyncio.sleep(1)
              await msg.edit(content="Git GUD!")
            elif Type.lower() == 'list':
              color = discord.Color(value=0x00ff00)
              em=discord.Embed(color=color, title="Current List of Awesome Animations:")
              em.description = "wtf (anim wtf), mom (anim mom), gethelp (anim gethelp), sike (anim sike), gitgud (anim gitgud)."
              em.set_footer(text="We will always be adding new animations!")
              await ctx.send(embed=em)
            else:
              await ctx.send('Probably a really cool animation, but we have not added them yet! But hang in there! You never know... For a current list, type *anim list')             
              
   
    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, message:str):
        """Really desperate? Ask the 8ball for advice. Only yes/no questions!"""
        choices = ['It is certain. :white_check_mark:', 'It is decidedly so. :white_check_mark:', 'Without a doubt. :white_check_mark:', 'Yes, definitely. :white_check_mark:', 'You may rely on it. :white_check_mark:', 'As I see it, yes. :white_check_mark:', 'Most likely. :white_check_mark:', ' Outlook good. :white_check_mark:', 'Yes. :white_check_mark:', 'Signs point to yes. :white_check_mark:', 'Reply hazy, try again. :large_orange_diamond: ', 'Ask again later. :large_orange_diamond: ', 'Better not tell you now. :large_orange_diamond: ', 'Cannot predict now. :large_orange_diamond: ', 'Concentrate and ask again. :large_orange_diamond: ', 'Do not count on it. :x:', 'My reply is no. :x:', 'My sources say no. :x:', 'Outlook not so good. :x:', 'Very doubtful. :x:']
        color = discord.Color(value=0xeaff29)
        em=discord.Embed(color=color, title=f"{message}", description=random.choice(choices))
        em.set_author(name="The Mighty 8 ball", icon_url="https://vignette.wikia.nocookie.net/battlefordreamislandfanfiction/images/5/53/8-ball_my_friend.png/revision/latest?cb=20161109021012")
        em.set_footer(text=f"Sent by {ctx.message.author.name}")
        await ctx.message.delete()
        await ctx.send(embed=em)

    
def setup(bot): 
    bot.add_cog(Fun(bot))   
