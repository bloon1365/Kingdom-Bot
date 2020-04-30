# Kingdom-Bot

This was a project that was origninally for a text based game some friends made up. This bot was used in discord to streamline some of the math that was required for playing the game aswell as some cool new features. This bot was never fully finished or used. Nevertheless, it still has some cool code in it.

### Future

THe future more than likey of this project is nothing. It will most likey sit here for the rest of time. But, if me or my friends decied to pickup this project again there is a possiblily that could not be true and that this is just the start of this project.

### Features

* No limit to players and counted all of their unique empire modifiers, armies, inventories and populations utlization
* A map system that uses discord's channels and a user to livestream a map to any player that joined a call. This system automatlly deteced a players kingdom and showed all armies and any armies that were in the sight range. This used Pygame.
* A automatic gameloop that worked once a day (this game is played slowly over weeks)
* A nifty interactive system that exploded in complexity that became too difficult to new users to use

## Examples of System

### Map

As you can see this project has no graphic design and that is a theme for the whole thing
A player can create an army (after being setup) by typing the command
```
!set army new [kingdomname] [population in army] [x coordinates on map] [y coordinates on map] [armyn ame]
```
and the bot would return this:
![Image of bot responding]()

Now to view this army, the user would join the voice channel named "Map" and the user already in the would automatically start streaming the map (the user would not be streaming 24/7 because of internet speeds)
![Image of map]()

Now that you have armies, you can move them. Use this command to make them in any cardinal direction.
```
!army move kingdom1 army1 right
```
![Image of bot responding]()
![Image of map]()
As you can see the bot has moved right on square. This is automatically tracked by the bot and can be limited to any number, unique to every army. There is also an enemy army, that is displayed as red. We can move right again and then again, (attempting to move onto the enemy square) this will automatically start a combat. I will not explain how combat is calculated, but you can see the result in the chat. One army will die, the other will survive with damage

### Jobs/Inventory

Just this was the orginal scope of the project
A player starts with 1000 population that they can assign jobs to. The only resourse that has function is food, but there is also Wood and Iron. This system was easly expandable to however many resources the game needed. A player would assign jobs by typing:
```
!set jobs kingdom1 food 500
```
and then view assigned population by typing
```
!view jobs kingdom1
```

![Image of Population being assigned]()

these numbers would be calculated at the end of the day to put the appropriate resources into the player's inventory.
```
!view inv kingdom1
```
![Image of Invetory]()

## Built With

* [Pygame](https://github.com/pygame/pygame) - System used to make map

## Authors

* [Bloon1365](https://github.com/bloon1365) - Programmer

## Acknowledgments

* **Gin and Tonic** - Original cocreator of game
* **TCab** - Original c0creator of game
