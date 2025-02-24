import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Game Menu")

# Colors
WHITE = (255, 255, 255)
GRAY = (170, 170, 170)
DARK_GRAY = (100, 100, 100)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)
PURPLE = (59, 15, 135)
DARK_PURPLE = (28, 7, 64)
BACKGROUND_COLOUR = (165, 151, 189)
CRIMSON = (94, 7, 46)

# Fonts
font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)

# Button properties
button_width, button_height = 200, 60
back_width, back_height = 150, 46
play_button = pygame.Rect((WIDTH // 2 - button_width // 2, 250), (button_width, button_height))
collection_button = pygame.Rect((WIDTH // 2 - button_width // 2, 350), (button_width, button_height))
back_button = pygame.Rect((10, 10), (back_width, back_height))


def draw_text(text, font, color, x, y):
    """Render text on screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x - text_surface.get_width() // 2, y))


def play_screen():
    """Play Screen Loop"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        draw_text("Play Screen", font, CRIMSON, WIDTH // 2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE

        pygame.draw.rect(screen, back_color, back_button)
        draw_text("Back", button_font, WHITE, 10 + back_width / 2, back_height / 2 - 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(mouse_x, mouse_y):
                return

        pygame.display.update()


def collection_screen():
    """Collection Screen Loop"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        draw_text("Collection Screen", font, CRIMSON, WIDTH // 2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE

        pygame.draw.rect(screen, back_color, back_button)
        draw_text("Back", button_font, WHITE, 10 + back_width/2, back_height/2 - 2)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(mouse_x, mouse_y):
                return

        pygame.display.update()

def main_menu():
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)

        # Title
        draw_text("Main Menu", font, CRIMSON, WIDTH // 2, 100)

        # Get mouse position
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Button hover effect
        play_color = DARK_GRAY if play_button.collidepoint(mouse_x, mouse_y) else GRAY
        collection_color = DARK_GRAY if collection_button.collidepoint(mouse_x, mouse_y) else GRAY

        # Draw buttons
        pygame.draw.rect(screen, play_color, play_button)
        pygame.draw.rect(screen, collection_color, collection_button)

        # Button text
        draw_text("Play", button_font, WHITE, WIDTH // 2, 270)
        draw_text("Collection", button_font, WHITE, WIDTH // 2, 370)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    play_screen()
                elif collection_button.collidepoint(event.pos):
                    collection_screen()

        pygame.display.update()  # Refresh screen

    pygame.quit()


# Run the menu
main_menu()
