import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print('ready')


@client.event
async def on_message(message):
    if message.content.startswitch("FIRE EAGLE소개"):
        await message.channel.send('FIRE EAGLE은 GTA5 online의 에어쇼팀이며 항공팀/ 지상팀/홍보팀으로 나뉘어져 있습니다.')


client.run("NzY0MDAzMTIyOTg4NDQ5ODIy.X3_7Ww.h31Ejo8-4WC8pTVx0YkdMsRb510")