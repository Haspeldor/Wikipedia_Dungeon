# import pygame module in this program 
import pygame 
 
# activate the pygame library 
# initiate pygame and give permission 
# to use pygame's functionality. 
pygame.init() 
clock = pygame.time.Clock()
 
# assigning values to X and Y variable 
X = 1920
Y = 1080 
  
# defining colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
ocean = (0, 255, 255)
purple = (255, 0, 255)
yellow = (255, 255, 0)


# create the display surface object 
# of specific dimension..e(X, Y). 
display_surface = pygame.display.set_mode((X, Y ), pygame.FULLSCREEN)
  
# set the pygame window name 
pygame.display.set_caption('Wiki Dungeon') 
  
# create a font object. 
# 1st parameter is the font file 
# which is present in pygame. 
# 2nd parameter is size of the font 
font = pygame.font.Font('freesansbold.ttf', 11) 
  
# create a text suface object, 
# on which text is drawn on it. 
text = font.render("section", True, (200, 200, 200)) 
  
# create a rectangular object for the 
# text surface object 
textRect = text.get_rect()  
  
# set the center of the rectangular object. 
textRect.center = (X // 2, Y // 2) 
  
walls_white = pygame.Rect(98, 98, 1724, 884)
walls_black = pygame.Rect(100, 100, 1720, 880)

# infinite loop 
while True : 

   # iterate over the list of Event objects 
    # that was returned by pygame.event.get() method. 
    for event in pygame.event.get() : 

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pygame.QUIT : 
  
            # deactivates the pygame library 
            pygame.quit() 
  
            # quit the program. 
            quit() 
  
    clock.tick(30)
  
    # completely fill the surface object 
    # with white color 
    display_surface.fill(black)

    pygame.draw.rect(display_surface, white, walls_white)
    pygame.draw.rect(display_surface, black, walls_black)

    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    display_surface.blit(text, textRect) 
 
    # Draws the surface object to the screen.   
    pygame.display.update()