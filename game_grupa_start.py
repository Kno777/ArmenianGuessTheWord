from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_OpenGameGrupe(object):
    def setupUi(self, OpenGameGrupe):
        OpenGameGrupe.setObjectName("Ui_OpenGameGrupe")
        OpenGameGrupe.resize(500, 400)
        OpenGameGrupe.setStyleSheet("background-color: rgb(135,206,250);")
        self.push_team1 = QtWidgets.QPushButton(OpenGameGrupe)
        self.push_team1.setGeometry(QtCore.QRect(20,48,190,76))
        self.push_team1.setText("Team 1")
        self.push_team1.setStyleSheet("background-color: rgb(176,196,222)")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.push_team1.setFont(font)
        self.push_team1.setObjectName("push_team1")

        self.push_team2 = QtWidgets.QPushButton(OpenGameGrupe)
        self.push_team2.setGeometry(QtCore.QRect(20,156,190,76))
        self.push_team2.setText("Team 2")
        self.push_team2.setStyleSheet("background-color: rgb(176,196,222)")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.push_team2.setFont(font)
        self.push_team1.setObjectName("push_team2")

        self.btn_back = QtWidgets.QPushButton(OpenGameGrupe)
        self.btn_back.setText("Back")
        self.btn_back.setGeometry(QtCore.QRect(365,350,120,40))
        self.btn_back.setStyleSheet("background-color: rgb(176,196,222)")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.btn_back.setFont(font)

        self.runText1 = QtWidgets.QTextEdit(OpenGameGrupe)
        self.runText1.setGeometry(QtCore.QRect(235,50,250,68))
        self.runText1.setStyleSheet("background-color: rgb(176,196,222)")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.runText1.setFont(font)


        self.runText2 = QtWidgets.QTextEdit(OpenGameGrupe)
        self.runText2.setGeometry(QtCore.QRect(235,160,250,68))
        self.runText2.setStyleSheet("background-color: rgb(176,196,222)")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.runText2.setFont(font)

        self.push_StartGame = QtWidgets.QPushButton(OpenGameGrupe)
        self.push_StartGame.setGeometry(QtCore.QRect(60,260,400,70))
        self.push_StartGame.setStyleSheet("background-color: rgb(176,196,222)")
        self.push_StartGame.setText("Start Game")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.push_StartGame.setFont(font)



        self.retranslateUi(OpenGameGrupe)
        QtCore.QMetaObject.connectSlotsByName(OpenGameGrupe)

    def retranslateUi(self, OpenGameGrupe):
        _translate = QtCore.QCoreApplication.translate
        OpenGameGrupe.setWindowTitle(_translate("ArmenianGuessTheWord", "ArmenianGuessTheWord"))
        
