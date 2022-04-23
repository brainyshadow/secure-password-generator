import random
import string
from PySide6.QtWidgets import (
    QApplication, QMessageBox, QWidget, QLabel, QPushButton, QVBoxLayout
)

app = QApplication([])


window = QWidget()
v_layout = QVBoxLayout()

btn1 = QPushButton('button 1')
btn2 = QPushButton('button 2')

v_layout.addWidget(QLabel('hello world'))
v_layout.addWidget(btn1)
v_layout.addWidget(btn2)


def on_btn1_clicked():
    alert = QMessageBox()
    alert.setText('this is an alert msg')
    alert.exec()


btn1.clicked.connect(on_btn1_clicked)

window.setLayout(v_layout)
window.show()
app.exec()

length = int(input('\nEnter the length of password: '))
lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
symbols = string.punctuation
all = lower + upper + num + symbols
temp = random.sample(all, length)
password = "".join(temp)

print("Your password is: " + password)