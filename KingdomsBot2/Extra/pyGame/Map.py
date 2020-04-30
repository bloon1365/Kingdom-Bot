import pygame
import os
import pickle as p

pygame.init()

display_width = 1920
display_height = 1080

colors = [[255, 0, 0], [255, 128, 0], [255, 255, 0], [0, 255, 0], [0, 255, 255], [0, 0, 255], [255, 0, 255]]

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Map')

black = (0, 0, 0)
white = (255, 255, 255)

clock = pygame.time.Clock()

# [kingdoms[armies[army[position, number, movementspeed]]]]

clock = pygame.time.Clock()

#triple
grid = (16, 9)

font = pygame.font.SysFont('arial', 32)
font2 = pygame.font.SysFont('arial', 16)

def within(army, army2, sight):
    x1 = army[3][0]
    y1 = army[3][1]
    x2 = army2[3][0]
    y2 = army2[3][1]

    distx = x1 - x2
    disty = y1 - y2

    if abs(distx) + abs(disty) <= sight:
        return True
    else:
        return False


def view(armies, armies2):
    sight = 2
    for kingdom in armies:
        for kingdom2 in armies2:
            for army in kingdom:
                for army2 in kingdom2:
                    if within(army, army2, sight):
                        drawArmy(army2, colors[0])


def drawMap():
    gameDisplay.fill(white)
    x = grid[1]
    y = grid[0]
    dist = display_height / x
    index = 1
    while index <= y:
        pygame.draw.line(gameDisplay, black, (index * dist, 0), (index * dist, display_height))
        index += 1
    dist = display_width / y
    index = 1
    while index <= x:
        pygame.draw.line(gameDisplay, black, (0, index * dist), (display_width, index * dist))
        index += 1


def drawArmy(army, color):
    x = ((army[3][0] + 0.5)-1) * (display_height / grid[1])
    y = ((army[3][1] + 0.5)-1) * (display_width / grid[0])
    num = army[0]
    movementspeed = [1]
    name = army[4]
    pygame.draw.circle(gameDisplay, color, (int(x), int(y)), 50, 3)
    text = font.render(str(num), True, color)
    gameDisplay.blit(text, (int(x) - 15, int(y) - 10))
    text = font2.render(str(name), True, color)
    gameDisplay.blit(text, (int(x) - 15, int(y) - 30))


def getDay():
    y = 0
    for x in os.listdir('C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data'):
        try:
            if int(x[14]) > y:
                y = int(x[14])
        except TypeError:
            pass
        except IndexError:
            pass
        except ValueError:
            pass

    infile = open('C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/MasterFile_Day{0}'.format(y), 'rb')
    day = p.load(infile)
    infile.close()
    return day[0]


def getKingdoms():
    infile = open('C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/pygame', 'rb')
    kingdomsnames = p.load(infile)
    infile.close()
    return kingdomsnames


def getArmies(day):
    y = []
    for x in getKingdoms():
        kingdomarmydir = 'C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/KingdomArmy_{0}_Day{1}'.format(x, day)
        infile = open(kingdomarmydir, 'rb')
        i = p.load(infile)
        infile.close()

        y.append(i)

    return y


def getKingdoms2():
    infile = open('C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/kingdomnames', 'rb')
    kingdomsnames = p.load(infile)
    infile.close()
    return kingdomsnames


def getArmies2(day):
    y = []
    for x in getKingdoms2():
        kingdomarmydir = 'C:/Users/Joel/Desktop/KingdomsBot2/Extra/Data/KingdomArmy_{0}_Day{1}'.format(x, day)
        infile = open(kingdomarmydir, 'rb')
        i = p.load(infile)
        infile.close()

        y.append(i)

    return y


def drawArmies():
    drawMap()
    day = getDay()

    armies = getArmies(day)

    index = 0
    for kingdom in armies:
        color = colors[index]
        for army in kingdom:
            drawArmy(army, colors[3])
            friend.append(army)
        index += 1


mark = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == 27:
                pygame.quit()
                quit()

    danger = False
    if danger:
        if getKingdoms() == [] and mark != True:
            mark = True
            os.system("C:/Users/Joel/Desktop/KingdomsBot2/Extra/Macros/kingdomsStopLive2.exe")
        elif getKingdoms() != [] and mark != False:
            mark = False
            os.system("C:/Users/Joel/Desktop/KingdomsBot2/Extra/Macros/kingdomsGoLive2.exe")

    drawMap()
    day = getDay()

    armies = getArmies(day)
    armies2 = getArmies2(day)

    index = 0
    friend = []
    for kingdom in armies:
        for army in kingdom:
            drawArmy(army, colors[3])
            friend.append(army)
        index += 1

    try:
        for x in armies:
            armies2.remove(x)
    except ValueError:
        pass

    view(armies, armies2)

    pygame.display.update()
    clock.tick(6)

pygame.quit()
quit()