#IMPORTS
from PyQt5 import QtCore, QtGui, QtWidgets
import img_rc
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5 import QtCore, QtGui, QtWidgets
import json
import GPT_func
import text_sumzer
import pyvis_KG
import text_to_speech
import threading
import pygame
import time
import RadarPlot as Rplot
import relevance_scores as rs
import sentiment_scores as ss

#GUI MAIN CLASS
class Ui_MainWindow(object):                   
        def setupUi(self, MainWindow):

#MAINWINDOW
                MainWindow.setObjectName("MainWindow")
                MainWindow.resize(1073, 660)
                MainWindow.setStyleSheet("background-color:rgb(51,51,51)")

                self.centralwidget = QtWidgets.QWidget(MainWindow)
                self.centralwidget.setObjectName("centralwidget")

#FONT STYLE

        #TITLE FONT
                Tfont = QtGui.QFont()
                Tfont.setFamily("Dubai")
                Tfont.setPointSize(14)
                Tfont.setBold(True)
                Tfont.setWeight(75)
        #BODY FONT
                Bfont = QtGui.QFont()
                Bfont.setFamily("Dubai")
                Bfont.setPointSize(10)
                Bfont.setBold(True)
                Bfont.setWeight(75)
        #TAB WIDGET
                sfont = QtGui.QFont()
                sfont.setFamily("Dubai")
                sfont.setPointSize(8)
                sfont.setBold(True)
                sfont.setWeight(75)


#KNOWLEDGE GRAPH

        #KG CONTAINER parent frame 
                self.kg_container = QtWidgets.QFrame(self.centralwidget)
                self.kg_container.setGeometry(QtCore.QRect(10, 10, 671, 621))
                self.kg_container.setStyleSheet("background-color:rgb(39,39,39);\n"
                                                "border-radius:25px;")
                self.kg_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.kg_container.setFrameShadow(QtWidgets.QFrame.Raised)
                self.kg_container.setObjectName("kg_container")

        #KG LABEL displays title 
                self.kg_label = QtWidgets.QLabel(self.kg_container)
                self.kg_label.setGeometry(QtCore.QRect(10, 10, 181, 21))
                self.kg_label.setFont(Tfont)
                self.kg_label.setStyleSheet("color:#dce4ee")
                self.kg_label.setObjectName("kg_label")
        
        #KG FRAME frame that contains the kgwrap
                self.kg_frame = QtWidgets.QFrame(self.kg_container)
                self.kg_frame.setGeometry(QtCore.QRect(10, 40, 651, 531))
                self.kg_frame.setStyleSheet("background-color:rgb(255,255,255);\n"
                                            "border-radius:20px;")
                self.kg_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.kg_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.kg_frame.setObjectName("kg_frame")

        #KG WRAP wraps around webview kg
                self.kg_wrap = QtWidgets.QFrame(self.kg_frame)
                self.kg_wrap.setGeometry(QtCore.QRect(9, 9, 631, 511))
                self.kg_wrap.setStyleSheet("background-color:white")
                self.kg_wrap.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.kg_wrap.setFrameShadow(QtWidgets.QFrame.Raised)
                self.kg_wrap.setObjectName("kg_wrap")

#ENTRY
                self.entry = QtWidgets.QTextEdit(self.kg_container)
                self.entry.setGeometry(QtCore.QRect(10, 580, 531, 31))
                self.entry.setStyleSheet("background-color:rgb(51,51,51);\n"
                                        "border-radius:13px;\n"
                                        "border:None;\n"
                                        "color:#dce4ee")
                self.entry.setObjectName("entry")

#SEARCH BUTTON

                self.search_button = QtWidgets.QPushButton(self.kg_container)
                self.search_button.setGeometry(QtCore.QRect(550, 580, 111, 31))
                self.search_button.setFont(Bfont)
                self.search_button.setStyleSheet("color:#dce4ee;\n"
                                                "border-radius:13px;\n"
                                                 "background-color:rgb(59,142,208);\n")
                self.search_button.clicked.connect(self.Search)
                self.search_button.setObjectName("search_button")

