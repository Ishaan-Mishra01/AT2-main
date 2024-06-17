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
        self.LOSE_TEXT = makeFont(100).render("You Died!", True, "#93221c")
        self.LOSE_TEXT_RECT = self.LOSE_TEXT.get_rect(center=(self.window.get_width() // 2, 100))

        self.MENU_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(self.window.get_width() // 2, 400), 
                                  text_input="Main Menu", font=makeFont(75), base_color="#20148f", hovering_color="White")
        self.QUIT_BUTTON = Button(image=pygame.image.load("Quit Rect.png"), pos=(self.window.get_width() // 2, 550), 
                                  text_input="Quit", font=makeFont(75), base_color="#20148f", hovering_color="White")

    def run(self):
        mouse_pos = pygame.mouse.get_pos()
        running = True

        while running:
            self.window.blit(self.scaled_background, (0, 0))
            self.window.blit(self.LOSE_TEXT, self.LOSE_TEXT_RECT)
            for button in [self.MENU_BUTTON, self.QUIT_BUTTON]:
                button.changeColor(mouse_pos)
                button.update(self.window)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.MENU_BUTTON.checkForInput(event.pos):
                        return 'menu'  # Return 'menu' when Main Menu button is clicked
                    if self.QUIT_BUTTON.checkForInput(event.pos):
                        pygame.quit()
                        sys.exit()
            mouse_pos = pygame.mouse.get_pos()
