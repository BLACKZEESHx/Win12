from pynput.keyboard import Key, Listener
import pyautogui, time, keyboard
time.sleep(1)
pyautogui.FAILSAFE = False

def on_press(key):
    if key == Key.right:
        pyautogui.tripleClick(1087, 584, 0.5)

def on_release(key):
    if key == Key.right:
        pyautogui.click(1087, 584)

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
# while True:
#     if keyboard.is_pressed('d'):
#         pyautogui.click(1087, 254)
# pyautogui.displayMousePosition(
# pyautogui.moveTo(1087, 254)