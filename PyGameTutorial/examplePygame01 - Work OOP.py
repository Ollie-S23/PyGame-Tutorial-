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
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y))

class Projectile(object):
    def __init__(self, x, y, radius, color, facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

#functions
def redrawGameWindow():
    win.blit(bg, (0,0)) 
    player.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


player = Player(300, 410, 64, 64) #64 x 64 is the size of the character sprite
bullets = []

run = True

#main loop
while run:
    clock.tick(27) #FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    for bullet in bullets:
        if bullet.x < screenWidth and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.pop(bullets.index(bullet))

    #shooting keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        bullet_amount = 5
        if player.left:
                facing = -1
        else:
                facing = 1
        if len(bullets) < bullet_amount:
            bullet_radius = 6
            bullets.append(Projectile(round(player.x + player.width // 2), round(player.y + player.height // 2), bullet_radius, (0,0,0), facing))

    #movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.x > player.vel:
        player.x -= player.vel
        player.left = True
        player.right = False
        player.standing = False
    elif keys[pygame.K_RIGHT] and player.x < screenWidth - player.width - player.vel:
        player.x += player.vel
        player.left = False
        player.right = True
        player.standing = False
    else:
        player.standing = True
        player.walkCount = 0
    if (not player.isJump):
        if keys[pygame.K_UP] and not player.isJump:
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