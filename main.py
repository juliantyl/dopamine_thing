import pygame
import json
from random import randint, choice
from loading import *

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
PINK = (201, 34, 165)

clock = pygame.time.Clock()

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

common_image = pygame.image.load("resources/images/Common.png")
common_image = pygame.transform.scale(common_image, (90, 90))

uncommon_image = pygame.image.load("resources/images/Uncommon.png")
uncommon_image = pygame.transform.scale(uncommon_image, (90, 90))

rare_image = pygame.image.load("resources/images/Rare.png")
rare_image = pygame.transform.scale(rare_image, (90, 90))

legendary_image = pygame.image.load("resources/images/Legendary.png")
legendary_image = pygame.transform.scale(legendary_image, (90, 90))

ultra_image = pygame.image.load("resources/images/Ultra Rare.png")
ultra_image = pygame.transform.scale(ultra_image, (90, 90))

common_locked_image = pygame.image.load("resources/images/common_locked.png")
common_locked_image = pygame.transform.scale(common_locked_image, (100, 100))

uncommon_locked_image = pygame.image.load("resources/images/uncommon_locked.png")
uncommon_locked_image = pygame.transform.scale(uncommon_locked_image, (100, 100))

rare_locked_image = pygame.image.load("resources/images/rare_locked.png")
rare_locked_image = pygame.transform.scale(rare_locked_image, (100, 100))

legendary_locked_image = pygame.image.load("resources/images/legendary_locked.png")
legendary_locked_image = pygame.transform.scale(legendary_locked_image, (100, 100))

ultra_locked_image = pygame.image.load("resources/images/ultra_locked.png")
ultra_locked_image = pygame.transform.scale(ultra_locked_image, (100, 100))


