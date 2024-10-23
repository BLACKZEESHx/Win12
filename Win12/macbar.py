import sys
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from pyautogui import size
from BlurWindow.blurWindow import GlobalBlur
import time
import win32gui  # Importing win32gui for window manipulation
import win32con  # Importing win32con
from dock import Dock


# Creating Window Class
class MackBar(QMainWindow):
    def __init__(self):
        width, height = size()
        super().__init__(
            flags=Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.last_y_position = None
        self.setGeometry(0, 0, width, 25)
        self.setStyleSheet("background-color:transparent; margin:0px;")

        # Blur effect
        hWnd = self.winId()
        GlobalBlur(hWnd, Acrylic=True, Dark=True, QWidget=self)

        # Set up layout for top bar elements
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        layout = QHBoxLayout(self.central_widget)
        layout.setContentsMargins(30, 0, 30, 0)

        # Apple icon (menu button)
        self.app_icon = QIcon("ico.svg")
        self.menu_button = QPushButton(self)
        self.menu_button.setIcon(self.app_icon)
        self.menu_button.setIconSize(QSize(23, 23))
        self.menu_button.setFixedSize(25, 25)
        self.menu_button.setStyleSheet(
            """*:hover{border-radius:150px; background-color:rgba(55,55,55, 55);}"""
        )
        layout.addWidget(self.menu_button)

        # System Menus
        self.File = QPushButton("File", self)
        self.File.setStyleSheet(
            "*{color:white;}* :hover{border-radius:150px; background-color:rgba(55,55,55, 55);}"
        )
        self.Edit = QPushButton("Edit", self)
        self.Edit.setStyleSheet(
            "*{color:white;}* :hover{border-radius:150px; background-color:rgba(55,55,55, 55);}"
        )
        self.View = QPushButton("View", self)
        self.View.setStyleSheet(
            "*{color:white;}* :hover{border-radius:150px; background-color:rgba(55,55,55, 55);}"
        )
        self.Window = QPushButton("Window", self)
        self.Window.setStyleSheet(
            "*{color:white;}* :hover{border-radius:1250px; background-color:rgba(55,55,55, 55);}"
        )
        self.Help = QPushButton("Help", self)
        self.Help.setStyleSheet(
            "*{color:white;}* :hover{border-radius:150px; background-color:rgba(55,55,55, 55);}"
        )
        layout.addSpacing(10)
        layout.addWidget(self.File)
        layout.addSpacing(10)
        layout.addWidget(self.Edit)
        layout.addSpacing(10)
        layout.addWidget(self.View)
        layout.addSpacing(10)
        layout.addWidget(self.Window)
        layout.addSpacing(10)
        layout.addWidget(self.Help)
        layout.addStretch()  # Spacer

        # Time display
        self.time_label = QLabel(self)
        self.time_label.setStyleSheet("color: white; font-size: 14px;")
        layout.addWidget(self.time_label)
        self.update_time()  # Set initial time

        # Adding a calendar icon or other status icons (battery, wifi, etc.)
        self.status_icon = QLabel(self)
        self.status_icon.setPixmap(QIcon("status_icon.svg").pixmap(20, 20))
        layout.addWidget(self.status_icon)

        # Periodically update the time every second
        self.timer_of_timeLablel = QTimer(self)
        self.timer_of_timeLablel.timeout.connect(self.update_time)
        self.timer_of_timeLablel.start(1000)

        # Timer to check the active window and resize it
        self.resize_timer = QTimer(self)
        self.resize_timer.timeout.connect(self.check_and_resize)
        self.resize_timer.start(1000)  # Check every second

    # Function to update the time display
    def update_time(self):
        current_time = time.strftime("%H:%M:%S")
        self.time_label.setText(current_time)

    def check_and_resize(self):
        exclude_hwnd = self.winId()  # Handle of the current window (top bar)
        self.resize_foreground_maximized_window(exclude_hwnd)

    def resize_foreground_maximized_window(self, exclude_hwnd):
        # global last_y_position  # Declare it as global to modify the global variable
        hwnd = win32gui.GetForegroundWindow()
        if hwnd:
            # Check if the window is the same as `exclude_hwnd`
            if hwnd == exclude_hwnd:
                print("Foreground window is the top bar, skipping resize.")
                return

        rect = win32gui.GetWindowRect(hwnd)
        x_pos = rect[0]  # Current x position
        y_pos = rect[1]  # Current y position
        # last_y_position = None
        # Move the window down only if it hasn't been moved already
        if self.last_y_position is None or y_pos != self.last_y_position:
            if win32gui.GetWindowPlacement(hwnd)[1] == win32con.SW_SHOWMAXIMIZED:
                # Move the window down by 25 pixels
                win32gui.SetWindowPos(
                    hwnd,
                    win32con.HWND_TOP,
                    x_pos,
                    y_pos + 25,  # Move down by 25 pixels
                    0,  # Keep width unchanged
                    0,  # Keep height unchanged
                    win32con.SWP_NOZORDER
                    | win32con.SWP_NOSIZE,  # Don't change the size or z-order
                )
                self.last_y_position = y_pos + 25  # Update the last position
            else:
                # print("No foreground window found.")
                pass


class MackBarApp(QApplication):
    def eventFilter(self, obj, event):
        # Event filter to catch when new windows are shown
        if event.type() == QEvent.Type.Show and isinstance(obj, QMainWindow):
            desktop = QGuiApplication.primaryScreen().availableGeometry()
            obj.setGeometry(
                0, 25, desktop.width(), desktop.height() - 25
            )  # Move window down
        return super().eventFilter(obj, event)


if __name__ == "__main__":
    app = MackBarApp(sys.argv)

    # Create the top bar
    mackbar = MackBar()
    mackbar.show()

    # Create and show the dock
    dock = Dock()
    dock.show()

    # Install event filter to catch window creation events
    app.installEventFilter(app)

    sys.exit(app.exec())
