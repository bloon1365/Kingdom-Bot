import pickle as p
import os
import random as ra

# Food, Wood, Iron
baseJobs = [0, 0, 0]
# Population, Food, Wood, Iron
baseInv = [1000, 0, 0, 0]
# Population Growth, Population Food Consumption, Resource Collection Rate,
baseMulti = [1.10, 1.00, 5.00]
# [num, movementspeed, (x,y)]
baseArmies = []

operators = ['add', 'sub', 'set']

kingdomlist = ['kingdom1', 'kingdom2', 'kingdom3']

datadir = 'C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/'


def gameConfig(day):
	# [Day]
	master = [day]

	x = '{0}MasterFile_Day{1}'.format(datadir, day)
	outfile = open(x, 'wb')
	p.dump(master, outfile)
	outfile.close()


def getDay():
	y = 0
	for x in os.listdir('{0}'.format(datadir)):
		try:
			if int(x[14]) > y:
				y = int(x[14])
		except TypeError:
			pass
		except IndexError:
			pass
		except ValueError:
			pass

	infile = open('{0}MasterFile_Day{1}'.format(datadir, y), 'rb')
	day = p.load(infile)
	infile.close()
	return day[0]


def find_all_indexes(input_str, search_str):
	l1 = []
	length = len(input_str)
	index = 0
	while index < length:
		i = input_str.find(search_str, index)
		if i == -1:
			return l1
		l1.append(i)
		index = i + 1
	return l1


def positions(string, int):
	spots = find_all_indexes(string, ' ')

	if int == 0:
		x = string[:0]
	elif len(spots) <= int:
		x = string[spots[-1] + 1:]
	else:
		x = string[(spots[int - 1]) + 1:spots[int]]

	return x


def positions2(string, int):
	spots = find_all_indexes(string, ',')

	if int == 0:
		x = string[:0]
	elif len(spots) <= int:
		x = string[spots[-1] + 1:]
	else:
		x = string[(spots[int - 1]) + 1:spots[int]]

	return x


def operators(string, start, end):
	global operatorss
	if string == operatorss[0]:
		return start + end
	if string == operatorss[1]:
		return start - end
	if string == operatorss[2]:
		return end


def configKingdomNames():
	kingdoms = ['kingdom1', 'kingdom2', 'kingdom3']
	outfile = open('{0}Kingdomnames'.format(datadir), 'wb')
	p.dump(kingdoms, outfile)
	outfile.close()


def configKingdom(kingdom, day):
	global baseInv
	global baseJobs
	global baseMulti
	global baseArmies

	kingdomjobsdir = '{0}KingdomJobs_{1}_Day{2}'.format(datadir, kingdom, day)
	kingdominvdir = '{0}KingdomInv_{1}_Day{2}'.format(datadir, kingdom, day)
	kingdommultidir = '{0}KingdomMulti_{1}_Day{2}'.format(datadir, kingdom, day)
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)

	outfile = open(kingdomjobsdir, 'wb')
	p.dump(baseJobs, outfile)
	outfile.close()

	outfile = open(kingdominvdir, 'wb')
	p.dump(baseInv, outfile)
	outfile.close()

	outfile = open(kingdommultidir, 'wb')
	p.dump(baseMulti, outfile)
	outfile.close()

	outfile = open(kingdomarmydir, 'wb')
	p.dump(baseArmies, outfile)
	outfile.close()


def getKingdoms():
	infile = open('{0}Kingdomnames'.format(datadir), 'rb')
	kingdomsnames = p.load(infile)
	infile.close()
	return kingdomsnames


def setJobs(kingdom, day, job, num):
	kingdomjobsdir = '{0}KingdomJobs_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomjobsdir, 'rb')
	x = p.load(infile)
	infile.close()

	if job == 'food':
		x[0] = int(num)
	if job == 'wood':
		x[1] = int(num)
	if job == 'iron':
		x[2] = int(num)

	outfile = open(kingdomjobsdir, 'wb')
	p.dump(x, outfile)
	outfile.close()


def setInv(inv, kingdom, day):
	kingdominvdir = '{0}KingdomInv_{1}_Day{2}'.format(datadir, kingdom, day)

	outfile = open(kingdominvdir, 'wb')
	kingdominv = p.dump(inv, outfile)
	outfile.close()

def removearmy(kingdom, army1):
	day = getDay()
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)
	armies = getArmy(kingdom, day)
	armies.remove(army1)

	outfile = open(kingdomarmydir, 'wb')
	x = p.dump(armies, outfile)
	outfile.close()


def appendArmy(pos, num, kingdom, day, name):
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomarmydir, 'rb')
	kingdomarmy = p.load(infile)
	infile.close()

	basemovement = 3

	kingdomarmy.append([num, basemovement, basemovement, pos, name])

	outfile = open(kingdomarmydir, 'wb')
	x = p.dump(kingdomarmy, outfile)
	outfile.close()


def setMulti(multi, kingdom, day, multiType):
	kingdommultisdir = '{0}KingdomMulti_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdommultisdir, 'rb')
	kingdommulti = p.load(infile)
	infile.close()

	x = kingdommulti
	x[multiType] = multi

	outfile = open(kingdommultisdir, 'wb')
	kingdommulti = p.dump(x, outfile)
	outfile.close()


