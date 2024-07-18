import pyautogui
import keyboard
import time

while True:
    
    pyautogui.scroll(-200)  
    time.sleep(5)
    keyboard.press_and_release('ctrl+tab')
    time.sleep(2)
    pyautogui.moveTo(100, 100)  
    pyautogui.click()

    keyboard.press_and_release('f12')

    time.sleep(2)
    keyboard.press_and_release('ctrl+shift+i')
    pyautogui.scroll(-200)  


    time.sleep(2)
