import sys
import PyQt5.QtWidgets as wigs


class MainWindow(wigs.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # -- _Attributes_
        self.window_width = 640
        self.window_height = 320

        # -- _Setup_ methods
        self.housekeeping()

        self.move_window_to_center()

        self.show()

    def housekeeping(self):
        # -- Set width and height of the window
        self.setFixedWidth(self.window_width)
        self.setFixedHeight(self.window_height)

    def move_window_to_center(self):
        # -- This returns a point in the center of the current screen
        center_point = wigs.QDesktopWidget().availableGeometry().center()
        # -- Get the main rectangle of this window
        main_rectangle = self.frameGeometry()
        # -- Move the main rectangles center to the point you found as the center of the screen
        main_rectangle.moveCenter(center_point)