def getInv(kingdom, day):
	kingdominvdir = '{0}KingdomInv_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdominvdir, 'rb')
	kingdominv = p.load(infile)
	infile.close()
	return kingdominv


def getJobs(kingdom, day):
	kingdomjobsdir = '{0}KingdomJobs_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomjobsdir, 'rb')
	kingdomjobs = p.load(infile)
	infile.close()
	return kingdomjobs


def getMulti(kingdom, day):
	kingdommultisdir = '{0}KingdomMulti_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdommultisdir, 'rb')
	kingdommulti = p.load(infile)
	infile.close()
	return kingdommulti


def getArmy(kingdom, day):
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomarmydir, 'rb')
	kingdomarmy = p.load(infile)
	infile.close()
	return kingdomarmy


def getArmy2(kingdom, day, name):
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomarmydir, 'rb')
	kingdomarmy = p.load(infile)
	infile.close()
	for army2 in kingdomarmy:
		if army2[4] == name:
			army = army2
	return army


def gameLoop():
	day = getDay()
	for x in getKingdoms():
		inv2 = []
		configKingdom(x, day + 1)
		jobs = getJobs(x, day)
		inv = getInv(x, day)
		multi = getMulti(x, day)

		# Population
		inv2.append(inv[0] * multi[0])
		# Food
		inv2.append(((inv[1]) - (inv[0] * multi[1])) + (jobs[0] * multi[2]))
		# Wood
		inv2.append(inv[2] + (jobs[1] * multi[2]))
		# Iron
		inv2.append(inv[3] + (jobs[2] * multi[2]))

		setInv(inv2, x, day + 1)

	gameConfig(day + 1)
	day = getDay()


def over(kingdom, day):
	jobs = getJobs(kingdom, day)
	inv = getInv(kingdom, day)
	if (jobs[0] + jobs[1] + jobs[2]) > inv[0]:
		return 'You assigned more Population than is in your inventory. Redistribute immediately'
	else:
		return None


def drawArmies(kingdoms):
	pygame = '{0}pygame'.format(datadir)

	outfile = open(pygame, 'wb')
	p.dump(kingdoms, outfile)
	outfile.close()


def blank():
	pygame = '{0}pygame'.format(datadir)

	outfile = open(pygame, 'wb')
	p.dump([], outfile)
	outfile.close()


def changearmy(kingdom, armyname, num=None, posx=None, posy=None, movement=0):
	# Army Format:
	# [num, movement speed, remaining movement speed, (x,y), name]
	day = getDay()
	kingdomarmydir = '{0}KingdomArmy_{1}_Day{2}'.format(datadir, kingdom, day)

	infile = open(kingdomarmydir, 'rb')
	armies = p.load(infile)
	infile.close()
	index = 0
	for army in armies:
		if army[4] == armyname:
			if num is not None:
				army[0] = num
			if posy is not None:
				army[3] = (army[3][0], int(posy))
			if posx is not None:
				army[3] = (int(posx), army[3][1])
			if movement is not 0:
				army[2] -= movement
		armies[index] = army
		index += 1

	outfile = open(kingdomarmydir, 'wb')
	x = p.dump(armies, outfile)
	outfile.close()


def getArmies(day):
	y = []
	for x in getKingdoms():
		kingdomarmydir = 'C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/KingdomArmy_{0}_Day{1}'.format(x, day)
		infile = open(kingdomarmydir, 'rb')
		i = p.load(infile)
		infile.close()

		y.append(i)

	return y

oof = 'oof'

def conflict(army, pos):
	global oof
	day = getDay()
	index = 0
	for kingdomarmies in getArmies(day):
		for army2 in kingdomarmies:
			if army2[4] == army[4]:
				pass
			if army2[3] == pos:
				oof = kingdomlist[index]
				return army2
		index += 1
	return None


def combat(army1, army2, kingdom):
	global oof
	totaldamage1 = 0
	totaldamage2 = 0
	day = getDay()
	army1 = getArmy2(kingdom, day, army1[4])
	army2 = getArmy2(oof, day, army2[4])
	while army1[0] >= 0 and army2[0] >= 0:
		damage1 = ra.randrange(0, army2[0])
		damage2 = ra.randrange(0, army1[0])
		totaldamage1 += damage1
		totaldamage2 += damage2
		changearmy(kingdom, army1[4], num=army1[0]-damage1)
		changearmy(oof, army2[4], num=army2[0]-damage2)
		army1 = getArmy2(kingdom, day, army1[4])
		army2 = getArmy2(oof, day, army2[4])


	deadarmy = []
	if army1[0] <= 0:
		removearmy(kingdom, army1)
		deadarmy.append(army1[4])
	if army2[0] <= 0:
		removearmy(kingdomlist[kingdomlist.index(oof)], army2)
		deadarmy.append(army2[4])

	return '{0} and {1} attacked each other and took {2} and {3} damage respectively\n{4} has died'.format(army1[4], army2[4], totaldamage1, totaldamage2, deadarmy)