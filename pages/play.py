from threading import Thread

from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QComboBox, QTextEdit, QProgressBar, QMessageBox

from libs import *

widgets = []
layout = QVBoxLayout()
def setMaximum(value):
    widgets[3].setMaximum(value)
def setProgressBar(value):
    widgets[3].setValue(value)
def setTextStatus(text):
    print(text)
    if text == "Installation complete":
        widgets[0].setEnabled(True)
        widgets[0].setText("Играть")
callback = {
    "setStatus": lambda text: setTextStatus(text),
    "setProgress": lambda value: setProgressBar(value),
    "setMax": lambda value: setMaximum(value)
}
def _start_install():
    widgets[0].setEnabled(False)
    widgets[0].setText("Установка...")
    idname = widgets[1].currentText()
    versions = getVersions()
    for version in versions:
        if versions[version]["name"] == idname:
            id = version
            break
    try:
        Thread(target=lambda: install_ver(id, callback)).start()
    except Exception as e:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Критическая ошибка")
        msg.setText("Произошла критическая ошибка!")
        msg.setInformativeText("Дополнительная информация об ошибке")
        msg.setDetailedText(f"Трассировка стека:\n {e}")
        msg.exec()

def init():
    global widgets, layout
    logged = True
    if logged:
        widgets.append(QPushButton(text="Играть"))
        widgets.append(QComboBox())
        widgets.append(QTextEdit())
        widgets.append(QProgressBar())
        widgets[3].setValue(45)
        widgets[3].setTextVisible(False)
        widgets[2].setReadOnly(True)
        widgets[2].setPlainText("Все логи")
        widgets[2].setStyleSheet("background: #000;color: #0f0")
        widgets[0].clicked.connect(lambda: _start_install())
        for version in getVersionList():
            widgets[1].addItem(version["name"])
    else:
        widgets.append(QLabel(text="Вы не вошли в аккаунт!"))
        widgets.append(QPushButton(text="Войти"))
        widgets.append(QPushButton(text="Зарегестироваться"))
    for widget in widgets:
        layout.addWidget(widget)