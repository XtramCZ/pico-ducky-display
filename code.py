import board
import os
import terminalio
import displayio
import digitalio
import busio
import supervisor
from adafruit_display_text import label
from adafruit_debouncer import Debouncer
from adafruit_st7789 import ST7789

from duckyinpython import *

# Release any resources currently in use for the displays
displayio.release_displays()

# --- Setup st7789 display---
# Define GPIOs for ST7789
tft_SCL = board.GP10
tft_SDA = board.GP11
tft_RES = board.GP12
tft_DC = board.GP8
tft_CS = board.GP9

# Setup the controls
joystick_up = digitalio.DigitalInOut(board.GP2)
joystick_up.direction = digitalio.Direction.INPUT
joystick_up.pull = digitalio.Pull.UP
joystick_up_deb = Debouncer(joystick_up)

joystick_down = digitalio.DigitalInOut(board.GP18)
joystick_down.direction = digitalio.Direction.INPUT
joystick_down.pull = digitalio.Pull.UP
joystick_down_deb = Debouncer(joystick_down)

joystick_center = digitalio.DigitalInOut(board.GP3)
joystick_center.direction = digitalio.Direction.INPUT
joystick_center.pull = digitalio.Pull.UP
joystick_center_deb = Debouncer(joystick_center)



# Setup display
tft_spi = busio.SPI(clock=tft_SCL, MOSI=tft_SDA)
display_bus = displayio.FourWire(tft_spi, command=tft_DC, chip_select=tft_CS, reset=tft_RES)
display = ST7789(display_bus, width=320, height=240, rotation=270)

# Make the display context
splash = displayio.Group()
display.root_group = splash
text_group = displayio.Group(scale=2, x=10, y=10)
selected = 1
selected_color = 0xff7f50

def clear_text():
    while len(text_group) > 0:
        text_group.pop()

def show_text(text):
    color = 0xffffff
    if len(text_group) > 0:
        text = "\n"*len(text_group) + text
    if len(text_group) == 0:
        color = 0x00ffff
    if len(text_group) == 1:
        color = selected_color
    text_area = label.Label(terminalio.FONT, text=text, color=color)
    text_group.append(text_area) 
 
# Functions
def select(direction):
    global selected
    global selected_color
    if direction == 1: # up
        if selected > 0:
            text_group[selected].color = 0xffffff
            selected -= 1
            text_group[selected].color = selected_color
        elif selected == 0:
            text_group[selected].color = 0x00ffff
            selected = len(text_group) - 1
            text_group[selected].color = selected_color

    elif direction == 0: # down
        if selected == len(text_group)-1:
            text_group[selected].color = 0xffffff
            selected = 0
            text_group[selected].color = selected_color
        elif selected == 0:
            text_group[selected].color = 0x00ffff
            selected = selected + 1
            text_group[selected].color = selected_color
        elif selected < len(text_group)-1:
            text_group[selected].color = 0xffffff
            selected = selected + 1
            text_group[selected].color = selected_color
 
 # Load the payloads
path = "payloads"
files = os.listdir(path)
def showFiles():
    # Build the breadcrumb, if pwd is root, then only / is shown
    breadcrumb = ".."+path[8:] if path[8:] is not "" else "/"

    clear_text()
    show_text(f"{breadcrumb}")
    # Check if empty
    if len(files) > 0:
        for file in files:
            if file.endswith(".dd"):
                show_text(file)
            else:
                show_text("/" + file)
    else:
        show_text("No payloads found")

showFiles()

# When the joystick button is pressed, run the selected script/folder
def run(): 
    global selected, files, path
    if selected == 0:
        if path == "payloads":
            return 
        else:
            path = "/".join(path.split("/")[:-1])
            print("path changed to " + path)
            files = os.listdir(path)
            showFiles()
    elif selected == 1 and len(files) == 0:
        return
    elif files[selected - 1].endswith(".dd"):
        print("Running " + files[selected - 1])
        runScript(path + "/" + files[selected - 1])
    else:
        path += f"/{files[selected -1]}"
        files = os.listdir(path)
        showFiles()
    selected = 1

# Append the text group to the splash
splash.append(text_group)

while True:
    joystick_up_deb.update()
    joystick_down_deb.update()
    joystick_center_deb.update()

    if joystick_up_deb.rose:
        select(1)
    elif joystick_down_deb.rose:
        select(0)
    elif joystick_center_deb.rose:
        run()