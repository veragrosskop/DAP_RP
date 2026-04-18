from typing import List, Dict

from PySide6 import QtGui, QtCore, QtWidgets

from dap_player.ui.widgets.menu_list import ListMenu


# ----------------------
# Concrete menus
# ----------------------
class MainMenu(ListMenu):
    def __init__(self):
        super().__init__(
            "Music",
            ["Playlists", "Artists", "Albums", "Songs", "Settings"],
        )

        self._widgets: Dict[str, QtWidgets.QWidget] = {
            "Playlists": None,
            "Artists": None,
            "Albums": None,
            "Songs": None,
            "Settings": SettingsMenu(),
        }

    def on_menu_item_selected(self) -> QtWidgets.QWidget:
        selected = self.list.currentItem().text()


class SettingsMenu(ListMenu):
    def __init__(self):
        super().__init__(
            "Settings",
            ["Backlight", "Shuffle", "About"],
        )


# ----------------------
# Now Playing screen
# ----------------------
class NowPlayingScreen(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        self.song_title = QtWidgets.QLabel("Song Title", alignment=QtCore.Qt.AlignCenter)
        self.song_title.setFont(QtGui.QFont("Arial", 12, QtGui.QFont.Bold))

        self.song_artist = QtWidgets.QLabel("Artist Name", alignment=QtCore.Qt.AlignCenter)
        self.song_artist.setFont(QtGui.QFont("Arial", 10))

        self.progress = QtWidgets.QProgressBar()
        self.progress.setValue(40)
        self.progress.setTextVisible(False)
        self.progress.setStyleSheet("QProgressBar { height: 10px; }")

        self.status = QtWidgets.QLabel("▶ 0:42 / 3:25", alignment=QtCore.Qt.AlignCenter)
        self.status.setFont(QtGui.QFont("Arial", 9))

        layout.addWidget(self.song_title)
        layout.addWidget(self.song_artist)
        layout.addStretch()
        layout.addWidget(self.progress)
        layout.addWidget(self.status)


# ----------------------
# Main DAP screen logic
# ----------------------
class DAPScreenUI(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("DAP Player")
        # self.resize(480, 320)
        self.setFixedSize(480, 320)

        # Central container
        central = QtWidgets.QWidget()
        self.setCentralWidget(central)
        main_layout = QtWidgets.QVBoxLayout(central)
        main_layout.setContentsMargins(5, 5, 5, 5)

        # Stacked widget for screens
        self.stack = QtWidgets.QStackedWidget()
        main_layout.addWidget(self.stack)

        # Create menus/screens
        self.main_menu = MainMenu()
        self.settings_menu = SettingsMenu()
        self.now_playing = NowPlayingScreen()

        # Add them to stack
        self.stack.addWidget(self.main_menu)  # index 0
        self.stack.addWidget(self.settings_menu)  # index 1
        self.stack.addWidget(self.now_playing)  # index 2

        # Navigation history stack (like back button)
        self.history = []

        # Start at main menu
        self.stack.setCurrentWidget(self.main_menu)

    # ----------------------
    # Key handling
    # ----------------------
    def keyPressEvent(self, event):
        current_widget = self.stack.currentWidget()

        if isinstance(current_widget, ListMenu):

            # Scroll navigation
            if event.key() == QtCore.Qt.Key_Up:
                row = current_widget.list.currentRow()
                current_widget.list.setCurrentRow(min(row - 1, 0))
            elif event.key() == QtCore.Qt.Key_Down:
                row = current_widget.list.currentRow()
                current_widget.list.setCurrentRow(max(row + 1, current_widget.list.count() - 1))

            elif event.key() in (QtCore.Qt.Key_Right, QtCore.Qt.Key_Enter, QtCore.Qt.Key_Return):
                self.select_menu_item(current_widget)

        # Global toggle to go back
        if event.key() == QtCore.Qt.Key_Left:
            self.go_back()

        # Global toggle to Now Playing
        if event.key() == QtCore.Qt.Key_M:
            self.toggle_now_playing()

    # ----------------------
    # Menu actions
    # ----------------------
    def select_menu_item(self, menu: ListMenu):
        """Handle Enter/Select on a menu item."""
        text = menu.list.currentItem().text()

        if isinstance(menu, MainMenu):
            if text == "Settings":
                self.history.append(self.stack.currentWidget())
                self.stack.setCurrentWidget(self.settings_menu)
            else:
                # For demo: go to Now Playing when selecting non-Settings
                self.history.append(self.stack.currentWidget())
                self.stack.setCurrentWidget(self.now_playing)

        elif isinstance(menu, SettingsMenu):
            # Example: any item in settings just goes to Now Playing
            self.history.append(self.stack.currentWidget())
            self.stack.setCurrentWidget(self.now_playing)

    def go_back(self):
        """Go back to previous screen."""
        if self.history:
            last = self.history.pop()
            self.stack.setCurrentWidget(last)

    def toggle_now_playing(self):
        """Quick toggle to Now Playing (M key)."""
        if self.stack.currentWidget() == self.now_playing:
            # Return to previous
            self.go_back()
        else:
            self.history.append(self.stack.currentWidget())
            self.stack.setCurrentWidget(self.now_playing)
