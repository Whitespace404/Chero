from discord.ext import commands
import discord
import os 
from chesscom_funcs import *
import db_funcs

BOT_TOKEN = os.environ.get("BOT_TOKEN")
MODERATOR_ROLES = ["Moderators", "Admin", "Twitch Moderator"]
client = commands.Bot(command_prefix="!")

@client.event
async def on_event():
    print("Bot ready! Signed in as", client.user)      

@client.command()
async def link_chesscom(ctx, username):
    verified = verify_account(username) # returns two values, verified[0] is a Boolean, and verified[1] is a string.
    
    # verified[0] = Boolean
    # True if 'chero-verify' was set as the location and False if it wasn't.

    # verified[1] = String
    # Contains the location found instead.
    
    if verified[0] == True:
        db_funcs.add_user(ctx.message.author, username)
        await ctx.send(f"{ctx.message.author.mention} Congratulations! You have linked your chess.com account with your Discord account successfully. :white_check_mark: ")
    else:
        await ctx.send(f"{ctx.message.author.mention} The Chess.com account, {username} does not have 'chero-verify' set as the Location, we found `{verified[1]}` instead. Use `!location` for more information.")

@client.command()
@commands.has_any_role(*MODERATOR_ROLES)
async def force_link_chesscom(ctx, discord_username:discord.Member, username):
    db_funcs.add_user(discord_username, username)
    await ctx.send(f"Discord user {discord_username.mention} linked to chess.com account {username}")

@client.command()
async def view_rating(ctx):
    message_author = ctx.message.author
    try:
        chesscom_username = db_funcs.get_chesscom_username(message_author)
    except TypeError:
        await ctx.send(f"There isn't a chess.com account linked to {message_author.mention}. Use `!link_chesscom <username>`")

    rapid_rating = get_rapid_rating(chesscom_username)
    blitz_rating = get_blitz_rating(chesscom_username)
    bullet_rating = get_bullet_rating(chesscom_username)

    await ctx.send(f"Rapid Rating: {rapid_rating} \n Blitz rating: {blitz_rating} \n Bullet rating: {bullet_rating}")

@client.command()
async def location(ctx):
    pass

@client.command()
async def ping(ctx):
    await ctx.send(f"{round(client.latency * 1000, 1)} ms")

client.run(BOT_TOKEN)
