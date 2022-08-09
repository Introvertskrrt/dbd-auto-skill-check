import os
import sys
import mss
import cv2
import mss
import time
import psutil
import pytesseract
import numpy as np

from AI_Requirements import downloader
from PIL import Image
from time import sleep
from colorama import Fore, init
from pynput.keyboard import Controller,Key
init(convert=True)
system = os.name

# Function
def dbdprocess_check(processName):
    for proc in psutil.process_iter():
        try:
            if processName.lower() in proc.name().lower():
                return False;
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return True;

def isRunning_text():
    if system == 'nt':
        os.system('cls')
    elif system == 'posix':
        os.system('clear')
    else:
        print('\n'*120)
    print(Fore.MAGENTA+"Auto Skill Check | Made By 1ntrovertskrrt\n"+Fore.RESET)
    print("Please NOTE that this Auto Skill Check isn't perfect, sometimes it doesn't hit the skill check!\nMake sure your Secondary Action Skill Check is SPACE BUTTON!")

    print(f"{Fore.GREEN}Auto Skill-check is running!{Fore.RESET}")
    time.sleep(4)

def autoSkill_Check(key):
    with mss.mss() as sct:
        monitor = {"top": 470, "left": 890, "width": 140, "height": 140}
        low_white = np.array([253, 253, 253])
        high_white = np.array([255, 255, 255])

        low_red = np.array([160, 0, 0])
        high_red = np.array([255, 30, 30])
        keyboard = Controller()

        cordsw = []

        while True:
            img = np.array(sct.grab(monitor))
            rgb_image = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            maskw = cv2.inRange(rgb_image, low_white, high_white)
            maskr = cv2.inRange(rgb_image, low_red, high_red)

            cordsr = []

            yw, xw = np.where(maskw != 0)
            yr, xr = np.where(maskr != 0)

            for i in range(len(yw)):
                cordsw.append([yw[i], xw[i]])
            for i in range(len(yr)):
                cordsr.append([yr[i], xr[i]])

            for i in range(len(cordsr)):
                if cordsr[i] in cordsw:
                    print(f"{Fore.GREEN}Successfully hit the Skill Check!{Fore.RESET}")
                    keyboard.press(key)
                    keyboard.release(key)
                    cordsw = []
                    break

            if len(yw) == 0 and len(yr) == 0:
                cordsw = []
            if len(cordsr) == 0:
                cordsw = []
                return

def main_program(): # Main Program!
    with mss.mss() as sct2:
        monitor2 = {"top": 830, "left": 825, "width": 70, "height": 30}

        while True:
            sct_img = sct2.grab(monitor2)
            pytesseract.pytesseract.tesseract_cmd = r'AI_Resources\Tesseract-OCR\tesseract.exe'
            mss.tools.to_png(sct_img.rgb, sct_img.size, output="detector.png")
            detector = pytesseract.image_to_string(Image.open("detector.png"))

            if "REPAIR" in detector:
                print(Fore.BLUE+"GENERATOR DETECTED!"+Fore.RESET)              
                autoSkill_Check(key=Key.space)

            elif "HEAL" in detector:
                print(Fore.BLUE+"HEAL DETECTED!"+Fore.RESET)
                autoSkill_Check(key=Key.space)
            
            else:
                print(Fore.WHITE+"GENERATOR/HEALING NOT DETECTED!"+Fore.RESET)
                pass

if __name__ == "__main__":
    downloader()
    isRunning_text()
    while dbdprocess_check("DeadByDaylight"):
            l = ['|', '/', '-', '\\']
            for i in l+l+l:
                sys.stdout.write('\r' + f'Waiting for Dead by Daylight...'+i)
                sys.stdout.flush()
                sleep(0.2)

    main_program()
