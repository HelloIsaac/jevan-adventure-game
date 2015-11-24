# ---------------- Initial Set-Up ---------------- #

#Import Pygame Library
import pygame

#Initialise Game Engine
pygame.init()

#Set Screen Size + Name
screensize = [700,500]
screen = pygame.display.set_mode(screensize)

pi = 3.1415926535897323

pygame.display.set_caption("Jevan Pipitone's Wild Adventure")

# ---------------- Colour & Font Definitions ---------------- #

#Define Some Colours
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)
sky = (51, 153, 255)
sun = (255, 153, 51)

mainFont = pygame.font.Font("C:/Windows/Fonts/comic.ttf", 25)
# ---------------- Done Loop / Clock ---------------- #

#Loop Game Until Closed
done = False

#Set Clock
clock=pygame.time.Clock()

# ---------------- Main Game Loop ---------------- #
while done == False:
    #ALL EVENT PROCESSING SHOULD GO BELOW THIS COMMENT
    for event in pygame.event.get(): # User Did Something
        if event.type == pygame.QUIT: #If They Quit,
            done = True #Flag Done as True to Exit
    #ALL EVENT PROCESSING SHOULD GO ABOVE THIS COMMENT


    #ALL GAME LOGIC SHOULD GO BELOW THIS COMMENT


    #ALL GAME LOGIC SHOULD GO ABOVE THIS COMMENT


    #ALL GAME DRAWING SHOULD GO BELOW THIS COMMENT
    screen.fill(black)

    for x in range(0, 730, 20):
        pygame.draw.line(screen, sky, [x, 0], [x, 500], 5)

    pygame.draw.rect(screen, red, [130, 130, 200, 220] )
    #pygame.draw.circle(screen, sun, [630, 65], 45)
    #pygame.draw.arc(screen, green, [100, 100, 250, 200], pi/2, pi, 2)
    pygame.draw.polygon(screen, white, [[120, 140], [230, 20], [340, 140], 5])

    #Text
    shopText = mainFont.render("Thai Cat Salon", True, green)
    screen.blit(shopText, [140, 145])

    #Final Flip = Display
    pygame.display.flip()
    #ALL GAME DRAWING SHOULD GO ABOVE THIS COMMENT


    #Set Clock at 20 FPS
    clock.tick(20)

# Quits Game When Done
pygame.quit()