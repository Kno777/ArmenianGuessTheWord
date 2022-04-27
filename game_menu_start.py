from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenNewGame(object):
    def setupUi(self, OpenNewGame):
        OpenNewGame.setObjectName("ArmenianGuessTheWord")
        OpenNewGame.resize(490, 390)
        OpenNewGame.setStyleSheet("background-color: rgb(114, 159, 207);\n"
"background-color: rgb(238, 238, 236);")
        self.lable_logo_guess = QtWidgets.QLabel(OpenNewGame)
        self.lable_logo_guess.setGeometry(QtCore.QRect(40, 0, 561, 201))
        self.lable_logo_guess.setText("")
        self.lable_logo_guess.setPixmap(QtGui.QPixmap("/home/kno/Desktop/ProjecsPython/ArmenianGuessTheWord/img/guess.png"))
        self.lable_logo_guess.setObjectName("lable_logo_guess")
        
        self.push_NewGame = QtWidgets.QPushButton(OpenNewGame)
        self.push_NewGame.setGeometry(QtCore.QRect(45, 215, 400, 70))
        self.push_NewGame.setText("New Game")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.push_NewGame.setFont(font)
        self.push_NewGame.setStyleSheet("background-color: rgb(176,196,222);\ncolor: rgb(46, 52, 54);")
        self.push_NewGame.setObjectName("push_NewGame")

        self.push_Rules = QtWidgets.QPushButton(OpenNewGame)
        self.push_Rules.setGeometry(QtCore.QRect(45,300,400,70))
        self.push_Rules.setText("Rules")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.push_Rules.setFont(font)
        self.push_Rules.setStyleSheet("background-color: rgb(176,196,222);\ncolor: rgb(46, 52, 54);")
        self.push_Rules.setObjectName("push_Rules")

        self.retranslateUi(OpenNewGame)
        QtCore.QMetaObject.connectSlotsByName(OpenNewGame)

    def retranslateUi(self, OpenNewGame):
        _translate = QtCore.QCoreApplication.translate
        OpenNewGame.setWindowTitle(_translate("ArmenianGuessTheWord", "ArmenianGuessTheWord"))
        self.push_NewGame.setText(_translate("ArmenianGuessTheWord","New Game"))
        self.push_Rules.setText(_translate("ArmenianGuessTheWord","Rules"))

