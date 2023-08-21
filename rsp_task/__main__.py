import sys

from PySide6 import QtWidgets

from rsp_task.main_window import MainWindow


def main() -> None:
    """Entry point."""
    app = QtWidgets.QApplication([])
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
