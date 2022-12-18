import pygame as pg
import random

# initiate program
pg.init()


# program variables=====================================================================================================

# set screen size and window title
size = (1920, 1020)
surface = pg.display.set_mode(size)

pg.display.set_caption("Snakey snek game :)")

# set font
font = pg.font.Font(pg.font.get_default_font(), 30)

# manage fps
clock = pg.time.Clock()

# Main game loop========================================================================================================
Running = True

while Running:

    # Variables=========================================================================================================

    # snake direction
    snakeDir = -1

    # snake starting position
    snakeY = 480
    snakeX = 960

    # detect fruit
    fruitOn = False

    # snake speed
    snakeSpeed = 2

    # snake length
    snakeSegments = [(snakeX, snakeY)]
    snakeLen = 1

    # snake color
    snakeColor = (0, 255, 0)

    # fruit color
    fruitColor = (255, 0, 0)

    # Secondary game loop===============================================================================================
    Dead = False

    while not Dead:
        # Get pygame events---------------------------------------------------------------------------------------------
        for event in pg.event.get():

            # Window closed event_______________________________________________________________________________________
            if event.type == pg.QUIT:
                Running = False
                Dead = True

            # key event_________________________________________________________________________________________________

            # detect if any key is being pressed________________________________________________________________________
            if event.type == pg.KEYDOWN:

                # keyW
                if event.key == pg.K_w or event.key == pg.K_UP and snakeDir != 2:
                    snakeDir = 0

                # keyA
                if event.key == pg.K_a or event.key == pg.K_LEFT and snakeDir != 3:
                    snakeDir = 1

                # keyS
                if event.key == pg.K_s or event.key == pg.K_DOWN and snakeDir != 0:
                    snakeDir = 2

                # keyD
                if event.key == pg.K_d or event.key == pg.K_RIGHT and snakeDir != 1:
                    snakeDir = 3

        # Background----------------------------------------------------------------------------------------------------
        if snakeLen < 10:
            surface.fill(color=(11, 84, 254))

        elif 10 <= snakeLen < 20:
            surface.fill(color=(71, 67, 239))

        elif 20 <= snakeLen < 30:
            surface.fill(color=(132, 50, 223))

        elif 30 <= snakeLen < 40:
            surface.fill(color=(192, 32, 208))

        elif 40 <= snakeLen < 50:
            surface.fill(color=(252, 15, 192))
            snakeColor = (0, 255, 251)
            fruitColor = (0, 0, 255)

        elif 50 <= snakeLen < 60:
            surface.fill(color=(252, 108, 133))

        elif 60 <= snakeLen < 70:
            surface.fill(color=(252, 148, 161))

        elif 70 <= snakeLen < 80:
            surface.fill(color=(255, 204, 203))

        elif 80 <= snakeLen < 90:
            surface.fill(color=(205, 255, 204))

        elif 90 <= snakeLen < 100:
            surface.fill(color=(176, 245, 171))
            snakeColor = (255, 165, 0)
            fruitColor = (0, 0, 0)

        # Draw operations===============================================================================================

        # snake direction_______________________________________________________________________________________________
        if snakeDir == 0:
            snakeY -= 60

        elif snakeDir == 1:
            snakeX -= 60

        elif snakeDir == 2:
            snakeY += 60

        elif snakeDir == 3:
            snakeX += 60

        # spawn fruit___________________________________________________________________________________________________
        if fruitOn is False:
            fruitX = random.randrange(0, 31) * 60
            fruitY = random.randrange(0, 16) * 60

            fruitOn = True
        pg.draw.rect(surface, fruitColor, pg.Rect(fruitX + 15, fruitY + 15, 30, 30))

        # detect snake/fruit collision__________________________________________________________________________________
        for segment in snakeSegments:
            if segment[0] == fruitX and segment[1] == fruitY:

                # increase snake length and speed and reset fruit location______________________________________________
                snakeSpeed += 0.2
                fruitOn = False

                # snake length
                snakeLen = snakeSegments.__len__() + 1

        # doesnt let snake get out of boundaries------------------------------------------------------------------------
        if snakeX > size[0]-60:
            snakeX -= size[0]

        elif snakeX < 0:
            snakeX += size[0]

        elif snakeY > size[1]-60:
            snakeY -= size[1]

        elif snakeY < 0:
            snakeY += size[1]

        # draw snake
        snakeSegments.append((snakeX, snakeY))
        if fruitOn is True:
            snakeSegments.pop(0)

        # detects if the snake has collided with itself_________________________________________________________________
        for segment in snakeSegments:
            if len(set(snakeSegments)) != len(snakeSegments):
                Dead = True

            pg.draw.rect(surface, snakeColor, pg.Rect(segment[0], segment[1], 60, 60))

        # get and print UI----------------------------------------------------------------------------------------------
        score = font.render(f'Snake size: {str(snakeLen)}', True, 'black')
        surface.blit(score, (15, 15))

        # Update========================================================================================================
        pg.display.flip()

        # Limits fps----------------------------------------------------------------------------------------------------
        clock.tick(snakeSpeed)

        # debug=========================================================================================================
        print(f'dir: {snakeDir}, sSp: {snakeSpeed}, len: {snakeLen}, '
              f'fX: {fruitX}, fY: {fruitY}, '
              f'sSegments: {snakeSegments}')

# closes window and quits-----------------------------------------------------------------------------------------------
pg.quit()
