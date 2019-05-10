# Classes and Objects
# Properties
# Behaviour
# Inititalizers and Instances
# Inheritance

class GameCharacter:
    name = ""           # Properties or here State
    maxHP = 0           # use __ for private
    currentHP = 0
    xPos = 0
    lives = 1

    def __init__(self, name, maxHP, xPos):
        self.name = name
        self.maxHP = maxHP
        self.currentHP = maxHP
        self.xPos = xPos

    def changeHP(self, changeinHP):
        self.currentHP += changeinHP   # self = this of python
        if self.currentHP > self.maxHP:
            self.currentHP = self.maxHP
        elif self.currentHP < 0:
            self.currentHP = 0

    def changePos(self, changeinXPos):
        self.xPos += changeinXPos


    # def getXPos(self):
    #     return self.xPos
    #
    # def setXPos(self, newXPos):
    #     self.xPos = newXPos


class PlayerCharacter(GameCharacter):
    lives = 0
    Inventory = []

    def __init__(self, name, maxHP, xPos):
        super(PlayerCharacter, self).__init__(name, maxHP, xPos)
        self.lives = 3
        self.Inventory = ["shirts","pants"]

    def addInventoryItem(self, newItem):
        self.Inventory.append(newItem)

    def changeHP(self, changeinHP):
        super(PlayerCharacter, self).changeHP(changeinHP)
        if self.currentHP <= 0:
            self.lives -= 1
            if self.lives < 0:
                self.lives = 0
                self.currentHP = self.maxHP

newGameCharacter = GameCharacter("R1pHunt3r",100,1)
newGameCharacter.changeHP(-50)
# print(newGameCharacter.name)
print(newGameCharacter.currentHP)
print(newGameCharacter.lives)
# print(newGameCharacter.xPos)
# newGameCharacter.changeHP(-60)
# print(newGameCharacter.currentHP)
# newGameCharacter.changePos(49)
# print(newGameCharacter.xPos)

newPlayer = PlayerCharacter("R1pHunt3r",120,2)
print(newPlayer.currentHP)
print(newPlayer.lives)

newPlayer.addInventoryItem("boot")
print(newPlayer.Inventory)

newPlayer.changeHP(-130)
print(newPlayer.currentHP)
print(newPlayer.lives)