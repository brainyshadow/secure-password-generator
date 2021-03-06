from email import charset
import sys
import string
import random
import math
import pyperclip
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QCheckBox,
    QApplication,
    QLabel,
    QLineEdit,
    QMainWindow,
    QVBoxLayout,
    QWidget,
)


def generatePassword(length):
    replacements = [["bang", "!"], ["star", "*"], ["pound", "#"],
                    ["at", "@"], ["dot", "."], ["dash", "-"], ["comma", ","], ["dollar", "$"]]
    averageEnglishWordLength = 4
    numWords = math.floor(length/averageEnglishWordLength)
    if(numWords > 1):
        numWords = numWords-1
    else:
        numWords = 1
    password = ""
    reminder = ""
    with open("dict.txt", "r") as file:
        data = file.read()
        words = data.split()

    passwordNotFound = True
    wordsFound = 0
    while passwordNotFound:
        index = random.randint(0, len(words))
        temp = words[index]
        if((len(password) + len(temp)) < length):
            password = password+temp
            reminder = reminder+" "+temp
            wordsFound += 1
        elif wordsFound == numWords:
            passwordNotFound = False
    charLeft = length-len(password)
    password = password
    for i in range(charLeft):
        index = random.randint(0, len(replacements))
        password = password+replacements[index][1]
        reminder = reminder + " " + replacements[index][0]
    return [password, reminder]

# Subclass QMainWindow to customize your application's main window


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Secure Password")

        layout = QVBoxLayout()

        self.passwordInput = QLineEdit("3")
        self.passwordInput.textChanged.connect(self.passwordLengthChange)
        image = QPixmap("./images/lock.png")

        img = QLabel(self)
        img.setPixmap(image)
        img.setStyle
        layout.addWidget(img)

        layout.addWidget(self.passwordInput)

        self.shouldCopy = QCheckBox("Copy to Clipboard", self)
        layout.addWidget(self.shouldCopy)

        [password, reminder] = generatePassword(3)

        self.passwordDisplay = QLabel("Password: "+password)
        self.passwordDisplay.setWordWrap(True)
        layout.addWidget(self.passwordDisplay)

        self.reminderDisplay = QLabel("Reminder: "+reminder)
        self.reminderDisplay.setWordWrap(True)
        layout.addWidget(self.reminderDisplay)

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
                [password, reminder] = generatePassword(int(text))
                shouldCopy = self.shouldCopy.checkState()
                if(shouldCopy):
                    pyperclip.copy(password)
                self.passwordDisplay.setText("Password: " + password)
                self.reminderDisplay.setText("Reminder: " + reminder)

        except:
            self.passwordDisplay.setText("Invalid input length")
            self.reminderDisplay.setText("Invalid input length")



app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
