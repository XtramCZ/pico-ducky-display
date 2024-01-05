import digitalio
import board
import storage

button_A = digitalio.DigitalInOut(board.GP15)
button_A.direction = digitalio.Direction.INPUT
button_A.pull = digitalio.Pull.UP

if(button_A.value == True):
    # don't show USB drive to host PC
    storage.disable_usb_drive()
    print("Disabling USB drive")
else:
    # normal boot
    print("USB drive enabled")