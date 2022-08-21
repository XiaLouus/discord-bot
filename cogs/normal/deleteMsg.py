from disnake.ext import commands
from disnake.ext.commands import Context

class deleteMsg(commands.Cog, name = "clear-normal"):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "clear",
        description = "clear message"
    )
    
    
    async def clear(self, context = Context, nums = 1) -> None:
        try:
            await context.channel.purge(limit = nums + 1)
        except Exception as e:
            await context.author.send(str(e))
        
def setup(bot):
    bot.add_cog(deleteMsg(bot))