#DESCRIPTON 

        #DESCRIPTION CONTAINER parent frame
                self.description_containter = QtWidgets.QFrame(self.centralwidget)
                self.description_containter.setGeometry(QtCore.QRect(690, 10, 371, 311))
                self.description_containter.setStyleSheet("background-color:rgb(39,39,39);\n"
                                                        "border-radius:25px;")
                self.description_containter.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.description_containter.setFrameShadow(QtWidgets.QFrame.Raised)
                self.description_containter.setObjectName("description_containter")

        #DESCRIPTION LABEL displays title
                self.description_label = QtWidgets.QLabel(self.description_containter)
                self.description_label.setGeometry(QtCore.QRect(20, 10, 131, 21))
                self.description_label.setFont(Tfont)
                self.description_label.setStyleSheet("color:#dce4ee")
                self.description_label.setObjectName("description_label")

        #DESCRIPTION FRAME child frame
                self.description_frame = QtWidgets.QFrame(self.description_containter)
                self.description_frame.setGeometry(QtCore.QRect(10, 39, 351, 261))
                self.description_frame.setStyleSheet("background-color:rgb(51,51,51);\n"
                                                "border-radius:20px;\n"
                                                "color:#dce4ee")
                self.description_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.description_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.description_frame.setObjectName("description_frame")

        #DESCRIPTION TEXTBROWSER holds description content
                self.textBrowser = QtWidgets.QTextBrowser(self.description_frame)
                self.textBrowser.setGeometry(QtCore.QRect(10, 10, 331, 191))
                self.textBrowser.setStyleSheet("border:None;")
                self.textBrowser.setObjectName("textBrowser")

#LISTEN BUTTON
                self.listen_button = QtWidgets.QPushButton(self.description_frame)
                self.listen_button.setGeometry(QtCore.QRect(300, 220, 41, 31))
                self.listen_button.setStyleSheet("image:url(:/butimg/speaker.png);\n"
                                                "background-color:rgb(51,51,51)")
                self.listen_button.setText("")
                self.listen_button.clicked.connect(self.speak)
                self.listen_button.setObjectName("listen_button")

#PROGRESS BAR
                self.progressBar = QtWidgets.QProgressBar(self.description_frame)
                self.progressBar.setGeometry(QtCore.QRect(20, 220, 271, 31))
                self.progressBar.setStyleSheet("QProgressBar {\n"
        "    border: 2px solid #262626; /* Border around the progress bar */\n"
        "    border-radius: 8px; /* Rounded corners for the left-top and left-bottom corners */\n"
        "    background-color: #111111; /* Background color of the progress bar */\n"
        "    text-align: none;\n"
        "}\n"
        "\n"
        "QProgressBar::chunk {\n"
        "    border-radius: 8px; /* Rounded corners for the left-top and left-bottom corners of the progress chunk */\n"
        "    background-color: #0074cc; /* Color of the progress bar\'s filled part */\n"
        "}\n"   
        "")
                self.progressBar.setProperty("value", 0)
                self.progressBar.setObjectName("progressBar")
                self.progressBar.setTextVisible(False)
               

