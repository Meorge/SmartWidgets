from PyQt5 import QtWidgets, QtCore
import sys
from time import sleep
from os.path import getmtime
import importlib

class UpdateThread(QtCore.QThread):
    updated = QtCore.pyqtSignal()

    def __init__(self, filename, parent=None):
        super(UpdateThread, self).__init__(parent)
        self.filename = filename
        self.lastModified = 0

    def run(self):
        while True:
            timeLastModified = getmtime(self.filename + '.py')
            if timeLastModified > self.lastModified:
                self.updated.emit()
                self.lastModified = timeLastModified
            sleep(1)



class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setUpUI(None)

        self.filename = "test_widget"

        self.updateThread = UpdateThread(self.filename)
        self.updateThread.updated.connect(self.update)
        self.updateThread.start()
        

    def setUpUI(self, contentWidget):
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.contentWidget = QtWidgets.QWidget() if contentWidget is None else contentWidget
        self.updateButton = QtWidgets.QPushButton("Update")
        self.updateButton.clicked.connect(self.update)

        self.mainLayout.addWidget(self.contentWidget)
        self.mainLayout.addWidget(self.updateButton)

        self.centralWidget = QtWidgets.QWidget()
        self.centralWidget.setLayout(self.mainLayout)
        self.setCentralWidget(self.centralWidget)

    def update(self):
        # read text from file and update
        if self.filename not in sys.modules:
            print(f"Importing module {self.filename}")
            importlib.import_module(self.filename)
        else:
            importlib.reload(sys.modules[self.filename])

        self.setUpUI(sys.modules[self.filename].getWidget())
        
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())