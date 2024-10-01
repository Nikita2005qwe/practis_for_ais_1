import sys
from os import getcwd, chdir
from LinkedList import LinkedList
from design import UiMainWindow
from PyQt5.QtWidgets import QApplication

def main() -> None:
    app = QApplication(sys.argv)
    ui = UiMainWindow()
    ui.setupUi()
    sys.exit(app.exec_())


if __name__ == "__main__":
    if getcwd().split("\\")[-1] == "src":
        pass
    elif getcwd().split("\\")[-1] == "ProjectStatistics":
        chdir("src")
    else:
        print("Перейдите в папку с приложением")
        sys.exit()
    main()
    