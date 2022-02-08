# bot.py
import os
import discord
import game
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

client = discord.Client()
game_session = game.Game()
points = {}


@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Members:\n - {members}")
    print(f"{client.user.name} has connected to Discord!")


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f"Hello {member.name}, welcome to the movie game!")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!newgame":
        await message.channel.send(
            "Starting New Game... \nPoints Reset... \n"
            + game_session.movie_blank
            + "\n"
            + game_session.shuffled_title
        )
        points.clear()

        for guild in client.guilds:
            if guild.name == GUILD:
                break
        for member in guild.members:
            print(member)
            points[member] = 0

    if message.content == game_session.sanitized_title:
        await message.channel.send("Correct!")
        print(message.author)
        ##points[message.author] += 1
        await message.channel.send(
            str(message.author) + " now has " + str(points[message.author]) + " points"
        )
        game_session.newPuzzle()
        await message.channel.send(
            game_session.movie_blank + "\n" + game_session.shuffled_title
        )

    if message.content == "!giveup":
        await message.channel.send("The answer was: " + game_session.full_movie_title)
        game_session.newPuzzle()
        await message.channel.send(
            game_session.movie_blank + "\n" + game_session.shuffled_title
        )

    if message.content == "!points":
        for member in points:
            if points[member] > 0:
                await message.channel.send(str(member) + ": " + str(points[member]))


client.run(TOKEN)
