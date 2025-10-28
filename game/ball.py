import pygame
from dataclasses import dataclass

@dataclass
class Ball:
    x: float
    y: float
    radius: int
    velocity_x: float
    velocity_y: float
    rect: pygame.Rect = None

    def __post_init__(self):
        self.rect = pygame.Rect(int(self.x - self.radius), int(self.y - self.radius),
                                self.radius * 2, self.radius * 2)

    def reset(self, x, y, vx=7, vy=0):
        self.x = x
        self.y = y
        self.velocity_x = vx
        self.velocity_y = vy
        self.rect.topleft = (int(self.x - self.radius), int(self.y - self.radius))

    def update(self, paddles, screen_rect, sounds):
        """
        Move ball, handle collisions:
         - Check wall collisions (top/bottom) -> reverse velocity_y
         - Move first, then check paddle collisions using rect overlap
           (important for high speed).
         - If collision with paddle, reverse velocity_x and play paddle sound.
         - If ball goes out left/right, return 'left' or 'right' to indicate scoring.
        """
        prev_vx = self.velocity_x
        prev_vy = self.velocity_y

        # Move ball by velocity
        self.x += self.velocity_x
        self.y += self.velocity_y
        self.rect.topleft = (int(self.x - self.radius), int(self.y - self.radius))

        # Wall collision (top/bottom)
        if self.rect.top <= screen_rect.top:
            self.rect.top = screen_rect.top
            self.y = self.rect.centery
            self.velocity_y = -self.velocity_y
        elif self.rect.bottom >= screen_rect.bottom:
            self.rect.bottom = screen_rect.bottom
            self.y = self.rect.centery
            self.velocity_y = -self.velocity_y

        # Play wall bounce sound if vertical direction changed
        if prev_vy != self.velocity_y and sounds.get("wall_bounce"):
            sounds["wall_bounce"].play()

        # Paddle collisions: check each paddle AFTER moving
        for paddle in paddles:
            if self.rect.colliderect(paddle.rect):
                # Determine from which side and adjust position to avoid tunneling
                if self.velocity_x > 0:
                    # moving right, hit right player's paddle -> place ball to left of paddle
                    self.rect.right = paddle.rect.left
                else:
                    # moving left, hit left player's paddle -> place ball to right of paddle
                    self.rect.left = paddle.rect.right

                # update x position floats
                self.x = self.rect.centerx

                # Reverse X velocity and slightly increase speed
                self.velocity_x = -self.velocity_x
                # Optionally slightly increase speed to make game more interesting:
                # keep sign of velocity
                if abs(self.velocity_x) < 25:
                    self.velocity_x *= 1.03

                # Add spin based on where it hit the paddle (optional)
                offset = (self.rect.centery - paddle.rect.centery) / (paddle.rect.height / 2)
                self.velocity_y += offset * 2.0

                # Play paddle hit sound
                if sounds.get("paddle_hit"):
                    sounds["paddle_hit"].play()

                break  # only handle one paddle collision per frame

        # Play sound if horizontal direction changed (paddle bounce)
        if prev_vx != self.velocity_x and sounds.get("paddle_hit") and prev_vx != 0:
            # already played above but this ensures any other change triggers sound
            pass

        # Check scoring: went off left or right side
        if self.rect.right < screen_rect.left:
            # Right player scores
            if sounds.get("score"):
                sounds["score"].play()
            return "right"
        elif self.rect.left > screen_rect.right:
            # Left player scores
            if sounds.get("score"):
                sounds["score"].play()
            return "left"

        return None

    def draw(self, surface):
        pygame.draw.ellipse(surface, (255, 255, 255), self.rect)
