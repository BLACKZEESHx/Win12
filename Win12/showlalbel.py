import time, win32con, win32gui
# import pyautogui
time.sleep(3)

print(win32gui.GetWindow(win32gui.GetForegroundWindow(), 5))
# win32gui.SetForegroundWindow(win32gui.GetDesktopWindow())
# win32gui.ShowWindow(win32gui.Get(), 0)
