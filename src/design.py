from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (QWidget, QPushButton, QVBoxLayout,
                             QHBoxLayout, QLabel, QListWidget,
                             QComboBox, QMainWindow, QInputDialog,
                             QLineEdit, QMessageBox, QFileDialog)
from PlayList import Composition, PlayList
from LinkedList import LinkedListItem, LinkedList


class UiMainWindow(object):
    def __init__(self):
        """
        Инициализация виджетов в основном окне
        
        label_2 - Текущий трек
        label_3 - Отсутствует
        label_4 - Выбрать плейлист
        pushButton_7 - Добавить трек
        pushButton_8 - Удалить трек
        pushButton_9 - Передвинуть вверх
        pushButton_10 - Передвинуть вниз
        pushButton - Добавить плейлист
        pushButton_2 - Удалить плейлист
        pushButton_6 - Предыдущий
        pushButton_5 - Следующий
        
        """
        self.main_window = QMainWindow()
        self.label_4 = QLabel(self.main_window)
        
        self.verticalLayoutWidget = QWidget(self.main_window)
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)

        self.verticalLayoutWidget_2 = QWidget(self.main_window)
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.comboBox = QComboBox(self.verticalLayoutWidget_2)
        self.listWidget = QListWidget(self.verticalLayoutWidget_2)

        self.verticalLayoutWidget_3 = QWidget(self.main_window)
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.pushButton = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_2 = QPushButton(self.verticalLayoutWidget_3)

        self.horizontalLayoutWidget = QWidget(self.main_window)
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.label_2 = QLabel(self.horizontalLayoutWidget)
        self.label_3 = QLabel(self.horizontalLayoutWidget)

        self.horizontalLayoutWidget_2 = QWidget(self.main_window)
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.pushButton_6 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_11 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_4 = QPushButton(self.horizontalLayoutWidget_2)
        self.pushButton_5 = QPushButton(self.horizontalLayoutWidget_2)
        
        self.playLists: list[PlayList] = []
        self.thisPlayList = None
        self.thisTrack: LinkedListItem = None
    
    def setupUi(self):
        """
        Функция устанавливающая расположение и размеры кнопок на основном окне
        """
        self.main_window.setObjectName("main_window")
        self.main_window.resize(724, 656)
        self.main_window.setMinimumSize(QtCore.QSize(724, 656))
        self.main_window.setMaximumSize(QtCore.QSize(724, 656))

        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.label_4.setObjectName("label_4")
        self.label_2.setObjectName("label_2")
        self.label_3.setObjectName("label_3")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11.setObjectName("pushButton_11")

        self.comboBox.setObjectName("comboBox")
        self.listWidget.setObjectName("listWidget")
        
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(20, 450, 241, 80))
        
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayoutWidget.setGeometry(QtCore.QRect(460, 480, 181, 151))

        self.verticalLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(300, 540, 151, 91))

        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(20, 540, 275, 101))

        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 661, 351))
        
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.label_4.setGeometry(QtCore.QRect(10, 20, 121, 31))
        
        self.horizontalLayout.addWidget(self.label_2)
        self.horizontalLayout.addWidget(self.label_3)
        
        self.verticalLayout.addWidget(self.pushButton_7)
        self.verticalLayout.addWidget(self.pushButton_8)
        self.verticalLayout.addWidget(self.pushButton_9)
        self.verticalLayout.addWidget(self.pushButton_10)

        self.verticalLayout_3.addWidget(self.pushButton)
        self.verticalLayout_3.addWidget(self.pushButton_2)
        
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        
        self.pushButton_11.setDefault(False)
        self.pushButton_11.setFlat(False)
        
        self.horizontalLayout_2.addWidget(self.pushButton_11)
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        
        self.comboBox.setCurrentText("")
        self.comboBox.setIconSize(QtCore.QSize(20, 20))
        
        self.verticalLayout_2.addWidget(self.comboBox)
        self.verticalLayout_2.addWidget(self.listWidget)
        
        self.addFuntions()
        
        self.retranslateUi(self.main_window)
        QtCore.QMetaObject.connectSlotsByName(self.main_window)
        self.main_window.show()

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "main_window"))
        self.label_2.setText(_translate("main_window", "Текущий трек:"))
        self.label_3.setText(_translate("main_window", "Отсутствует"))
        self.label_4.setText(_translate("main_window", "Выбрать плейлист"))
        self.pushButton_7.setText(_translate("main_window", "Добавить трек"))
        self.pushButton_8.setText(_translate("main_window", "Удалить трек"))
        self.pushButton_9.setText(_translate("main_window", "Передвинуть вверх"))
        self.pushButton_10.setText(_translate("main_window", "Передвинуть вниз"))
        self.pushButton.setText(_translate("main_window", "Добавить плейлист"))
        self.pushButton_2.setText(_translate("main_window", "Удалить плейлист"))
        self.pushButton_6.setText(_translate("main_window", "Предыдущий"))
        self.pushButton_5.setText(_translate("main_window", "Следующий"))
    
    def addFuntions(self):
        """
        Метод привязывающий функции к кнопкам
        """
        button_assignment: dict[QtWidgets.QPushButton, callable] = {
            self.pushButton: self.addPlayList
        }
        for btn in button_assignment:
            btn.clicked.connect(button_assignment[btn])
        return 0
    
    def addPlayList(self):
        """
        Добавляет плэйлист с выбором названия в список,
        """
        inpDialog = QInputDialog()
        string_name, ok = inpDialog.getText(None, "Название плейлиста", "Строка?", QLineEdit.Normal, "")
        if not ok:
            self.showInfo("Ошибка, не введено название", "Ошибка")
            return

        fileName: str = QFileDialog.getOpenFileName(
            None, "Выбрать файл", "../test_music", "mp3 (*.mp3)")[0]

        if not fileName:
            self.showInfo("Произошла ошибка при загрузке файла", "Ошибка")
            return
        
        comp = Composition(name=string_name, path=fileName)
        itm = LinkedListItem(comp)
        
        plLst = PlayList(itm)
        print(plLst)
        
        #plLst.append(itm)
        #self.playLists[0] = plLst
        
        self.comboBox.addItem(string_name)

    def addTrack(self):
        # выбрать путь к композиции
        self.thisPlayList.append()
        # по новой вывести список композиций
    
    def deletePlayList(self):
        """
        Удалить плэйлист из списка
        """
        self.playLists.remove(self.thisPlayList)
        # по новой вывести список плейлистов
    
    def deleteTrack(self):
        self.thisPlayList.remove(self.thisTrack)
        # по новой вывести список композиций
    
    def chooseNextTrack(self):
        self.thisPlayList.next_track()
        self.thisTrack = self.thisPlayList.current
        # изменить название текущего трэка
    
    def choosePreviousTrack(self):
        self.thisPlayList.previous_track()
        self.thisTrack = self.thisPlayList.current
        # изменить название текущего трэка
    
    def PlayThisTrack(self):
        self.thisPlayList.play_all(self.thisTrack)
    
    def PlayPreviousTrack(self):
        self.choosePreviousTrack()
        self.PlayThisTrack()

    def PlayNextTrack(self):
        self.chooseNextTrack()
        self.PlayThisTrack()
    
    def moveTrackUp(self):
        pass
    
    def moveTrackDown(self):
        pass
    
    def printPlayList(self):
        """Функция для вывода всех узлов связного списка и их данных"""
        if self.first_item is None:
            return "Список пуст"
        
        current_item = self.first_item
        string = ""
        cnt = 1
        while True:
            string += f"{cnt}. {current_item.data.name}\n"
            current_item = current_item.next
            cnt += 1
            if current_item == self.first_item:
                break
        return string

    @staticmethod
    def showInfo(text: str, title: str):
        """
        Метод выводящий сообщение на экран пользователям

        text:str - текст сообщения
        msg:QMessageBox - окно с информацией
        """
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.exec_()
        return 0
