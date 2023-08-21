from PySide6 import QtWidgets


class MainWindow(QtWidgets.QMainWindow):
    """Main window of program."""

    def __init__(self) -> None:
        super().__init__()
        self.central_widget = QtWidgets.QWidget(self)
        self.vertical_layout = QtWidgets.QVBoxLayout(self.central_widget)
        self.tab_widget = QtWidgets.QTabWidget()
        self.main_tab = QtWidgets.QWidget()

        self.tab_widget.addTab(self.main_tab, "Main")

        self.vertical_layout.addWidget(self.tab_widget)

        self.setCentralWidget(self.central_widget)
