from SmartWidgets import Window, Label, Spacer, VStack, HStack

class MyWindow(Window):
    def __init__(self):
        self.setRootElement(VStack([
            Label("Title"),
            Label("Subtitle"),
            Spacer(),
            Label("Some body text goes here"),
            Spacer(),
            Label("Choose a button!"),
            HStack([
                Button("Left button", onClick=self.printLeft),
                Button("Middle button", onClick=self.printMiddle),
                Button("Right button", onClick=self.printRight)
            ]),
            Label("I'll tell you what button you clicked!", identifier="whichButtonLabel")
        ]))
        self.labl = self.getElement("whichButtonLabel")

    def printLeft(self):
        self.labl.setText("Left button pressed")

    def printMiddle(self):
        self.labl.setText("Middle button pressed")

    def printRight(self):
        self.labl.setText("Right button pressed")

window = MyWindow()
window.show()