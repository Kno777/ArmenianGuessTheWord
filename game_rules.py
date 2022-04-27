from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OpenGameRules(object):
    def setupUi(self, OpenGameRules):
        OpenGameRules.setObjectName("OpenGameRules")
        OpenGameRules.resize(400, 300)
        OpenGameRules.setStyleSheet("background-color: rgb(176,196,222);\ncolor: rgb(46, 52, 54);")
        self.textEdit = QtWidgets.QTextBrowser(OpenGameRules)
        self.textEdit.setStyleSheet("background-color: rgb(230,230,250)")
        self.textEdit.setGeometry(QtCore.QRect(5, 11, 391, 221))
        self.textEdit.setPlainText("""Guess The Word {0} ​​սեղանի խաղի կանոնները
                        Խաղացողները բաժանվում են թիմերի (երկու հոգուց), որոշում են 
                        հերթականությունը, թիմում պայմանավորվում են, թե ով է 
                        բացատրելու և ով կընկալի, որոշում են քարտերի բառերի թիվը, 
                        դնում են ավազի ժամացույց և փորձում են մեկ րոպե հասկանալ միմյանց։""".format('🤭​'))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.textEdit.setFont(font)
        self.textEdit.setObjectName("MyTextRules")

        self.push_back = QtWidgets.QPushButton(OpenGameRules)
        self.push_back.setGeometry(QtCore.QRect(300, 240, 91, 41))
        self.push_back.setStyleSheet("background-color: rgb(176,196,222);\ncolor rgb(105,105,105)")
        self.push_back.setText("Back")
        self.push_back.setObjectName("push_back")
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        self.push_back.setFont(font)
        self.retranslateUi(OpenGameRules)
        QtCore.QMetaObject.connectSlotsByName(OpenGameRules)

    def retranslateUi(self, OpenGameRules):
        _translate = QtCore.QCoreApplication.translate
        OpenGameRules.setWindowTitle(_translate("OpenGameRules", "ArmenianGuessTheWord"))
        self.push_back.setText(_translate("OpenGameRules","Back"))
