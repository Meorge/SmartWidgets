from PyQt5 import QtWidgets

def getWidget():
    layout = QtWidgets.QVBoxLayout()
    layout.addWidget(QtWidgets.QLabel("label 1"))
    layout.addWidget(QtWidgets.QLabel("label 2"))
    layout.addWidget(QtWidgets.QLineEdit("line edit"))
    widget = QtWidgets.QWidget()
    widget.setLayout(layout)
    return QtWidgets.QLabel("Pretty cool, huh?")