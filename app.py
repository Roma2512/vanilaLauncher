import sys
from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout,
    QPushButton, QListWidget, QStackedWidget, QLabel, QFrame, QProgressBar, QSpacerItem, QSizePolicy
)
from pages import account, play, settings


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.page = 0
        self.setWindowTitle("vanilaLauncher")
        self.setFixedSize(800, 600)

        # Главный виджет и layout
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QHBoxLayout(self.central_widget)
        
        # Меню
        self.menu_frame = QFrame()
        self.menu_frame.setMaximumSize(50, 600)

        self.menu_bar = QVBoxLayout(self.menu_frame)
        self.menu_bar.setContentsMargins(3, 3, 3, 3)
        self.main_layout.addWidget(self.menu_frame)

        # Виджеты в меню
        self.menu_widgets = []
        self.menu_widgets.append(QPushButton(text="А"))
        self.menu_widgets[0].setToolTip("Аккаунт")
        self.menu_widgets.append(QPushButton())
        self.menu_widgets[1].setIcon(QIcon("icons/play.png"))
        self.menu_widgets[1].setToolTip("Играть")
        self.menu_widgets.append(QPushButton())
        self.menu_widgets[2].setIcon(QIcon("icons/settings.png"))
        self.menu_widgets[2].setToolTip("Настройки")
        self.menu_widgets.append(QPushButton())
        self.menu_widgets[3].setIcon(QIcon("icons/exit.png"))
        self.menu_widgets[3].setToolTip("Выйти")
        for i in range(3):
            self.menu_bar.addWidget(self.menu_widgets[i])
        self.menu_bar.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        self.menu_bar.addWidget(self.menu_widgets[3])

        self.menu_widgets[0].clicked.connect(lambda: self.setPage(1))
        self.menu_widgets[1].clicked.connect(lambda: self.setPage(2))
        self.menu_widgets[2].clicked.connect(lambda: self.setPage(3))
        self.menu_widgets[3].clicked.connect(lambda: QApplication.instance().quit())

        #Инициализация
        self.initPages()
        #self.setPage(1)
    def initPages(self):
        account.init()
        play.init()
        settings.init()
    def clearDisplay(self):
        account.close()
    def setPage(self, page: int):
        match self.page:
            case 1:
                self.main_layout.removeItem(account.layouts[0])
                for widget in account.widgets:
                    widget.hide()
            case 2:
                self.main_layout.removeItem(play.layout)
                for widget in play.widgets:
                    widget.hide()
            case 3:
                self.main_layout.removeItem(settings.layout)
                settings.scroll[0].hide()
                for widget in settings.widgets:
                    widget.hide()
        self.page = page
        match page:
            case 1:
                for layout in account.layouts: 
                    self.main_layout.addLayout(layout)
                for widget in account.widgets:
                    widget.show()
            case 2:
                self.main_layout.addLayout(play.layout)
                for widget in play.widgets:
                    widget.show()
            case 3:
                self.main_layout.addLayout(settings.layout)
                settings.scroll[0].show()
                for widget in settings.widgets:
                    widget.show()
if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Установка стиля (опционально)
    app.setStyle("Fusion")
    with open("themes/default/style.qss") as f:
        style = f.read()
    app.setStyleSheet(style)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())