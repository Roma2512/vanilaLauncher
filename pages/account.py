from PyQt6.QtWidgets import QPushButton, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout

widgets = []
layouts = [QVBoxLayout()]

def init():
    global widgets, layouts
    logged = True
    if logged:
        layouts.append(QHBoxLayout())
        widgets.append(QLabel(text="Волосатый глист"))
        widgets.append(QPushButton(text="Редактировать"))
        widgets.append(QPushButton(text="Выйти"))
        layouts[1].addWidget(widgets[0])
        layouts[1].addWidget(widgets[1])
        layouts[1].addWidget(widgets[2])
        layouts[0].addLayout(layouts[1])
    else:
        widgets.append(QLineEdit())
        widgets[0].setPlaceholderText("Логин")
        widgets.append(QLineEdit())
        widgets[1].setPlaceholderText("Пароль")
        widgets.append(QPushButton(text="Войти"))
        widgets.append(QLabel(text="Неверный пользователь"))
        widgets[3].setStyleSheet("background: rgba(255, 0, 0, 0.3); border: 1px solid red; color: red;")
        widgets[3].setMaximumSize(800, 50)
        for widget in widgets:
            layouts[0].addWidget(widget)