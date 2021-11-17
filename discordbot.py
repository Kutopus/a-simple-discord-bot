import random
from discord.ext import commands
import discord

client = discord.Client()
bot = commands.Bot(command_prefix="?")
adms = [a, b, c, d]   # Change the admins here
comandos = ["help", "hi", "bye", "coin", "highfive", "hf", "beautiful", "avatar"]
comandos.sort()
comandos = " | ".join(comandos)

@client.event
async def on_ready():
    print("BOT Status: ONLINE")
    print("BOT Name: ", client.user.name)
    print("BOT ID: ", client.user.id)
    print('---------------')

@client.event
async def on_message(message):
    if message.content == "?hi":
        await message.channel.send("hiiii")
    if message.content == "?bye":
        await message.channel.send("bye bye")
    if message.content == "?coin":
        choice = random.randint(1, 2)
        if choice == 1:
            await message.channel.send("heads")
        elif choice == 2:
            await message.channel.send("tails")
    if message.content == "?highfive" or message.content == "?hf":
        await message.add_reaction("✋")
    if message.content == "?iadmin":
        for adm in adms:
            if message.author.id == adm:
                await message.channel.send("hi adm love you")
                break
    if message.content == "?avatar":
        await message.channel.send(message.author.avatar_url)
    if message.content == "?help":
        await message.channel.send(f'Comandos: {comandos}')
    if message.content == "?secret":
        await message.channel.send("there is no secreeet")

        
# Ignore that
'''@bot.command()
async def args(ctx, arg1, arg2):
    if ctx.content.startWith("?mensagem"):
        await ctx.channel.send('You sent {} and {}'.format(arg1, arg2))'''





client.run("") # Token
