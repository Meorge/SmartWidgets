from PyQt5 import QtWidgets, QtGui, QtCore
import sys

class MyWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)

        self.rootWidget = QtWidgets.QWidget()

        self.rootLayout = QtWidgets.QVBoxLayout()
        self.rootLayout.addWidget(QtWidgets.QLabel("Title"))
        self.rootLayout.addWidget(QtWidgets.QLabel("Subtitle"))
        self.rootLayout.addWidget(QtWidgets.QWidget())
        self.rootLayout.addWidget(QtWidgets.QLabel("Some body text goes here"))
        self.rootLayout.addWidget(QtWidgets.QWidget())
        self.rootLayout.addWidget(QtWidgets.QLabel("Choose a button!"))

        self.buttonLayout_leftButton = QtWidgets.QPushButton("Left button")
        self.buttonLayout_leftButton.clicked.connect(self.printLeft)
        self.buttonLayout_middleButton = QtWidgets.QPushButton("Middle button")
        self.buttonLayout_middleButton.clicked.connect(self.printMiddle)
        self.buttonLayout_rightButton = QtWidgets.QPushButton("Right button")
        self.buttonLayout_rightButton.clicked.connect(self.printRight)

        self.buttonLayout = QtWidgets.QHBoxLayout()
        self.buttonLayout.addWidget(self.buttonLayout_leftButton)
        self.buttonLayout.addWidget(self.buttonLayout_middleButton)
        self.buttonLayout.addWidget(self.buttonLayout_rightButton)
        self.buttonWidget = QtWidgets.QWidget()
        self.buttonWidget.setLayout(self.buttonLayout)

        self.rootLayout.addWidget(self.buttonWidget)

        self.labl = QtWidgets.QLabel("I'll tell you which button you clicked!")

        self.rootLayout.addWidget(self.labl)

        self.rootWidget.setLayout(self.rootLayout)
        self.setCentralWidget(self.rootWidget)

    def printLeft(self):
        self.labl.setText("Left button pressed")

    def printMiddle(self):
        self.labl.setText("Middle button pressed")

    def printRight(self):
        self.labl.setText("Right button pressed")


app = QtWidgets.QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec_())