#STATISTICS 

        #STATISTIC CONTAINER
                self.stat_container = QtWidgets.QFrame(self.centralwidget)
                self.stat_container.setGeometry(QtCore.QRect(690, 330, 371, 301))
                self.stat_container.setStyleSheet("background-color:rgb(39,39,39);\n"
                                                        "border-radius:25px;")
                self.stat_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.stat_container.setFrameShadow(QtWidgets.QFrame.Raised)
                self.stat_container.setObjectName("stat_container")

        #STATISTIC FRAME
                self.stat_frame = QtWidgets.QFrame(self.stat_container)
                self.stat_frame.setGeometry(QtCore.QRect(9, 39, 351, 251))
                self.stat_frame.setStyleSheet("background-color:rgb(255,255,255);\n"
                                                "border-radius:20px;")
                self.stat_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.stat_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.stat_frame.setObjectName("stat_frame")

        #STATISTICS LABEL
                self.stat_label = QtWidgets.QLabel(self.stat_container)
                self.stat_label.setGeometry(QtCore.QRect(20, 10, 131, 21))
                self.stat_label.setFont(Tfont)
                self.stat_label.setStyleSheet("color:#dce4ee")
                self.stat_label.setObjectName("stat_label")

        #TAB WIDGET child to stat frame
                self.tabWidget = QtWidgets.QTabWidget(self.stat_frame)
                self.tabWidget.setGeometry(QtCore.QRect(10, 10, 331, 231))
                self.tabWidget.setFont(sfont)
                self.tabWidget.setStyleSheet("QTabWidget {\n"
        "    background-color: rgb(51, 51, 51); /* Background color of the QTabWidget */\n"
        "   /* border: 1px solid #262626; 1px solid border with color #262626 */\n"
        "    color: #dce4ee; /* Text color for unselected tabs */\n"
        "    \n"
        "}\n"
        "\n"
        "QTabWidget::pane {\n"
        "    border: None; /* Add a border to the entire QTabWidget */\n"
        "}\n"
        "\n"
        "QTabBar::tab {\n"
        "    background-color: rgb(51, 51, 51); /* Background color of unselected tabs */\n"
        "    color: #dce4ee; /* Text color for unselected tabs */\n"
        "    border: 1px solid #262626; /* Border around each tab */\n"
        "    padding: 5px 10px; /* Adjust padding as needed */\n"
        "    border-radius:7px;\n"
        "}\n"
        "\n"
        "QTabBar::tab:selected {\n"
        "    background-color: rgb(39, 39, 39); /* Background color of the selected tab */\n"
        "}\n"
        "")
                self.tabWidget.setObjectName("tabWidget")

        #TAB1 SENTIMENT
                self.tab = QtWidgets.QWidget()
                self.tab.setObjectName("tab")

        #SENTIMENT FRAME
                self.sent_frame = QtWidgets.QFrame(self.tab)
                self.sent_frame.setGeometry(QtCore.QRect(0, 0, 331, 201))
                self.sent_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.sent_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.sent_frame.setObjectName("sent_frame")
                self.tabWidget.addTab(self.tab, "")

        #TAB2 RELEVANCE
                self.tab_2 = QtWidgets.QWidget()
                self.tab_2.setObjectName("tab_2")

        #RELEVANCE FRAME
                self.rel_frame = QtWidgets.QFrame(self.tab_2)
                self.rel_frame.setGeometry(QtCore.QRect(0, 0, 331, 201))
                self.rel_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
                self.rel_frame.setFrameShadow(QtWidgets.QFrame.Raised)
                self.rel_frame.setObjectName("rel_frame")
                self.tabWidget.addTab(self.tab_2, "")
        
#STATUS BAR
                MainWindow.setCentralWidget(self.centralwidget)
                self.statusbar = QtWidgets.QStatusBar(MainWindow)
                self.statusbar.setObjectName("statusbar")
                MainWindow.setStatusBar(self.statusbar)
        
                self.retranslateUi(MainWindow)
                self.tabWidget.setCurrentIndex(1)
                QtCore.QMetaObject.connectSlotsByName(MainWindow)

#WEBVEIEW
                self.web_view = QWebEngineView(self.kg_wrap)
                self.web_view.setGeometry(QtCore.QRect(0, 0, 631, 511))             
                self.web_view.setObjectName("web_view")

