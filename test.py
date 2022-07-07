import pygame as p
import sys
import random as r
import psutil

size = width, height = 600,600
screen = p.display.set_mode(size)
p.init()
p.font.init()
active = True
FPS = 60
CLOCK = p.time.Clock()
cpu_usage = p.font.SysFont('Arial', 50)
frames_per_sec = p.font.SysFont('Arial', 50)

def main():
 frame = 0
 while active:
  for event in p.event.get():
   if event.type == p.QUIT:
    sys.exit()
  color = (r.randint(0,255), r.randint(0,255), r.randint(0,255))
  cpu = psutil.cpu_percent(interval=0)
  frame += 1
  text_s = cpu_usage.render(str(cpu) + ' ' + str(frame), False, (0, 255, 0))
  screen.fill('black')
  screen.blit(text_s, (10, 10))
  frames = frames_per_sec.render(str(CLOCK.get_fps()), False, (0, 255, 0))
  screen.blit(frames, (10, 50))
  CLOCK.tick(FPS)
  p.display.flip()


main()