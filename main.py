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
GREEN = (16, 135, 70)
CRIMSON = (94, 7, 46)
DARK_GREEN = (6, 64, 32)

# Fonts
font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)

# Button properties
button_width, button_height = 200, 60
back_width, back_height = 150, 46

play_button = pygame.Rect((WIDTH // 2 - button_width // 2, 250), (button_width, button_height))
collection_button = pygame.Rect((WIDTH // 2 - button_width // 2, 350), (button_width, button_height))
back_button = pygame.Rect((10, 10), (back_width, back_height))



tasks = [{"task": "Buy groceries", "checked": False, "collected": False},
         {"task": "Finish homework", "checked": False, "collected": False},
         {"task": "Call mom", "checked": False, "collected": False},]
packs = {"small": 1, "large": 0}
input_font = pygame.font.Font(None, 35)
input_text = ""

# Load checkmark image
checkmark_img = pygame.image.load("checkmark_img.png")
checkmark_img = pygame.transform.scale(checkmark_img, (30, 30))

not_checked_img = pygame.image.load("not_checked_img.png")
not_checked_img = pygame.transform.scale(not_checked_img, (30, 30))


def draw_text(text, font, color, x, y):
    """Render text on screen."""
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x - text_surface.get_width() // 2, y))

def draw_text_left(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x, y))  # Aligns text to the left


def play_screen():
    """To-Do List Screen"""
    global tasks, packs
    collect_width, collect_height = 200, 60
    collect_button = pygame.Rect((WIDTH // 2 - collect_width // 2, 450), (collect_width, collect_height))

    running = True
    while running:
        screen.fill(WHITE)

        # Draw title
        draw_text("To-Do List", font, BLUE, WIDTH//2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        collect_color = DARK_GREEN if collect_button.collidepoint(mouse_x, mouse_y) else GREEN

        # Draw tasks
        y_offset = 100
        uncollected = 0
        for i, dic in enumerate(tasks):
            color = GRAY if dic["checked"] else BLACK  # Checked tasks are grayed out
            if dic["checked"]:
                screen.blit(checkmark_img, (50, y_offset))
            else:
                screen.blit(not_checked_img, (50, y_offset))
            draw_text_left(f"   {dic["task"]}", font, color, 50, y_offset)
            y_offset += 50

            if dic["checked"] and not dic["collected"]:
                uncollected += 1

        if uncollected > 0:
            pygame.draw.rect(screen, collect_color, collect_button)
            draw_text("Collect", input_font, BLACK, WIDTH // 2, 470)

        # Instructions
        draw_text("Left Click: Check | Right Click: Uncheck | ESC: Back", input_font, BLACK, WIDTH//2, HEIGHT - 40)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return  # Go back to menu
            if event.type == pygame.MOUSEBUTTONDOWN:
                if collect_button.collidepoint(mouse_x, mouse_y):
                    for i in range(len(tasks)):
                        if tasks[i]["checked"] and not tasks[i]["collected"]:
                            tasks[i]["collected"] = True
                            packs["small"] += 1
                    if all(task["checked"] for task in tasks):
                        packs["large"] += 1
                        print("all collected!")
                y_offset = 100
                for i in range(len(tasks)):
                    if 50 <= mouse_x <= WIDTH - 50 and y_offset <= mouse_y <= y_offset + 40 and tasks[i]["collected"] == False:
                        if event.button == 1:
                            tasks[i]["checked"] = True
                        elif event.button == 3:
                            tasks[i]["checked"] = False
                    y_offset += 50

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
