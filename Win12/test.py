# import win32gui
# foregroundwin =  win32gui.FindWindow(u'Shell_TrayWnd', None)
# rect1 = win32gui.GetWindowRect(foregroundwin)
# x1, y1, w1, h1 = rect1
# import time
# time.sleep(2)
# sd = win32gui.GetForegroundWindow()
# rect2 = win32gui.GetWindowRect(sd)
# x2, y2, w2, h2 = rect2

# win32gui.MoveWindow(sd, w1//4, y2, w2, h2, True)
import pyautogui, win32gui, win32con
from time import sleep
sleep(3)
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


foregroundwin =  win32gui.FindWindow(u'Shell_TrayWnd', None)
idsnames = get_child_ids(foregroundwin)

# id1 = get_child_ids(idsnames[8])
# print(id1)
# id2 = get_child_ids(id1[0])
# print(get_child_ids(id2[0]))

exit()
def ResizeCurrentWindow():
    desktop = pyautogui.size()
    height, width = desktop.height, desktop.width
    foregroundwin =  win32gui.FindWindow(u'Shell_TrayWnd', None)
    rect = win32gui.GetWindowRect(foregroundwin)
    x, y, w, h = rect
    print(x, foregroundwin)
    # win32gui.SetWindowPos(foregroundwin, 0, 0, 0, width-56, height-52, win32con.SWP_FRAMECHANGED)
    # win32gui.MoveWindow(foregroundwin, 76 , 87, w, h, True)
    # win32gui.ShowWindow(foregroundwin, 1)
    # win32gui.SetWindowPos(foregroundwin, None,12, 23, 122, 122, win32con.SWP_SHOWWINDOW )
    start = win32gui.FindWindowEx(foregroundwin, 1050592, None, None)
    print(start)
    # rect = win32gui.GetWindowRectEx(foregroundwin)
    win32gui.SetWindowPos(start, None, 122, 728, 123, 123, win32con.SWP_SHOWWINDOW)
    # win32gui.CreateRoundRectRgn(122, 122, 122, 122, 555, 666)
    # win32gui.rgn
    return foregroundwin
ResizeCurrentWindow()


exit()
import win32gui
NIIF_USER = 4
# ...
msg = "sorry"
hwnd = win32gui.GetForegroundWindow()
hinst = win32gui.GetModuleHandle(None)
hicon = win32gui.LoadImage(hinst, r"D:\Py code\Win12\closewindow.png", win32gui.IMAGE_BITMAP, 122, 122, win32gui.LR_LOADFROMFILE )
title = "Close Window"

win32gui.Shell_NotifyIcon(win32gui.NIM_MODIFY,
                                  (hwnd, 0, win32gui.NIF_INFO,
                                   win32con.WM_USER+20, hicon,
                                   "Notification", msg, 200, title, NIIF_USER))
                                   
# import win32gui

# # create a NOTIFYICONDATA object
# nid = (win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP)
# nid.hWnd = win32gui.GetForegroundWindow()
# nid.uID = 0
# nid.uFlags = win32gui.NIF_ICON | win32gui.NIF_MESSAGE | win32gui.NIF_TIP
# nid.hIcon = win32gui.LoadImage()
# nid.uCallbackMessage = win32con.WM_USER+20
# nid.szTip = "Tooltip"

# # add the icon to the taskbar
# win32gui.Shell_NotifyIcon(win32gui.NIM_ADD, nid)

# # remove the icon from the taskbar
# win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, nid)

# exit()
import win32gui, time, win32con

# Get the window handle of the taskbar
taskbar_handle = win32gui.FindWindow("Shell_TrayWnd", None)

# Get the window handle of the battery icon
battery_handle = win32gui.FindWindowEx(taskbar_handle, 0, "TrayNotifyWnd", None)
battery_handle = win32gui.FindWindowEx(battery_handle, 0, "SysPager", None)
battery_handle = win32gui.FindWindowEx(battery_handle, 0, "ToolbarWindow32", "User Promoted Notification Area")
win32gui.ShowWindow(battery_handle, 1)
time.sleep(2)
foregroundwin = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(foregroundwin, 0)
win32gui.SetWindowPos(foregroundwin, 0, 0, 120, 120, 0, win32con.SWP_SHOWWINDOW)
win32gui.Shell_NotifyIcon(win32gui.NIM_DELETE, win32gui.py)


print(f"The window handle of the battery icon is {battery_handle}. and {win32gui.GetForegroundWindow()}")
