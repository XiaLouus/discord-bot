from disnake.ext import commands
from disnake.ext.commands import Bot, Context
import disnake
import json
import os
import sys

if not os.path.isfile("config.json"):
    sys.exit("config.json not found")
else:
    with open("config.json") as file:
        config = json.load(file)

intents = disnake.Intents.default()
intents.message_content = True
bot = Bot(command_prefix = commands.when_mentioned_or(config["prefix"]), intents = intents, help_command = None)
bot.config = config


@bot.event
async def on_ready():
    print('Bot is already')
    
def load_commands(command_type: str):
    for filename in os.listdir(f"./cogs/{command_type}"):
        if filename.endswith(".py"):
            extension = filename[:-3]
            try:
                bot.load_extension(f"cogs.{command_type}.{extension}")
                print(f"Load extension {extension}")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"fail to load extension {extension} \n {exception}")

if __name__ == '__main__':
    load_commands('normal')

bot.run(config["token"])