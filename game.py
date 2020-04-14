# import pygame module in this program 
import pygame 
from character import Character
 
class TextRectException:
    def __init__(self, message = None):
        self.message = message
    def __str__(self):
        return self.message

class Game():

    def __init__(self, level):
        pygame.init()
        self.player = Character()
        self.load_room(level.starting_room)

    def render_textrect(self, string, font, rect, text_color, background_color, justification=0):
        """Returns a surface containing the passed text string, reformatted
        to fit within the given rect, word-wrapping as necessary. The text
        will be anti-aliased.

        Takes the following arguments:

        string - the text you wish to render. \n begins a new line.
        font - a Font object
        rect - a rectstyle giving the size of the surface requested.
        text_color - a three-byte tuple of the rgb value of the
                    text color. ex (0, 0, 0) = BLACK
        background_color - a three-byte tuple of the rgb value of the surface.
        justification - 0 (default) left-justified
                        1 horizontally centered
                        2 right-justified

        Returns the following values:

        Success - a surface object with the text rendered onto it.
        Failure - raises a TextRectException if the text won't fit onto the surface.
        """
        
        final_lines = []

        requested_lines = string.splitlines()

        # Create a series of lines that will fit on the provided
        # rectangle.

        for requested_line in requested_lines:
            if font.size(requested_line)[0] > rect.width:
                words = requested_line.split(' ')
                # if any of our words are too long to fit, return.
                for word in words:
                    if font.size(word)[0] >= rect.width:
                        raise TextRectException("The word " + word + " is too long to fit in the rect passed.")
                # Start a new line
                accumulated_line = ""
                for word in words:
                    test_line = accumulated_line + word + " "
                    # Build the line while the words fit.    
                    if font.size(test_line)[0] < rect.width:
                        accumulated_line = test_line 
                    else: 
                        final_lines.append(accumulated_line) 
                        accumulated_line = word + " " 
                final_lines.append(accumulated_line)
            else: 
                final_lines.append(requested_line) 

        # Let's try to write the text out on the surface.

        surface = pygame.Surface(rect.size) 
        surface.fill(background_color) 

        accumulated_height = 0 
        for line in final_lines: 
            if accumulated_height + font.size(line)[1] >= rect.height:
                raise TextRectException("Once word-wrapped, the text string was too tall to fit in the rect.")
            if line != "":
                tempsurface = font.render(line, 1, text_color)
                if justification == 0:
                    surface.blit(tempsurface, (0, accumulated_height))
                elif justification == 1:
                    surface.blit(tempsurface, ((rect.width - tempsurface.get_width()) / 2, accumulated_height))
                elif justification == 2:
                    surface.blit(tempsurface, (rect.width - tempsurface.get_width(), accumulated_height))
                else:
                    raise TextRectException("Invalid justification argument: " + str(justification))
            accumulated_height += font.size(line)[1]

        return surface


# is called when a new room is entered and needs to be loaded
    def load_room(self, room, x_pos=935, y_pos=500):
        exit_font = pygame.font.Font('freesansbold.ttf', 25)
        title_font = pygame.font.Font('freesansbold.ttf', 50)
        text_font = pygame.font.Font('freesansbold.ttf', 20)
        self.current_room = room
        self.player.spawn(x_pos, y_pos)
        self.title = title_font.render(self.current_room.title, True, (200, 200, 200)) 
        self.title_rect = self.title.get_rect()
        self.title_rect.center = (960, 200)
        self.text_rect = pygame.Rect(240, 270, 1440, 600)
        self.text = self.render_textrect(self.current_room.text, text_font, self.text_rect, (200, 200, 200), (0, 0, 0))
        self.exits = []
        self.exit_signs = []
        if self.current_room.top_exit:
            exit_text = exit_font.render(self.current_room.top_exit.title, True, (200, 200, 200)) 
            exit_text = pygame.transform.rotozoom(exit_text, 0, 1)
            text_rect = exit_text.get_rect()  
            text_rect.center = (960, 50) 
            self.exit_signs.append((exit_text, text_rect))
            exit_rect = pygame.Rect(885, 100, 150, 50)
            self.exits.append(exit_rect)
        if self.current_room.bottom_exit:
            exit_text = exit_font.render(self.current_room.bottom_exit.title, True, (200, 200, 200)) 
            exit_text = pygame.transform.rotozoom(exit_text, 0, 1)
            text_rect = exit_text.get_rect()  
            text_rect.center = (960, 1030) 
            self.exit_signs.append((exit_text, text_rect))
            exit_rect = pygame.Rect(885, 930, 150, 50)
            self.exits.append(exit_rect)
        if self.current_room.left_exit:
            exit_text = exit_font.render(self.current_room.left_exit.title, True, (200, 200, 200)) 
            exit_text = pygame.transform.rotozoom(exit_text, 90, 1)
            text_rect = exit_text.get_rect()  
            text_rect.center = (50, 540) 
            self.exit_signs.append((exit_text, text_rect))
            exit_rect = pygame.Rect(100, 465, 50, 150)
            self.exits.append(exit_rect)
        if self.current_room.right_exit:
            exit_text = exit_font.render(self.current_room.right_exit.title, True, (200, 200, 200)) 
            exit_text = pygame.transform.rotozoom(exit_text, 270, 1)
            text_rect = exit_text.get_rect()  
            text_rect.center = (1870, 540) 
            self.exit_signs.append((exit_text, text_rect))
            exit_rect = pygame.Rect(1770, 465, 50, 150)
            self.exits.append(exit_rect)

# starts the game
    def start_game(self):
           
        # activate the pygame library 
        # initiate pygame and give permission 
        # to use pygame's functionality. 
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
        
                # if event object type is QUIT 
                # then quitting the pygame 
                # and program both. 
                if event.type == pygame.QUIT : 
        
                    # deactivates the pygame library 
                    pygame.quit() 
        
                    # quit the program. 
                    quit()
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.player.move_up()
            if keys[pygame.K_DOWN]:
                self.player.move_down()
            if keys[pygame.K_LEFT]:
                self.player.move_left()
            if keys[pygame.K_RIGHT]:
                self.player.move_right()
        

            # manages the frame rate   
            clock.tick(30)
        
            # completely fill the surface object 
            # with black color 
            display_surface.fill(black)

            # draws the walls
            pygame.draw.rect(display_surface, white, walls_white)
            pygame.draw.rect(display_surface, black, walls_black)

            # draws the title and text
            display_surface.blit(self.title, self.title_rect)
            display_surface.blit(self.text, self.text_rect)

            # draws the exits and their text
            for exit_rect in self.exits:
                pygame.draw.rect(display_surface, green, exit_rect)
                
            for exit_text in self.exit_signs:
                display_surface.blit(exit_text[0], exit_text[1]) 
                
            # draws the character
            player_rect = pygame.Rect(self.player.x_pos, self.player.y_pos, self.player.x_size, self.player.y_size)
            pygame.draw.rect(display_surface, self.player.color, player_rect)

            # check for exit collision
            collision = player_rect.collidelistall(self.exits)
            if collision:
                if self.player.x_pos < 200:
                    self.load_room(self.current_room.left_exit)

                if self.player.x_pos > 1500:
                    self.load_room(self.current_room.right_exit)

                if self.player.y_pos < 200:
                    self.load_room(self.current_room.top_exit)

                if self.player.y_pos > 700:
                    self.load_room(self.current_room.bottom_exit)

           
            # Draws the surface object to the screen.   
            pygame.display.update()