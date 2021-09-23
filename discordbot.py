import discord 
import asyncio
import os

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('재민')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "사랑해 재민":
        await message.channel.send("나두 사랑해 ㅎㅎ") 

    if message.content == "우끼끼":
        await message.channel.send("원숭이야? ㅎㅎ") 

    if message.content == "뭐해 재민":
        await message.channel.send("너 생각 ㅎㅎ") 

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
