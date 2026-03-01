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

#character variables
starting_x = 10 #left and right
starting_y = 400 #up and down 
width = 64 #based on the size of the character sprite
height = 64 #based on the size of the character sprite
vel = 5
#Movement variables
isJump = False
jumpCount = 10
player_left = False
player_right = False
WalkCount = 0

#functions
def redrawGameWindow():
    global WalkCount
    
    win.blit(bg, (0,0)) 
    if WalkCount + 1 >= 27:
        WalkCount = 0
    if player_left:
        win.blit(walkLeft[WalkCount//3], (starting_x, starting_y))
        WalkCount += 1
    elif player_right:
        win.blit(walkRight[WalkCount//3], (starting_x, starting_y))
        WalkCount += 1
    else:
        win.blit(char, (starting_x, starting_y))
    pygame.display.update()


run = True

#main loop
while run:
    clock.tick(27) #FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and starting_x > vel:
        starting_x -= vel
        player_left = True
        player_right = False
    elif keys[pygame.K_RIGHT] and starting_x < screenWidth - width - vel:
        starting_x += vel
        player_left = False
        player_right = True
    else:
        player_left = False
        player_right = False
        WalkCount = 0
    if (not isJump):
        # if keys[pygame.K_UP] and starting_y > vel:
        #     starting_y -= vel
        # if keys[pygame.K_DOWN] and starting_y < screenHeight - height - vel:
        #     starting_y += vel
        if keys[pygame.K_SPACE] and not isJump:
            isJump = True
            player_right = False
            player_left = False
            WalkCount = 0
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            starting_y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
            
        else:
            isJump = False
            jumpCount = 10

    #added func
    redrawGameWindow()
pygame.quit()