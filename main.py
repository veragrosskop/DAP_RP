import sys

from PySide6 import QtWidgets

from dap_player.ui.main_menu import DAPScreenUI
from dap_player.ui.style.theme import Stylesheet, Theme

# ----------------------
# Run app
# ----------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = DAPScreenUI()
    window.setStyleSheet(Stylesheet.stylesheet(Theme.purple))
    window.show()
    sys.exit(app.exec())