def json_init(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data


def json_save(path, data):
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def json_save_collection(path, data):
    for item in data:
        item["loaded"] = None
    with open(path, "w") as file:
        json.dump(data, file, indent=4)

def json_save_all():
    json_save("resources/data/tasks.json", tasks)
    json_save("resources/data/packs.json", packs)


    json_save_collection("resources/data/commons.json", commons)
    json_save_collection("resources/data/uncommons.json", uncommons)
    json_save_collection("resources/data/rares.json", rares)
    json_save_collection("resources/data/legendaries.json", legendaries)
    json_save_collection("resources/data/ultra_rares.json", ultra_rares)


def daily_reset():
    for task in tasks:
        task["checked"] = False
        task["collected"] = False

def collection_reset():
    for c in commons:
        c["acquired"] = False
        c["count"] = 0
    for u in uncommons:
        u["acquired"] = False
        u["count"] = 0
    for r in rares:
        r["acquired"] = False
        r["count"] = 0
    for l in legendaries:
        l["acquired"] = False
        l["count"] = 0
    for ur in ultra_rares:
        ur["acquired"] = False
        ur["count"] = 0


tasks = json_init("resources/data/tasks.json")
packs = json_init("resources/data/packs.json")

commons = load_commons()
uncommons = load_uncommons()
rares = load_rares()
legendaries = load_legendaries()
ultra_rares = load_ultra_rares()


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
    total_scroll = 0
    SCROLL_SPEED = 50
    icon_size = 100
    y_offset = 200
    col = 0

    common_title_y = 125
    common_rects = []
    common_count = 0
    for i, item in enumerate(commons):
        row = i % 5
        col = i // 5
        common_rects.append((pygame.rect.Rect((WIDTH // 6) * (row + 1) - icon_size//2, (icon_size + 10)*col + y_offset, icon_size, icon_size), item))
        if item["acquired"]:
            common_count += 1

    # account for all and name of next
    y_offset += (icon_size + 10)*col + 125
    uncommon_title_y = y_offset
    y_offset += 75

    uncommon_rects = []
    uncommon_count = 0
    for i,item in enumerate(uncommons):
        row = i % 5
        col = i // 5
        uncommon_rects.append((
            pygame.rect.Rect((WIDTH // 6) * (row + 1) - icon_size // 2, (icon_size + 10) * col + y_offset, icon_size,
                             icon_size), item))
        if item["acquired"]:
            uncommon_count += 1

    y_offset += (icon_size + 10)*col + 125
    rare_title_y = y_offset
    y_offset += 75

    rare_rects = []
    rare_count = 0
    for i,item in enumerate(rares):
        row = i % 5
        col = i // 5
        rare_rects.append((
            pygame.rect.Rect((WIDTH // 6) * (row + 1) - icon_size // 2, (icon_size + 10) * col + y_offset, icon_size,
                             icon_size), item))
        if item["acquired"]:
            rare_count += 1

    y_offset += (icon_size + 10) * col + 125
    legendary_title_y = y_offset
    y_offset += 75

    legendary_rects = []
    legendary_count = 0
    for i, item in enumerate(legendaries):
        row = i % 5
        col = i // 5
        legendary_rects.append((
            pygame.rect.Rect((WIDTH // 6) * (row + 1) - icon_size // 2, (icon_size + 10) * col + y_offset, icon_size,
                             icon_size), item))
        if item["acquired"]:
            legendary_count += 1
    y_offset += (icon_size + 10) * col + 125
    ultra_title_y = y_offset
    y_offset += 75

    ultra_rects = []
    ultra_count = 0
    for i, item in enumerate(ultra_rares):
        row = i % 5
        col = i // 5
        ultra_rects.append((
            pygame.rect.Rect((WIDTH // 6) * (row + 1) - icon_size // 2, (icon_size + 10) * col + y_offset, icon_size,
                             icon_size), item))
        if item["acquired"]:
            ultra_count += 1


    running = True
    while running:

        screen.fill(BACKGROUND_COLOUR)


        mouse_x, mouse_y = pygame.mouse.get_pos()
        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE

        # drawing commons
        for rec in common_rects:
            pygame.draw.rect(screen, WHITE, rec[0])
            if not rec[1]["acquired"]:
                screen.blit(common_locked_image, (rec[0].x, rec[0].y))
            else:
                screen.blit(rec[1]["loaded"], (rec[0].x, rec[0].y))
        for rec in uncommon_rects:
            pygame.draw.rect(screen, GREEN, rec[0])
            if not rec[1]["acquired"]:
                screen.blit(uncommon_locked_image, (rec[0].x, rec[0].y))
            else:
                screen.blit(rec[1]["loaded"], (rec[0].x, rec[0].y))
        for rec in rare_rects:
            pygame.draw.rect(screen, BLUE, rec[0])
            if not rec[1]["acquired"]:
                screen.blit(rare_locked_image, (rec[0].x, rec[0].y))
            else:
                screen.blit(rec[1]["loaded"], (rec[0].x, rec[0].y))
        for rec in legendary_rects:
            pygame.draw.rect(screen, GOLD, rec[0])
            if not rec[1]["acquired"]:
                screen.blit(legendary_locked_image, (rec[0].x, rec[0].y))
            else:
                screen.blit(rec[1]["loaded"], (rec[0].x, rec[0].y))
        for rec in ultra_rects:
            pygame.draw.rect(screen, PINK, rec[0])
            if not rec[1]["acquired"]:
                screen.blit(ultra_locked_image, (rec[0].x, rec[0].y))
            else:
                screen.blit(rec[1]["loaded"], (rec[0].x, rec[0].y))

        # draw titles
        draw_text(f'Common ({common_count}/265)', font, BLACK, WIDTH // 2, common_title_y)
        draw_text(f'Uncommon ({uncommon_count}/125)', font, BLACK, WIDTH // 2, uncommon_title_y)
        draw_text(f'Rare ({rare_count}/70)', font, BLACK, WIDTH // 2, rare_title_y)
        draw_text(f'Legendary ({legendary_count}/25)', font, BLACK, WIDTH // 2, legendary_title_y)
        draw_text(f'Ultra Rare ({ultra_count}/15)', font, BLACK, WIDTH // 2, ultra_title_y)



        # top and bottom bars
        pygame.draw.rect(screen, BACKGROUND_COLOUR, pygame.rect.Rect(0,0,WIDTH, 100))
        pygame.draw.rect(screen, BACKGROUND_COLOUR, pygame.rect.Rect(0,HEIGHT - 100,WIDTH, 100))

        draw_text("Collection Screen", font, CRIMSON, WIDTH // 2, 20)

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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
                if total_scroll >= 0:
                    continue
                total_scroll += SCROLL_SPEED
                for rec in common_rects:
                    rec[0].y += SCROLL_SPEED
                for rec in uncommon_rects:
                    rec[0].y += SCROLL_SPEED
                for rec in rare_rects:
                    rec[0].y += SCROLL_SPEED
                for rec in legendary_rects:
                    rec[0].y += SCROLL_SPEED
                for rec in ultra_rects:
                    rec[0].y += SCROLL_SPEED
                # remember to update title positions too
                common_title_y += SCROLL_SPEED
                uncommon_title_y += SCROLL_SPEED
                rare_title_y += SCROLL_SPEED
                legendary_title_y += SCROLL_SPEED
                ultra_title_y += SCROLL_SPEED
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
                if total_scroll <= -y_offset + 150:
                    continue
                total_scroll -= SCROLL_SPEED
                for rec in common_rects:
                    rec[0].y -= SCROLL_SPEED
                for rec in uncommon_rects:
                    rec[0].y -= SCROLL_SPEED
                for rec in rare_rects:
                    rec[0].y -= SCROLL_SPEED
                for rec in legendary_rects:
                    rec[0].y -= SCROLL_SPEED
                for rec in ultra_rects:
                    rec[0].y -= SCROLL_SPEED
                # remember to update title positions too
                common_title_y -= SCROLL_SPEED
                uncommon_title_y -= SCROLL_SPEED
                rare_title_y -= SCROLL_SPEED
                legendary_title_y -= SCROLL_SPEED
                ultra_title_y -= SCROLL_SPEED


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
                pack_opening(False)
            elif event.type == pygame.MOUSEBUTTONDOWN and open_rare_button.collidepoint(mouse_x, mouse_y) and packs["large"] > 0:
                packs["large"] -= 1
                pack_opening(True)

        pygame.display.update()


def calculate_result(init_speed, rarity_ls):
    return


def pick_and_unlock(rarity):
    if rarity == "X":
        target_ls = ultra_rares
    elif rarity == "L":
        target_ls = legendaries
    elif rarity == "R":
        target_ls = rares
    elif rarity == "U":
        target_ls = uncommons
    else:
        target_ls = commons

    random_item = choice(target_ls)
    random_item["acquired"] = True
    random_item["count"] += 1
    return random_item


def pack_opening(is_rare):
    """Ideally, the pack is pre-opened as in the result is pre-calculated so if the user quits,
    they don't lose the result"""
    opening = True
    speed = randint(45, 80)
    init_speed = speed
    box_list = []
    box_rarity_list = []
    for i in range(150):
        box_list.append(pygame.rect.Rect(i*94, 200, 90, 90))
        rarity = randint(1, 1000)
        if 1 <= rarity < 4:
            box_rarity_list.append("X")
        elif 4 <= rarity < 34:
            box_rarity_list.append("L")
        elif 34 <= rarity < 154:
            box_rarity_list.append("R")
        elif 154 <= rarity < 281:
            box_rarity_list.append("U")
        else:
            box_rarity_list.append("C")

    background_box = pygame.rect.Rect(0, 180, WIDTH, 130)

    while opening:
        screen.fill(BACKGROUND_COLOUR)
        draw_text("Opening Pack...", font, CRIMSON, WIDTH // 2, 20)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        pygame.draw.rect(screen, DARK_GRAY, background_box)

        for i, box in enumerate(box_list):
            if box_rarity_list[i] == "X":
                image = ultra_image
            elif box_rarity_list[i] == "L":
                image = legendary_image
            elif box_rarity_list[i] == "R":
                image = rare_image
            elif box_rarity_list[i] == "U":
                image = uncommon_image
            else:
                image = common_image
            pygame.draw.rect(screen, WHITE, box)
            screen.blit(image, (box.x, box.y))

        pygame.draw.line(screen, BLACK, (WIDTH//2, 180), (WIDTH//2, 310), 4)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                calculate_result(box_rarity_list, init_speed)
                pygame.quit()
                json_save_all()
                return


        pygame.display.update()

        for box in box_list:
            box.x -= speed
        speed -= speed/130
        if speed <= 0.3:
            opening = False
        clock.tick(30)

    opened_pack = "C"
    for i, box in enumerate(box_list):
        if box.x - 2 <= WIDTH // 2 < box.x + box.width + 2:
            print(f'Box: {i}, Rarity: {box_rarity_list[i]}')
            opened_pack = box_rarity_list[i]

    if opened_pack == "C":
        rarity_name = "Common"
        rarity_colour = CRIMSON
    elif opened_pack == "U":
        rarity_name = "Uncommon"
        rarity_colour = GREEN
    elif opened_pack == "R":
        rarity_name = "Rare"
        rarity_colour = BLUE
    elif opened_pack == "L":
        rarity_name = "Legendary"
        rarity_colour = GOLD
    else:
        rarity_name = "Ultra Rare"
        rarity_colour = PINK

    unboxed_item = pick_and_unlock(opened_pack)

    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        draw_text("Pack Opened", font, CRIMSON, WIDTH // 2, 20)
        draw_text(f'It\'s {rarity_name}!', font, rarity_colour, WIDTH // 2, 100)

        # load image
        image = pygame.image.load(unboxed_item["img_path"])
        image = pygame.transform.scale(image, (150, 150))
        screen.blit(image, (WIDTH // 2 - 75, 180))

        draw_text(f'{unboxed_item["name"]}!', font, BLACK, WIDTH // 2, 340)

        mouse_x, mouse_y = pygame.mouse.get_pos()

        reset_confirm_button_color = DARK_GREEN if reset_confirm_button.collidepoint(mouse_x, mouse_y) else GREEN

        pygame.draw.rect(screen, reset_confirm_button_color, reset_confirm_button)
        draw_text("Cool..", button_font, WHITE, WIDTH // 2, 370)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                json_save_all()
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                return
            if event.type == pygame.MOUSEBUTTONDOWN and reset_confirm_button.collidepoint(mouse_x, mouse_y):
                return

        pygame.display.update()

def reset_confirm_screen():
    """Reset Confirmation"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)


        reset_col_button = pygame.rect.Rect(WIDTH // 2 - 120, HEIGHT - 50, 240, 40)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE
        reset_confirm_button_color = DARK_GREEN if reset_confirm_button.collidepoint(mouse_x, mouse_y) else GREEN
        reset_col_button_colour = DARK_GRAY if reset_col_button.collidepoint(mouse_x, mouse_y) else GRAY

        pygame.draw.rect(screen, back_color, back_button)
        pygame.draw.rect(screen, reset_confirm_button_color, reset_confirm_button)
        pygame.draw.rect(screen, reset_col_button_colour, reset_col_button)
        draw_text("Reset Collection", button_font, WHITE, WIDTH // 2, HEIGHT - 40)
        draw_text("Are you Sure?", font, CRIMSON, WIDTH // 2, 20)
        draw_text("Yes, Reset", button_font, WHITE, WIDTH // 2, 370)
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
            if event.type == pygame.MOUSEBUTTONDOWN and reset_confirm_button.collidepoint(mouse_x, mouse_y):
                daily_reset()
                return
            if event.type == pygame.MOUSEBUTTONDOWN and reset_col_button.collidepoint(mouse_x, mouse_y):
                reset_confirm_confirm_screen()
                return

        pygame.display.update()


def reset_confirm_confirm_screen():
    """Reset Confirmation for Collection"""
    running = True
    while running:
        screen.fill(BACKGROUND_COLOUR)
        mouse_x, mouse_y = pygame.mouse.get_pos()

        back_color = DARK_PURPLE if back_button.collidepoint(mouse_x, mouse_y) else PURPLE
        reset_confirm_button_color = DARK_GREEN if reset_confirm_button.collidepoint(mouse_x, mouse_y) else GREEN

        pygame.draw.rect(screen, back_color, back_button)
        pygame.draw.rect(screen, reset_confirm_button_color, reset_confirm_button)
        draw_text("Are you 100% sure?", font, CRIMSON, WIDTH // 2, 20)
        draw_text("Yes, Reset", button_font, WHITE, WIDTH // 2, 370)
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
            if event.type == pygame.MOUSEBUTTONDOWN and reset_confirm_button.collidepoint(mouse_x, mouse_y):
                collection_reset()
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
