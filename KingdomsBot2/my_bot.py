import discord
from discord.ext import commands, tasks
import pickle as p
from Extra import MessageControl as ms
from Extra import FileManagement as fs
import time


Tokendir = 'C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/token'

infile = open(Tokendir, 'rb')
TOKEN = p.load(infile)
infile.close()

# TOKEN = 'Njc5OTIzMDI5MTY1NjA0ODk2.XnU4Wg.KJNJ9ARRWOLFYjWErzICySM8Aog'

masterdir = 'C:/Users/Joel/Desktop/KingdomsBot2'

kingdomnames = '{0}/kingdomnames'.format(masterdir)

client = discord.Client()



# infile = open(kingdomnames, 'rbkingdomnames')		
# kingdoms = p.load(infile)
# infile.close()



@client.event
async def on_message(message):
	guild = client.get_guild(679922444886474791)
	msg = 'temp'
	if message.author in guild.get_role(688174797359808532).members:
		if message.content.startswith('!start gameloop'):
			loop.start()
			msg = 'Gameloop started'
	if message.content.startswith('!') == False:
		msg = None

	if message.author == client.user:
		msg = None

	if msg == None or msg == 'Gameloop started':
		pass
	else: msg = ms.on_message(message, client)

	if msg == None:
		pass
	else:
		await message.channel.send(msg)

@client.event
async def on_ready():
	print('Logged in as')
	print(client.user.name)
	print(client.user.id)
	print('------')


@client.event
async def on_voice_state_update(member, before, after):
	if after.self_stream == False and before.self_stream == False:
		guild = client.get_guild(679922444886474791)
		if str(member.name) != 'oof':
			ms.voice(member, before, after, client)
	

@tasks.loop(hours = 24)
async def loop():
	channel = client.get_channel(679922444886474794)
	fs.gameLoop()
	day = fs.getDay()
	await channel.send('===============Day {0} Has Ended===============\n===============Day {1} Has Begun==============='.format(day-1,day))




client.run(TOKEN)