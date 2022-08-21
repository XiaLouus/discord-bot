from disnake.ext import commands
from disnake.ext.commands import Context

class reload(commands.Cog):
    
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(
        name = "reload",
        description = "reload"
    )
    @commands.is_owner()
    async def reload(self, context, type, extension) -> None:
        try:
            self.bot.reload_extension(f'cogs.{type}.{extension}')
            print("1")
            await context.send(f"{extension} 已更新")
        except Exception as e:
            await context.send(e)

def setup(bot):
    bot.add_cog(reload(bot))