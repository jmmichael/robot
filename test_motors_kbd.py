from Raspi_MotorHAT import Raspi_MotorHAT

import time
import atexit
import pygame
import sys

from pygame.locals import *

pygame.init()
pygame.display.set_mode((240, 280))


mh = Raspi_MotorHAT(addr=0x6f)
lm = mh.getMotor(1)
rm = mh.getMotor(2)
#set speed
speed = 25
bspeed = -5
#set increment
inc = 5

def turn_off_motors():
        lm.run(Raspi_MotorHAT.RELEASE)
        rm.run(Raspi_MotorHAT.RELEASE)
atexit.register(turn_off_motors)

'''lm.setSpeed(speed + inc)# M1 fan
rm.setSpeed(speed)# M2

lm.run(Raspi_MotorHAT.FORWARD)
rm.run(Raspi_MotorHAT.FORWARD)
time.sleep(2)
'''
while True:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_UP:
                inc = inc + 5
                rm.setSpeed(speed + inc)
                rm.run(Raspi_MotorHAT.FORWARD)
                print ("rm")+(str(inc))
            elif event.key == K_DOWN:
                inc = inc - 5
                rm.setSpeed(speed + inc)
                rm.run(Raspi_MotorHAT.FORWARD)
                print ("rm")+(str(inc))

            elif event.key == K_RIGHT:
                inc = inc + 5
                lm.setSpeed(speed + inc)
                lm.run(Raspi_MotorHAT.FORWARD)
                print ("lm")+(str(inc))
            elif event.key == K_LEFT:
                inc = inc - 5
                lm.setSpeed(speed + inc)
                lm.run(Raspi_MotorHAT.FORWARD)
                print ("lm")+(str(inc))
            elif event.key == K_KP8:#keypad8
				inc = inc + 5
				rm.setSpeed(bspeed + inc)
				rm.run(Raspi_MotorHAT.BACKWARD)
				print ("bb")+(str(inc))
                
				
        if event.type == QUIT:
             turn_off_motors
             print ("bye")
                
