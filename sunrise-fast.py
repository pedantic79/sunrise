#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys
from time import sleep

from lifxlan import LifxLAN, RED, ORANGE, YELLOW


def main():
    lifx = LifxLAN(1)
    devices = lifx.get_lights()
    count = 0
    while len(devices) == 0 and count < 10:
        sleep(2)
        devices = lifx.get_lights()
        count += 1

    bulb = devices[0]
    bulb.set_power("on")
    bulb.set_color(RED, 10, True)
    sunrise(bulb, 30, 100)


def sunrise(bulb, duration_secs, max_brightness):
    colors = [
        [65535, 65535, 0, 3500],  # RED
        [6500, 65535, 0, 3500],  # ORANGE
        [9000, 65535, 0, 3500],  # YELLOW
        [58275, 0, 0, 1500],
        [58275, 0, 0, 2000],
        [58275, 0, 0, 2500],
        [58275, 0, 0, 3000],
        [58275, 0, 0, 3500],
        [58275, 0, 0, 4000],
        [58275, 0, 0, 4500],
        [58275, 0, 0, 5000],
        [58275, 0, 0, 5500],
        [58275, 0, 0, 6000],
        [58275, 0, 0, 6500],
    ]

    time_slice = duration_secs / len(colors)
    power_step = int((65535 * max_brightness / 100) / len(colors))

    power = 0
    for color in colors:
        power = power + power_step
        color[2] = power  # override the brightness
        bulb.set_color(color, time_slice * 1000, False)
        sleep(time_slice)


if __name__ == "__main__":
    main()
