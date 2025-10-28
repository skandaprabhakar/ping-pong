import pygame
from dataclasses import dataclass

@dataclass
class Paddle:
    x: int
    y: int
    width: int
    height: int
    speed: float
    rect: pygame.Rect = None

    def __post_init__(self):
        self.rect = pygame.Rect(int(self.x), int(self.y), self.width, self.height)

    def move_ip(self, dx=0, dy=0):
        self.rect.x += int(dx)
        self.rect.y += int(dy)

    def update_player(self, dy, screen_rect):
        # dy is a delta movement (could be -speed or +speed)
        self.rect.y += int(dy)
        # Clamp to screen
        if self.rect.top < screen_rect.top:
            self.rect.top = screen_rect.top
        if self.rect.bottom > screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom

    def update_ai(self, ball, screen_rect):
        # Simple AI: move toward ball center, limit by speed
        if ball.rect.centery > self.rect.centery + 5:
            self.rect.y += int(self.speed)
        elif ball.rect.centery < self.rect.centery - 5:
            self.rect.y -= int(self.speed)

        # Clamp
        if self.rect.top < screen_rect.top:
            self.rect.top = screen_rect.top
        if self.rect.bottom > screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), self.rect)
