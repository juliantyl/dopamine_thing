import pygame
import json

IMG_SIZE = (100, 100)

def json_init_again(path):
    with open(path, "r") as file:
        data = json.load(file)
    return data

def load_commons():
    output = json_init_again("resources/data/commons.json")
    for item in output:
        img = pygame.image.load(item["img_path"])
        item["loaded"] = pygame.transform.scale(img, IMG_SIZE)
    return output

def load_uncommons():
    output = json_init_again("resources/data/uncommons.json")
    for item in output:
        img = pygame.image.load(item["img_path"])
        item["loaded"] = pygame.transform.scale(img, IMG_SIZE)
    return output

def load_rares():
    output = json_init_again("resources/data/rares.json")
    for item in output:
        img = pygame.image.load(item["img_path"])
        item["loaded"] = pygame.transform.scale(img, IMG_SIZE)
    return output

def load_legendaries():
    output = json_init_again("resources/data/legendaries.json")
    for item in output:
        img = pygame.image.load(item["img_path"])
        item["loaded"] = pygame.transform.scale(img, IMG_SIZE)
    return output

def load_ultra_rares():
    output = json_init_again("resources/data/ultra_rares.json")
    for item in output:
        img = pygame.image.load(item["img_path"])
        item["loaded"] = pygame.transform.scale(img, IMG_SIZE)
    return output

# FOR INITIALISING BLANK ONLY
def initialize_commons():
    output = []
    for i in range(265):
        output.append({"name": "Placeholder",
                       "description": "placeholder description",
                       "acquired": False,
                       "count": 0,
                       "img_path": f"resources/card_pics/placeholder.png",
                       "category": "none",
                       "loaded": None
                       })
    return output

def initialize_uncommons():
    output = []
    for i in range(125):
        output.append({"name": "Placeholder",
                       "description": "placeholder description",
                       "acquired": False,
                       "count": 0,
                       "img_path": f"resources/card_pics/placeholder.png",
                       "category": "none",
                       "loaded": None
                       })
    return output

def initialize_rares():
    output = []
    for i in range(70):
        output.append({"name": "Placeholder",
                       "description": "placeholder description",
                       "acquired": False,
                       "count": 0,
                       "img_path": f"resources/card_pics/placeholder.png",
                       "category": "none",
                       "loaded": None
                       })
    return output

def initialize_legendaries():
    output = []
    for i in range(25):
        output.append({"name": "Placeholder",
                       "description": "placeholder description",
                       "acquired": False,
                       "count": 0,
                       "img_path": f"resources/card_pics/placeholder.png",
                       "category": "none",
                       "loaded": None
                       })
    return output

def initialize_ultra_rares():
    output = []
    for i in range(15):
        output.append({"name": "Placeholder",
                       "description": "placeholder description",
                       "acquired": False,
                       "count": 0,
                       "img_path": f"resources/card_pics/placeholder.png",
                       "category": "none",
                       "loaded": None
                       })
    return output

def initialize():
    commons = initialize_commons()
    uncommons = initialize_uncommons()
    rares = initialize_rares()
    legendaries = initialize_legendaries()
    ultra_rares = initialize_ultra_rares()
    return commons, uncommons, rares, legendaries, ultra_rares


