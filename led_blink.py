# -*- coding: utf-8 -*-
try:
    from RPi import GPIO
except RuntimeError:
    print('Could not import RPi.GPIO. Please make sure you are a root user')
import time

PIN = 12


def blink(pin, sleep_time=0.5):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(sleep_time)

    GPIO.output(pin, GPIO.LOW)
    time.sleep(sleep_time)


def init(pin):
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin, GPIO.OUT)
    GPIO.setwarnings(False)

init(PIN)
timeout = float(raw_input('Enter the amount of seconds for each blink: '))

try:
    while True:
        blink(PIN, timeout)
except KeyboardInterrupt:
    pass
GPIO.cleanup(PIN)
