#!/usr/bin/python3

import sys
from PyQt4 import QtGui, QtCore


class Window(QtGui.QWidget):
    """Window Class conatining all gui elements"""

    class TextEditor(QtGui.QTextEdit):

        def keyPressEvent(self, e):
            """Overrides default event handler to handle "Return" key press"""
            if e.key() == QtCore.Qt.Key_Return:
                Window.SendButtonClick(self.parent())
            else:
                super(Window.TextEditor, self).keyPressEvent(e)

    def __init__(self):
        super(Window, self).__init__()
        self.lastmsg = ''
        self.userturn = True
        self.initUI()

    def initUI(self):
        """Initializes window with all gui elements"""
        self.chat = QtGui.QTextEdit(self)
        self.chat.setReadOnly(True)
        self.InsertText("WelcomeEverybody")
        self.text = self.TextEditor(self)
        self.btn = QtGui.QPushButton('Send', self)

        self.btn.clicked.connect(self.SendButtonClick)

        self.grid = QtGui.QGridLayout()
        self.grid.setSpacing(10)

        self.grid.addWidget(self.chat, 1, 0, 9, 1)
        self.grid.addWidget(self.text, 10, 0, 2, 1)
        self.grid.addWidget(self.btn, 10, 1)

        self.setLayout(self.grid)

        self.setGeometry(100, 100, 1000, 500)
        self.setWindowTitle('yolo')

        self.show()

    def SendButtonClick(self):
        """When it's user turn it send text from texteditor to chat window"""
        if self.userturn:
            self.chat.append("")
            self.lastmsg = self.text.toPlainText()
            self.chat.append("User: "+self.text.toPlainText())
            self.text.clear()
            self.userturn = False

    def InsertText(self, n):
        """Inserts text to chat window"""
        self.chat.insertPlainText(n)

    def SetUserTurn(self):
        """Allows user to send message"""
        self.userturn = True

    def GetLastUserMessage(self):
        """Returns string containing last message sent by user"""
        return self.lastmsg


def main():
    app = QtGui.QApplication(sys.argv)
    win = Window()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
