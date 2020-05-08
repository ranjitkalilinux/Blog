from PyQt5.QtWidgets import *
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3
import mysql.connector
import datetime
import time
import os
class Main(QWidget):
  def __init__(self):
    super().__init__()
    self.Gui()
  def Gui(self):
    self.setWindowTitle("ImageCloud")
    self.setGeometry(300,200,700,400)
    # adding main window to center
    self.frame = self.frameGeometry()
    center = QDesktopWidget().availableGeometry().center()
    self.frame.moveCenter(center)
    self.move(self.frame.topLeft())
    #####################################
    ## adding layout
    
    self.layout1 = QVBoxLayout(self)
    self.layout1.setAlignment(Qt.AlignCenter)
    
    
    ## adding text widget
    
    

    self.lab = QLabel("Login", self)
    self.text1 = QLineEdit(self)
   
    self.text2 = QLineEdit(self) 
    self.showbutton = QPushButton("Show", self.text2)
    self.showbutton.move(440,7)
    ## adding stlle to showbutton
    self.showbutton.setStyleSheet("QPushButton{background-color:transparent;"
        "font-size:12px;}"
        "QPushButton:hover{color:blue;}")
    self.showbutton.setCursor(Qt.PointingHandCursor)
    self.showbutton.setCheckable(True)
    self.showbutton.clicked.connect(self.showpass)
    ########################33
    self.text2.returnPressed.connect(self.createaccout)
    self.forgetpassword = QPushButton("Forget Password", self)
    self.submit1 = QPushButton("Submit", self)
    self.submit1.clicked.connect(self.createaccout)
    
    # small style
    self.lab.setStyleSheet("font-size:35px;"
        "font-family:Constantia;")
    self.create1 = QPushButton("Create Acoount", self)
    self.create1.setCursor(Qt.PointingHandCursor)
    self.create1.clicked.connect(self.insertintodata)
    
    self.create1.setStyleSheet("QPushButton{background-color:transparent;"
        "font-family:Constantia;"
        "font-size:13px;}"
        "QPushButton:hover{color:blue;"
        "border:1px solid white;"
        "border-radius:5%;"
        "background-color:white;}")
    self.create1.move(10,10)
    ## adding text
    self.forgetpassword.clicked.connect(self.forgetpass)
    self.layout1.addWidget(self.lab, alignment=Qt.AlignCenter)
    self.layout1.addWidget(self.text1, alignment=Qt.AlignCenter)
    self.layout1.addWidget(self.text2, alignment=Qt.AlignCenter)
    self.layout1.addWidget(self.forgetpassword, alignment=Qt.AlignRight)
    self.layout1.addWidget(self.submit1, alignment=Qt.AlignCenter)
    
    
    ##############################3

    ###########################################################
    self.text1.setPlaceholderText("  Enter Your Name")
    self.text1.setStyleSheet("QLineEdit{"    
        "border:2px inset transparent;"
        "width:500px;"
        "font-family:Constantia;"
        "height:35px;"
        "border-radius:8px;"
        "font-family:Constantia;"
        "font-size:15px;"
        "background-color:white;"
        "margin:5px;}"
        "QLineEdit:hover{border:2px inset #7CEC9F;"
        "background-color:white;"
        "border-color:#7CEC9F;"
        ";}")
    #################################
    self.text2.setStyleSheet("QLineEdit{border:2px solid transparent;"
        "width:500px;"
        "height:35px;"
        "border-radius:8px;"
        "font:15px;"
        "background-color:white;"
        "font-family:Constantia"
        "}"
        "QLineEdit:hover{border:2px outset #7CEC9F;"
        "background-color:white;}")

    self.text2.setPlaceholderText("  Enter Your Password")
    ## done with all the text 
    #############################################
    self.text2.setEchoMode(QLineEdit.Password)
    ###########################################
    ## adding shadow to text1
    
    ###########################
    ### adding Style to button
    

    ## adding submit stylesheet
    self.submit1.setStyleSheet("QPushButton{background-color:#EAF0F1;"
        "border-radius:10%;"
        "width:100px;"
        "height:27px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:white;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:#67E6DC;"
        ";}")
    self.forgetpassword.setStyleSheet("QPushButton{background-color:transparent;"
        "font-size:12px;"
        "height:19px;"
        "width:103px;"
        "font-family:Constantia}"
        "QPushButton:hover{color:blue;"
        "border:1px solid white;"
        "border-radius:9%;"
        "height:px;"
        "background-color:white;}"
        )
    self.setStyleSheet("background-color:#add8e6;")
    ##############################################
    ## adding corsor to cerat s
    
    self.forgetpassword.setCursor(Qt.PointingHandCursor)
    self.submit1.setCursor(Qt.PointingHandCursor)

    ########################################
    ############ triggerd all the buttons
    
    self.list12 = QListWidget(self)
    self.list12.itemClicked.connect(self.getlistitem)
    # copy code from Stackoverflow 

    self.list12.hide()
    ############
    self.list12.setStyleSheet("QListWidget{margin-top:7px;border:1px solid transparent;font-size:20px;width:100px;"
        "font-family:Georgia;"
        "margin-left:30px;"
        "margin-right:30px;}"
        "QListWidget::item{"
        "width:40px;"
        "border:2px solid transparent;"
        "border-radius:8px;"
        "font:bold;"
        "margin:3px;"
        "padding:2px;"
        "background-color:white;"
        "color:black;"
        "font-size:30pt;}"
        "QListWidget::item:hover{color:blue;}")
    # main cloud configration
    self.accountinfo = QPushButton("", self)
    self.accountinfo.setCheckable(True)
    self.accountinfo.clicked.connect(self.showframe)
    self.accountinfo.setStyleSheet("QPushButton{background-color:#25CCF7;"
        "border:1px solid transparent;"
        "color:white;"
        "border-radius:20%;"
        "font-size:20px;}"
        "QPushButton:pressed{border:3px solid #dae4ee;}")
    self.accountinfo.resize(40,40)
    self.accountinfo.move(10,2)
    self.accountinfo.setCursor(Qt.PointingHandCursor)
    self.accountinfo.hide()
    ########################
    # adding list
   
    ##############3
    
    
    ##########
    self.availableblog = QLabel("Available Blogs", self)
    self.layout1.addWidget(self.availableblog,alignment=Qt.AlignCenter)
    self.availableblog.setStyleSheet("QLabel{font-size:30px;font-family:Georgia;color:blue;}")
    self.availableblog.hide()
    ######

    self.layout1.addWidget(self.list12)
    ###
    
    ##
    self.setLayout(self.layout1)
    self.autologin()
    self.show()
  def insertintodata(self):
    self.dilog = QDialog(self)
    self.welecome = QVBoxLayout(self.dilog)
    self.welecome.setAlignment(Qt.AlignCenter)
    self.dilog.setWindowTitle("Welcome")
    self.dilog.resize(400,400)
    self.dilog.setFixedSize(400,400)
    self.dilog.setStyleSheet("QDialog{background-color:white;}")
    
    self.line = QLineEdit(self.dilog)
    self.line2 = QLineEdit(self.dilog)
    self.emial = QLineEdit(self.dilog)
    self.line2.setEchoMode(QLineEdit.Password)
    self.showbutton1 = QPushButton("Show", self.line2)
    self.showbutton1.setCheckable(True)
    self.showbutton1.move(290,6)
    self.showbutton1.setStyleSheet("QPushButton{background-color:transparent;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{color:blue;}")
    self.showbutton1.setCursor(Qt.PointingHandCursor)
    self.showbutton1.clicked.connect(self.showpass1)
    self.line.setPlaceholderText("  Set Your User Name")
    self.line2.setPlaceholderText(" Set Your Password")
    self.emial.setPlaceholderText(" Enter Your E-Mail")
    ##########3
    self.welecome.addWidget(self.line, alignment=Qt.AlignCenter)
    self.welecome.addWidget(self.line2, alignment=Qt.AlignCenter)
    self.welecome.addWidget(self.emial, alignment=Qt.AlignCenter)
    #
    self.line2.setStyleSheet("QLineEdit{border:2px solid white;"
        "border-radius:12%;"
        "width:350px;"
        "height:32px;"
        "font-size:14px;"
        "font-family:Constantia;"
        "background-color:#25CCF7}"
        "QLineEdit:hover{border-bottom-color:black;}")
    self.emial.setStyleSheet("QLineEdit{border:2px solid white;"
        "border-radius:12%;"
        "font-size:14px;"
    
        "font-size:14px;"
        "width:350px;"
        "height:32px;"
        "background-color:#25CCF7;"
        "font-family:Constantia;}"
        "QLineEdit:hover{border-bottom-color:black;}")

    self.emial.move(50,120)
    self.line.move(50,160)
    self.line.resize(300,35)
    self.emial.resize(300,35)
    
    self.line2.move(50,200)
    self.line2.resize(300,35)
    self.line.setStyleSheet("QLineEdit{border:2px solid white;"
        "border-radius:8px;"
        "font-size:14px;"
        "width:350px;"
        "height:32px;"
        "height:32px;"
        "font-size:14px;"
        "background-color:#25CCF7;"
        "font-family:Constantia}"
        "QLineEdit:hover{border-bottom-color:black;}")
    submit_button = QPushButton("Submit", self.dilog)
    self.welecome.addWidget(submit_button, alignment=Qt.AlignCenter)
    submit_button.clicked.connect(self.insertdata)
    submit_button.move(145, 240)
    submit_button.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:8%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;}"
        "QPushButton:hover{background-color:#ebf6f7;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    ##################################################
    # chaking user name
    
    self.dilog.exec_()
  def autologin(self):
    try:
        conection = sqlite3.connect("localimage.db")
        cour = conection.cursor()
        data = cour.execute("SELECT * FROM information")
        data = data.fetchall()
        namedata = None
        passdata = None
        for i in data:
            namedata = i[0]
            passdata = i[1]
        self.text1.setText(namedata)
        self.text2.setText(passdata)
        if self.text1.text() == namedata and self.text2.text() == passdata:
            connection = mysql.connector.connect(host="localhost",user="root",passwd="")
            cour = connection.cursor()
            cour.execute("USE information")
            result = cour.execute('SELECT  * FROM all_info WHERE name=%s and passwd=%s',(namedata, passdata)) 
            ##adiing all hide and show 
            self.text1.hide()
            self.text2.hide()
            self.submit1.hide()
            self.forgetpassword.hide()
            self.lab.hide()
            self.create1.hide()
            self.accountinfo.show()
            self.list12.show()
            
            self.availableblog.show()
            ###############
            conection = sqlite3.connect("localimage.db")
            cour = conection.cursor()
            result1 = cour.execute("SELECT * FROM information")
            result1 = result1.fetchall()
            name2 = None
            for i in result1:
                name2 = i[0]
            setname = name2[0].capitalize()
            ##adding blog showconfigration
            con = mysql.connector.connect(host="localhost", user="root", passwd="")
            cour =con.cursor()
            cour.execute("USE information")
            # cour.execute("INSERT INTO blog VALUES (%s,%s,%s)",("3","python", "ppri"))
            cour.execute("SELECT * FROM blog ")
            blog = cour.fetchall()
            blog_data = []
            for i in blog:
                blog_data.append(i[1])
            print(blog_data)
            
            self.accountinfo.setText(setname)
    
            self.list12.addItems(blog_data)
        else:
            print("No")
    except Exception as e:
        print(e)
  def createaccout(self):
    try:
        username = self.text1.text()
        password = self.text2.text()
        
        connection = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour = connection.cursor()
        cour.execute("USE information")
        result = cour.execute("SELECT * FROM all_info WHERE name=%s and passwd=%s", (username, password))
        if (len(cour.fetchall()) > 0):
            self.msg1 = QMessageBox(self)
            self.msg1.setWindowTitle("Error")
            self.msg1.setText("Successfully LogIn")
            self.msg1.setStyleSheet("QMessageBox{background-color:white;"
                "width:400px;color:white;}"
                "QMessageBox QLabel{background-color:white;color:green;padding-right:100px;"
                "font-size:20px;}"
                "QMessageBox QPushButton{width:100px;"
                "height:30px;"
                "border-radius:8%;}"
                "QMessageBox QPushButton:pressed{background-color:lime;}")
            self.msg1.exec_()
            ##adiing  hide configratio 
            self.text1.hide()
            self.text2.hide()
            self.create1.hide()
            self.submit1.hide()
            self.forgetpassword.hide()
            self.lab.hide()
            self.accountinfo.show()
            self.list12.show()
            self.availableblog.show()
            #################
            

            # adding a text to button

            ######
            name = self.text1.text()
            pass1 = self.text2.text()
            conection = sqlite3.connect("localimage.db")
            cour = conection.cursor()
            cour.execute('CREATE TABLE information(name varchar(100), pass varchar(100))')
            cour.execute('INSERT INTO information(name,pass) VALUES(?,?)',(name, pass1))
            data = cour.execute("SELECT * FROM information ")
            data = data.fetchall()
            namedata = None
            passdata = None
            for i in data:
                namedata =  i[0]
                passdata = i[1]
            conection.commit()
            conection.close()
            print(namedata[0])
            print(passdata)
            setaccoutname = namedata[0].capitalize()
            print(setaccoutname)
            self.accountinfo.show()
            conection = sqlite3.connect("localimage.db")
            cour = conection.cursor()
            result1 = cour.execute("SELECT * FROM information")
            result1 = result1.fetchall()
            name2 = None
            for i in result1:
                name2 = i[0]
            setname = name2[0].capitalize()
            ####
            self.accountinfo.setText(setname)
            con = mysql.connector.connect(host="localhost", user="root", passwd="")
            cour =con.cursor()
            cour.execute("USE information")
            # cour.execute("INSERT INTO blog VALUES (%s,%s,%s)",("3","python", "ppri"))
            cour.execute("SELECT * FROM blog ")
            blog = cour.fetchall()
            blog_data = []
            for i in blog:
                blog_data.append(i[1])
            self.list12.addItems(blog_data)
            print(blog_data)
        else:
            self.msg2 = QMessageBox(self)
            self.msg2.setWindowTitle("Error")
            self.msg2.setText("Kindky Check Username or Password")
            self.msg2.setStyleSheet("QMessageBox{background-color:white;"
                "width:400px;color:white;}"
                "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
                "font-size:20px;}"
                "QMessageBox QPushButton{width:100px;"
                "height:30px;"
                "border-radius:10%;}"
                "QMessageBox QPushButton:pressed{background-color:lime;}")
            self.msg2.exec_()
    except Exception as e:
        print(e,"Error")
    ## cgeking name

  def forgetpass(self):
    self.forgetdilog = QDialog(self)
    self.forgetdilog.setWindowTitle("Forget Password")
    self.forgetdilog.setFixedSize(500,250)
    ## adding layout
    self.layout = QVBoxLayout(self.forgetdilog)
    self.layout.setAlignment(Qt.AlignCenter)
    ###########3
    self.username = QLineEdit(self)
    self.email = QLineEdit(self)
    self.otp = QLineEdit(self)
    self.otp.hide()
    self.otp.setPlaceholderText("Enter 5-Digit OTP Here")
    self.otp.setValidator(QIntValidator(0,99999))
    self.forpass = QPushButton("Reset Password")
    self.forpass.clicked.connect(self.checkusrnamepassword)
    self.layout.addWidget(self.username,alignment=Qt.AlignCenter)
    self.layout.addWidget(self.email,alignment=Qt.AlignCenter)
    self.layout.addWidget(self.otp, alignment=Qt.AlignCenter)
    self.layout.addWidget(self.forpass,alignment=Qt.AlignCenter)
    self.forgetdilog.setStyleSheet("background-color:white")
    self.username.setStyleSheet("QLineEdit{background-color:#7fffd4;"
        "border:1px solid gray;"
        "width:400px;"
        "height:25px;"
        "border-radius:10%;"
        "font-family:Constantia;"
        "font-size:13px;}")
    self.username.setPlaceholderText(" Enter Your Username")
    self.email.setPlaceholderText(" Enter Your Email")
    self.email.setStyleSheet("QLineEdit{background-color:#7fffd4;"
        "border:1px solid gray;"
        "width:400px;"
        "height:25px;"
        "border-radius:10%;"
        "font-family:Constantia;"
        "font-size:13px;}")
    self.forpass.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:9%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:#ebf6f7;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    self.otp.setStyleSheet("QLineEdit{background-color:#7fffd4;"
        "border:1px solid gray;"
        "width:400px;"
        "height:25px;"
        "border-radius:10%;"
        "font-size:13px;}")
    self.resetpass = QPushButton("Reset Password", self)
    self.layout.addWidget(self.resetpass, alignment=Qt.AlignCenter)
    self.otp.returnPressed.connect(self.setnewpassword)
    self.resetpass.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:9%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:#ebf6f7;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    self.resetpass.clicked.connect(self.setnewpassword)
    self.resetpass.hide()
    self.forgetdilog.exec_()
  def insertdata(self):
    name = self.line.text()
    pass1 = self.line2.text()
    email = self.emial.text()
    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    result = cour.execute("SELECT * FROM all_info")
    result = cour.fetchall()
    matching_result = None
    for i in result:
        matching_result = i[1]
    if name == matching_result:
        self.msg0 = QMessageBox(self)
        self.msg0.setWindowTitle("Error")
        self.msg0.setText("User Name Is Already Taken")
        self.msg0.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg0.exec_()
    elif name == "" and pass1 == "":
        self.msg = QMessageBox(self)
        self.msg.setWindowTitle("Error")
        self.msg.setText("Blank Value Not Will Be Allowed")
        self.msg.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        
        self.msg.exec_()
    elif len(pass1) < 8:
        self.msg1 = QMessageBox(self)
        self.msg1.setWindowTitle("Error")
        self.msg1.setText("Password Length Must Be 8 character")
        self.msg1.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg1.exec_()
    else: 
        conection = sqlite3.connect("localimage.db")
        cour = conection.cursor()
        cour.execute('CREATE TABLE information(name varchar(100), pass varchar(100))')
        cour.execute('INSERT INTO information(name,pass) VALUES(?,?)',(name, pass1))
        data = cour.execute("SELECT * FROM information ")
        data = data.fetchall()
        namedata = None
        passdata = None
        for i in data:
            namedata =  i[0]
            passdata = i[1]
        namedata = str(namedata)
        passdata = str(passdata)
        self.text1.setText(namedata)
        self.text2 .setText(passdata)
        conection.commit()
        ## main Mysql Connection
        connection = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour = connection.cursor()

        x = datetime.datetime.now()
        print(type(namedata))
        print(type(passdata))

        cour.execute("USE information")
        cour.execute("INSERT INTO all_info(name,passwd,data,email) VALUES(%s,%s,%s,%s)", (namedata,passdata,x,email))
        connection.commit()
        connection.close()
        self.dilog.close()
        # linux
        conection = sqlite3.connect("localimage.db")
        cour = conection.cursor()
        result1 = cour.execute("SELECT * FROM information")
        result1 = result1.fetchall()
        name2 = None
        for i in result1:
            name2 = i[0]
        setname = name2[0].capitalize()
        self.accountinfo.setText(setname)
        cour.close()

        con = mysql.connector.connect(host="localhost", user="root", passwd="")
        cour =con.cursor()
        cour.execute("USE information")
        # cour.execute("INSERT INTO blog VALUES (%s,%s,%s)",("3","python", "ppri"))
        cour.execute("SELECT * FROM blog ")
        blog = cour.fetchall()
        blog_data = []
        for i in blog:
            blog_data.append(i[1])
        print(blog_data)
        
        self.accountinfo.setText(setname)

        self.list12.addItems(blog_data)
  def showpass(self,state):
    if state:
        self.text2.setEchoMode(QLineEdit.Normal)
        self.showbutton.setText("Hide")
    else:
        self.showbutton.setText("Show")
        self.text2.setEchoMode(QLineEdit.Password)
  def showpass1(self,state):
    if state:
        self.line2.setEchoMode(QLineEdit.Normal)
        self.showbutton1.setText("Hide")
    else:
        self.line2.setEchoMode(QLineEdit.Password)
        self.showbutton1.setText("Show")

  def checkusrnamepassword(self):
    try:
        name = self.username.text()
        email_data = self.email.text()
        connection = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour = connection.cursor()
        cour.execute("USE information")
        result = cour.execute("SELECT * FROM all_info WHERE name='%s'"% (name))
        result = cour.fetchall()
        self.namecheck = None
        self.emailcheck = None
        for i in result:
            self.namecheck = i[1]
            self.emailcheck = i[2]
        if name == self.namecheck and email_data == self.emailcheck:
            import smtplib
            import random
            self.sendotp = random.randrange(10000, 90000)

            # sender_email = "ranjitkalilinux@gmail.com"
            
            # password = "ranjitmaity123456789$&Sonali"

            # server = smtplib.SMTP('smtp.gmail.com', 587)

            # server.starttls()
            # server.login(sender_email, password)
            # server.sendmail(sender_email, email_data, f"your Otp Is {self.sendotp}")
            print(self.sendotp)
            self.username.setDisabled(True)
            self.email.setDisabled(True)
            self.otp.show()  
            self.forpass.hide()
            self.resetpass.show()
        else:
            self.msg1 = QMessageBox(self)
            self.msg1.setWindowTitle("Error")
            self.msg1.setText("Username or E-Mail Not Correct\n Kindly Check")
            self.msg1.setStyleSheet("QMessageBox{background-color:white;"
                "width:400px;color:white;}"
                "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
                "font-size:20px;"
                "font-family:Constantia;}"
                "QMessageBox QPushButton{width:100px;"
                "height:30px;"
                "border-radius:10%;}"
                "QMessageBox QPushButton:pressed{background-color:lime;}")
            self.msg1.exec_()
    except Exception as e:
        print(e)
  def setnewpassword(self):
    self.setnewpassword1 = QDialog(self)
    
    self.setnewpassword1.setFixedSize(500,250)
    self.setnewpassword1.setStyleSheet("background-color:white;")
    self.layout = QVBoxLayout(self.setnewpassword1)
    self.layout.setAlignment(Qt.AlignCenter)
    self.enterpassword = QLineEdit(self)
    self.enterpassword.setPlaceholderText(" Enter New Password")
    
    self.reenterpassword = QLineEdit(self)
    self.reenterpassword.setPlaceholderText(" Reenter Your Password")
    self.button = QPushButton("Chnage Password", self)
    self.button.clicked.connect(self.checkpassoword)
    self.layout.addWidget(self.enterpassword, alignment=Qt.AlignCenter)
    self.layout.addWidget(self.reenterpassword, alignment=Qt.AlignCenter)
    self.layout.addWidget(self.button, alignment=Qt.AlignCenter)
    self.enterpassword.setStyleSheet("QLineEdit{background-color:#7fffd4;"
        "border:1px solid gray;"
        "width:400px;"
        "height:25px;"
        "border-radius:10%;"
        "font-family:Constantia;"
        "font-size:13px;}")
    self.reenterpassword.setStyleSheet("QLineEdit{background-color:#7fffd4;"
        "border:1px solid gray;"
        "width:400px;"
        "height:25px;"
        "border-radius:10%;"
        "font-family:Constantia;"
        "font-size:13px;}")
    self.button.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:9%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:#ebf6f7;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    if self.sendotp == int(self.otp.text()):
        self.forgetdilog.close()
        self.setnewpassword1.exec_()
  def checkpassoword(self):
    name  = self.namecheck
    password = self.enterpassword.text()
    repassword = self.reenterpassword.text()
    if password == "" and repassword == "":
        self.msg0 = QMessageBox(self)
        self.msg0.setWindowTitle("Error")
        self.msg0.setText("Blank Value Will Be Not Allowed")
        self.msg0.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;"
            "font-family:Constantia;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg0.exec_() 
    elif password != repassword:
        self.msg1 = QMessageBox(self)
        self.msg1.setWindowTitle("Error")
        self.msg1.setText("Password Does Not Match")
        self.msg1.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;"
            "font-family:Constantia;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg1.exec_()
    elif len(password) < 8:
        self.msg2 = QMessageBox(self)
        self.msg2.setWindowTitle("Error")
        self.msg2.setText("Password Length Must Be 8 Character")
        self.msg2.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;"
            "font-family:Constantia;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:10%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg2.exec_()
    else:
       
        connection1 = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour1 = connection1.cursor()
        cour1.execute("USE information")

        updatemain = cour1.execute("UPDATE all_info SET passwd=%s WHERE name=%s", (repassword, name))
        connection1.commit()

        self.text2.clear()
        self.setnewpassword1.close()
  def showframe(self,state):
    if state:
        conection = sqlite3.connect("localimage.db")
        cour = conection.cursor()
        result1 = cour.execute("SELECT * FROM information")
        result1 = result1.fetchall()
        name2 = None
        for i in result1:
            name2 = i[0]
        setname = name2[0].capitalize()
        
        ########################
        name = self.text1.text()
        connection = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour = connection.cursor()
        cour.execute("USE information")
        cour.execute("SELECT * FROM all_info WHERE name='%s' "% (name))
        emailresult = cour.fetchall()
        main_email = None
        for i in emailresult:
            main_email = i[2]
        print(main_email)

        self.frame = QFrame(self)
        self.frame.setWindowTitle("Write Blog")
        self.frame.setWindowOpacity(0.5)
        self.layoutf = QVBoxLayout(self.frame)
        self.button1 = QPushButton("", self.frame)
        self.button1.setText(setname)
        self.button1.setStyleSheet("QPushButton{border:none;"
            "background-color:#25CCF7;"
            "height: 50px;"
            "width: 50px;"
            "font-size:20px;"
            "border-radius:25%;"
            "padding:2px;}")
        self.layoutf.setAlignment(Qt.AlignTop)
        self.layoutf.addWidget(self.button1, alignment=Qt.AlignCenter)
        
        self.frame.setStyleSheet("QFrame{background-color:rgba(255,255,255, 223);"
            "border:1px solid transparent;"
            "border-radius:8px;"
            "width:400px;"
            "padding-left:100px;"
            "padding-right:100px;"
            "height:40px;}")
        self.name = QLabel(name, self.frame) 
        self.layoutf.addWidget(self.name, alignment=Qt.AlignCenter)
        self.name.setStyleSheet("font-size:20px;font-family:Georgia;padding:1px;color:black;")
        #############################################################33

        self.set_email = QLabel(main_email, self.frame)
        self.layoutf.addWidget(self.set_email, alignment=Qt.AlignCenter)
    
        self.set_email.setStyleSheet("font-size:13px;font-family:Georgia;padding:1px;margin-top:4px;")
        ######################
        self.chnagepassword = QPushButton("Chnage Password", self)

        self.chnagepassword.setStyleSheet("QPushButton{background-color:#00ffff;"
            "color:black;"
            "border-radius:9%;"
            "margin-top:10px;"
            "width:130px;"
            "height:27px;"
            "font-size:13px;"
            "margin-right:150px;"
            "padding:1px;"
            "font-family:Constantia;}"
            "QPushButton:hover{background-color:#ebf6f7;"
            "border:1px solid gray;}"
            "QPushButton:pressed{background-color:lime}")

        self.showpassword = None
        self.layoutf.addWidget(self.chnagepassword, alignment=Qt.AlignCenter)
        self.frame.resize(500,240)
        self.frame.move(35,37)
        self.shadow1 = QGraphicsDropShadowEffect()
        self.shadow1.setBlurRadius(80)
        self.shadow1.setXOffset(15)
        self.shadow1.setYOffset(15)
        self.frame.setGraphicsEffect(self.shadow1)

        
        
        #################
        self.button2 = QPushButton("Write Your Blog", self.frame)

        self.button2.clicked.connect(self.writeknowledleg)
        self.button2.move(250,143)
        self.button2.resize(120,30)
        self.button2.setStyleSheet("QPushButton{background-color:#00ffff;"
            "color:black;"
            "border-radius:9%;"
            "padding:1px;"
            "font-size:13px;"
            "font-family:Constantia;}"
            "QPushButton:hover{background-color:#ebf6f7;"
            "border:1px solid gray;}"
            "QPushButton:pressed{background-color:lime}")
        #############33
        self.youblog = QPushButton("Your Blog", self.frame)
        self.youblog.clicked.connect(self.Yourwriteblog)
        self.youblog.setStyleSheet("QPushButton{background-color:#00ffff;"
            "color:black;"
            "border-radius:9%;"
            "padding:1px;"
            "font-size:13px;"
            "font-family:Constantia;}"
            "QPushButton:hover{background-color:#ebf6f7;"
            "border:1px solid gray;}"
            "QPushButton:pressed{background-color:lime}")
        self.youblog.move(110,190)
        self.youblog.resize(130,27)
        ####################
        self.removeblog = QPushButton("Delete Blog", self.frame)
        self.removeblog.clicked.connect(self.deleteblog)
        self.removeblog.setStyleSheet("QPushButton{background-color:#00ffff;"
            "color:black;"
            "border-radius:9%;"
            "padding:1px;"
            "font-size:13px;"
            "font-family:Constantia;}"
            "QPushButton:hover{background-color:#ebf6f7;"
            "border:1px solid gray;}"
            "QPushButton:pressed{background-color:lime}")
        self.removeblog.move(250,190)
        self.removeblog.resize(130,27)
        self.frame.show()
    else:
        self.frame.close()
  def writeknowledleg(self):
    self.blogadd = QDialog(self)
    self.blogadd.resize(600,400)
    ############################
    self.writeblog = QLabel("Wirte Your \n           Knowledge")
    self.bloglayout = QVBoxLayout(self.blogadd)
    self.bloglayout.addWidget(self.writeblog, alignment=Qt.AlignCenter)
    self.writeblog.setStyleSheet("QLabel{color:#45CE30;"
        "font-size:20px;"
        "background-color:transparent;"
        "font-family:Constantia;}")
    self.blogadd.setStyleSheet("background-color:white;")
    ############

    

    self.blogadd.setStyleSheet("QDialog{background-color:rgba(255,255,255, 223);"
            "border:1px solid transparent;"
            "border-radius:8px;"
            "width:400px;"
            "padding-left:100px;"
            "padding-right:100px;"
            "height:40px;}")
    self.blogtitle = QLineEdit(self.blogadd)
    self.blogtitle.setPlaceholderText("Enter Your Blog Title")
    self.blogtitle.setStyleSheet("QLineEdit{"    
        "border:2px inset transparent;"
        "width:500px;"
        "font-family:Constantia;"
        "height:35px;"
        "border-radius:8px;"
        "font-family:Constantia;"
        "font-size:15px;"
        "background-color:white;"
        "margin:5px;}"
        "QLineEdit:hover{border:2px inset #7CEC9F;"
        "background-color:white;"
        "border-color:#7CEC9F;"
        ";}")
    self.blogcontent = QTextEdit(self)
    
    self.blogcontent.setStyleSheet("QTextEdit{"    
        "border:2px inset transparent;"
        "width:500px;"
        "font-family:Constantia;"
        "height:35px;"
        "border-radius:8px;"
        "font-family:Constantia;"
        "font-size:15px;"
        "background-color:white;"
        "margin:5px;}"
        "QTextEdit:hover{border:2px inset #7CEC9F;"
        "background-color:white;"
        "border-color:#7CEC9F;"
        ";}")
    self.submitblog = QPushButton("Submit Your Blog", self)
    
    self.blogcontent.setPlaceholderText("Write Your Blog Content")
    self.submitblog.setStyleSheet("QPushButton{background-color:#00ffff;"
            "color:black;"
            "border-radius:8%;"
            "padding:1px;"
            "width:140px;"
            "height:25px;"
            "font-size:18px;"
            "font-family:Constantia;}"
            "QPushButton:hover{background-color:#ebf6f7;"
            "border:1px solid gray;}"
            "QPushButton:pressed{background-color:lime}")
    self.bloglayout.addWidget(self.blogtitle,alignment=Qt.AlignTop)
    self.bloglayout.addWidget(self.blogcontent)
    self.bloglayout.addWidget(self.submitblog, alignment=Qt.AlignCenter)
    #adding shadow
    self.shadow1 = QGraphicsDropShadowEffect()
    self.shadow1.setBlurRadius(400)
    self.shadow1.setXOffset(10)
    self.shadow1.setYOffset(10)
    self.blogtitle.setGraphicsEffect(self.shadow1)
    self.submitblog.clicked.connect(self.enteryoblog)
    
    
    self.blogadd.exec_()

  def enteryoblog(self):
    entername = self.text1.text()
    blog_data = self.blogcontent.toPlainText()
    header_title = self.blogtitle.text()
    print(entername)
    if blog_data == "" and header_title == "":
        self.msg1 = QMessageBox(self)
        self.msg1.setWindowTitle("Error")
        self.msg1.setText("Blank Vlaue Not Allowed")
        self.msg1.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:red;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:8%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.msg1.exec_()
    else:
        connection = mysql.connector.connect(host="localhost",user="root",passwd="")
        cour = connection.cursor()
        cour.execute("USE information")
        
        # self.list12.addItem(header_title)
        getid = None
        id1 = cour.execute("SELECT * FROM all_info WHERE name='%s'"%(entername))
        for i in cour.fetchall():
            getid = i[0]
        #################################3
        x = datetime.datetime.now()
        cour.execute('''INSERT INTO blog VALUES(%s, %s, %s, %s)''', (getid,header_title,blog_data,x))
        connection.commit()
        self.list12.addItem(header_title)
        self.blogadd.close()
  def getlistitem(self):
    showblogdetils = QDialog()
    showblogdetils.setWindowTitle("Blog Content")
    showblogdetils.setStyleSheet("QDialog{background-color:white;}  "
        "QMenuBar{color:black;"
        "color: rgb(255,255,100);"
        "border:1px solid red;}"
        "QMenuBar::item {"
            "background-color: rgb(49,49,49);"
            "color: rgb(255,255,255)}"
        "QMenuBar::item::selected {"
            "background-color: rgb(30,30,30);"
        "}"
        "QMenu {"
            "background-color: rgb(49,49,49);"
            "color: rgb(255,255,255);"
            "border: 1px solid #000;"           
        "}")
    showblogdetils.resize(600,400)
    self.showauthor = QLabel("")
    self.showauthor.setStyleSheet("QLabel{color:blue;"
        "font-size:13px;"
        "font-family:Georgia;}")
    self.showblogdetilslayout = QVBoxLayout(showblogdetils)
    # self.showblogdetilslayout.setAlignment(Qt.AlignTop)
    self.try1 = QTextBrowser(showblogdetils)
    self.try1.setText("gsdjhfgdfffsdfdfa")
  

    self.try1.setStyleSheet("QTextBrowser{font-size:25px;"
        "font-family:Georgia;"
        "border:1px solid white;}")
    ################
    itme = self.list12.currentItem().text()
    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    
    # self.list12.addItem(header_title)
    getblogcontent = None
    authorid = None
    uploaddate = None
    id1 = cour.execute("SELECT * FROM blog WHERE hader='%s'"%(itme))
    for i in cour.fetchall():
        getblogcontent = i[2]
        authorid = i[0]
        uploaddate = i[3]
    uploaddate = uploaddate.strftime('%Y-%m-%d')
    

    print(authorid)
    #########3
    authorname = None
    authordata = cour.execute("SELECT * FROM all_info WHERE id='%s'"%(authorid))
    for i in cour.fetchall():
        authorname = i[1]
    print(authorname)
    self.showauthor.setText(f"Written By {authorname}")
    ###########################3
    print(getblogcontent)
    getblogcontent = str(getblogcontent)
    ###############################3
    self.showuploaddate = QLabel("", self)
    self.showuploaddate.setText(f"Upload on {uploaddate}")
    self.showuploaddate.setStyleSheet("QLabel{color:blue;"
        "font-size:13px;"
        '''font-family:"Lucida Console", Courier, serif;}''')
    ##########
    self.showblogdetilslayout.addWidget(self.showauthor, alignment=Qt.AlignRight)
    self.showblogdetilslayout.addWidget(self.try1)
    self.showblogdetilslayout.addWidget(self.showuploaddate, alignment=Qt.AlignLeft)
    self.try1.setText(getblogcontent)
    showblogdetils.exec_()
  def Yourwriteblog(self):

    self.showyourblog = QDialog(self)
    self.showyourblog.setWindowTitle("Your Blogs")
    self.showyourblog.setStyleSheet("background-color:white;")
    self.showyourblog.resize(400,400)
    self.addshowlayout = QVBoxLayout(self.showyourblog)
    yourname = self.text1.text()
    # print(yourname)
    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    
    # self.list12.addItem(header_title)
    getid = None
    id1 = cour.execute("SELECT * FROM all_info WHERE name='%s'"%(yourname))
    for i in cour.fetchall():
        getid = i[0]
    print(getid)
    ##another connectyion
    getblogtitle = []
    ##################
    connectiona = mysql.connector.connect(host="localhost",user="root",passwd="")
    coura = connection.cursor()
    coura.execute("USE information")

    title = coura.execute("SELECT * FROM blog WHERE id=%s"%(getid))
    for k in coura.fetchall():
        getblogtitle.append(k[1])
    
    self.yourBlogs = QLabel("Your Written \n      Blogs")
    self.yourBlogs.setStyleSheet("QLabel{font-size:20px;"
        "font-family:Constantia;"
        "color:blue;}")

    print(getblogtitle)
    self.addyourblog = QListWidget()
    self.addyourblog.itemClicked.connect(self.yourblogcontent)
    self.addshowlayout.addWidget(self.yourBlogs, alignment=Qt.AlignCenter)
    self.addshowlayout.addWidget(self.addyourblog)
    self.addyourblog.addItems(getblogtitle)

    self.addyourblog.setStyleSheet("QListWidget{margin-top:7px;border:1px solid transparent;font-size:20px;width:100px;"
        "font-family:Georgia;"
        "margin-left:30px;"
        "margin-right:30px;}"
        "QListWidget::item{"
        "width:40px;"
        "border:2px solid transparent;"
        "border-radius:8px;"
        "font:bold;"
        "margin:3px;"
        "padding:2px;"
        "background-color:white;"
        "color:black;"
        "font-size:30pt;}"
        "QListWidget::item:hover{color:blue;}")
    self.edit = QPushButton("Edit", self.showyourblog)
    self.addshowlayout.addWidget(self.edit,alignment=Qt.AlignRight)
    self.edit.hide()
    self.edit.clicked.connect(self.editblog1)
    self.edit.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:8%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:#EAF0F1;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    self.showyourblog.exec_()
  def yourblogcontent(self):
    self.itme = self.addyourblog.currentItem().text()
    self.edit.show()
  def editblog1(self):
    self.editblog = QDialog(self)
    self.editblog.setWindowTitle("Update Your Blog")
    self.editblog.setStyleSheet("background-color:white;")
    self.editlayout = QVBoxLayout(self.editblog)
    self.edittext = QTextEdit(self)
    self.editblog.resize(500,500)
    self.edittext.setPlaceholderText("Update Your Blog Content")
    self.edittext.setStyleSheet("QTextEdit{font-size:20px;"
        "font-family:Georgia;"
        "border:1px solid white;}")
    self.UpdateButton = QPushButton("Update Blog")
    self.UpdateButton.clicked.connect(self.updatenblog)
    self.UpdateButton.setStyleSheet("QPushButton{background-color:#00ffff;"
        "border-radius:8%;"
        "width:100px;"
        "height:25px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:#EAF0F1;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:lime}")
    self.editlayout.addWidget(self.edittext)
    self.editlayout.addWidget(self.UpdateButton,alignment=Qt.AlignCenter)
    ############################################
    print(self.itme)

    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    
    # self.list12.addItem(header_title)
    getblogcontent = None
  
    id1 = cour.execute("SELECT * FROM blog WHERE hader='%s'"%(self.itme))
    for i in cour.fetchall():
        getblogcontent = i[2]
    print(getblogcontent)
    self.edittext.setText(getblogcontent)
    ##########################
    self.editblog.exec_()

    #####################
  def updatenblog(self):
    textdata = self.edittext.toPlainText()

    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    
    # self.list12.addItem(header_title)
    getblogcontent = None
  
    id1 = cour.execute("SELECT * FROM blog WHERE hader='%s'"%(self.itme))
    for i in cour.fetchall():
        getblogcontent = i[2]
    if textdata == getblogcontent:
        self.nottupdate = QMessageBox(self)
        self.nottupdate.setWindowTitle("Error")
        self.nottupdate.setText("Update Successfully")
        self.nottupdate.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:green;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:8%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.nottupdate.exec_()
        self.editblog.close()
    else:
        cour.execute("UPDATE blog SET data=%s WHERE data=%s", (textdata,getblogcontent))
        connection.commit()
        self.doneupdate = QMessageBox(self)
        self.doneupdate.setWindowTitle("Error")
        self.doneupdate.setText("Update Successfully")
        self.doneupdate.setStyleSheet("QMessageBox{background-color:white;"
            "width:400px;color:white;}"
            "QMessageBox QLabel{background-color:white;color:green;padding-right:100px;"
            "font-size:20px;}"
            "QMessageBox QPushButton{width:100px;"
            "height:30px;"
            "border-radius:8%;}"
            "QMessageBox QPushButton:pressed{background-color:lime;}")
        self.doneupdate.exec_()
        self.editblog.close()
  def deleteblog(self):
    self.delete = QDialog()
    self.delete.resize(400,400)
    self.delete.setWindowTitle("Delete Blog")
    self.delete.setStyleSheet("background-color:white")
    self.deletelayut = QVBoxLayout(self.delete)
    #################################
    name = self.text1.text()
    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    
    # self.list12.addItem(header_title)
    getnameid = None
    #########################33
    id1 = cour.execute("SELECT * FROM all_info WHERE name='%s'"%(name))
    for i in cour.fetchall():
        getnameid = i[0]
    print(getnameid)
    ################33
    title1 = []
    getheader = cour.execute("SELECT * FROM blog WHERE id=%s"%(getnameid))
    for k in cour.fetchall():
        title1.append(k[1])
    #########################
    self.addtitle = QLabel("       Which Blog \nYou Want To Delete")
    self.addtitle.setStyleSheet("QLabel{font-size:20px;"
        "font-family:Constantia;"
        "color:#FFF222;}")
    ####################3
    self.addinglist = QListWidget()
    self.addinglist.itemClicked.connect(self.remove)
    self.addinglist.addItems(title1)
    self.addinglist.setStyleSheet("QListWidget{margin-top:7px;border:1px solid transparent;font-size:20px;width:100px;"
        "font-family:Georgia;"
        "margin-left:30px;"
        "margin-right:30px;}"
        "QListWidget::item{"
        "width:40px;"
        "border:2px solid transparent;"
        "border-radius:8px;"
        "font:bold;"
        "margin:3px;"
        "padding:2px;"
        "background-color:white;"
        "color:black;"
        "font-size:30pt;}"
        "QListWidget::item:hover{color:blue;}")

    self.deletebutton = QPushButton("Delete Blog",self)
    self.deletebutton.setStyleSheet("QPushButton{background-color:#EAF0F1;"
        "border-radius:10%;"
        "width:100px;"
        "height:27px;"
        "font-size:12px;"
        "font-family:Constantia;}"
        "QPushButton:hover{background-color:white;"
        "border:1px solid gray;}"
        "QPushButton:pressed{background-color:#67E6DC;"
        ";}")
    self.deletebutton.hide()
    self.deletebutton.clicked.connect(self.removeselectdblog)
    self.deletelayut.addWidget(self.addtitle, alignment=Qt.AlignCenter)
    self.deletelayut.addWidget(self.addinglist)
    self.deletelayut.addWidget(self.deletebutton, alignment=Qt.AlignRight)
    
    # dletet = cour.execute('''DELETE FROM blog WHERE hader='%s' '''% (new))
    # connection.commit()
    self.delete.exec_()
  def remove(self):
    self.deletebutton.show()
  def removeselectdblog(self):
    dataofblog = self.addinglist.currentItem().text()
    self.delete.close()
    ####################
    connection = mysql.connector.connect(host="localhost",user="root",passwd="")
    cour = connection.cursor()
    cour.execute("USE information")
    print(dataofblog)
    ###############################
    cour.execute("SELECT * FROM blog")
    comparelist = cour.fetchall()

    check_list = []
    for i in comparelist:
        check_list.append(i[1])
    print(check_list)
    #finding a index
    getindex = check_list.index(dataofblog)
    removeindex = self.list12.takeItem(getindex)
    dletet = cour.execute('''DELETE FROM blog WHERE hader='%s' '''% (dataofblog))
    connection.commit()
    
Winodw = QApplication(sys.argv)
App = Main()
sys.exit(Winodw.exec_())