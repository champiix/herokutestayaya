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

@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

@client.command()
async def ping(ctx):
    await ctx.send(f'pong! {round(client.latency * 1000)}ms')


@client.command(aliases=["8ball"])
async def _8ball(ctx):
    responses = ["yes",
                 "maybe",
                 "my sources say no",
                 "my sources say yes",
                 "no",
                 "bitch tf you crazy?"]
    await ctx.send( f" {random.choice(responses)}, "+ctx.message.author.mention)

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
async def pravda(ctx):
    await ctx.send("Workers of the world unite!")

@client.command()
async def culprits(ctx):
    await ctx.send("AKM > AK103")



@client.command(pass_context=True, aliases=["propaganda"])
async def manifesto(ctx):

  embed = discord.Embed(
    colour = discord.Colour.red()
  )

  embed.set_author(name="Pravda Manifesto Preface")
  embed.add_field(name="uwu", value="The Pravda Union is a conglomeration of United Republics spanning from Eastern Europe and Northern Asia into Siberia. The works of the party have driven the parasites out of her borders and have continued to ensure safety within her beloved empire. The Central Committee and works have exceeded their mortal ambitions, and restored order and prosperity to the vast Union. Pravda stands as a turning point in history, about the enter into a state of hard work and productivity. To accomplish such a remarkable task, we must end the exploitation by the bourgeoisie, spread out socialist ideals and stand victorious over our foes. Workers of the world, unite! ☭")

  await ctx.send(embed=embed)

@client.command()
async def info(ctx):
    embed = discord.Embed(title="red velvet", description="communist bot with a kpop pfp", color=0xf4c2c2)

    # give info about you here
    embed.add_field(name="Author", value="champii~")

    # Shows the number of servers the bot is member of.
    embed.add_field(name="Server count", value=f"{len(client.guilds)}")

    # give users a link to invite thsi bot to their server
    embed.add_field(name="Invite", value="not a public bot rn")

    await ctx.send(embed=embed)

@client.command()
async def logo(ctx):
    embed = discord.Embed(colour=discord.Colour.red())
    embed.set_image(url="https://cdn.discordapp.com/attachments/684090883158573109/697947452099002378/1586474027404.gif")
    await ctx.send(embed=embed)








keep_alive()
client.run("TOKEN")
