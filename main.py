import asyncio
import pygame as py
from constpygame import *

# Try to declare all your globals at once to facilitate compilation later.
COUNT_DOWN = 3
py.init()


clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)
# Screen
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
py.display.set_icon(py.image.load("icon.bmp"))
screen.fill(WHITE)
# Do init here
# Load any assets right now to avoid lag at runtime or network errors.
surf = py.Surface((WIDTH, 200))
bita = py.Surface((50, 50))

ball = py.image.load("img/ball.png")
ball = py.transform.scale(ball, (100, 100))
ball_rect = ball.get_rect()

py.mixer.music.load("sounds/marsh.mp3")
py.mixer.music.play(1, 0, 0)
py.mixer.music.set_volume(0.3)

surf.fill(BLUE)
bita.fill(RED)
bita.set_alpha(0)

bx, by = 0, 150
x, y = 0, 0

py.display.update()

async def main():
    global COUNT_DOWN
    global bx, by, x, y

    # avoid this kind declaration, prefer the way above
    COUNT_DOWN = 3

    while True:
        for event in py.event.get():
            if event.type == py.QUIT:  # закрытие игры крестиком
                exit()
        # Отрисовка поверхностей
        surf.fill(BLUE)
        surf.blit(bita, (bx, by))
        bita.set_alpha(int(255 - bx // 3.2))  # изменение прозрачности 0 .. 250
        print(bx)
        # Измененние координат поверхностей
        if bx < WIDTH:
            bx += 5
        else:
            bx = 0
        if y < HEIGHT:
            y += 1
        else:
            y = 0
        screen.fill(WHITE)
        screen.blit(surf, (x, y))
        screen.blit(ball, ball_rect)
        # движение на клавиатуре
        if event.type == py.KEYDOWN:
            if event.key == py.K_LEFT:
                x -= 10
            elif event.key == py.K_RIGHT:
                x += 10
            elif event.key == py.K_UP:
                y -= 10
            elif event.key == py.K_DOWN:
                y += 10

        py.display.update()
        clock.tick(FPS)  # 60 кадров в секунду
        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices

        print(f"""

            Hello[{COUNT_DOWN}] from Python

""")
        # pygame.display.update() should go right next line

        await asyncio.sleep(0)  # Very important, and keep it 0

        # if not COUNT_DOWN:
        #     return
        #
        # COUNT_DOWN = COUNT_DOWN - 1

# This is the program entry point:
asyncio.run(main())

# Do not add anything from here, especially sys.exit/pygame.quit
# asyncio.run is non-blocking on pygame-wasm and code would be executed
# right before program start main()