import win32gui, win32con

def get_child_ids(hwnd):
    child_ids = []
    child = win32gui.GetWindow(hwnd, win32con.GW_CHILD)
    child_name = win32gui.GetWindowText(child)
    v=0
    while child != 0:
        child_ids.append(f"{child_name}{0}")
        child_ids.append(child)
        child = win32gui.GetWindow(child, win32con.GW_HWNDNEXT)
        child_name = win32gui.GetWindowText(child)
        v+=1
    return child_ids

class Taskbar:
    def __init__(self):            
        # hWnd
        self.hTaskbar =  win32gui.FindWindow(u'Shell_TrayWnd', None)
        self.idsnames = get_child_ids(self.hTaskbar)
        print(self.idsnames)
        self.hTray = self.idsnames[-1]
        self.hStartbtn = self.idsnames[1]
        self.hStartMenu = win32gui.FindWindow("Windows.UI.Core.CoreWindow", "Start")
        # import time
        # time.sleep(2)
        # print(get_child_ids(win32gui.GetForegroundWindow()))
        # win32gui.ShowWindow(3278804, 5)

        # Rects
        self.tx, self.ty, self.twidth, self.theight = win32gui.GetWindowRect(self.hTaskbar)
        self.Trayrect = win32gui.GetWindowRect(self.hTray)
        self.hstartMrect = win32gui.GetWindowRect(self.hStartMenu)
        # Print

    # Tray
    def Tray(self):
        x, y, w, h = self.Trayrect
        # print(self.Trayrect)
        win32gui.MoveWindow(self.hTray, 22, 0, w-22, 0, True)
        rect = win32gui.GetWindowRect(self.hTray)
        x, y, w, h = rect
        print(rect)


    # Taskbar 
    def TaskbarIcon(self):
        rect = win32gui.GetWindowRect(self.idsnames[5])
        x, y, w, h = rect
        sx,sy,sw,sh = self.hstartMrect
        print(rect)
        print(f"Start {sx, sy, sw, sh}")
        win32gui.MoveWindow(self.idsnames[5], sx+160, 0, w, h, True)
        rect = win32gui.GetWindowRect(self.idsnames[5])
        x, y, w, h = rect
        print("Taskbar", rect)
        

    def Rounded_Taskbar(self):

        # Get the width and height of the window
        width = win32gui.GetWindowRect(self.hTaskbar)[2] - win32gui.GetWindowRect(self.hTaskbar)[0]
        height = win32gui.GetWindowRect(self.hTaskbar)[3] - win32gui.GetWindowRect(self.hTaskbar)[1]
        width = win32gui.GetWindowRect(self.hTaskbar)[2] - win32gui.GetWindowRect(self.hTaskbar)[0]
        height = win32gui.GetWindowRect(self.hTaskbar)[3] - win32gui.GetWindowRect(self.hTaskbar)[1]

        # Create a region object with rounded corners
        rect = win32gui.GetWindowRect(self.idsnames[5])
        sx,sy,sw,sh = self.hstartMrect
        x, y, w, h = rect
        win32gui.SetWindowRgn(self.hTaskbar, win32gui.CreateRoundRectRgn(0, 0, width, height, 0, 0), True)
        rgn = win32gui.CreateRoundRectRgn(width//2-sx+20, 1, width//2+sx, height, 15, 15)
        # Set the window region to the region object
        win32gui.SetWindowRgn(self.hTaskbar, rgn, True)

if __name__ == "__main__":
    taskbar = Taskbar()
    taskbar.TaskbarIcon()
    # taskbar.Rounded_Taskbar()