import random
import pygame
from assets import GAME_ASSETS
from enemy import Enemy
from character import Character

class HealthBar:
    def __init__(self, x, y, w, h, player):
        """
        Initialize the HealthBar.

        Args:
            x (int): The x-coordinate of the health bar.
            y (int): The y-coordinate of the health bar.
            w (int): The width of the health bar.
            h (int): The height of the health bar.
            player (Character): The player character instance.
        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.player = player  # The player character instance
        self.initial_max_hp = player.max_hp  # Store the initial max health of the player
        self.current_hp = player.hit_points

    def update(self):
        """Update the current health based on the player's health."""
        self.current_hp = self.player.hit_points

    def draw(self, screen):
        """Draw the health bar on the screen."""
        # Calculate health percentage based on initial max health
        health_percentage = self.current_hp / self.initial_max_hp
        current_width = int(self.width * health_percentage)

        # Draw the background bar (empty health)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # Draw the foreground bar (current health)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, current_width, self.height))


class StaminaBar:
    def __init__(self, x, y, w, h, player):
        """
        Initialize the StaminaBar.

        Args:
            x (int): The x-coordinate of the stamina bar.
            y (int): The y-coordinate of the stamina bar.
            w (int): The width of the stamina bar.
            h (int): The height of the stamina bar.
            player (Character): The player character instance.
        """
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.player = player
        self.max_stamina = player.max_stamina
        self.current_stamina = player.stamina

    def update(self):
        self.current_stamina = self.player.stamina

    def draw(self, screen):
        stamina_percentage = self.current_stamina / self.max_stamina
        current_width = int(self.width * stamina_percentage)
        pygame.draw.rect(screen, (255, 255, 0), (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, (0, 0, 255), (self.x, self.y, current_width, self.height))


class Map:
    EXPERIENCE_POINTS_PER_ENEMY = 100

    def __init__(self, window, level = 1):
        """
        Initialize the Map class.

        Args:
            window (pygame.Surface): The game window surface.
        """
        self.health_bar = None
        self.stamina_bar = None
        self.window = window
        self.level = level
        self.load_map()
        self.load_player_images()
        self.player_position = [self.window.get_width() / 2, self.window.get_height() / 2]
        self.enemies = self.spawn_enemies()
        self.in_combat = False
        self.current_enemy = None
        self.blue_orb = None
        self.game_over = False

    def load_map(self):
        map_key = "dungeon_map" if self.level == 1 else "dungeon_map_two"
        self.map_image = pygame.image.load(GAME_ASSETS[map_key]).convert_alpha()
        self.map_image = pygame.transform.scale(self.map_image, (self.window.get_width(), self.window.get_height()))

    def load_player_images(self):
        self.player_images = {
            'Warrior': pygame.image.load(GAME_ASSETS['knight']).convert_alpha(),
            'Mage': pygame.image.load(GAME_ASSETS['mage']).convert_alpha(),
            'Rogue': pygame.image.load(GAME_ASSETS["rogue"]).convert_alpha()
        }

    def spawn_enemies(self):
        if self.level == 1:
            return [
                Enemy(GAME_ASSETS["4_enemies_1_idle_002"], [50, 50], self.window),
                Enemy(GAME_ASSETS["9_enemies_1_idle_002"], [self.window.get_width() - 120, 50], self.window),
                Enemy(GAME_ASSETS["3_enemies_1_idle_002"], [50, self.window.get_height() - 120], self.window),
                Enemy(GAME_ASSETS["3_enemies_1_attack_004"], [self.window.get_width() - 120, self.window.get_height() - 120], self.window)
            ]
        elif self.level == 2:
            return [
                Enemy(GAME_ASSETS["4_enemies_1_attack_011"], [150, 150], self.window),
                Enemy(GAME_ASSETS["9_enemies_1_idle_018"], [self.window.get_width() - 220, 150], self.window),
                Enemy(GAME_ASSETS["9_enemies_1_attack_006"], [150, self.window.get_height() - 220], self.window),
                Enemy(GAME_ASSETS["3_enemies_1_idle_009"], [self.window.get_width() - 220, self.window.get_height() - 220], self.window),
                Enemy(GAME_ASSETS["3_enemies_1_idle_002"], [self.window.get_width() // 2+ 50, self.window.get_height() // 2+ 50], self.window)
            ]
    
    def load_player(self, character_type):
        """
        Load the player character.

        Args:
            character_type (str): The type of character to load.
        """
        self.player_type = character_type
        self.player_image = self.player_images[character_type]
        self.player_image = pygame.transform.scale(self.player_image, (int(self.player_image.get_width()), int(self.player_image.get_height())))
        self.player = Character("Player", character_type, 5)
        self.player_death = False
        self.health_bar = HealthBar(10, 10, 200, 20, self.player)
        self.stamina_bar = StaminaBar(10, 35, 200, 15, self.player)

    def check_for_combat(self):
        """
        Check if the player is in combat with any enemy.

        Returns:
            bool: True if the player is in combat, False otherwise.
        """
        for enemy in self.enemies:
            if pygame.math.Vector2(enemy.position).distance_to(self.player_position) < 50:
                self.in_combat = True
                self.current_enemy = enemy
                return True
        return False


    def handle_combat(self):
        if self.in_combat and self.current_enemy:
            '''
            current_fighter = 1
            total_fighters = 2
            action_cooldown = 0
            action_wait_time = 90
            if self.player.is_alive() == True:
                if current_fighter ==1:
                    action_cooldown+=1
                    if action_cooldown>=action_wait_time:
                        self.player.
            '''
            player_damage = random.randint(5, 10) * self.level
            enemy_defeated = self.current_enemy.take_damage(player_damage)
            print(f"Player attacks! Deals {player_damage} damage to the enemy. Enemy has {self.current_enemy.health} health.")
            if enemy_defeated:
                print("Enemy defeated!")
                self.enemies.remove(self.current_enemy)
                self.in_combat = False
                self.current_enemy = None
                self.player.gain_experience(Map.EXPERIENCE_POINTS_PER_ENEMY)
                if not self.enemies:
                    self.spawn_blue_orb()
            else:
                enemy_damage = random.randint(4, 9)
                print(f"Enemy attacks back! Deals {enemy_damage} damage to the player.")
                self.player.take_damage(enemy_damage)

            if self.player.is_alive == False:
                self.player_death = True
                return 'lose'  # Return 'lose' when the player's health is 0 or less
            self.health_bar.update()


    def draw(self):
        """
        Draw the game objects on the window.
        """
        self.window.fill((0, 0, 0))
        self.window.blit(self.map_image, (0, 0))
        self.window.blit(self.player_image, (self.player_position[0], self.player_position[1]))
        for enemy in self.enemies:
            enemy.draw()
        if self.blue_orb:
            self.window.blit(self.blue_orb, self.orb_position)
        self.health_bar.draw(self.window)
        self.stamina_bar.draw(self.window)
        pygame.display.flip()

    def spawn_blue_orb(self):
        """
        Spawn the blue orb in the center of the map.
        """
        self.blue_orb = pygame.image.load(GAME_ASSETS["blue_orb"]).convert_alpha()
        self.blue_orb = pygame.transform.scale(self.blue_orb, (50, 50))
        self.orb_position = [self.window.get_width() / 2, self.window.get_height() / 2]

    def check_orb_collision(self):
        """
        Check if the player has collided with the blue orb.

        Returns:
            bool: True if the player has collided with the blue orb, False otherwise.
        """
        if self.blue_orb and pygame.math.Vector2(self.orb_position).distance_to(self.player_position) < 25:
            if self.level == 1:
                print("Level 1 complete!")
                return 'next_level'
            else:
                self.game_over = True
                print("YOU WIN")
                return 'quit'
        return False

    def handle_events(self):
        """
        Handle user input events.
        
        Returns:
            str: 'quit' if the game is over and should be exited, None otherwise.
        """
        if self.game_over:
            return 'lose'  # Stop processing events if game is over
        #

        keys = pygame.key.get_pressed()
        move_speed = 1
        if keys[pygame.K_ESCAPE]:
            pygame.quit()
        if keys[pygame.K_LEFT]:
            self.player_position[0] -= move_speed
            if self.player_position[0] <= -28:
                self.player_position[0] = -28
        if keys[pygame.K_RIGHT]:
            self.player_position[0] += move_speed
            if self.player_position[0] >= 1350:
                self.player_position[0] = 1350
        if keys[pygame.K_UP]:
            self.player_position[1] -= move_speed
            if self.player_position[1] <= -48:
                self.player_position[1] = -48
        if keys[pygame.K_DOWN]:
            self.player_position[1] += move_speed
            if self.player_position[1] >= 790:
                self.player_position[1] = 790

        if not self.in_combat:
            if self.check_for_combat():
                return
        self.handle_combat()

        orb_collision_result = self.check_orb_collision()
        if orb_collision_result:
            return orb_collision_result

    def update(self):
        self.health_bar.update()
        self.stamina_bar.update()
        self.draw()
