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


