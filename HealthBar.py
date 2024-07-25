import pygame

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
        self.max_hp = player.max_hp  # Access max_hp from the player character
        self.current_hp = player.hit_points

    def update(self):
        """Update the current health based on the player's health."""
        self.current_hp = self.player.hit_points

    def draw(self, screen):
        """Draw the health bar on the screen."""
        # Calculate health percentage
        health_percentage = self.current_hp / self.max_hp
        current_width = int(self.width * health_percentage)

        # Draw the background bar (empty health)
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # Draw the foreground bar (current health)
        pygame.draw.rect(screen, (0, 255, 0), (self.x, self.y, current_width, self.height))