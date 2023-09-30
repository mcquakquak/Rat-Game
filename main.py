import pygame, sys
from pygame.locals import QUIT

#Assignment 1
#Draw Out The Target Logo Using Circles

#__SETUP__#
pygame.init()
#--Resolution--#
DISPLAYSURF = pygame.display.set_mode((1000, 720))
#--Tab_Name--#
pygame.display.set_caption('Player Class')
#--Frames_Per_Second--#
clock = pygame.time.Clock()

#ADD MORE LATER, SOUND EFFECT, AND ANIMATIONS
#Get hitboxes --
#Make a loop to check if rat touched hitbox of meat grinder --
#If rat touched meat grinder, rat.png turn into deadRat.png, meat grinder will have meat in it --


class Player(pygame.sprite.Sprite):

    #Implement additinoal parameters, so you can spawn slimes in different coordinates

    #---Init Method---#
    def __init__(self, x, y, speed, sizeX=50, sizeY=50, skin="slime.png"):
        pygame.sprite.Sprite.__init__(self)
        #---Properties---#
        self.image = pygame.image.load(skin)
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    #---Update---#
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:  # down key
            self.rect.y += self.speed  # move down
        elif key[pygame.K_UP]:  # up key
            self.rect.y -= self.speed  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.rect.x += self.speed  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.rect.x -= self.speed  # move left

    #--ChangeSkin--#
    def skinChanger(self, newSkin, sizeX=100, sizeY=100):
        self.image = pygame.image.load(newSkin)
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))


class Obsticle(pygame.sprite.Sprite):

    def __init__(self,
                 x=200,
                 y=300,
                 sizeX=200,
                 sizeY=200,
                 image="meatGrinder.png"):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (sizeX, sizeY))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


#Create a sprite group
playerGroup = pygame.sprite.Group()
meatgrinderGroup = pygame.sprite.Group()
#Genearating a player from your class
question = input("Rattituy or chiken or sliime (R C S)")

if question == "R":
    permSkin = "rat.png"
    character = Player(50, 50, 9, 200, 200, permSkin)
elif question == "C":
    permSkin = "chicky.png"
    character = Player(50, 50, 9, permSkin)
elif question == "S":
    permSkin = "slime.png"
    character = Player(50, 50, 9, permSkin)
else:
    character = Player(50, 50, 9)

meatGrinder = Obsticle()

playerGroup.add(character)
meatgrinderGroup.add(meatGrinder)

while True:
    #__Infinite Loop__#
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    character.update()

    #Refill background
    DISPLAYSURF.fill((240, 240, 240))

    #DRAW ENTITITES
    playerGroup.draw(DISPLAYSURF)
    meatgrinderGroup.draw(DISPLAYSURF)

    #Checking collision
    ifColided = pygame.sprite.spritecollideany(character, meatgrinderGroup)

    if ifColided != None:
        character.skinChanger("ground_beef.jpg")

    pygame.display.flip()
    clock.tick(60)
