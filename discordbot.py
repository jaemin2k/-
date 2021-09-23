import discord 
import asyncio

client = discord.Client()

token = "ODkwNjAwMzcyNTEzNzAxODk4.YUyKOw.kfmJakSbmAczb_Tok3SecReVPD0"

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


client.run(token)