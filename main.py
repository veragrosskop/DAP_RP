import sys

from PySide6 import QtWidgets

from dap_player.main_menu import DAPScreenUI, Theme

# ----------------------
# Run app
# ----------------------
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    # Load and apply QSS stylesheet
    try:
        app.setStyleSheet(Theme.setTheme("purple"))
        # with open("dap_player/style.qss", "r") as f:
        #     app.setStyleSheet(f.read())
    except Exception as e:
        print(f"Failed to load QSS: {e}")
    window = DAPScreenUI()
    window.show()
    sys.exit(app.exec())
