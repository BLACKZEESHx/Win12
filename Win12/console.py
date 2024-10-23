# Original piece of code
import time, win32con, win32gui


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


foregroundwin = win32gui.FindWindow("Shell_TrayWnd", None)
idsnames = get_child_ids(foregroundwin)

rect = win32gui.GetWindowRect(idsnames[4])
x, y, wn, hn = rect

# win32gui.MoveWindow(idsnames[0], x+448, 0, -480, 40, True)
rectx1 = win32gui.GetWindowRect(idsnames[0])
x, y, w, h = rectx1
# win32gui.MoveWindow(idsnames[0], 448, 0, w, h, win32con.SW_SHOW)
while False:
    rectx1 = win32gui.GetWindowRect(idsnames[0])
    x, y, w, h = rectx1
    while x != 488 and y != 728:
        # win32gui.SetWindowPos(idsnames[0], None, 448, 0, w, h, win32con.SWP_SHOWWINDOW)
        win32gui.SetWindowPos(idsnames[0], None, 448, 0, w, h, win32con.SW_SHOW)
        rectx1 = win32gui.GetWindowRect(idsnames[0])
        print(rectx1)

    # win32gui.ShowWindow(idsnames[0], win32con.SW_SHOW)

print(rectx1)


import time, win32con, win32gui

time.sleep(4)


def round_window(window_handle):
    # Get window dimensions
    left, top, right, bottom = win32gui.GetWindowRect(window_handle)
    width = right - left
    height = bottom - top

    # Create a rounded region
    region = win32gui.CreateRoundRectRgn(0, 0, width, height, 24, 24)

    # Set the window region
    win32gui.SetWindowRgn(window_handle, region, True)
    # Remove border but keep minimize and maximize buttons
    current_style = win32gui.GetWindowLong(window_handle, win32con.GWL_STYLE)
    new_style = (
        (current_style & ~win32con.WS_OVERLAPPEDWINDOW)
        | win32con.WS_POPUP
        | win32con.WS_MINIMIZEBOX
        | win32con.WS_MAXIMIZEBOX
    )
    win32gui.SetWindowLong(window_handle, win32con.GWL_STYLE, new_style)


while True:
    try:
        round_window(window_handle=win32gui.GetForegroundWindow())
        print("window is being rounded")
    except:
        time.sleep(3)
    time.sleep(3)
exit()

# # Optimized piece of code
# import win32gui

# def round_window(window_handle):
#     # Get window dimensions
#     x, y, width, height = win32gui.GetWindowRect(window_handle)

#     corner_radius = 20
#     rounded_region = win32gui.CreateRoundRectRgn(12, -12, x + width, y + height, corner_radius, corner_radius)

#     # Set the window region to the rounded region
#     win32gui.SetWindowRgn(window_handle, rounded_region, True)
# round_window(win32gui.GetForegroundWindow())
# exit()
import pyautogui, win32gui, win32con, ctypes


# win32gui.LoadIcon(None, win32con.IDI_QUESTION)
def roundtaskbar():
    hwnd = win32gui.FindWindow("Shell_TrayWnd", None)
    print(win32gui.GetWindowRect(hwnd))
    hRgn = win32gui.CreateRoundRectRgn(2, -29, 1363, 72, 1363, 72)
    print(win32gui.GetWindowRect(hwnd))

    win32gui.SetWindowRgn(hwnd, hRgn, True)


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


foregroundwin = win32gui.FindWindow("Shell_TrayWnd", None)
idsnames = get_child_ids(foregroundwin)
print(idsnames)


# taskbar
def taskbar():
    print(idsnames)
    rect = win32gui.GetWindowRect(idsnames[4])
    x, y, w, h = rect

    print(rect)
    win32gui.MoveWindow(idsnames[4], w // 2, 0, w, h, True)
    rect = win32gui.GetWindowRect(idsnames[4])
    x, y, w, h = rect
    print(rect)


# tray
def tray():
    rect = win32gui.GetWindowRect(idsnames[8])
    x, y, w, h = rect
    print(rect)

    win32gui.MoveWindow(idsnames[8], 12, 0, w - 12, h - 728, True)
    rect = win32gui.GetWindowRect(idsnames[8])
    x, y, w, h = rect
    print(rect)


print(get_child_ids(idsnames[9 + 1]))
tray()
taskbar()
win32gui.ShowWindow(get_child_ids(idsnames[9 + 1])[12], win32con.SW_HIDE)
# print(start)
rect = win32gui.GetWindowRect(foregroundwin)
ctypes.windll.user32
rectx = win32gui.GetWindowRect(foregroundwin)
x, y, w, h = rectx
print(rectx)
x, y, w, h = rectx
# rect = win32gui.GetWindowRect(idsnames[4])
# x, y, wn, hn = rect

# win32gui.MoveWindow(idsnames[0], x-48, 0, 48-155, 40, True)
# rectx1 = win32gui.GetWindowRect(idsnames[0])
# print(rectx1)

# print(win32gui.GetMenu(foregroundwin))

# def get_child_idsnames(hwnd):
#     child_ids_names = {}
#     child = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
#     while child != 0:
#         child_name = win32gui.GetWindowText(child)
#         child_ids_names.update({child_name: child})
#         child = win32gui.GetWindow(child, win32con.GW_HWNDNEXT)
#     return child_ids_names
