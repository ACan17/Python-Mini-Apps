import psutil as pc
from pynotifier import Notification
import time

while True:
    battery = pc.sensors_battery()
    plugged = battery.power_plugged
    percent = str(battery.percent)

    remaining = "Battery is at " + percent + "%"
    if plugged:
        remaining += " and is plugged in."
    else:
        remaining += " and is not plugged in."

    if battery.percent <= 30:
        Notification(
            title="Battery Low",
            description=remaining,
            icon_path="battery.ico",
            duration=5, # Duration in seconds
            urgency="CRITICAL"
        ).send()

    if battery.percent >= 30 and battery.percent <= 60:
        Notification(
            title="Battery Medium",
            description=remaining,
            icon_path="battery.ico",
            duration=5, # Duration in seconds
            urgency="NORMAL"
        ).send()

    if battery.percent == 100:
        Notification(
            title="Battery Full",
            description=remaining,
            icon_path="battery.ico",
            duration=5, # Duration in seconds
            urgency="CRITICAL"
        ).send()

    time.sleep(60*60)
