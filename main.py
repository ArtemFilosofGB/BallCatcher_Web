import asyncio
import pygame as py
import pygame
from random import randint
from constpygame import *

img_path="/data/data/org.afilosof.ballcatcker/files/app/"
img_path=""
class Ball(pygame.sprite.Sprite):
    def __init__(self,x, speed_fall, surf,score, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = surf
        self.image = pygame.transform.scale(self.image, (100, 100))
        #self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = speed_fall
        self.score = score
        self.add(group)


    def update(self,*args):
        if self.rect.y < args[0]-20:
            self.rect.y+=self.speed
        else:
            self.kill()
        # Вращение мяча

def create_ball(group):
    indx = randint(0, len(ball_surf) - 1)
    x = randint(20, WIDTH - 20)
    speed = randint(1, 4)
#    s_kick.play()

    return Ball(x, speed, ball_surf[indx], balls_data[indx]['scope'], group)
# Try to declare all your globals at once to facilitate compilation later.


def collide_balls():
    global game_score
    for ball in balls:
        if catcher_rect.collidepoint(
                ball.rect.center):  # пересечение: координата центра мяча ball.rect.center, прямоугольник вратаря
            #s_catch.play()
            game_score += ball.score
            ball.kill()


def gate_goal():
    global game_goals
    for ball in balls:
        if gate_rect.collidepoint(
                ball.rect.center):  # пересечение: координата центра мяча ball.rect.center, прямоугольник вратаря
            game_goals += 1
            print("Goals: ", game_goals)
            ball.kill()


def difficult_up( new_catcher_speed: int):
    global catcher_speed
    catcher_speed = new_catcher_speed


def game_over():
    global game_score
    if game_goals == 3:
        py.mixer.music.stop()
        
        screen.blit(game_goals_img, (WIDTH // 2 - 50, HEIGHT // 2 - 50))
        print("Game over")
        game_score = "GAME OVER"

        py.quit()
        exit()

#py.mixer.pre_init(44100, -16, 1, 512)  # инициализация до py.init()

py.init()


clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)
# Screen
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")
#py.display.set_icon(py.image.load(img_path + "img/icon.bmp"))
screen.fill(WHITE)
# Do init here
# Load any assets right now to avoid lag at runtime or network errors.
surf = py.Surface((WIDTH, 200))
bita = py.Surface((50, 50))

ball = py.image.load(img_path + "img/ball.png")
ball = py.transform.scale(ball, (100, 100))
ball_rect = ball.get_rect()

py.mixer.music.load(img_path + "sounds/marsh.mp3")
py.mixer.music.play(1, 0, 0)
py.mixer.music.set_volume(0.3)



surf.fill(BLUE)
bita.fill(RED)
bita.set_alpha(0)

bx, by = 0, 150
x, y = 0, 0



py.time.set_timer(py.USEREVENT, 2000)


#s_catch = py.mixer.Sound("sounds/arena.wav")

#s_kick = py.mixer.Sound("sounds/kick.mp3")

WIDTH, HEIGHT = 800, 600

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

clock = py.time.Clock()
FPS = 60
RGB = (255, 255, 255)

screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Pygame game game")


background = py.image.load((img_path + "img/sky.png")).convert()
background = py.transform.scale(background, (WIDTH, HEIGHT))  # масштабирование фона

score = py.image.load(img_path + "img/field.jpg").convert_alpha()
score = py.transform.scale(score, (100, 100))
f = py.font.SysFont("Verdana", 30)

game_goals_img = py.image.load(img_path + "img/field.jpg").convert_alpha()
game_goals_img = py.transform.scale(game_goals_img, (100, 100))

gate = py.Surface((WIDTH, 10))
gate.fill((0, 0, 0))
gate.set_alpha(100)  # прозрачность
gate_rect = gate.get_rect(topleft=(0, HEIGHT - 10))

balls_data = ({'path': 'ball.png', 'scope': 100},
            {'path': 'ball2.png', 'scope': 150},
            {'path': 'ball3.png', 'scope': 200})

ball_surf = [py.image.load('img/' + data['path']).convert_alpha() for data in balls_data]

balls = py.sprite.Group()  # создание группы спрайтов для совместного управления

# вратарь
catcher = py.image.load("img/catcher.png").convert_alpha()
catcher = py.transform.scale(catcher, (200, 200))
catcher_rect = catcher.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 150))

catcher_l = catcher
catcher_r = py.transform.flip(catcher, True, False)

game_score = 0  # игровой счёт
game_goals = 0  # счётчик пропущеных голов

catcher_speed = 10  # скорость вратаря
catchaer_offset = 0

create_ball(balls)

angle_ball = 0


py.display.update()

async def main():
    global COUNT_DOWN
    global bx, by, x, y
    global catchaer_offset
    global catcher
    # avoid this kind declaration, prefer the way above


    while True:
        for event in py.event.get():
            if event.type == py.QUIT:  # закрытие игры крестиком
                exit()

            if event.type == py.USEREVENT:
                create_ball(balls)

        keys = py.key.get_pressed()
        if keys[py.K_LEFT]:
            catcher_rect.x -= catcher_speed
            catcher = catcher_l  # переключение спрайтов направления вратаря
            catchaer_offset = -catcher_speed // 5
            if catcher_rect.x < 0:
                catcher_rect.x = 0
        elif keys[py.K_RIGHT]:
            catcher_rect.x += catcher_speed
            catcher = catcher_r
            catchaer_offset = catcher_speed // 5
            if catcher_rect.x > WIDTH - catcher_rect.width:
                catcher_rect.x = WIDTH - catcher_rect.width
        elif keys[py.K_ESCAPE] or keys[py.K_q]:
            exit()

        if catcher_rect.x < 0 or catcher_rect.x > WIDTH - catcher_rect.width:
            catchaer_offset = 0
        catcher_rect.x += catchaer_offset

        if game_score > 1000 and game_score <= 2000:
            difficult_up(5)
        elif game_score > 2000 and game_score <= 3000:
            difficult_up(3)
        elif game_score > 3000:
            difficult_up(1)

        collide_balls()  # сначала контролируем столкновение потом прорисовываем картинку
        gate_goal()  # вывод пропущеных голов

        # Отрисовка всех поверхностей
        screen.blit(background, (0, 0))
        screen.blit(score, (0, 0))
        screen.blit(game_goals_img, (WIDTH - 100, 0))

        # вывод очков
        screen_text = f.render(str(game_score), True, (0, 0, 0))
        screen.blit(screen_text, (20, 50))
        # вывод пропущеных голов
        screen_text = f.render(str(game_goals), True, (0, 0, 0))
        screen.blit(screen_text, (WIDTH - 50, 50))

        balls.draw(screen)
        screen.blit(catcher, catcher_rect)
        screen.blit(gate, (0, HEIGHT - 10))
        py.display.update()

        # Основной код
        balls.update(HEIGHT)
        game_over()
        clock.tick(FPS)  # 60 кадров в секунду
        # Do your rendering here, note that it's NOT an infinite loop,
        # and it is fired only when VSYNC occurs
        # Usually 1/60 or more times per seconds on desktop
        # could be less on some mobile devices


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