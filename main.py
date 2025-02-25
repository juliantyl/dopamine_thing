import pygame
import json

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
GRAYED_OUT = (136, 125, 138)
GREEN = (16, 135, 70)
CRIMSON = (94, 7, 46)
DARK_GREEN = (6, 64, 32)
GOLD = (214, 202, 26)
DARK_GOLD = (143, 135, 13)

# Fonts
font = pygame.font.Font(None, 60)
button_font = pygame.font.Font(None, 40)

# Button properties
button_width, button_height = 200, 60
back_width, back_height = 150, 46

play_button = pygame.Rect((WIDTH // 2 - button_width // 2, 250), (button_width, button_height))
collection_button = pygame.Rect((WIDTH // 2 - button_width // 2, 340), (button_width, button_height))
open_packs_button = pygame.Rect((WIDTH // 2 - button_width // 2, 430), (button_width, button_height))
reset_button = pygame.Rect((WIDTH // 2 - button_width // 2, 520), (button_width, button_height))
reset_confirm_button = pygame.Rect((WIDTH // 2 - button_width // 2, 350), (button_width, button_height))
back_button = pygame.Rect((10, 10), (back_width, back_height))

open_small_button = pygame.Rect((WIDTH // 3 - button_width // 2, 430), (button_width, button_height))
open_rare_button = pygame.Rect(((2 * WIDTH) // 3 - button_width // 2, 430), (button_width, button_height))

input_font = pygame.font.Font(None, 35)
input_text = ""

# Load images
checkmark_img = pygame.image.load("resources/images/checkmark_img.png")
checkmark_img = pygame.transform.scale(checkmark_img, (30, 30))

not_checked_img = pygame.image.load("resources/images/not_checked_img.png")
not_checked_img = pygame.transform.scale(not_checked_img, (30, 30))

small_pack_image = pygame.image.load("resources/images/small_pack.png")
small_pack_image = pygame.transform.scale(small_pack_image, (90, 90))

rare_pack_image = pygame.image.load("resources/images/rare_pack.png")
rare_pack_image = pygame.transform.scale(rare_pack_image, (90, 90))

def json_init(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data


def json_save(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)


def json_save_all():
    json_save("resources/data/tasks.json", tasks)
    json_save("resources/data/packs.json", packs)


def daily_reset():
    for task in tasks:
        task["checked"] = False
        task["collected"] = False


tasks = json_init("resources/data/tasks.json")
packs = json_init("resources/data/packs.json")


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
        screen.fill(BACKGROUND_COLOUR)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        # Draw title
        draw_text("To-Do List", font, CRIMSON, WIDTH // 2, 20)

        # Back Button
        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE
        pygame.draw.rect(screen, back_color, back_button)
        draw_text("Back", button_font, WHITE, 10 + back_width / 2, back_height / 2 - 2)

        collect_color = DARK_GREEN if collect_button.collidepoint(mouse_x, mouse_y) else GREEN

        # Draw tasks
        y_offset = 100
        uncollected = 0
        for i, dic in enumerate(tasks):
            color = GREEN if dic["checked"] else BLACK  # Checked tasks are grayed out
            if dic["checked"]:
                screen.blit(checkmark_img, (50, y_offset))
            else:
                screen.blit(not_checked_img, (50, y_offset))
            draw_text_left(f'    {dic["task"]}', font, color, 50, y_offset)
            y_offset += 50

            if dic["checked"] and not dic["collected"]:
                uncollected += 1

        if uncollected > 0:
            pygame.draw.rect(screen, collect_color, collect_button)
            draw_text("Collect", input_font, BLACK, WIDTH // 2, 470)

        # Instructions
        draw_text("Left Click: Check | Right Click: Uncheck | ESC: Back", input_font, BLACK, WIDTH // 2, HEIGHT - 40)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                json_save_all()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(pygame.mouse.get_pos()):
                return
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
                    if 50 <= mouse_x <= WIDTH - 50 and y_offset <= mouse_y <= y_offset + 40 and tasks[i][
                        "collected"] == False:
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
        draw_text("Back", button_font, WHITE, 10 + back_width / 2, back_height / 2 - 2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                json_save_all()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(mouse_x, mouse_y):
                return

        pygame.display.update()


def open_packs_screen():
    """Packs Screen Loop"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        draw_text("Open Packs", font, CRIMSON, WIDTH // 2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE
        open_color = GRAYED_OUT if packs["small"] <= 0 else (DARK_GRAY if open_small_button.collidepoint(mouse_x, mouse_y) else GRAY)
        open_rare_color = GRAYED_OUT if packs["large"] <= 0 else (DARK_GOLD if open_rare_button.collidepoint(mouse_x, mouse_y) else GOLD)

        open_font_color = GRAY if packs["small"] <= 0 else WHITE
        open_rare_font_color = GRAY if packs["large"] <= 0 else WHITE

        pygame.draw.rect(screen, back_color, back_button)
        pygame.draw.rect(screen, open_color, open_small_button)
        pygame.draw.rect(screen, open_rare_color, open_rare_button)
        draw_text("Back", button_font, WHITE, 10 + back_width / 2, back_height / 2 - 2)
        draw_text("Open Pack", button_font, open_font_color, WIDTH // 3 , 450)
        draw_text("Open Rare", button_font, open_rare_font_color, (2 * WIDTH) // 3 , 450)
        draw_text(f'x{packs["small"]}', button_font, BLACK, WIDTH // 3 + 40 , 300)
        draw_text(f'x{packs["large"]}', button_font, BLACK, (2 * WIDTH) // 3 + 40, 300)

        screen.blit(small_pack_image, (WIDTH // 3 - 70, 250))
        screen.blit(rare_pack_image, ((2 * WIDTH) // 3 - 70, 250))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                json_save_all()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(mouse_x, mouse_y):
                return
            if event.type == pygame.MOUSEBUTTONDOWN and open_small_button.collidepoint(mouse_x, mouse_y) and packs["small"] > 0:
                packs["small"] -= 1
            elif event.type == pygame.MOUSEBUTTONDOWN and open_rare_button.collidepoint(mouse_x, mouse_y) and packs["large"] > 0:
                packs["large"] -= 1

        pygame.display.update()


def reset_confirm_screen():
    """Reset Confirmation"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)

        draw_text("Are you Sure?", font, CRIMSON, WIDTH // 2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE
        reset_confirm_button_color = DARK_GREEN if reset_confirm_button.collidepoint(mouse_x, mouse_y) else GREEN

        pygame.draw.rect(screen, back_color, back_button)
        pygame.draw.rect(screen, reset_confirm_button_color, reset_confirm_button)
        draw_text("Back", button_font, WHITE, 10 + back_width / 2, back_height / 2 - 2)
        draw_text("Yes, Reset", button_font, WHITE, WIDTH // 2, 370)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                json_save_all()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and back_button.collidepoint(mouse_x, mouse_y):
                return
            if event.type == pygame.MOUSEBUTTONDOWN and reset_confirm_button.collidepoint(mouse_x, mouse_y):
                daily_reset()
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
        reset_color = DARK_GRAY if reset_button.collidepoint(mouse_x, mouse_y) else GRAY
        open_packs_button_color = DARK_GRAY if open_packs_button.collidepoint(mouse_x, mouse_y) else GRAY

        # Draw buttons
        pygame.draw.rect(screen, play_color, play_button)
        pygame.draw.rect(screen, collection_color, collection_button)
        pygame.draw.rect(screen, reset_color, reset_button)
        pygame.draw.rect(screen, open_packs_button_color, open_packs_button)

        # Button text
        draw_text("Play", button_font, WHITE, WIDTH // 2, 270)
        draw_text("Collection", button_font, WHITE, WIDTH // 2, 360)
        draw_text("Open Packs", button_font, WHITE, WIDTH // 2, 450)
        draw_text("Reset", button_font, WHITE, WIDTH // 2, 540)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    play_screen()
                elif collection_button.collidepoint(event.pos):
                    collection_screen()
                elif open_packs_button.collidepoint(event.pos):
                    open_packs_screen()
                elif reset_button.collidepoint(event.pos):
                    reset_confirm_screen()

        pygame.display.update()

    pygame.quit()
    json_save_all()


# Run the menu
main_menu()
