# dock.py

import sys
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6.QtGui import *
from BlurWindow.blurWindow import GlobalBlur
import win32gui


class Dock(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedHeight(70)  # Height of the dock
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint
            | Qt.WindowType.WindowStaysOnTopHint
            | Qt.WindowType.Tool
        )
        self.setStyleSheet(
            "background-color: transparent;"
        )  # Semi-transparent background
        # Blur effect
        hWnd = self.winId()
        GlobalBlur(hWnd, Acrylic=True, Dark=True, QWidget=self)

        # Layout for dock items
        self.dock_layout = QHBoxLayout()
        self.buttons = []  # To keep track of buttons
        for i in range(50):
            button = QPushButton(
                QIcon("ico.svg"), "", self
            )  # Replace "ico.svg" with your icon path
            button.setFixedSize(50, 50)
            button.setStyleSheet(
                "border-radius: 25px; background-color: rgba(255, 255, 255, 0.5);"
            )
            button.setAttribute(Qt.WidgetAttribute.WA_Hover, True)  # Enable hover event
            button.setMouseTracking(True)
            button.enterEvent = lambda event, btn=button: self.hover_enter(btn)
            button.leaveEvent = lambda event, btn=button: self.hover_leave(btn)

            self.dock_layout.addWidget(button)
            self.buttons.append(button)  # Add button to the list

        # Create a central widget and set layout
        central_widget = QWidget(self)
        central_widget.setLayout(self.dock_layout)
        self.setCentralWidget(central_widget)

        # Position the dock at the bottom of the screen
        self.screen_geometry = self.screen().availableGeometry()
        self.dock_y_pos = (
            self.screen_geometry.height() - 70
        )  # Initial Y position of the dock
        self.setGeometry(0, self.dock_y_pos, self.screen_geometry.width(), 70)

        # Timer for auto-hiding the dock
        self.hide_timer = QTimer(self)
        self.hide_timer.setInterval(1000)  # Check every second
        self.hide_timer.timeout.connect(self.check_mouse_and_hide)

        # Start the timer
        self.hide_timer.start()

        # Connect mouse events
        self.setMouseTracking(True)

        # Animation for the dock
        self.animation = QPropertyAnimation(self, b"pos")
        self.animation.setDuration(100)  # Animation duration in milliseconds
        self.animation.setEasingCurve(
            QEasingCurve.Type.InOutCirc
        )  # Easing curve for smooth animation

    def check_mouse_and_hide(self):
        """Check the mouse position and hide/show the dock accordingly."""
        mouse_x, mouse_y = win32gui.GetCursorPos()
        self.screen_geometry = self.screen().availableGeometry()

        # Check if the dock is currently visible
        if mouse_y < self.screen_geometry.height() - 100:
            self.hide_dock()
        if mouse_y >= self.screen_geometry.height() - 100:
            self.show_dock()

    def hide_dock(self):
        """Hide the dock by changing its Y position with animation."""
        if (
            self.dock_y_pos < self.screen().availableGeometry().height()
        ):  # Ensure it's not already hidden
            self.animation.setStartValue(QPoint(0, self.dock_y_pos))
            self.dock_y_pos += 100  # Move down by 100 pixels
            self.animation.setEndValue(QPoint(0, self.dock_y_pos))
            self.animation.start()

    def show_dock(self):
        """Show the dock by resetting its Y position with animation."""
        if (
            self.dock_y_pos > self.screen().availableGeometry().height() - 70
        ):  # Ensure it's not already visible
            self.animation.setStartValue(QPoint(0, self.dock_y_pos))
            self.dock_y_pos -= 100  # Move up by 100 pixels
            self.animation.setEndValue(QPoint(0, self.dock_y_pos))
            self.animation.start()

    def create_animation_minimum_size(
        self, button, start_start, start_end, end_start, end_end
    ):
        """Create an animation to minimize the size of the dock."""
        animation = QPropertyAnimation(button, b"minimumSize")
        animation.setDuration(300)  # Animation duration in milliseconds
        animation.setEasingCurve(
            QEasingCurve.Type.InOutQuad
        )  # Easing curve for smooth animation
        animation.setStartValue(QSize(start_start, start_end))
        animation.setEndValue(QSize(end_start, end_end))  # Final size
        animation.start()

    def hover_enter(self, button: QPushButton):
        """Handle mouse enter event for button."""
        # Increase the size of the hovered button
        # button.setMinimumSize(65, 65)  # Increase size of hovered button
        self.create_animation_minimum_size(button, 50, 50, 65, 65)
        for btn in self.buttons:
            if btn != button:  # Only resize unhovered buttons
                btn.setMinimumSize(20, 20)  # Decrease size of unhovered buttons
                blur_effect = QGraphicsBlurEffect()
                blur_effect.setBlurRadius(5)  # Adjust the blur radius as needed
                btn.setGraphicsEffect(blur_effect)  # Apply blur effect

    def hover_leave(self, button: QPushButton):
        """Handle mouse leave event for button."""
        # Reset the size of the hovered button
        button.setMinimumSize(50, 50)  # Reset size of hovered button
        for btn in self.buttons:
            btn.setMinimumSize(50, 50)  # Reset size of all buttons
            btn.setGraphicsEffect(None)  # Remove blur effect


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dock = Dock()
    dock.show()
    sys.exit(app.exec())
