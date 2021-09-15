import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("Bot is ready!")
    
@client.command()
async def hello(ctx):
    await ctx.send("hi mf")

@client.command()
async def ping(ctx):
    await ctx.send(f'Your Ping is: {round (client.latency * 1000)}ms ')

@client.command()
async def quote(ctx):
    responses = open('quotes.txt').read().splitlines()
    random.seed(a=None)
    response = random.choice(responses)
    await ctx.send(response)

client.run("ODQyNjUxNDI0NjU5MDc5MjA4.YJ4aSw.VU17vbNZETlZelrWdS_tQcuh5fY") 
