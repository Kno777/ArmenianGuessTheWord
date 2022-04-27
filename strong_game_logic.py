#from pathlib import Path
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

from game_menu_start import Ui_OpenNewGame
from game_grupa_start import Ui_OpenGameGrupe
from game_text_start import Ui_OpenGameText
from game_rules import Ui_OpenGameRules
from you_win import Ui_OpenGameWinner


app = QtWidgets.QApplication(sys.argv)
OpenNewGame = QtWidgets.QWidget()
ui = Ui_OpenNewGame()
ui.setupUi(OpenNewGame)
OpenNewGame.show()


# team name string
team1 = ""
team2 = ""
start_team = ""
points_team1 = 0
points_team2 = 0
total_results = {}
res1 = 0
res2 = 0
stop_game = False
start_second = False
isStart = False
startTime = 0
second = 1000
words = ["մաչո","ակումուլյատոր","լեքսիկոն","պարոդիա","մկկալ","բլբլալ","բոռալ","կենդանի"
        ,"հով","շլոփա","մորուք","սկեսուր","թպրտալ","ոռնալ","որթ","վարսափաթթուկ","հանկարծաստեղծում"
        ,"պարոդիա","ինքնաբռթբռթիչ","հեռուստացանց","ջենտլմեն","պռառեխ","գոգաթիակ","պենոպլաստ"]

# .......................................

