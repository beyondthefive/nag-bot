import os, discord

verifiedRoleID = 714279112671232020
guildID = 722966418861326459
oldServerID = 606596846445527076

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
  
    async def on_message(self, message):
        if message.content == 'bt5 alive':
            await message.channel.send("I'm alive!")
        elif message.content == 'bt5 nag':
          user_id_list = ['kdoggyeet#0144']
          for user_id in user_id_list:
            user = await MyClient.get_user_info(user_id)
            await user.send('hello')

def CheckRoles(client):
  print("sup")
  


client = MyClient()
client.run(os.getenv('token'))
