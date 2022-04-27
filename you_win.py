from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenGameWinner(object):
    def setupUi(self, OpenGameWinner):
        OpenGameWinner.setObjectName("OpenGameWinner")
        OpenGameWinner.resize(625, 400)
        OpenGameWinner.setStyleSheet("background-color: rgb(114, 159, 207);")
        
        self.leble_photo_logo = QtWidgets.QLabel(OpenGameWinner)
        self.leble_photo_logo.setGeometry(QtCore.QRect(0,0,1000,300))
        self.leble_photo_logo.setText("")
        self.leble_photo_logo.setPixmap(QtGui.QPixmap("/home/kno/Desktop/ProjecsPython/ArmenianGuessTheWord/img/aaa.webp"))
        self.leble_photo_logo.setObjectName("leble_potho_winner")

        self.this_is_winner = QtWidgets.QLineEdit(OpenGameWinner)
        self.this_is_winner.setGeometry(QtCore.QRect(180,305,280,70))
        self.this_is_winner.setStyleSheet("background-color: rgb(240,248,255);\ncolor rgb(0,0,0)")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.this_is_winner.setFont(font)
        self.this_is_winner.setObjectName("This is Winner team")

        self.retranslateUi(OpenGameWinner)
        QtCore.QMetaObject.connectSlotsByName(OpenGameWinner)

    def retranslateUi(self, OpenGameWinner):
        _translate = QtCore.QCoreApplication.translate
        OpenGameWinner.setWindowTitle(_translate("ArmenianGuessTheWord", "ArmenianGuessTheWord"))
        self.this_is_winner.setText(_translate("ArmenianGuessTheWord","      Team1 "))
