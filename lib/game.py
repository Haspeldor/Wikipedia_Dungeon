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
exit_font = pygame.font.Font('freesansbold.ttf', 22) 
  
# create a text suface object, 
# on which text is drawn on it. 
exit1_text = exit_font.render("section", True, (200, 200, 200)) 
exit1_text = pygame.transform.rotozoom(exit1_text, 0, 1)
exit2_text = exit_font.render("section", True, (200, 200, 200)) 
exit2_text = pygame.transform.rotozoom(exit2_text, 0, 1)
exit3_text = exit_font.render("section", True, (200, 200, 200)) 
exit3_text = pygame.transform.rotozoom(exit3_text, 90, 1)
exit4_text = exit_font.render("section", True, (200, 200, 200)) 
exit4_text = pygame.transform.rotozoom(exit4_text, 270, 1)

# create a rectangular object for the 
# text surface object 
  
textRect1 = exit1_text.get_rect()  
textRect2 = exit2_text.get_rect()  
textRect3 = exit3_text.get_rect()  
textRect4 = exit4_text.get_rect()  

# set the center of the rectangular object. 
textRect1.center = (960, 50) 
textRect2.center = (960, 1030) 
textRect3.center = (50, 540) 
textRect4.center = (1870, 540) 
  
walls_white = pygame.Rect(98, 98, 1724, 884)
walls_black = pygame.Rect(100, 100, 1720, 880)
exit1 = pygame.Rect(885, 100, 150, 50)
exit2 = pygame.Rect(885, 930, 150, 50)
exit3 = pygame.Rect(100, 465, 50, 150)
exit4 = pygame.Rect(1770, 465, 50, 150)

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
    pygame.draw.rect(display_surface, green, exit1)
    pygame.draw.rect(display_surface, green, exit2)
    pygame.draw.rect(display_surface, green, exit3)
    pygame.draw.rect(display_surface, green, exit4)


    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    display_surface.blit(exit1_text, textRect1) 
    display_surface.blit(exit2_text, textRect2) 
    display_surface.blit(exit3_text, textRect3) 
    display_surface.blit(exit4_text, textRect4) 
 
    # Draws the surface object to the screen.   
    pygame.display.update()