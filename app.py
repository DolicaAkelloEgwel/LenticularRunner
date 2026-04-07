import sys
import os

from app import App
from app_components import clear_background
import imu

from events.input import Buttons, BUTTON_TYPES

# Reminder: https://ctrlaltdelete4real.itch.io/running-animation

if sys.implementation.name == "micropython":
    apps = os.listdir("/apps")
    path = ""
    for a in apps:
        # This is important for apps deployed to the appstore
        # The Snake app from naomi stored at
        # https://github.com/npentrel/tildagon-snake/
        # has all its files in the folder
        # npentrel_tildagon_snake
        if a == "DolicaAkelloEgwel_lenticular":
            path = "/apps/" + a
    ASSET_PATH = path + "/assets/"
else:
    # while testing, put your files in the folder you are developing in,
    # for example: example/streak.jpg
    ASSET_PATH = "apps/lenticular/assets/"

ASSET_PATH = "apps/lenticular/assets/"

IMAGE_COUNT = 19


class LenticularGuy(App):
    def __init__(self):
        self.button_states = Buttons(self)
        self.image_paths = [f"frame_{i:02d}_delay-0.04s.png" for i in range(19)]

    def update(self, delta):
        if self.button_states.get(BUTTON_TYPES["CANCEL"]):
            self.button_states.clear()
            self.minimise()

    def draw(self, ctx):
        clear_background(ctx)
        tilt = int(imu.acc_read()[1] * 3)
        ctx.image(ASSET_PATH + self.image_paths[tilt % IMAGE_COUNT], -100, -100, 200, 200)


__app_export__ = LenticularGuy
