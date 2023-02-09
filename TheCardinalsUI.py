from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QVBoxLayout,
    QFontDialog,
    QLabel,
    QLineEdit,
    QGridLayout,
    QComboBox,
    QWidget,
    QCheckBox,
    QSystemTrayIcon,
    QInputDialog,
    QSpacerItem,
    QSizePolicy,
    QPushButton,
    QMenu,
    QAction,
    QStyle,
    qApp,
)

class SecondWindow(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        vbox = QVBoxLayout()

        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed,
            QSizePolicy.Fixed)

        btn.move(20, 20)

        vbox.addWidget(btn)

        btn.clicked.connect(self.showDialog)

        self.lbl = QLabel('Knowledge only matters', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setGeometry(300, 300, 250, 180)
        self.setWindowTitle('Font dialog')


    def showDialog(self):

        font, ok = QFontDialog.getFont()
        if ok:
            self.lbl.setFont(font)


class TheCardinalMainWindow(QMainWindow):

    check_box = None
    tray_icon = None

    # Переопределяем конструктор класса
    def __init__(self): #, _TheWatcher
        # self._TheWatcher = _TheWatcher
        # Обязательно нужно вызвать метод супер класса
        QMainWindow.__init__(self)

        self.setWindowFlags( Qt.CustomizeWindowHint | Qt.WindowCloseButtonHint )

        self.setMinimumSize(QSize(480, 180))  # Устанавливаем размеры
        self.setWindowTitle(
            "System Tray Application")  # Устанавливаем заголовок окна
            
        central_widget = QWidget(self)  # Создаём центральный виджет
        self.setCentralWidget(
            central_widget)  # Устанавливаем центральный виджет
        
        
        grid_layout = QGridLayout(self)  # Создаём QGridLayout
        central_widget.setLayout(
            grid_layout
        )  # Устанавливаем данное размещение в центральный виджет
        grid_layout.addWidget(
            QLabel("Может ли приложение быть спрятано?", self), 0, 0
            )

        # Добавляем чекбокс, от которого будет зависеть поведение программы при закрытии окна
        self.check_box = QCheckBox("Сворачивать")
        grid_layout.addWidget(self.check_box, 1, 0)
        # grid_layout.addItem(
        #     QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Expanding), 2,
        #     0)
        self.check_box.setChecked(True) #Начальное значение

        self.TWStatus = QLabel("The Wathcer status: ", self)
        grid_layout.addWidget(
            self.TWStatus, 2, 0)

        grid_layout.addWidget(
            QLabel("Хоткеи", self), 3, 0)

        txt = QLineEdit(self)
        txt.resize(200, 10)
        grid_layout.addWidget(
            txt, 4, 0)

        btn_settings = QPushButton("settings")
        btn_settings.clicked.connect(self.showSecond)
        grid_layout.addWidget(
            btn_settings, 5, 0
        )
        
        btn_save = QPushButton("Save")
        grid_layout.addWidget(
            btn_save, 6, 0
        )

        # Инициализируем QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(self)
        # self.tray_icon.setIcon(self.style().standardIcon(QStyle.SP_ComputerIcon))
        self.tray_icon.setIcon(QIcon('./qwer.ico'))
        """
            Объявим и добавим действия для работы с иконкой системного трея
            show - показать окно
            hide - скрыть окно
            exit - выход из программы
        """
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        # self.window2 = SecondWindow()

    # Переопределение метода closeEvent, для перехвата события закрытия окна
    # Окно будет закрываться только в том случае, если нет галочки в чекбоксе
    def closeEvent(self, event):
        if self.check_box.isChecked():
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000,
            )

    def minimizedEvent(self, event):
        if self.check_box.isChecked():
            event.ignore()
            self.hide()
            self.tray_icon.showMessage(
                "Tray Program",
                "Application was minimized to Tray",
                QSystemTrayIcon.Information,
                2000,
            )
            
    def showSecond(self):
        pass
        # self.window2.show()

    def TWStatusChanged(self):
        self.TWStatus.text = ""