

import discord
import datetime
import asyncio
import random
import time

class MyClient(discord.Client):
    async def on_ready(self):
        assert isinstance(self.user, object)
        print('봇이 성공적으로 부팅되었습니다.', self.user)
        game = discord.Game("")
        await client.change_presence(status=discord.Status.online, activity=game)

    async def on_message(self: object, message: object) -> object:
        if message.author == self.user:
            return

        #욕설 변수값:: **수동으로 추가하세요**
        dyrtjf = ["시발", "병신", "장애", "섹스", "보지", "자지", "느금마", "니애미", "니애비", "후장", "느금빠", "ㅅㅂ", "지랄", "씨발"]

        # !내정보 로 자신의 정보를 표시합니다.
        if message.content.startswith("!내정보"):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0xff00ff)
            embed.add_field(name="닉네임", value=message.author.name, inline=True)
            embed.add_field(name="서버 닉네임", value=message.author.display_name, inline=True)
            embed.add_field(name="디스코드가입일", value=str(date.year) + "/" + str(date.month) + "/" + str(date.day), inline=True)
            embed.add_field(name="제작자:! DuLi#7777", value=message.author.name + "님 환영해요!", inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await message.channel.send(embed=embed)

        #욕설감지
        for word in dyrtjf:
            if message.content.count(word) > 0:
                print("욕설이 감지되어 삭제처리 되었습니다.")
                await message.channel.purge(limit=1)

        #욕설감지 메세지 출력
        for word in dyrtjf:
            author = message.guild.get_member(int(message.author.id))
            if message.content.count(word) > 0:
                await message.channel.send(f"{author.mention}욕설이 감지되어 삭제되었습니다. 지속적인 욕설 사용시 추방됩니다.")


client = MyClient()
client.run('NzI3MzQ3NDU4Mjg3MzM3NTEy.XvqhGw.57E3j4vH5hp4snayqLY8cIcBxOo')
