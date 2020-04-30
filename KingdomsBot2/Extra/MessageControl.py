import discord
from . import FileManagement as fs
import os

kingdomids = [688208534957326348, 688208572446015712, 688472896284131431]
kingdomlist = ['kingdom1', 'kingdom2', 'kingdom3']


def on_message(message, client):
	guild = client.get_guild(679922444886474791)

	if message.content.startswith('!set'):
		if fs.positions(message.content, 1) == 'jobs':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					job = fs.positions(message.content, 3)
					num = fs.positions(message.content, 4)
					day = fs.getDay()

					fs.setJobs(kingdom, day, job, num)

					test = fs.over(kingdom, day)
					if test == None:
						pass
					else:
						return test

					return '{0} Population assigned to {1}'.format(num, job)
				else:
					return 'you do not have permissions for this'
			else:
				return 'Kingdom not reconized'

		if fs.positions(message.content, 1) == 'multi':
			if message.author in guild.get_role(688174797359808532).members:
				if fs.positions(message.content, 2) in fs.getKingdoms():
					kingdom = fs.positions(message.content, 2)
					multiType = int(fs.positions(message.content, 3))
					multi = fs.positions(message.content, 4)
					day = fs.getDay()

					fs.setMulti(multi, kingdom, day, multiType)
					if multiType == 0:
						x = 'Population Growth'
					if multiType == 1:
						x = 'Population Food Consumption'
					if multiType == 2:
						x = 'Resource Collection Rate'

					return '{0} Multiplier set to {1}'.format(x, multi)
				else:
					return 'Kingdom not reconized'

		if fs.positions(message.content, 1) == 'army':
			if fs.positions(message.content, 2) == 'new':
				if fs.positions(message.content, 3) in fs.getKingdoms():
					x = fs.getKingdoms().index(fs.positions(message.content, 3))
					y = kingdomids[x]
					if message.author in guild.get_role(y).members:
						kingdom = fs.positions(message.content, 3)
						num = int(fs.positions(message.content, 4))
						pos = (int(fs.positions(message.content, 5)), int(fs.positions(message.content, 6)))
						day = fs.getDay()
						if pos[0] < 1 or pos[0] > 16:
							return 'x value beyond bounds'
						if pos[1] < 1 or pos[1] > 9:
							return 'y value beyond bounds'
						if num >= fs.getInv(kingdom, day)[0]:
							return 'army too big for current population'
						name = fs.positions(message.content, 7)

						fs.appendArmy(pos, num, kingdom, day, name)
						inv = fs.getInv(kingdom, day)
						inv[0] -= num
						fs.setInv(inv, kingdom, day)

						return '{0} Population army created with name {1}'.format(num, name)
				else:
					return 'you do not have permissions for this'

			if fs.positions(message.content, 2) == 'change':
				if fs.positions(message.content, 3) in fs.getKingdoms():
					x = fs.getKingdoms().index(fs.positions(message.content, 3))
					y = kingdomids[x]
					if message.author in guild.get_role(y).members:
						kingdom = fs.positions(message.content, 3)
						thingname = fs.positions(message.content, 4)
						thing = fs.positions(message.content, 5)
						name = fs.positions(message.content, 6)
						day = fs.getDay()

						army = fs.getArmy2(kingdom, day, name)

						if thingname == 'movement':
							fs.changearmy(kingdom, name, movement=thing)
							return 'movement value reduced by {0}'.format(thing)
						if thingname == 'num':
							fs.changearmy(kingdom, name, num=thing)
							return 'population value changed to {0}'.format(thing)
						if thingname == 'posx':
							if army[3][0] + thing > 16 or army[3][0] + thing < 1:
								return 'x value out of bounds'
							fs.changearmy(kingdom, name, posx=thing)
							return 'posx changed to {0}'.format(thing)
						if thingname == 'posy':
							if army[3][1] + thing > 9 or army[3][1] + thing < 1:
								return 'y value out of bounds'
							fs.changearmy(kingdom, name, posy=thing)
							return 'posy changed to {0}'.format(thing)

						return 'name of thing to change not recognized'
				else:
					return 'you do not have permissions for this'

		if fs.positions(message.content, 1) == 'inv':
			if message.author in guild.get_role(688174797359808532).members:
				if fs.positions(message.content, 2) in fs.getKingdoms():
					kingdom = fs.positions(message.content, 2)
					invtype = fs.positions(message.content, 3)
					inv = int(fs.positions(message.content, 5))
					day = fs.getDay()
					thing = fs.positions(message.content, 4)

					if invtype == 'pop':
						x = 0
					if invtype == 'food':
						x = 1
					if invtype == 'wood':
						x = 2
					if invtype == 'iron':
						x = 3

					current = fs.getInv(kingdom, day)

					oof = fs.operators(thing, current[x], inv)

					current[x] = oof

					fs.setInv(current, kingdom, day)

					return "{0} {1} {2} to {3}'s inventory".format(inv, invtype, thing, kingdom)

				else:
					return 'Kingdom not reconized'

			else:
				return 'you do not have permissions for this'

		return ('command not within set function')

	if message.content.startswith('!view'):
		if fs.positions(message.content, 1) == 'kingdomnames':
			return (fs.getKingdoms())

		if fs.positions(message.content, 1) == 'inv':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					day = fs.getDay()

					inv = fs.getInv(kingdom, day)

					return 'Your inventory is: \n Population: {0} \n Food: {1} \n Wood: {2} \n Iron: {3}'.format(inv[0],
																												 inv[1],
																												 inv[2],
																												 inv[3])
				else:
					return 'you do not have permissions for this'
			else:
				return 'Kingdom not reconized'

		if fs.positions(message.content, 1) == 'jobs':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					day = fs.getDay()

					inv = fs.getJobs(kingdom, day)

					return 'Your current jobs are: \nFood: {0} \nWood: {1} \nIron: {2}'.format(inv[0], inv[1], inv[2])
				else:
					return 'you do not have permissions for this'
			else:
				return 'Kingdom not reconized'

		if fs.positions(message.content, 1) == 'multi':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					day = fs.getDay()

					inv = fs.getMulti(kingdom, day)

					return 'Your current multipliers are:\nPopulation Growth: {0} \nPopulation Food Consumption: {1} \nResource Collection Rate: {2}'.format(
						inv[0], inv[1], inv[2])
				else:
					return 'you do not have permissions for this'
			else:
				return 'Kingdom not reconized'

		if fs.positions(message.content, 1) == 'army':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					day = fs.getDay()

					armies = fs.getArmy(kingdom, day)
					string = 'Your current armies are:\n'

					for army in armies:
						string += 'Army name: {0}, {1} Population, movement speed of {2}, remaining movement speed of {3} and a position of {4} \n'.format(
							army[4], army[0], army[1], army[2], army[3])

					return string
				else:
					return 'you do not have permissions for this'
			else:
				return 'Kingdom not reconized'

		return ('command not within view function')

	if message.content.startswith('!config'):
		if message.author in guild.get_role(688174797359808532).members:
			if fs.positions(message.content, 1) == 'master':
				fs.gameConfig(1)
				return 'Game has been configured'

			if fs.positions(message.content, 1) in fs.getKingdoms():
				kingdom = fs.positions(message.content, 1)
				fs.configKingdom(kingdom, 1)

				return '{0} has been configured'.format(kingdom)

			return ('command not within !config function')
		else:
			return ('you do not have permissions for this')

	if message.content.startswith('!test'):
		if message.author in guild.get_role(688174797359808532).members:
			if fs.positions(message.content, 1) == 'startlive':
				os.system("C:/Users/Joel/Desktop/KingdomsBot2/Extra/Macros/kingdomsGoLive2.exe")
				return ('Gone Live')

			if fs.positions(message.content, 1) == 'stoplive':
				os.system("C:/Users/Joel/Desktop/KingdomsBot2/Extra/Macros/kingdomsStopLive2.exe")
				return ('Stopped Live')

			if fs.positions(message.content, 1) == 'army':
				fs.changearmy('kingdom1', 'oof', )

			return ('command not within test function')
		else:
			return ('you do not have permissions for this')

	if message.content.startswith('!dump'):
		if message.author in guild.get_role(688174797359808532).members:

			if fs.positions(message.content, 1) == 'kingdomnames':
				kingdomnames = fs.positions(message.content, 2)
				fs.configKingdomNames()

				return 'Dumped {0}'.format(kingdomnames)

			return ('command not within dump function')
		else:
			return ('you do not have permissions for this')

	if message.content.startswith('!loop'):
		if message.author in guild.get_role(688174797359808532).members:
			fs.gameLoop()
			day = fs.getDay()

			return (
				'===============Day {0} Has Ended===============\n===============Day {1} Has Begun==============='.format(
					day - 1, day))

			return ('command not within loop function')
		else:
			return ('you do not have permissions for this')

	if message.content.startswith('!oof'):
		return ('https://www.youtube.com/watch?v=D00YBm5A6Z4')

	if message.content.startswith('!army'):
		if fs.positions(message.content, 1) == 'move':
			if fs.positions(message.content, 2) in fs.getKingdoms():
				x = fs.getKingdoms().index(fs.positions(message.content, 2))
				y = kingdomids[x]
				if message.author in guild.get_role(y).members:
					kingdom = fs.positions(message.content, 2)
					day = fs.getDay()
					armyname = fs.positions(message.content, 3)
					direction = fs.positions(message.content, 4)
					army = fs.getArmy2(kingdom, day, armyname)
					msg = 'direction {0} not reconized'.format(direction)
					if army[2] == 0:
						msg = '{0} has no movement points remaining'.format(armyname)
					if direction == 'up':
						posy = army[3][1] - 1
						army2 = fs.conflict(army, (army[3][0], army[3][1] - 1))
						if army2 is not None:
							msg = fs.combat(army, army2, kingdom)
						elif army[3][1] - 1 < 1:
							msg = 'moving these units would send them off the edge of that map'
						else:
							fs.changearmy(kingdom, armyname, posy=posy)
							fs.changearmy(kingdom, armyname, movement=1)
							msg = '{0} moved up'.format(armyname)
					if direction == 'down':
						posy = army[3][1] + 1
						army2 = fs.conflict(army, (army[3][0], army[3][1] + 1))
						if army2 is not None:
							msg = fs.combat(army, army2,kingdom)
						elif army[3][1] + 1 > 9:
							msg = 'moving these units would send them off the edge of that map'
						else:
							fs.changearmy(kingdom, armyname, posy=posy)
							fs.changearmy(kingdom, armyname, movement=1)
							msg = '{0} moved down'.format(armyname)
					if direction == 'left':
						posx = army[3][0] - 1
						army2 = fs.conflict(army, (army[3][0] - 1, army[3][1]))
						if army2 is not None:
							msg = fs.combat(army, army2, kingdom)
						elif army[3][0] - 1 < 1:
							msg = 'moving these units would send them off the edge of that map'
						else:
							fs.changearmy(kingdom, armyname, posx=posx)
							fs.changearmy(kingdom, armyname, movement=1)
							msg = '{0} moved left'.format(armyname)
					if direction == 'right':
						posx = army[3][0] + 1
						army2 = fs.conflict(army, (army[3][0] + 1, army[3][1]))
						if army2 is not None:
							msg = fs.combat(army, army2, kingdom)
						elif army[3][0] + 1 > 16:
							msg = 'moving these units would send them off the edge of that map'
						else:
							fs.changearmy(kingdom, armyname, posx=posx)
							fs.changearmy(kingdom, armyname, movement=1)
							msg = '{0} moved right'.format(armyname)

					return msg

	return ('super command not reconized')


def voice(member, before, after, client):
	guild = client.get_guild(679922444886474791)
	if before.channel == None:
		index = 0
		perms = []
		for kingdomid in kingdomids:
			if member in guild.get_role(kingdomid).members:
				perms.append(kingdomlist[index])

			fs.drawArmies(perms)

			index += 1
	else:
		fs.drawArmies([])
