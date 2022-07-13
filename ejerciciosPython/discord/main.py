import discord
from discord import message

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Realizado! {self.user}')

    async def on_message(self, message):
        if message.content == 'ping':
            await message.channel.send('pong')

    class VoiceClient(discord.VoiceClient):
        async def voice_state(connect):
            if message.channel.send('cx!Join'):
                await connect(timeout=60.0, reconnect=True)
    

client = MyClient()
client.run('NzMzNDU4ODc3Mzk1MzcwMDM1.XxDczw.LHvr1v-9QGyw-3hodsc9XDfBIYA')