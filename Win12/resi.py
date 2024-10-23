import win32gui
import win32con


def remove_title_bar(hwnd):
    # Get the current window style
    style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
    # Remove the title bar and border styles
    style &= ~(win32con.WS_CAPTION | win32con.WS_THICKFRAME)
    # Apply the new style
    win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style)
    # Update the window with the new style
    win32gui.SetWindowPos(
        hwnd, None, 0, 0, 12, 0, win32con.SWP_NOZORDER | win32con.SWP_FRAMECHANGED
    )


# Example usage
hwnd = win32gui.GetForegroundWindow()  # Replace with your window title
remove_title_bar(hwnd)
