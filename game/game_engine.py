import pygame
FONT_NAME = None

def draw_scores(surface, left_score, right_score, font):
    score_text = f"{left_score}    {right_score}"
    text = font.render(score_text, True, (255, 255, 255))
    rect = text.get_rect(center=(surface.get_width() // 2, 30))
    surface.blit(text, rect)

def draw_center_text(surface, text_str, font, y):
    text = font.render(text_str, True, (255, 255, 255))
    rect = text.get_rect(center=(surface.get_width() // 2, y))
    surface.blit(text, rect)

def show_game_over(surface, winner_is_player, font):
    surface.fill((0, 0, 0))
    if winner_is_player:
        msg = "Player Wins!"
    else:
        msg = "AI Wins!"
    draw_center_text(surface, msg, font, surface.get_height() // 2 - 30)
    draw_center_text(surface, "Press 3 = Best of 3, 5 = Best of 5, 7 = Best of 7, ESC = Exit", font, surface.get_height() // 2 + 30)
    pygame.display.flip()

def show_replay_prompt(surface, font):
    surface.fill((0, 0, 0))
    draw_center_text(surface, "Choose: 3 / 5 / 7 or ESC to quit", font, surface.get_height() // 2)
    pygame.display.flip()
