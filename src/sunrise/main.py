from time import sleep

from lifxlan import RED, LifxLAN

from sunrise import sunrise


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
    sunrise(bulb, 20 * 60, 100)


if __name__ == "__main__":
    main()
