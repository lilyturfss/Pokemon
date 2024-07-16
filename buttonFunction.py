import pygame

# Button Function
def start(start_button, scrn, frontimg, backimg, front, previous_pokemon_button, next_pokemon_button, id):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pos()[0] > start_button.x and pygame.mouse.get_pos()[0] < start_button.x + start_button.width:
                    if pygame.mouse.get_pos()[1] > start_button.y and pygame.mouse.get_pos()[1] < start_button.y + start_button.height:
                        front = not front

                        if front == True:
                            pygame.draw.rect(scrn, (0,0,0), pygame.Rect(140, 60, 70, 70))
                            scrn.blit(frontimg, (90, 20))
                            pygame.display.update()

                        else:
                            pygame.draw.rect(scrn, (0,0,0), pygame.Rect(140, 60, 70, 70))
                            scrn.blit(backimg, (90, 20))
                            pygame.display.update()

                elif previous_pokemon_button.isOver(pygame.mouse.get_pos()):
                    new_id = (int(id) - 1) % 1025
                    changePokemon(scrn, str(new_id))

                elif next_pokemon_button.isOver(pygame.mouse.get_pos()):
                    new_id = (int(id) + 1) % 1025
                    changePokemon(scrn, str(new_id))

# Import al final para prevenir circular import
from changePokemon import changePokemon

