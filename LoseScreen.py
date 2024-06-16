import pygame, sys
from assets import GAME_ASSETS
from button import Button

def makeFont(size):
    return pygame.font.Font("font.ttf", size)
    
class loseScreen():
    def __init__(self, window):
        self.window = window
        self.font = makeFont(36)
        self.background_image = pygame.image.load('LoseScreen.png')
        self.scaled_background = pygame.transform.scale(self.background_image, (self.window.get_width(), self.window.get_height()))
        self.LOSE_TEXT = makeFont(100).render("You Died !", True, "#93221c") #the variables have to be capitals because of the font apparently
        self.LOSE_TEXT_RECT = self.LOSE_TEXT.get_rect(center=(896, 80))
        self.BACK_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(896, 828), 
                                text_input="Back", font=makeFont(75), base_color="#20148f", hovering_color="White")
    
        
        

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        running = True

        while running:
            self.window.blit(self.scaled_background, (0, 0))
            self.window.blit(self.LOSE_TEXT, self.LOSE_TEXT_RECT)
            for button in [self.BACK_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.window)
            pygame.display.flip()

            for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if self.BACK_BUTTON.checkForInput(event.pos):
                            self.state = 'menu'
                            if self.state == 'menu':  # If the state is 'menu'
                                result = self.menu.run()  # Run the menu and get the result
                            if result == 'Start Game':  # If the result is 'Start Game'
                                self.state = 'character_select'  # Change the state to 'character_select'
                            elif result == 'Settings':  # If the result is 'Settings'
                                pass  # Settings handling would go here
                            elif result == 'Exit':  # If the result is 'Exit'
                                pygame.quit()  # Quit pygame
                                return  # Exit the run method