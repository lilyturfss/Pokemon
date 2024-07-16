import pygame
import requests
import json
import io
from urllib.request import urlopen

from drawStats import screenPrint
from pygameButtonClass import Button


def fetch_pokemon_data(pokemon_id):
    try:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon_id}')
        response.raise_for_status()
        pokemon_data = response.json()
        return pokemon_data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching Pokemon data: {e}")
        return None

def load_pokemon_images(id, flip_button, scrn):
    # Load Images
    try:
        frontimg = pygame.image.load(io.BytesIO(urlopen(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png").read())).convert()
    except:
        print("Could not load front image.")
        frontimg = pygame.image.load(io.BytesIO(urlopen("https://upload.wikimedia.org/wikipedia/commons/5/59/Empty.png").read())).convert()

    try:
        backimg = pygame.image.load(io.BytesIO(urlopen(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/{id}.png").read())).convert()
        flip_button.draw(scrn)
    except:
        print("Could not load back image.")
        backimg = pygame.image.load(io.BytesIO(urlopen("https://upload.wikimedia.org/wikipedia/commons/5/59/Empty.png").read())).convert()

    return frontimg, backimg

def changePokemon(scrn, id, previous_pokemon_button, next_pokemon_button):
    # Fetch Pokemon data
    pokemon_data = fetch_pokemon_data(id)
    if not pokemon_data:
        return

    # Extract necessary information
    stats = [stat["base_stat"] for stat in pokemon_data["stats"]]
    types = [type["type"]["name"] for type in pokemon_data["types"]]
    namepoke = pokemon_data["forms"][0]["name"]

    scrn.fill((0,0,0))  # Clear the screen

    # Render text for stats and types
    my_font = pygame.font.SysFont('Arial', 20)
    name = my_font.render(f'Base Stats | {namepoke.upper()}', False, (255, 255, 255))
    hp = my_font.render(f'Hit Points: {stats[0]}', False, (255, 255, 255))
    attack = my_font.render(f'Attack: {stats[1]}', False, (255, 255, 255))
    defs = my_font.render(f'Defense: {stats[2]}', False, (255, 255, 255))
    sp_a = my_font.render(f'Special Attack: {stats[3]}', False, (255, 255, 255))
    sp_d = my_font.render(f'Special Defense: {stats[4]}', False, (255, 255, 255))
    speed = my_font.render(f'Speed: {stats[5]}', False, (255, 255, 255))
    typess = my_font.render(f'Types', False, (255, 255, 255))

    # Buttons
    flip_button = Button((255, 255, 255), 230, 60, 50, 25, 'Flip')
    previous_pokemon_button.draw(scrn)
    next_pokemon_button.draw(scrn)
    pygame.display.update()

    # Load Pokemon images
    from pokemonMain2 import load_pokemon_images
    frontimg, backimg, load = load_pokemon_images(id, flip_button, scrn)

    # Display Pokemon stats and images
    screenPrint(scrn, frontimg, name, hp, attack, defs, sp_a, sp_d, speed, typess, types, my_font, id)
    pygame.display.flip()  # Update the display

    front = True
    # Event loop to handle button clicks
    while True:
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if flip_button.isOver(pygame.mouse.get_pos()) and load == True:
                        front = not front
                        rect_width, rect_height = 100, 100
                        rect_x, rect_y = 90, 20
                        pygame.draw.rect(scrn, (0, 0, 0), (rect_x, rect_y, rect_width, rect_height))

                        if front:
                            screenPrint(scrn, frontimg, name, hp, attack, defs, sp_a, sp_d, speed, typess, types, my_font, id)
                        else:
                            screenPrint(scrn, backimg, name, hp, attack, defs, sp_a, sp_d, speed, typess, types, my_font, id)
                        pygame.display.flip()

                    elif previous_pokemon_button.isOver(pygame.mouse.get_pos()):
                        new_id = 1025 if int(id) == 1 else int(id) - 1
                        changePokemon(scrn, new_id, previous_pokemon_button, next_pokemon_button)

                    elif next_pokemon_button.isOver(pygame.mouse.get_pos()):
                        new_id = (int(id) + 1) % 1025 if int(id) == 1025 else int(id) + 1
                        changePokemon(scrn, new_id, previous_pokemon_button, next_pokemon_button)
        except:
            exit()

if __name__ == "__main__":
    import pygame
    pygame.init()
    X, Y = 300, 400
    scrn = pygame.display.set_mode((X, Y))
    pygame.display.set_caption('Pokedex')

    previous_pokemon_button = Button((255, 255, 255), 200, 90, 50, 25, 'Back')
    next_pokemon_button = Button((255, 255, 255), 200, 130, 50, 25, 'Next')
