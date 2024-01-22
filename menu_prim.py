from hashlib import new

import pygame as py

M_RED = (131, 20, 9)
M_BLUE = (0, 155, 217)
M_YELLOW = (252, 207, 0)
M_GREEN = (68, 175, 53)

"""
Class Button:
Создание кнопки
"""


class Button:
    def __init__(self, window: py.surface.Surface, btnX=100, btnY=100, btnW=200, btnH=100, btntext="Button", font=None,
                 btnColor=M_RED, bgColor=M_YELLOW, font_Color=M_RED):
        self.btnX = btnX
        self.btnY = btnY
        self.btnW = btnW
        self.btnH = btnH
        self.btnColor = btnColor
        self.bgColor = bgColor
        self.btntext = btntext
        self.font = font
        self.font_Color = font_Color
        self.rect = py.Rect(btnX, btnY, btnW, btnH)
        self.text = py.font.SysFont(self.font, self.btnX).render(self.btntext, True, self.font_Color)
        self.window = window

    def update(self):
        pass

    def draw(self, window):
        py.draw.rect(window, self.bgColor, self.rect)
        py.draw.rect(window, self.btnColor, self.rect, 10)
        self.window.blit(self.text, (self.btnX + (self.btnW / 2 - self.text.get_width() / 2),
                                     self.btnY + (self.btnH / 2 - self.text.get_height() / 2)))
    def print_text(self,text):
        text_print = py.font.SysFont(self.font, self.btnX).render(text, True, self.font_Color)
        self.window.blit(text_print,(10,10))

    def render_multi_line(self, text, x, y, fsize):
        lines = text.splitlines()
        lines_rendered = []
        for line in range(len(lines)-1):
            text_print = py.font.SysFont(self.font, fsize).render(lines[line], True, self.font_Color)
            lines_rendered[line] = text_print
        self.window.fill((0, 0, 0))
        for line in range(len(lines_rendered)):
            self.window.blit(lines_rendered[line], (x, y+fsize*line))

    def draw_multiline_text(self, text, pos, font, color):
        words = [word.split(' ') for word in text.splitlines()]  # Splitting the text into lines and words
        space = font.size(' ')[0]  # Calculating the width of a space in the given font
        x, y = pos  # Getting the starting position
        self.window.fill((0, 0, 0))
        for line in words:
            for word in line:
                word_surface = font.render(word, True, color)  # Rendering each word
                word_width, word_height = word_surface.get_size()
                if x + word_width >= self.window.get_width():
                    x = pos[0]  # Reset the x position if the word exceeds the surface width
                    y += word_height  # Move to the next line
                self.window.blit(word_surface, (x, y))
                x += word_width + space  # Moving the x position to the right for the next word
            x = pos[0]  # Reset the x position for the next line
            y += word_height  # Move to the next line
