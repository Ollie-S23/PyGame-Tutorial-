import pygame 
pygame.init() #initializes the pygame module, which is necessary before using any of its functions.

screenWidth = 500
screenHeight = 500

#Window size
#                                  w             h
win = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("First Game")

#sprites
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

#character variables
starting_x = 50
starting_y = 10
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
    #                       r   g   b   
    pygame.draw.rect(win, (0, 255, 0), (starting_x, starting_y, width, height))
    pygame.display.update()


run = True

#main loop
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    #movement keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and starting_x > vel:
        starting_x -= vel
    if keys[pygame.K_RIGHT] and starting_x < screenWidth - width - vel:
        starting_x += vel
    if (not isJump):
        # if keys[pygame.K_UP] and starting_y > vel:
        #     starting_y -= vel
        # if keys[pygame.K_DOWN] and starting_y < screenHeight - height - vel:
        #     starting_y += vel
        if keys[pygame.K_SPACE] and not isJump:
            isJump = True
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