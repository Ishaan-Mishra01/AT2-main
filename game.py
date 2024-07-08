import pygame
from menu import MainMenu
from character_select import CharacterSelect
from map import Map
from assets import load_assets, GAME_ASSETS
from LoseScreen import loseScreen
from character import Character

class Game:
    def __init__(self):
        pygame.init()
        load_assets()  # load the game image assets
        self.window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.menu = MainMenu(self.window)  # Create an instance of the MainMenu class
        self.character_select = CharacterSelect(self.window)  # Create an instance of the CharacterSelect class
        self.state = 'menu'  # Set the initial state to 'menu'
        self.current_character = None  # To store the chosen character
        self.health_bar = None  # Initialize health bar

    def run(self):
        while True:
            if self.state == 'menu':  # If the state is 'menu'
                result = self.menu.run()  # Run the menu and get the result
                if result == 'Start Game':  # If the result is 'Start Game'
                    self.state = 'character_select'  # Change the state to 'character_select'
                elif result == 'Settings':  # If the result is 'Settings'
                    pass  # Settings handling would go here
                elif result == 'Exit':  # If the result is 'Exit'
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method

            elif self.state == 'character_select':  # If the state is 'character_select'
                selected_character_class = self.character_select.run()  # Run the character select screen and get the selected character class
                if selected_character_class == 'back':  # If the selected character class is 'back'
                    self.state = 'menu'  # Change the state to 'menu'
                elif selected_character_class:  # If a character class is selected
                    self.current_character = Character("Player", selected_character_class, "Basic Armor")  # Set the current character to the selected character
                    self.game_map = Map(self.window)  # Re-initialize the Map class
                    self.game_map.load_player(selected_character_class)  # Load the selected character into the game map
                    self.health_bar = self.game_map.health_bar  # Initialize health bar with the one from game_map
                    self.state = 'game_map'  # Change the state to 'game_map'

            elif self.state == 'game_map':  # If the state is 'game_map'
                result = self.game_map.handle_events()  # Handle events in the game map and get the result
                if result == 'back':  # If the result is 'back'
                    self.state = 'character_select'  # Change the state to 'character_select'
                elif result == 'quit':  # If the result is 'quit'
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method
                elif result == 'lose':  # If the result is 'lose'
                    self.state = 'lose_screen'
                else:
                    self.game_map.draw()  # Draw the game map
                    if self.health_bar:
                        self.health_bar.update()  # Update the health bar
                        self.health_bar.draw(self.window)  # Draw the health bar

            elif self.state == 'lose_screen':
                lose_screen = loseScreen(self.window)
                result = lose_screen.run()  # Run the lose screen and get the result
                if result == 'menu':  # If result is menu from lose screen
                    self.state = 'menu'  # Change state back to 'menu'

            for event in pygame.event.get():  # Iterate over the events in the event queue
                if event.type == pygame.QUIT:  # If the event type is QUIT
                    pygame.quit()  # Quit pygame
                    return  # Exit the run method
            
if __name__ == "__main__":
    game = Game()  # Create an instance of the Game class
    game.run()  # Run the game