#PLOTS
        #RELEVANCE VIEW
                self.rel_view = QWebEngineView(self.rel_frame)
                self.rel_view.setGeometry(QtCore.QRect(0, 0, 321, 191))
                self.web_view.setObjectName("rel_view")

        #SENTIMENT VIEW
                self.sent_view = QWebEngineView(self.sent_frame)
                self.sent_view.setGeometry(QtCore.QRect(0, 0, 321, 191))
                self.web_view.setObjectName("sent_view")

              
#SETTING UI TEXT
        def retranslateUi(self, MainWindow):
                _translate = QtCore.QCoreApplication.translate
                MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.kg_label.setText(_translate("MainWindow", "KNOWLEDGE GRAPH "))
                self.search_button.setText(_translate("MainWindow", "SEARCH"))
                self.description_label.setText(_translate("MainWindow", "DESCRIPTION"))
                self.listen_button.setWhatsThis(_translate("MainWindow", "<html><head/><body><p><img src=\":/butimg/speaker.png\"/></p></body></html>"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "SENTIMENT"))
                self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "RELEVANCE"))
                self.stat_label.setText(_translate("MainWindow", "STATISTICS"))

#SEARCH FUNCTION MAIN
        def Search(self):
                global data
                #setting progressbar to be visible only during the duration of search
                self.progressBar.show()
                self.statusbar.showMessage("query received")

                #extracting query from input 
                query = self.entry.toPlainText()
                self.progressBar.setValue(5)
                
                
                # Query processing text -> json
                data = GPT_func.Ask(query)
                self.progressBar.setValue(30)
                self.textBrowser.setText(data)

                #summarizing query
                summarized_data = text_sumzer.summarize_text(data)
                self.progressBar.setValue(45)
          
                JSdata = GPT_func.text2json(summarized_data)
                self.progressBar.setValue(60)
                JSdata = json.loads(JSdata)
                self.progressBar.setValue(90)
                pyvis_KG.plot_knowledge_graph(JSdata, mode='save')
               
                self.progressBar.setValue(100)

                # Plotting JSON knowledge graph and viewing HTML
                self.ViewHTML()

                #tts init
                text_to_speech.process_text(data)

                #sentimentanalysis
                self.Viewradar()
                self.progressBar.hide()
                self.statusbar.showMessage("Succesfully finished")
  

        def Viewradar(self):
               rdata = rs.get_relevance_scores(data)
               sdata = ss.get_sentiment_scores(data)
               Rplot.Radar(rdata,mode='r')
               Rplot.Radar(sdata,mode='s')
               self.rel_view.setUrl(QUrl('file:///radar_chart_R.html'))
               self.sent_view.setUrl(QUrl('file:///radar_chart_S.html'))
               self.stat_frame.setStyleSheet("background-color:rgb(51,51,51)")


        def ViewHTML(self):
                print('view HTML')
                url = 'file:///nx.html'
                self.web_view.setUrl(QUrl(url))
                self.kg_frame.setStyleSheet("background-color:#333333")

        def speak(self):
                print('play')
                self.listen_button.setStyleSheet("image:url(:/butimg/speaker2.png);\n"
                "background-color:rgb(51,51,51)")
                def speak_text():
                        pygame.mixer.init()
                        pygame.mixer.music.set_volume(0.7)
                        pygame.mixer.music.load("speech.wav")
                        pygame.mixer.music.play()

                        while pygame.mixer.music.get_busy():
                                time.sleep(1)
                        self.listen_button.setStyleSheet("image:url(:/butimg/speaker.png);\n"
                        "background-color:rgb(51,51,51)")
                        
                speak_thread = threading.Thread(target=speak_text)
                speak_thread.start()
                self.listen_button.clicked.connect(self.stop_speak)
                

        def stop_speak(self):
                print('stop')
                self.listen_button.setStyleSheet("image:url(:/butimg/speaker.png);\n"
                "background-color:rgb(51,51,51)")
                pygame.mixer.music.pause()
                self.listen_button.clicked.connect(self.speak)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle('ASK GPT')
    MainWindow.show()
    sys.exit(app.exec_())
