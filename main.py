# python game with pygame : Jumping dino
# by. BlockDMask
import pygame
import sys

pygame.init()
pygame.display.set_caption('Pizza School')
background = pygame.image.load('images/bg.gif')
MAX_WIDTH = 1280
MAX_HEIGHT = 720


def main():
    # set screen, fps
    screen = pygame.display.set_mode((MAX_WIDTH, MAX_HEIGHT))
    fps = pygame.time.Clock()

    # dino
    pizza1 = pygame.image.load('images/pizza1.png')
    dino_height = pizza1.get_size()[1]
    dino_bottom = MAX_HEIGHT - dino_height
    dino_x = 50
    dino_y = dino_bottom
    jump_top = 450
    leg_swap = True
    is_bottom = True
    is_go_up = False

    # tree
    imgTree = pygame.image.load('images/hurdle.png')
    tree_height = imgTree.get_size()[1]
    tree_x = MAX_WIDTH
    tree_y = MAX_HEIGHT - tree_height

    while True:
        screen.fill((255, 255, 255))
        screen.blit(background, (0, 0))
        pygame.display.update()

        # event check
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if is_bottom:
                    is_go_up = True
                    is_bottom = False

        # dino move
        if is_go_up:
            dino_y -= 12.0
        elif not is_go_up and not is_bottom:
            dino_y += 12.0

        # dino top and bottom check
        if is_go_up and dino_y <= jump_top:
            is_go_up = False

        if not is_bottom and dino_y >= dino_bottom:
            is_bottom = True
            dino_y = dino_bottom

        # tree move
        tree_x -= 12.0
        if tree_x <= 0:
            tree_x = MAX_WIDTH

        # draw tree
        screen.blit(imgTree, (tree_x, tree_y))

        # draw dino
        if leg_swap:
            screen.blit(pizza1, (dino_x, dino_y))
            leg_swap = False
        else:
            screen.blit(pizza1, (dino_x, dino_y))
            leg_swap = True

        # update
        pygame.display.update()
        fps.tick(30)


if __name__ == '__main__':
    main()