def OpenNewGameWindowe():
    global OpenGameGrupe
    OpenGameGrupe = QtWidgets.QWidget()
    ui = Ui_OpenGameGrupe()
    ui.setupUi(OpenGameGrupe)
    OpenNewGame.close()
    OpenGameGrupe.show()

    def returnToBack():
        OpenGameGrupe.close()
        OpenNewGame.show()

    ui.btn_back.clicked.connect(returnToBack)

    ui.runText1.setPlaceholderText("Enter your team!")
    ui.runText2.setPlaceholderText("Enter your team!")

    def get_text_one():
        global team1,team2
        team1 = ui.runText1.toPlainText()
        print("Team1 :",team1)
    
    def get_text_two():
        global team1,team2
        team2 = ui.runText2.toPlainText()
        print("Team2 :",team2)

    
    ui.push_team1.clicked.connect(get_text_one)
    ui.push_team2.clicked.connect(get_text_two)

    def name_conflict():
        global team1,team2
        
        if ui.push_team1.isChecked() == ui.push_team2.isChecked():
            print(team1,team2)
            if team1 == team2:
                openConflict = QMessageBox()
                openConflict.setWindowTitle("Name Error!")
                openConflict.setText("Name 'team1' and 'team2' equal: Please change names!")
                openConflict.setIcon(QMessageBox.Warning)
                openConflict.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)

                openConflict.setDefaultButton(QMessageBox.Ok)

                openConflict.buttonClicked.connect(error_box)
                openConflict.exec_()

    def error_box(btn):
            if btn.text() == "Ok":
                print("Ok")
            elif btn.text() == "Reset":
                OpenNewGameWindowe()
    

    def openStartGame():
        global team1,team2
        if team1 == team2:
            name_conflict()
            OpenGameGrupe.close()
            OpenNewGame.show()
        else:
            global OpenGameText
            OpenGameText = QtWidgets.QWidget()
            ui = Ui_OpenGameText()
            ui.setupUi(OpenGameText)
            
            OpenGameText.show()
            OpenGameGrupe.close()

        def exit_game():
            stop_game = True
            if stop_game:
                sys.exit(app.exec_())
        
        ui.push_exit.clicked.connect(exit_game)

        def time_start():
            global isStart,startTime
            isStart = True
            startTime = time.time()

        def reset_func():
            global isStart
            isStart = False
        
        ui.push_reset.clicked.connect(reset_func)
        ui.push_start_time.clicked.connect(time_start)

        def timerFunction():
            global isStart,startTime
            if isStart:
                timer_r = int(time.time() - startTime)

                hours = timer_r // 3600
                minuts = (timer_r % 3600) // 60
                second = timer_r % 60
                #print(second)

                if second > 60:
                    isStart = False
                else:
                    hours = str(hours);minuts = str(minuts); second = str(second)

                    time_str = '0'*(2-len(hours))+hours+':'+'0'*(2-len(minuts))+minuts+':'+'0'*(2-len(second))+second 
                    ui.push_second.setText(time_str)
        
        timer = QtCore.QTimer(OpenGameText)
        timer.timeout.connect(timerFunction)
        timer.start(1000)


        def returnRandomTextTeam1():
            global points_team1
            global total_results
            
            print("Started " + team1 + " good time!", " and your points: ",points_team1)
            
            points_team1 = 0
            ui.btn_text1.setCheckable(True)
            ui.btn_text2.setCheckable(True)
            ui.btn_text3.setCheckable(True)
            ui.btn_text4.setCheckable(True)
            ui.btn_text5.setCheckable(True)
            ui.btn_text6.setCheckable(True)
            ui.btn_text7.setCheckable(True)
            ui.btn_text8.setCheckable(True)
            ui.btn_text9.setCheckable(True)
            ui.btn_text10.setCheckable(True)
            ui.btn_text11.setCheckable(True)
            ui.btn_text12.setCheckable(True)

            ui.btn_text1.setText(words[0])
            if ui.btn_text1.isChecked():
                points_team1 += 7
            ui.btn_text2.setText(words[1])
            if ui.btn_text2.isChecked():
                points_team1 += 7
            ui.btn_text3.setText(words[2])
            if ui.btn_text3.isChecked():
                points_team1 += 7
            ui.btn_text4.setText(words[3])
            if ui.btn_text4.isChecked():
                points_team1 += 7
            ui.btn_text5.setText(words[4])
            if ui.btn_text5.isChecked():
                points_team1 += 7
            ui.btn_text6.setText(words[5])
            if ui.btn_text6.isChecked():
                points_team1 += 7
            ui.btn_text7.setText(words[6])
            if ui.btn_text7.isChecked():
                points_team1 += 7
            ui.btn_text8.setText(words[7])
            if ui.btn_text8.isChecked():
                points_team1 += 7
            ui.btn_text9.setText(words[8])
            if ui.btn_text9.isChecked():
                points_team1 += 7
            ui.btn_text10.setText(words[9])
            if ui.btn_text10.isChecked():
                points_team1 += 7
            ui.btn_text11.setText(words[10])
            if ui.btn_text11.isChecked():
                points_team1 += 7
            ui.btn_text12.setText(words[11])
            if ui.btn_text12.isChecked():
                points_team1 += 7
            
            res1 = points_team1
            total_results[team1] = res1
            print(total_results.items())

            ui.btn_text1.clicked.connect(returnRandomTextTeam1)
            ui.btn_text2.clicked.connect(returnRandomTextTeam1)
            ui.btn_text3.clicked.connect(returnRandomTextTeam1)
            ui.btn_text4.clicked.connect(returnRandomTextTeam1)
            ui.btn_text5.clicked.connect(returnRandomTextTeam1)
            ui.btn_text6.clicked.connect(returnRandomTextTeam1)
            ui.btn_text7.clicked.connect(returnRandomTextTeam1)
            ui.btn_text8.clicked.connect(returnRandomTextTeam1)
            ui.btn_text9.clicked.connect(returnRandomTextTeam1)
            ui.btn_text10.clicked.connect(returnRandomTextTeam1)
            ui.btn_text11.clicked.connect(returnRandomTextTeam1)
            ui.btn_text12.clicked.connect(returnRandomTextTeam1)

        
        def openStartTeam2():
            global OpenGameText
            OpenGameText = QtWidgets.QWidget()
            ui = Ui_OpenGameText()
            ui.setupUi(OpenGameText)
            OpenGameGrupe.close()
            OpenGameText.show()


            def exit_game():
                stop_game = True
                if stop_game:
                    sys.exit(app.exec_())
            
            ui.push_exit.clicked.connect(exit_game)

            def time_start():
                global isStart,startTime
                isStart = True
                startTime = time.time()

            def reset_func():
                global isStart
                isStart = False
            
            ui.push_reset.clicked.connect(reset_func)
            ui.push_start_time.clicked.connect(time_start)

            def timerFunction():
                global isStart,startTime
                if isStart:
                    timer_r = int(time.time() - startTime)

                    hours = timer_r // 3600
                    minuts = (timer_r % 3600) // 60
                    second = timer_r % 60
                    #print(second)

                    if second > 60:
                        isStart = False
                    else:
                        hours = str(hours);minuts = str(minuts); second = str(second)

                        time_str = '0'*(2-len(hours))+hours+':'+'0'*(2-len(minuts))+minuts+':'+'0'*(2-len(second))+second 
                        ui.push_second.setText(time_str)
            
            timer = QtCore.QTimer(OpenGameText)
            timer.timeout.connect(timerFunction)
            timer.start(1000)

            def goToWinnerTeam():
                global OpenGameWinner
                OpenGameWinner = QtWidgets.QWidget()
                ui = Ui_OpenGameWinner()
                ui.setupUi(OpenGameWinner)
                OpenGameGrupe.close()
                OpenGameText.close()
                OpenGameWinner.show()
                        
                print("Resulttt",total_results.items())

                def returnWinnerTeam():
                    global points_team1,points_team2
                    global res1,res2
                    print(res1,res2)
                    print(points_team1,points_team2)
                    if points_team1 > points_team2:
                        ui.this_is_winner.setText("You Win "+team1)
                    elif points_team1 < points_team2:
                        ui.this_is_winner.setText("You Win "+team2)
                    else:
                        ui.this_is_winner.setText("Equal")
                returnWinnerTeam()

            ui.push_next.clicked.connect(goToWinnerTeam)


            def teamtwologic():
                global points_team2
                global res1,res2
                global total_results
                print("Started " + team2 + " good time! ","and your points: ",points_team2)
                
                points_team2 = 0
                ui.btn_text1.setCheckable(True)
                ui.btn_text2.setCheckable(True)
                ui.btn_text3.setCheckable(True)
                ui.btn_text4.setCheckable(True)
                ui.btn_text5.setCheckable(True)
                ui.btn_text6.setCheckable(True)
                ui.btn_text7.setCheckable(True)
                ui.btn_text8.setCheckable(True)
                ui.btn_text9.setCheckable(True)
                ui.btn_text10.setCheckable(True)
                ui.btn_text11.setCheckable(True)
                ui.btn_text12.setCheckable(True)

                ui.btn_text1.setText(words[12])
                if ui.btn_text1.isChecked():
                    points_team2 += 7
                ui.btn_text2.setText(words[13])
                if ui.btn_text2.isChecked():
                    points_team2 += 7
                ui.btn_text3.setText(words[14])
                if ui.btn_text3.isChecked():
                    points_team2 += 7
                ui.btn_text4.setText(words[15])
                if ui.btn_text4.isChecked():
                    points_team2 += 7
                ui.btn_text5.setText(words[16])
                if ui.btn_text5.isChecked():
                    points_team2 += 7
                ui.btn_text6.setText(words[17])
                if ui.btn_text6.isChecked():
                    points_team2 += 7
                ui.btn_text7.setText(words[18])
                if ui.btn_text7.isChecked():
                    points_team2 += 7
                
                ui.btn_text8.setText(words[19])
                if ui.btn_text8.isChecked():
                    points_team2 += 7

                ui.btn_text9.setText(words[20])
                if ui.btn_text9.isChecked():
                    points_team2 += 7
                
                ui.btn_text10.setText(words[21])
                if ui.btn_text10.isChecked():
                    points_team2 += 7
                
                ui.btn_text11.setText(words[22])
                if ui.btn_text11.isChecked():
                    points_team2 += 7
                
                ui.btn_text12.setText(words[23])
                if ui.btn_text12.isChecked():
                    points_team2 += 7

                
                res2 = points_team2
                total_results[team2] = res2
                print(total_results.items())
                
                ui.btn_text1.clicked.connect(teamtwologic)
                ui.btn_text2.clicked.connect(teamtwologic)
                ui.btn_text3.clicked.connect(teamtwologic)
                ui.btn_text4.clicked.connect(teamtwologic)
                ui.btn_text5.clicked.connect(teamtwologic)
                ui.btn_text6.clicked.connect(teamtwologic)
                ui.btn_text7.clicked.connect(teamtwologic)
                ui.btn_text8.clicked.connect(teamtwologic)
                ui.btn_text9.clicked.connect(teamtwologic)
                ui.btn_text10.clicked.connect(teamtwologic)
                ui.btn_text11.clicked.connect(teamtwologic)
                ui.btn_text12.clicked.connect(teamtwologic)
            
            teamtwologic()

        ui.push_start_team_two.clicked.connect(openStartTeam2)

        returnRandomTextTeam1()


        def goToWinnerTeam():
                global OpenGameWinner
                OpenGameWinner = QtWidgets.QWidget()
                ui = Ui_OpenGameWinner()
                ui.setupUi(OpenGameWinner)
                OpenGameGrupe.close()
                OpenGameText.close()
                OpenGameWinner.show()
                        
                print("Resulttt",total_results.items())

                def returnWinnerTeam():
                    global points_team1,points_team2
                    global res1,res2
                    print(res1,res2)
                    print(points_team1,points_team2)
                    if points_team1 > points_team2:
                        ui.this_is_winner.setText("You Win "+team1)
                    elif points_team1 < points_team2:
                        ui.this_is_winner.setText("You Win "+team2)
                    else:
                        ui.this_is_winner.setText("Equal")
                returnWinnerTeam()

        ui.push_next.clicked.connect(goToWinnerTeam)




    ui.push_StartGame.clicked.connect(openStartGame)



ui.push_NewGame.clicked.connect(OpenNewGameWindowe)




def openRulesWindowe():
    global OpenGameRules
    OpenGameRules = QtWidgets.QWidget()
    ui = Ui_OpenGameRules()
    ui.setupUi(OpenGameRules)
    OpenGameRules.show()

    def returnToMenu():
        OpenGameRules.close()
        OpenNewGame.show()
    
    ui.push_back.clicked.connect(returnToMenu)

ui.push_Rules.clicked.connect(openRulesWindowe)


sys.exit(app.exec_())