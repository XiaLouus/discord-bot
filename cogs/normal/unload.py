from disnake.ext import commands
from disnake.ext.commands import Context

class unload(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "unload",
        description = "Unload"
    )
    @commands.is_owner()
    async def unload(self, context, type, extension) -> None:
        try:
            self.bot.unload_extension(f'cogs.{type}.{extension}')
            print("1")
            await context.send(f"{extension} 已卸載")
        except Exception as e:
            await context.send(e)

def setup(bot):
    bot.add_cog(unload(bot))