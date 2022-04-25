import sys
import string
import random
import pyperclip

from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


def generatePassword(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
    while(len(all) < length):
        all = all+all
    temp = random.sample(all, length)
    password = "".join(temp)
    return password

# Subclass QMainWindow to customize your application's main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Secure Password")

        layout = QVBoxLayout()

        self.passwordInput = QLineEdit("3")
        self.passwordInput.textChanged.connect(self.passwordLengthChange)
        layout.addWidget(self.passwordInput)
        randomPassword = generatePassword(3)
        self.passwordDisplay = QLabel("Password: "+randomPassword)
        self.passwordDisplay.setWordWrap(True)
        layout.addWidget(self.passwordDisplay)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def passwordLengthChange(self, text):
        try:
            if(int(text) > 10000):
                self.passwordDisplay.setText("Password length too long")
            else:
                password = generatePassword(int(text))
                pyperclip.copy(password)
                self.passwordDisplay.setText("Password: " + password)

        except:
            print("Invalid length input")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
