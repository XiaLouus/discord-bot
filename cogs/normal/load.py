from disnake.ext import commands
from disnake.ext.commands import Context

class load(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "load",
        description = "load"
    )
    @commands.is_owner()
    async def load(self, context, type, extension) -> None:
        try:
            self.bot.load_extension(f'cogs.{type}.{extension}')
            print("1")
            await context.send(f"{extension} 功能上線")
        except Exception as e:
            await context.send(e)

def setup(bot):
    bot.add_cog(load(bot))