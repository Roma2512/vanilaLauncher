from PyQt6.QtWidgets import QPushButton, QLabel, QVBoxLayout, QComboBox, QScrollArea, QWidget

widgets = []
scroll = []
layout = QVBoxLayout()

def init():
    global widgets, layout, scroll
    scroll.append(QScrollArea())
    scroll.append(QWidget())
    scroll.append(QVBoxLayout(scroll[1]))
    for i in range(100):
        widgets.append(QLabel(text=f"res ({i})"))
    for widget in widgets:
        scroll[2].addWidget(widget)
    scroll[0].setWidget(scroll[1])
    layout.addWidget(scroll[0])

    