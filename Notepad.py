import subprocess
import pyautogui
import time

def notepad(text):
    subprocess.Popen(['notepad.exe'])
    time.sleep(2)
    pyautogui.typewrite(text, interval=0.1)
