from time import sleep

import lifxlan


def sunrise(
    bulb: lifxlan.Light, duration_secs: int, max_brightness_percentage: int
) -> None:
    # The brightness will be controlled seperately via power
    colors = [lifxlan.RED, lifxlan.ORANGE, lifxlan.YELLOW]

    for temperature in range(1500, 6501, 500):
        color = (*lifxlan.WHITE[:3], temperature)
        colors.append(color)

    time_slice = duration_secs / len(colors)
    power_step = (65535 * max_brightness_percentage / 100) / len(colors)

    power = 0
    for color in colors:
        power = power + power_step
        new_color = (color[0], color[1], int(power), color[3])
        bulb.set_color(new_color, int(time_slice * 1000), False)
        sleep(time_slice)


def main_helper(duration_secs: int) -> None:
    lifx_lan = lifxlan.LifxLAN(1)
    devices = lifx_lan.get_color_lights()
    count = 0
    while len(devices or []) == 0 and count < 10:
        sleep(2)
        devices = lifx_lan.get_color_lights()
        count += 1

    assert devices is not None
    assert len(devices) > 0

    bulb = devices[0]

    bulb.set_power("on")
    bulb.set_color(lifxlan.RED, 10, True)
    sunrise(bulb, duration_secs, 100)
