import pygame
import sys
from pygame.locals import *
from random import randint


class Planes():
    def __init__():
        pass


#游戏选项
screen_x = 1440
screen_y = 900
game_name = "客舱营救"
background_image = "a330-300.png"

#初始化声音
#初始化
pygame.init()
window = pygame.display.set_mode((screen_x,screen_y))
pygame.display.set_caption(game_name)
screen = pygame.display.get_surface()
#调入场景（关卡）
finished =False
#初始化变量
clock = pygame.time.Clock()
#设置背景
background=pygame.transform.scale(pygame.image.load(background_image),(screen_x,screen_y)).convert()

while not finished:
    #空白屏幕
    #检查事件
    for event in pygame.event.get():
        if event.type == QUIT:
            finished = True
        #绘制游戏背景
        screen.blit(background,(0,0))
        #刷新显示
        pygame.display.flip()
        #设置游戏速度
        clock.tick(60)