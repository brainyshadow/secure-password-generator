import sys
import string
import random

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
)


def generatePassword(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    num = string.digits
    symbols = string.punctuation
    all = lower + upper + num + symbols
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
        layout.addWidget(self.passwordDisplay)

        widget = QWidget()
        widget.setLayout(layout)

        # Set the central widget of the Window. Widget will expand
        # to take up all the space in the window by default.
        self.setCentralWidget(widget)

    def passwordLengthChange(self, text):
        try:
            password = generatePassword(int(text))
            self.passwordDisplay.setText("Password: " + password)
        except:
            print("Invalid length input")


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec_()
