import discord
import random
from discord.ext import commands
import asyncio
from webserver import keep_alive
import os

client = commands.Bot(command_prefix = ".")

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game("uwu"))
    print("bot is ready")


@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')

@client.command(aliases=["8ball"])
async def _8ball(ctx, *, question):
    responses = ["yes",
                 "maybe",
                 "my sources say no",
                 "my sources say yes",
                 "no",
                 "bitch tf you crazy?"]
    await ctx.send(f"Question: {question}\nAnswer: {random.choice(responses)}")

@client.command(aliases=["roll"])
async def dice(ctx):
    responses = ["1",
                 "2",
                 "3",
                 "4",
                 "5",
                 "6"]
    await ctx.send(f"{random.choice(responses)}")

@client.command(aliases=["cf"])
async def coinflip(ctx):
    responses = ["heads",
                 "tails",]
    await ctx.send(f"{random.choice(responses)}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=0):
    await ctx.channel.purge(limit=amount + 1)

@client.command()
@commands.has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f"kicked {member} for {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f"banned {member} for {reason}")

@client.command()
@commands.has_permissions(manage_messages=True)
async def mute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.add_roles(role)
    await ctx.send(f"{member} muted")

@client.command()
@commands.has_permissions(manage_messages=True)
async def unmute(ctx, member: discord.Member):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    await member.remove_roles(role)
    await ctx.send(f'{member} unmuted')

@client.command()
async def intro(ctx):
  await ctx.send("https://cdn.discordapp.com/attachments/667446394977779754/667448774645383169/RaGe_2020_Intro.mp4")

@client.command()
async def logo(ctx):
  embed = discord.Embed()
  embed.set_image(url="https://media.discordapp.net/attachments/483227709992861696/590435949658374170/rage_traced_2d.png?width=474&height=474")
  await ctx.send(embed=embed)


@client.command()
async def logo3d(ctx):
  embed = discord.Embed()
  embed.set_image(url="https://media.discordapp.net/attachments/483227709992861696/590435953466933262/rage_traced_3d.png?width=474&height=474")
  await ctx.send(embed=embed)


@client.command()
async def info(ctx):
    embed = discord.Embed(title="Rage Boot", description="communist bot with a rage pfp", color=0xf4c2c2)

    # give info about you here
    embed.add_field(name="Author", value="champii~")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="not a public bot rn")

    await ctx.send(embed=embed)

@client.command()
async def wheelchair(ctx):
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/684090883158573109/697947452099002378/1586474027404.gif")
    await ctx.send(embed=embed)
















keep_alive()
client.run("TOKEN")
