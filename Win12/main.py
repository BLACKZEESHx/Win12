import time, win32con, win32gui
import pyautogui, threading
# from win32ui import CreateButton
time.sleep(4)
desktop = pyautogui.size()
height, width = desktop.height, desktop.width

def get_child_ids(hwnd):
    child_ids = []
    child = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    child_name = win32gui.GetWindowText(child)

    while child != 0:
        child_ids.append(child)
        child_ids.append(child_name)
        child = win32gui.GetWindow(child, win32con.GW_HWNDNEXT)
        child_name = win32gui.GetWindowText(child)
    return child_ids

taskbar =  win32gui.FindWindow(u'Shell_TrayWnd', None)
idsnames = get_child_ids(taskbar)
print(idsnames)
hStartMenu = win32gui.FindWindow("Windows.UI.Core.CoreWindow", "Start")

# def get_window_rgn(hwnd):
#     # Get the window region and return it as a tuple (left, top, right, bottom)
#     rgn = win32gui.CreateRectRgnIndirect((0, 0, 0, 0))
#     result = win32gui.GetWindowRgn(hwnd, rgn)

#     if result == win32con.COMPLEXREGION:
#         # Handle complex regions if needed
#         pass

#     left, top, right, bottom = win32gui.GetRgnBox(rgn)
#     return (left, top, right, bottom)

def round_window(window_handle):
    # {
    # # Method 1 //I don't like it
    # # Get window dimensions
    # # left, top, right, bottom = win32gui.GetWindowRect(window_handle)
    # # width = right - left
    # # height = bottom - top
    
    # # # Create a rounded region
    # # region = win32gui.CreateRoundRectRgn(11, 12*2+9, width-12, height-9+1, 14, 14)
    
    # # # Set the window region
    # # win32gui.SetWindowRgn(window_handle, region, True)

    # }
    if window_handle != 0:
        print(window_handle)
        # Method 2 //I love it
        # Get the width and height of the window
        width = win32gui.GetWindowRect(window_handle)[2] - win32gui.GetWindowRect(window_handle)[0]
        height = win32gui.GetWindowRect(window_handle)[3] - win32gui.GetWindowRect(window_handle)[1]
        # Create a region object with rounded corners    
        width = win32gui.GetWindowRect(window_handle)[2] - win32gui.GetWindowRect(window_handle)[0]
        height = win32gui.GetWindowRect(window_handle)[3] - win32gui.GetWindowRect(window_handle)[1]
        win32gui.SetWindowRgn(window_handle, win32gui.CreateRoundRectRgn(0, 0, width, height, 0, 0), True)
        rgn = win32gui.CreateRoundRectRgn(0, 0, width, height, 25, 25)
        # Set the window region to the region object
        win32gui.SetWindowRgn(window_handle, rgn, True)
# Tray
def Tray():
    rect = win32gui.GetWindowRect(idsnames[8])
    x, y, w, h = rect
    print(rect)

    win32gui.MoveWindow(idsnames[8], 22, 0, w-22, 0, True)
    rect = win32gui.GetWindowRect(idsnames[8])
    x, y, w, h = rect
    print(rect)

# Taskbar 
def Taskbar():
    rect = win32gui.GetWindowRect(idsnames[4])
    x, y, w, h = rect
    print(rect)
    win32gui.MoveWindow(idsnames[4], w//2, 0, w, h, True)
    rect = win32gui.GetWindowRect(idsnames[4])
    x, y, w, h = rect
    print("Taskbar", rect)

def MoveStart():
    rect = win32gui.GetWindowRect(idsnames[0])
    x, y, w, h = rect
    print(rect)
    rect = win32gui.GetWindowRect(idsnames[4])
    x, y, wn, hn = rect

    win32gui.MoveWindow(idsnames[0], x-48, 0, 48, 40, True)
    # win32gui.SetWindowPos(idsnames[0], None, w//2-12, y, w, 0, win32con.SWP_SHOWWINDOW)
    # win32gui.MoveWindow(idsnames[0], x-58, 0, 58-155, 40, True)
    # win32gui.MoveWindow(idsnames[0], 155, 0, 48-155, 40, True)

    rect = win32gui.GetWindowRect(idsnames[0])
    x, y, w, h = rect
    print("Start", rect)
    
def Rounded_Start(hwnd, radius):
  rect = win32gui.GetWindowRect(hStartMenu)
  x, y, w, h = rect
  # Get the width and height of the window
  width = win32gui.GetWindowRect(hwnd)[2] - win32gui.GetWindowRect(hwnd)[0]
  height = win32gui.GetWindowRect(hwnd)[3] - win32gui.GetWindowRect(hwnd)[1]
  # Create a region object with rounded corners
  
  width = win32gui.GetWindowRect(hwnd)[2] - win32gui.GetWindowRect(hwnd)[0]
  height = win32gui.GetWindowRect(hwnd)[3] - win32gui.GetWindowRect(hwnd)[1]
#   win32gui.SetWindowPos(hStartMenu, None, (width//2)//2, y, width, height, win32con.SWP_SHOWWINDOW)
  rgn = win32gui.CreateRoundRectRgn(3, 3, width-3, height-3, radius, radius)
#   if time == 1:

  # Set the window region to the region object
  win32gui.SetWindowRgn(hwnd, rgn, True)
  
def main():
    # Tray()
    Taskbar()
    print(win32gui.GetClassName(win32gui.GetForegroundWindow()))
    print(win32gui.GetWindowText(win32gui.GetForegroundWindow()))
    # while True:
    # MoveStart()

    # round_window(window_handle=win32gui.GetForegroundWindow())
# main()
# fg = win32gui.GetForegroundWindow()
# rect = win32gui.GetWindowRect(fg)
# x, y, wsd, h = rect
# alls = x+y+wsd+h
# Rounded_Start(hStartMenu, 455)
# Rounded_Start(fg, 15)
# round_window(fg)
def run_periodically():
    while True:
        round_window(win32gui.GetForegroundWindow())
        time.sleep(3)  # Wait for 1 second before running the function again

# Create and start a new thread to run the function periodically
thread = threading.Thread(target=run_periodically)
# thread.daemon = True  # This makes the thread exit when the main program exits
thread.start()
# check_matching_regions(win32gui.GetForegroundWindow())

# main()
# while True:
    # MoveStart()