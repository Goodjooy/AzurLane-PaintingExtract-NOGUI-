import time

import pygame
import os
import sys
import win32api


def re_int(num):
    """四舍五入"""
    int_num = int(num)
    float_num = num - int_num

    if float_num >= 0.5:
        return int_num + 1
    if float_num < 0.5:
        return int_num


def show():
    pygame.init()

    scr = pygame.display.set_mode((re_int(1920 / 1), re_int(1080 / 1)), pygame.FULLSCREEN, 32)

    scr_rect = scr.get_rect()

    show_part = pygame.Rect(0, 0, scr_rect.height, scr_rect.height)
    else_part = pygame.Rect(1081, 0, 1920 - 1080, 1080)

    pic_lists = os.listdir('out')

    font = pygame.font.Font('files\\char.ttf', 40)

    num = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        show_pic = pygame.image.load("out\\%s" % pic_lists[num])
        scale = 1
        show_pic_rect = show_pic.get_rect()

        if show_pic_rect.width > show_part.width or show_pic_rect.height > show_part.height:
            scale = min(show_part.width / show_pic_rect.width, show_part.height / show_pic_rect.height)

        show_pic = pygame.transform.smoothscale(show_pic,
                                                (re_int(show_pic_rect.width * scale),
                                                 re_int(show_pic_rect.height * scale)))
        show_pic_rect = show_pic.get_rect()

        show_pic_rect.center = show_part.center

        number = font.render('第%d个' % (num + 1), True, (255, 255, 255), (0, 0, 0))
        number_rect = number.get_rect()
        number_rect.bottomright = scr_rect.bottomright

        name = pic_lists[num].split('.')[0]
        name = font.render('%s' % name, True, (255, 255, 255), (0, 0, 0))
        name_rect = name.get_rect()
        name_rect.topright = scr_rect.topright

        pygame.draw.rect(scr, (255, 255, 255), show_part)
        pygame.draw.rect(scr, (0, 0, 0), else_part)
        scr.blit(show_pic, (show_pic_rect.x, show_pic_rect.y))
        scr.blit(number, (number_rect.x, number_rect.y))
        scr.blit(name, (name_rect.x, name_rect.y))
        time.sleep(2)

        pygame.display.update()
        num += 1
