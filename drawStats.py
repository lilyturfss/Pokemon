import pygame

def printPokemonTypes(types, my_font, scrn):
    x = 1
    y = 0
    z = 280
    for type in types:
        type1 = my_font.render(f'Slot {x}: {type[0].upper() + type[1:]}', False, (255, 255, 255))
        scrn.blit(type1, (30, z))
        x += 1
        y += 1
        z += 20

def screenPrint(scrn, frontimg, name, hp, attack, defs, sp_a, sp_d, speed, typess, types, my_font, id):
    scrn.blit(frontimg, (90, 30))    
    scrn.blit(name, (20, 15))        
    scrn.blit(hp, (20, 120))         
    scrn.blit(attack, (20, 140))     
    scrn.blit(defs, (20, 160))       
    scrn.blit(sp_a, (20, 180))       
    scrn.blit(sp_d, (20, 200))       
    scrn.blit(speed, (20, 220))      
    scrn.blit(typess, (20, 260))
    scrn.blit(my_font.render(f'ID: {id}', False, (255, 255, 255)), (20, 350))       
    printPokemonTypes(types, my_font, scrn)
