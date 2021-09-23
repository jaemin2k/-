import discord 
import asyncio
import os
import random

client = discord.Client()

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다.')
    game = discord.Game('League of Legends')
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "사랑해 재민":
        await message.channel.send("나두 사랑해 ㅎㅎ") 

    if message.content == "우끼끼":
        await message.channel.send("원숭이야? ㅎㅎ") 

    if message.content == "뭐해 재민":
        await message.channel.send("너 생각 ㅎㅎ") 

    if message.content == "ㅎㅇ 재민":
        ran = random.randint(0,3)
        if ran == 0:
            d = "ㅎㅇ"
        if ran == 1:
            d = "하이하이"
        if ran == 2:
            d = "누구세요?"
        if ran == 3:
            d == "안녕? ㅎㅎ"
        await message.channel.send(d)
        
    if message.content == "안녕 재민":
        ran = random.randint(0,3)
        if ran == 0:
            d = "ㅎㅇ"
        if ran == 1:
            d = "하이하이"
        if ran == 2:
            d = "누구세요?"
        if ran == 3:
            d == "안녕? ㅎㅎ"
        await message.channel.send(d)\
        
    if message.content == "하이 재민":
        ran = random.randint(0,3)
        if ran == 0:
            d = "ㅎㅇ"
        if ran == 1:
            d = "하이하이"
        if ran == 2:
            d = "누구세요?"
        if ran == 3:
            d == "안녕? ㅎㅎ"
        await message.channel.send(d)

access_token = os.environ['BOT_TOKEN']
client.run(access_token)
