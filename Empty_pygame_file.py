import pygame as py
from menu_prim import *
py.init()
WIDTH, HEIGHT = 800, 600


clock = py.time.Clock()
FPS = 60
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("menu game")


#Основной цикл
while True:
    for event in py.event.get():
        if event.type == py.QUIT:  # закрытие игры крестиком
            exit()

#Основной код

    button1= Button(screen, 100, HEIGHT//7, WIDTH-200, HEIGHT//7, "Старт")
    button2= Button(screen, 100, 3*HEIGHT//7, WIDTH-200,HEIGHT//7, "Првила")
    button3= Button(screen, 100, 5*HEIGHT//7, WIDTH-200, HEIGHT//7, "Выход")
    btn_list = [button1, button2, button3]
    for button in btn_list:
        button.draw(screen)


    if button1.rect.collidepoint(py.mouse.get_pos()):
        button1.bgColor = py.Color("Green")
        button1.font_Color = py.Color("Black")
    if button2.rect.collidepoint(py.mouse.get_pos()):
        print("Првила")
    if button3.rect.collidepoint(py.mouse.get_pos()):
        print("Выход")
        exit()

    py.display.update()
    clock.tick(FPS)  # 60 кадров в секунду