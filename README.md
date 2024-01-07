<h1 align="center">pico-ducky</h1>

<div align="center">
  <strong>Make a cheap but powerful USB Rubber Ducky with a Raspberry Pi Pico</strong>
</div>

# Disclaimer
This project was originally done by [@dbisu](https://github.com/dbisu/pico-ducky), not me. I have only changed the code to work with a display.

## Quick Start Guide

You will need:
- Raspberry Pi Pico (With headers)
- Waveshare LCD 1.3 (4 buttons, recommended) or Waveshare LCD 1.14 (2 buttons). With only two buttons you may miss out on some features in the future. You also may need to tweak the UI on 1.14 a bit, so that it fits.
  
# Full Install Instructions

Install and have your USB Rubber Ducky working in less than 5 minutes.

1. Clone the repo to get a local copy of the files. `https://github.com/XtramCZ/pico-ducky-display`

2. Download [CircuitPython for the Raspberry Pi Pico](https://circuitpython.org/board/raspberry_pi_pico/). *Updated to 8.0.0  

3. Plug the device into a USB port while holding the boot button. It will show up as a removable media device named `RPI-RP2`.

4. Copy the downloaded `.uf2` file to the root of the Pico (`RPI-RP2`). The device will reboot and after a second or so, it will reconnect as `CIRCUITPY`.

5. Download `adafruit-circuitpython-bundle-8.x-mpy-YYYYMMDD.zip` [here](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases/latest) and extract it outside the device.

6. Navigate to `lib` in the recently extracted folder and copy `adafruit_hid`, `asyncio` and `adafruit_display_text` to the `lib` folder on your Raspberry Pi Pico.

7. Copy `adafruit_debouncer.mpy`, `adafruit_st7789.mpy` and `adafruit_ticks.mpy` to the `lib` folder on your Raspberry Pi Pico.

8. Copy `boot.py`, `duckyinpython.py` and `code.py` to the root folder of the Pico.

9. Find a script [here](https://github.com/hak5/usbrubberducky-payloads) or [create your own one using Ducky Script](https://docs.hak5.org/hak5-usb-rubber-ducky/ducky-script-basics/hello-world) and save it in the _payloads_ folder. Currently, pico-ducky only supports DuckyScript 1.0, not 3.0.

## Navigation

You may navigate via the display UI with the joystick. UP for going UP and DOWN for going DOWN. Press the stick for execution.
The red text is your selection. If you select a payload and click the joystick it is going to be executed. If you selected a folder then you will go into the folder. If your selection is on the top "breadcrumb" you will go a directory back. 

## USB enable/disable mode

If you need the pico-ducky to show up as a USB mass storage device for editing the files, hold the A button while plugging in your Pico.


## Changing Keyboard Layouts

Copied from [Neradoc/Circuitpython_Keyboard_Layouts](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/blob/main/PICODUCKY.md)  

#### How to use one of these layouts with the pico-ducky repository.

**Go to the [latest release page](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/releases/latest), look if your language is in the list.**

#### If your language/layout is in the bundle

Download the `py` zip, named `circuitpython-keyboard-layouts-py-XXXXXXXX.zip`

**NOTE: You can use the mpy version targetting the version of Circuitpython that is on the device, but on Raspberry Pi Pico you don't need it - they only reduce file size and memory use on load, which the pico has plenty of.**

#### If your language/layout is not in the bundle

Try the online generator, it should get you a zip file with the bundles for yout language

https://www.neradoc.me/layouts/

#### Now you have a zip file

#### Find your language/layout in the lib directory

For a language `LANG`, copy the following files from the zip's `lib` folder to the `lib` directory of the board.  
**DO NOT** modify the adafruit_hid directory. Your files go directly in `lib`.  
**DO NOT** change the names or extensions of the files. Just pick the right ones.  
Replace `LANG` with the letters for your language of choice.

- `keyboard_layout_win_LANG.py`
- `keycode_win_LANG.py`

Don't forget to get [the adafruit_hid library](https://github.com/adafruit/Adafruit_CircuitPython_HID/releases/latest).

This is what it should look like **if your language is French for example**.

![CIRCUITPY drive screenshot](https://github.com/Neradoc/Circuitpython_Keyboard_Layouts/raw/main/docs/drive_pico_ducky.png)

#### Modify the pico-ducky code to use your language file:

At the start of the file comment out these lines:

```py
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayout
from adafruit_hid.keycode import Keycode
```

Uncomment these lines:  
*Replace `LANG` with the letters for your language of choice. The name must match the file (without the py or mpy extension).*
```py
from keyboard_layout_win_LANG import KeyboardLayout
from keycode_win_LANG import Keycode
```

##### Example:  Set to German Keyboard (WIN_DE)

```py
from keyboard_layout_win_de import KeyboardLayout
from keycode_win_de import Keycode
```

Copy the files keyboard_layout_win_de.mpy and keycode_win_de.mpy to the /lib folder on the Pico board
```
adafruit_hid/
keyboard_layout_win_de.mpy
keycode_win_de.mpy
```



## Useful links and resources

### How to recover your Pico if it becomes corrupted or doesn't boot.

[Reset Instructions](RESET.md)

### Installation Tool

[raspberrydeveloper](https://github.com/raspberrydeveloper) Created a tool to convert a blank RPi Pico to a ducky.  
You can find the tool [here](https://github.com/raspberrydeveloper/pyducky)

### Docs

[CircuitPython](https://circuitpython.readthedocs.io/en/6.3.x/README.html)

[CircuitPython HID](https://learn.adafruit.com/circuitpython-essentials/circuitpython-hid-keyboard-and-mouse)

[Ducky Script](https://github.com/hak5darren/USB-Rubber-Ducky/wiki/Duckyscript)

### Video tutorials

[pico-ducky tutorial by **NetworkChuck**](https://www.youtube.com/watch?v=e_f9p-_JWZw)

[USB Rubber Ducky playlist by **Hak5**](https://www.youtube.com/playlist?list=PLW5y1tjAOzI0YaJslcjcI4zKI366tMBYk)

[CircuitPython tutorial on the Raspberry Pi Pico by **DroneBot Workshop**](https://www.youtube.com/watch?v=07vG-_CcDG0)
