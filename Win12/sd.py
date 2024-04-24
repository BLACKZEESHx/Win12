from console import taskbar
import win32gui, time, win32con
import pyautogui

time.sleep(2)
hStartMenu = win32gui.FindWindow("Windows.UI.Core.CoreWindow", "Start")
desktop = pyautogui.size()
height, width = desktop.height, desktop.width
# hStartMenu = win32gui.FindWindow(None, "Shell_TrayWnd")
rect = win32gui.GetWindowRect(hStartMenu)
x, y, w, h = rect

def Rounded_Start(hwnd, radius):
  # Get the width and height of the window
  width = win32gui.GetWindowRect(hwnd)[2] - win32gui.GetWindowRect(hwnd)[0]
  height = win32gui.GetWindowRect(hwnd)[3] - win32gui.GetWindowRect(hwnd)[1]

  # Create a region object with rounded corners
  rgn = win32gui.CreateRoundRectRgn(0, height//6-25, width-w//2+(52*3)-12, height, radius, radius)
  width = win32gui.GetWindowRect(hwnd)[2] - win32gui.GetWindowRect(hwnd)[0]
  height = win32gui.GetWindowRect(hwnd)[3] - win32gui.GetWindowRect(hwnd)[1]
  win32gui.SetWindowPos(hStartMenu, None, (width//2)//2, y-9+1, width, height, win32con.SWP_SHOWWINDOW)



  # Set the window region to the region object
  win32gui.SetWindowRgn(hwnd, rgn, True)
Rounded_Start(hStartMenu, 25)
print(win32gui.GetClassName(win32gui.GetForegroundWindow()))
print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
