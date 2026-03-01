import pygame 
pygame.init() #initializes the pygame module, which is necessary before using any of its functions.

screenWidth = 500
screenHeight = 480

#Window size
#                                  w             h
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

#sprites
walkRight = [pygame.image.load('Assets/Images/Sprites/R1.png'), pygame.image.load('Assets/Images/Sprites/R2.png'), pygame.image.load('Assets/Images/Sprites/R3.png'), pygame.image.load('Assets/Images/Sprites/R4.png'), pygame.image.load('Assets/Images/Sprites/R5.png'), pygame.image.load('Assets/Images/Sprites/R6.png'), pygame.image.load('Assets/Images/Sprites/R7.png'), pygame.image.load('Assets/Images/Sprites/R8.png'), pygame.image.load('Assets/Images/Sprites/R9.png')]
walkLeft = [pygame.image.load('Assets/Images/Sprites/L1.png'), pygame.image.load('Assets/Images/Sprites/L2.png'), pygame.image.load('Assets/Images/Sprites/L3.png'), pygame.image.load('Assets/Images/Sprites/L4.png'), pygame.image.load('Assets/Images/Sprites/L5.png'), pygame.image.load('Assets/Images/Sprites/L6.png'), pygame.image.load('Assets/Images/Sprites/L7.png'), pygame.image.load('Assets/Images/Sprites/L8.png'), pygame.image.load('Assets/Images/Sprites/L9.png')]
bg = pygame.image.load('Assets/Images/bg.jpg')
char = pygame.image.load('Assets/Images/Sprites/standing.png')

clock = pygame.time.Clock()

class Player(object):
    def __init__(self, x, y, width, height):
        self.x = x #left and right
        self.y = y #up and down 
        self.width = width #based on the size of the character sprite
        self.height = height #based on the size of the character sprite

        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if self.left:
            win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        elif self.right:
            win.blit(walkRight[self.walkCount//3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(char, (self.x, self.y))

#functions
def redrawGameWindow():
    win.blit(bg, (0,0)) 
    player.draw(win)
    pygame.display.update()


player = Player(300, 410, 64, 64) #64 x 64 is the size of the character sprite

run = True

#main loop
while run:
    clock.tick(27) #FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.vel:
        player.x += player.vel
        player.left = False
        player.right = True
    else:
        player.left = False
        player.right = False
        player.walkCount = 0
    if (not player.isJump):
        if keys[pygame.K_SPACE] and not player.isJump:
            player.isJump = True
            player.right = False
            player.left = False
            player.walkCount = 0
    else:
        if player.jumpCount >= -10:
            neg = 1
            if player.jumpCount < 0:
                neg = -1
            player.y -= (player.jumpCount ** 2) * 0.5 * neg
            player.jumpCount -= 1
            
        else:
            player.isJump = False
            player.jumpCount = 10

    #added func
    redrawGameWindow()
pygame.quit()