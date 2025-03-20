from PyQt6.QtWidgets import QApplication, QLabel, QWidget, QLineEdit, QVBoxLayout, QGridLayout, QComboBox
from PyQt6.QtCore import Qt
import sys
import requests
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")

app = QApplication([])
inputCurrency = 'AED'
outputCurrency = 'AED'

url = f"https://openexchangerates.org/api/latest.json?app_id={api_key}"
response = requests.get(url)

if response.status_code == 200:
    exchangeRate = response.json()
else:
    print("Fehler beim Abrufen der Daten:", response.status_code)

label = QLabel()

def convert(label: QLabel):
    def inner():
        try:
            number = float(input.text())
        except ValueError:
            number = -1
        print(number)
        print(exchangeRate['rates'][inputCurrency])
        print(exchangeRate['rates'][outputCurrency])
        print(inputCurrency)
        print(outputCurrency)
        number = number / exchangeRate['rates'][inputCurrency]
        print(number)
        number = number * exchangeRate["rates"][outputCurrency]
        print(number)
        # number = number/Wert von Input Currency inputCurrency
        # anschließend number+ Wert von output Currency, um das Endergebnis zu erhalten
        # Muss gemacht werden, da nur base USD möglich ist.
        #number = number*2
        result = str(number)
        if(number > 0):
            label.setText(result)  # Falls du den Text verwenden willst
        else:
            label.setText('')
    return inner

def inputCurrencyChanged(stringValue):
    global inputCurrency, label
    print(stringValue)
    inputCurrency = searchForCode(stringValue)
    convert(label)()

def outputCurrencyChanged(stringValue):
    global outputCurrency, label
    print(stringValue)
    outputCurrency = searchForCode(stringValue)
    convert(label)()

def searchForCode(currencyName:str) -> str:
    for code, name in currencies.items():
        if name == currencyName:
            return code
    return None


window = QWidget()
window.setWindowTitle("PyQt Currency Exchange")
window.setGeometry(700,300,500,300)

Header = QLabel("<h1> Currency Exchange </h1>", parent=window, alignment=Qt.AlignmentFlag.AlignHCenter)


input = QLineEdit()
input.textChanged.connect(convert(label))
input.setPlaceholderText("Enter the number to convert")

inputCurrencyChoices = QComboBox()
inputCurrencyChoices.currentTextChanged.connect(inputCurrencyChanged)

outputCurrencyChoices = QComboBox()
outputCurrencyChoices.currentTextChanged.connect(outputCurrencyChanged)

layout = QGridLayout()
layout.addWidget(Header, 0, 1, 0, 2)
layout.addWidget(input, 1, 1, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(label, 2, 1, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(inputCurrencyChoices, 1, 2, alignment=Qt.AlignmentFlag.AlignTop)
layout.addWidget(outputCurrencyChoices, 2, 2, alignment=Qt.AlignmentFlag.AlignTop)

URL ='https://openexchangerates.org/api/currencies.json'

responseAllCurrencies = requests.get(URL)

if responseAllCurrencies.status_code == 200:
    currencies = responseAllCurrencies.json()
else:
    print("Fehler beim Abrufen der Daten:", responseAllCurrencies.status_code)

for code, name in currencies.items():
    display_text = f"{name}"
    inputCurrencyChoices.addItem(display_text, code)
    outputCurrencyChoices.addItem(display_text, code)

window.setLayout(layout)
window.show()
sys.exit(app.exec())

