from disnake.ext import commands
from disnake.ext.commands import Context

class Hello(commands.Cog, name = "Hello-normal"):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "hello",
        description = "hello"
    )
    async def hello(self, context = Context) -> None:
        await context.send("Hello")
        
def setup(bot):
    bot.add_cog(Hello(bot))