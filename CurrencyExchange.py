from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QComboBox
from PyQt6.QtCore import Qt
import sys
app = QApplication([])

def textChanged(stringValue):
    print(stringValue)

def convert(label: QLabel):
    def inner():
        try:
            number = float(input.text())
        except ValueError:
            number = 0
        number = number*2
        result = str(number)
        if(number != 0):
            label.setText(result)  # Falls du den Text verwenden willst
        else:
            label.setText('')
    return inner




window = QWidget()
window.setWindowTitle("PyQt Currency Exchange")
window.setGeometry(700,300,500,300)

Header = QLabel("<h1> Currency Exchange </h1>", parent=window, alignment=Qt.AlignmentFlag.AlignHCenter)
label = QLabel()

input = QLineEdit()
input.textChanged.connect(convert(label))
input.setPlaceholderText("Enter the number to convert")

inputCurrencyChoices = QComboBox()
inputCurrencyChoices.addItems(["Euro", "US-Dollar", "Pound"])
inputCurrencyChoices.currentTextChanged.connect(textChanged)

outputCurrencyChoices = QComboBox()
outputCurrencyChoices.addItems(["Euro", "US-Dollar", "Pound"])
outputCurrencyChoices.currentTextChanged.connect(textChanged)

layout = QGridLayout()
layout.addWidget(Header, 0, 1, 0, 2)
layout.addWidget(input, 1, 1, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(label, 2, 1, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(inputCurrencyChoices, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(outputCurrencyChoices, 2, 2, alignment=Qt.AlignmentFlag.AlignTop)

window.setLayout(layout)
window.show()
sys.exit(app.exec())