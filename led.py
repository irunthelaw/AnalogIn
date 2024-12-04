# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials: PWM with Fixed Frequency example."""
import time
import board
import pwmio
from analogio import AnalogIn

pot = AnalogIn(board.A1)
led = pwmio.PWMOut(board.D0, frequency=5000, duty_cycle=0)

max_val = 65535

while True:
            led.duty_cycle = pot.value 
