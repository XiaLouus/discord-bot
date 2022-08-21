from disnake.ext import commands
from disnake.ext.commands import Context   
from email.mime.text import MIMEText
import smtplib

class word(commands.Cog, name = "word-normal"):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "word",
        description = "word"
    )
    async def word(self, context = Context, n = None, nums = 0) -> None:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        try: 
            smtp.ehlo()
            smtp.starttls()
            smtp.login('a91321987@gmail.com','rgimrxjtobqaihcs')
            status = smtp.sendmail('a91321987@gmail.com', ['a91321987@gmail.com'], n)
            await context.author.send(f"郵件傳遞成功 {n}  {nums}")
            smtp.quit() 
        except Exception as e:
            await context.author.send("郵件傳遞失敗" + str(e))
                
def setup(bot):
    bot.add_cog(word(bot))