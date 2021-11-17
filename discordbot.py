import random
from discord.ext import commands
import discord

client = discord.Client()
bot = commands.Bot(command_prefix="?")
adms = [226880541738139648, 543109910506766338, 529801585451335680, 322803186475728896]
comandos = ["ajuda", "oi", "tchau", "moeda", "tocaaqui", "hf", "linda", "avatar"]
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
    if message.content == "?oi":
        await message.channel.send("Oiii")
    if message.content == "?tchau":
        await message.channel.send("Tchauzinho")
    if message.content == "?moeda":
        choice = random.randint(1, 2)
        if choice == 1:
            await message.channel.send("caraaa")
        elif choice == 2:
            await message.channel.send("coroaa")
    if message.content == "?tocaaqui" or message.content == "?hf":
        await message.add_reaction("✋")
    if message.content == "?oid":
        for adm in adms:
            if message.author.id == adm:
                await message.channel.send("oi adm linda fofa")
                break
    if message.content == "?linda":
        await message.channel.send("<@226880541738139648>")
    if message.content == "?avatar":
        await message.channel.send(message.author.avatar_url)
    if message.content == "?ajuda":
        await message.channel.send(f'Comandos: {comandos}')
    if message.content == "?secreto":
        await message.channel.send("Não tem secreto bobinho(a)")
    if message.content == "?geo":
        await message.channel.send("geolink")

@bot.command()
async def args(ctx, arg1, arg2):
    if ctx.content.startWith("?mensagem"):
        await ctx.channel.send('You sent {} and {}'.format(arg1, arg2))





client.run("ODkyMDQwNjUxMjg4NDc3NzQ2.YVHHmA.J_QwExfYM7uKNJ0VSEs2nfXGhX4")