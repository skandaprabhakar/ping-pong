import pygame
import sys
from nall import Ball
from paddle import Paddle
import game_engin as ge

# --- Configuration ---
SCREEN_W = 900
SCREEN_H = 500
FPS = 60

# Sound filenames (place these .wav files in same folder):
PADDLE_HIT_WAV = "paddle_hit.wav"
WALL_BOUNCE_WAV = "wall_bounce.wav"
SCORE_WAV = "score.wav"

def load_sounds():
    sounds = {}
    try:
        sounds["paddle_hit"] = pygame.mixer.Sound(PADDLE_HIT_WAV)
    except Exception:
        sounds["paddle_hit"] = None
    try:
        sounds["wall_bounce"] = pygame.mixer.Sound(WALL_BOUNCE_WAV)
    except Exception:
        sounds["wall_bounce"] = None
    try:
        sounds["score"] = pygame.mixer.Sound(SCORE_WAV)
    except Exception:
        sounds["score"] = None
    return sounds

def reset_positions(ball, left_paddle, right_paddle):
    ball.reset(SCREEN_W // 2, SCREEN_H // 2, vx=7, vy=0)
    left_paddle.rect.center = (40, SCREEN_H // 2)
    right_paddle.rect.center = (SCREEN_W - 40, SCREEN_H // 2)

def main():
    pygame.init()
    # Initialize mixer before loading sounds
    try:
        pygame.mixer.init()
    except Exception:
        print("Warning: pygame.mixer could not be initialized; sound disabled.")

    screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont(None, 36)

    sounds = load_sounds()

    # Create objects
    ball = Ball(SCREEN_W // 2, SCREEN_H // 2, radius=8, velocity_x=7, velocity_y=0)
    left_paddle = Paddle(20, SCREEN_H // 2 - 40, width=12, height=80, speed=7)
    right_paddle = Paddle(SCREEN_W - 32, SCREEN_H // 2 - 40, width=12, height=80, speed=6)

    left_score = 0
    right_score = 0
    winning_score = 5  # default target

    screen_rect = screen.get_rect()

    running = True
    game_over = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Input
        keys = pygame.key.get_pressed()
        dy = 0
        if keys[pygame.K_w]:
            dy = -left_paddle.speed
        elif keys[pygame.K_s]:
            dy = left_paddle.speed
        left_paddle.update_player(dy, screen_rect)

        # Update AI
        right_paddle.update_ai(ball, screen_rect)

        # Update ball and get scoring result
        scorer = ball.update([left_paddle, right_paddle], screen_rect, sounds)

        if scorer == "right":
            right_score += 1
            # Reset ball to center moving toward the side that conceded
            ball.reset(SCREEN_W // 2, SCREEN_H // 2, vx=-7, vy=0)
        elif scorer == "left":
            left_score += 1
            ball.reset(SCREEN_W // 2, SCREEN_H // 2, vx=7, vy=0)

        # Check game over
        if left_score >= winning_score or right_score >= winning_score:
            game_over = True
            winner_is_player = left_score > right_score

        # Drawing
        screen.fill((0, 0, 0))
        # center line
        pygame.draw.line(screen, (100, 100, 100), (SCREEN_W // 2, 0), (SCREEN_W // 2, SCREEN_H), 2)
        left_paddle.draw(screen)
        right_paddle.draw(screen)
        ball.draw(screen)
        ge.draw_scores(screen, left_score, right_score, font)
        pygame.display.flip()

        # Game over handling
        if game_over:
            ge.show_game_over(screen, winner_is_player, font)

            # keep the loop running so players can see the message and choose replay
            choosing = True
            while choosing:
                for e in pygame.event.get():
                    if e.type == pygame.QUIT:
                        choosing = False
                        running = False
                    elif e.type == pygame.KEYDOWN:
                        if e.key == pygame.K_ESCAPE:
                            choosing = False
                            running = False
                        elif e.key == pygame.K_3:
                            winning_score = 2  # best of 3 -> first to 2
                            left_score = 0
                            right_score = 0
                            reset_positions(ball, left_paddle, right_paddle)
                            game_over = False
                            choosing = False
                        elif e.key == pygame.K_5:
                            winning_score = 3  # best of 5 -> first to 3
                            left_score = 0
                            right_score = 0
                            reset_positions(ball, left_paddle, right_paddle)
                            game_over = False
                            choosing = False
                        elif e.key == pygame.K_7:
                            winning_score = 4  # best of 7 -> first to 4
                            left_score = 0
                            right_score = 0
                            reset_positions(ball, left_paddle, right_paddle)
                            game_over = False
                            choosing = False
                clock.tick(30)  # reduce CPU while waiting

            # small delay before possibly closing pygame (user asked)
            if not running:
                pygame.time.delay(1000)
                break

        clock.tick(FPS)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
