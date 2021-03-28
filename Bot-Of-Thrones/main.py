# -*- coding: utf-8 -*-

import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = "!", description = "Je suis là pour vous acceuillir et gérer vos demandes")

@bot.event
async def on_ready():
    print("ready !")

bot.run("NzE0Nzc2OTEzMzgxNDI1MTgy.Xszl4A.shPDNMijUlOTa7EuX65GlfCqqeE")