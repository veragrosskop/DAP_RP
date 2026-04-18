from typing import List

from PySide6 import QtWidgets, QtCore


class ListMenu(QtWidgets.QWidget):
    """
    A fixed menu that does not change dynamically at runtime. E.g. to be used for menus
    to select categories, settings etc.

    """

    def __init__(self, title: str, items: List[str]):
        super().__init__()
        layout = QtWidgets.QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(2)

        # Header
        self.header = QtWidgets.QLabel(title, alignment=QtCore.Qt.AlignCenter)
        self.header.setFixedHeight(30)
        layout.addWidget(self.header)

        # List of items
        self.list = QtWidgets.QListWidget()
        for text in items:
            self.list.addItem(QtWidgets.QListWidgetItem(text))
        self.list.setCurrentRow(0)
        layout.addWidget(self.list)

    def on_menu_item_selected(self) -> QtWidgets.QWidget:
        """
        Callback for when a menu item is selected. This function must handle the logic of selecting the next widget.
        """
        raise NotImplemented
