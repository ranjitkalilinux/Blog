# # from PyQt5.QtWidgets import *
# # import sys
# # from PyQt5.QtCore import *
# # from PyQt5.QtGui import *
# # import mysql.connector
# # class Main(QWidget):
# #   def __init__(self):
# #     super().__init__()
# #     self.Gui()
# #   def Gui(self):
# #   	self.setGeometry(120,120,500,500)
# #   	self.layput = QVBoxLayout(self)
# #   	self.frame = QFrame(self)
# #   	list1 = ["rafdsf","Fsdfsdf","Fsdfsdf","FSDfsdfs","FDSf"]
# #   	self.list1 = QListWidget()

# # print(re)

  	
# #   	self.button = QPushButton("press")
  	
  	
# #   	self.button.clicked.connect(self.showframe)
  	
# #   	self.layput.setAlignment(Qt.AlignCenter)
# #   	self.layput.addWidget(self.button, alignment=Qt.AlignRight)
# #   	self.layput.addWidget(self.frame, alignment=Qt.AlignCenter)
# #   	self.layput.addWidget(self.list1, alignment=Qt.AlignCenter)

# #   	self.setLayout(self.layput)
# #     con = mysql.connector.connect(host="localhost", user="root", passwd="")
# #   	self.show()
# #   def showframe(self):
  	
# #   	self.layoutf = QVBoxLayout(self.frame)

  	
 
# #   	self.button1 = QPushButton("R", self.frame)
# #   	self.button1.setStyleSheet("QPushButton{border:none;"
# #   		"background-color:#25CCF7;"
# #   		"height: 50px;"
# #   		"width: 50px;"
# #   		"font-size:20px;"
# #   		"border-radius:25%;"
# #   		"padding:2px;}")
# #   	self.layoutf.setAlignment(Qt.AlignTop)
# #   	self.layoutf.addWidget(self.button1, alignment=Qt.AlignCenter)
# #   	self.frame.setStyleSheet("QFrame{background-color:white;"
# #   		"border:1px solid white;"
# #   		"border-radius:8px;"
# #   		"width:400px;"
# #   		"padding-left:100px;"
# #   		"padding-right:100px;"
# #   		"height:40px;}")
# #   	self.name = QLabel("ranjit", self.frame) 
# #   	self.layoutf.addWidget(self.name, alignment=Qt.AlignCenter)
# #   	self.name.setStyleSheet("font-size:20px;font-family:Georgia;padding:1px;")
# #   	#############################################################33

# #   	self.pass1 = QLabel("sdfsdfsfdfddgdfdfgd@gmail.com", self.frame)
# #   	self.layoutf.addWidget(self.pass1, alignment=Qt.AlignCenter)
# #   	self.pass1.move(70,50)
# #   	self.pass1.setStyleSheet("font-size:13px;font-family:Georgia;padding:1px;")
# #   	######################
# #   	self.chnagepassword = QPushButton("Chnage Password", self)

# #   	self.chnagepassword.setStyleSheet("QPushButton{background-color:#00ffff;"
# #         "border-radius:9%;"
# #         "width:100px;"
# #         "height:25px;"
# #         "font-size:12px;"
# #         "padding:1px;"
# #         "font-family:Constantia;}"
# #         "QPushButton:hover{background-color:#ebf6f7;"
# #         "border:1px solid gray;}"
# #         "QPushButton:pressed{background-color:#0A79DF}")
# #   	self.layoutf.addWidget(self.chnagepassword, alignment=Qt.AlignCenter)

# #   	self.frame.show()
# #   	self.frame.resize(500,200)
# #   	self.frame.move(10,30)
# #   	self.shadow1 = QGraphicsDropShadowEffect()
# #   	self.shadow1.setBlurRadius(80)
# #   	self.shadow1.setXOffset(15)
# #   	self.shadow1.setYOffset(15)
# #   	self.frame.setGraphicsEffect(self.shadow1)

# #   	self.list1.hide()

# #   	self.button.show()
# # Winodw = QApplication(sys.argv)
# # App = Main()
# # sys.exit(Winodw.exec_())
# list1 = [12,80,12]
# list2 = [78,45,67]

# newlist1 = []
# getlist = []

# for i in range(len(list1)):
# 	data = (list1[i], list2[i])
# 	newlist1.append(str(data))
# print(newlist1)

# testdate = []
    # for i in range(self.addinglist.count()):
    #     testdate.append(self.addinglist.item(i).text())
    # print(testdate)
    # dletet = cour.execute('''DELETE FROM blog WHERE hader='%s' '''% (dataofblog))
import sqlite3
conection = sqlite3.connect("localimage.db")
cour = conection.cursor()
cour.execute(" TABLES")