#-*- coding: cp1254 -*-
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os
import time
import datetime
import RPi.GPIO as GPIO
import string

app 	= QApplication(sys.argv)
pencere=QWidget()
table 	= QTableWidget()
tableItem   = QTableWidgetItem()
btnR1=QPushButton()
btnR1.setText("1. Röle")
btnR2=QPushButton()
btnR2.setText("2. Röle")
btnR3=QPushButton()
btnR3.setText("3. Röle")
btnR4=QPushButton()
btnR4.setText("4. Röle")
txtR1=QTextEdit()
txtR1.setText("")
txtR2=QTextEdit()
txtR2.setText("")
txtR3=QTextEdit()
txtR3.setText("")
txtR4=QTextEdit()
txtR4.setText("")

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
 
#R1=21,R2=22,R3=23,R4=24
Pinler=[21,22,23,24]
#Pinleri sırasıyla output modunda ayarladık ve sıfırladık
for pin in Pinler:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, 0)

#Belirtilen pini, verilen süre kadar aktif yapan metod
def degerGonder(pin,sure):
    GPIO.output(pin, 1)
    time.sleep(sure)       
    GPIO.output(pin, 0)
    btnR1.setStyleSheet("background-color:#d3d3d3")
    btnR2.setStyleSheet("background-color:#d3d3d3")
    btnR3.setStyleSheet("background-color:#d3d3d3")
    btnR4.setStyleSheet("background-color:#d3d3d3")
    txtR1.setText("")
    txtR2.setText("")
    txtR3.setText("")
    txtR4.setText("")
    return

#Butona tıklandığında TextBox'dan gelen değer 1000'den büyükse ilgili pine değer 1000'e bölünerek gönderiliyor
def btnR1Clicked():    
    if (txtR1.toPlainText() == ""):
        txtR1.setText("Bos Deger")     
    elif (int(txtR1.toPlainText())>=1000):
        degerGonder(21,int(txtR1.toPlainText()) / 1000.0)
    else:
        txtR1.setText(">1000 olmali")
def btnR2Clicked():     
    if (txtR2.toPlainText() == ""):
        txtR2.setText("Bos Deger")
    elif (int(txtR2.toPlainText())>=1000):
        degerGonder(22,int(txtR2.toPlainText()) / 1000.0)
    else:
        txtR3.setText(">1000 olmali")
def btnR3Clicked():     
    if (txtR3.toPlainText() == ""):
        txtR3.setText("Bos Deger")
    elif (int(txtR3.toPlainText())>=1000):
        degerGonder(23,int(txtR3.toPlainText()) / 1000.0)
    else:
        txtR3.setText(">1000 olmali")
def btnR4Clicked():     
    if (txtR4.toPlainText() == ""):
        txtR4.setText("Bos Deger")
    elif (int(txtR4.toPlainText())>=1000):
        degerGonder(24,int(txtR4.toPlainText()) / 1000.0)
    else:
        txtR4.setText(">1000 olmali")
#TextBox içerisine değer girildiğinde buton rengi değiştiriliyor
def txtR1Changed():     
    if (txtR1.toPlainText() != ""):
        btnR1.setStyleSheet("background-color:darkGray")
    else:
        btnR1.setStyleSheet("background-color:lightGray")
def txtR2Changed():     
    if (txtR2.toPlainText() != ""):
        btnR2.setStyleSheet("background-color:darkGray")
    else:
        btnR2.setStyleSheet("background-color:lightGray")
def txtR3Changed():     
    if (txtR3.toPlainText() != ""):
        btnR3.setStyleSheet("background-color:darkGray")
    else:
        btnR3.setStyleSheet("background-color:lightGray")
def txtR4Changed():     
    if (txtR4.toPlainText() != ""):
        btnR4.setStyleSheet("background-color:darkGray")
    else:
        btnR4.setStyleSheet("background-color:lightGray")

def main(args):
    pencere.setWindowTitle(u'TURTA RÖLE KONTROLU - '+ time.strftime("%d/%m/%Y"))

    screen_rect = app.desktop().screenGeometry()
    #490x150 boyutlarında 2 satır 4 sütunluk bir tablo oluşturduk
    table.resize(490, 150)    
    table.setRowCount(2)
    table.setColumnCount(4)
    
    #Satır yüksekliklerini ve sütun genişliklerini ayarladık
    table.setColumnWidth(0,100);
    table.setColumnWidth(1,130);
    table.setColumnWidth(2,130);
    table.setRowHeight(0,60);
    table.setRowHeight(1,60);    

    #satır ve sütun başlıklarını gizledik
    table.horizontalHeader().setVisible(False)
    table.verticalHeader().setVisible(False)

    font = QFont("Arial", 12)
    table.setFont(font);

    #buton kontrolünün boyutlarını belirledik
    btnR1.setGeometry(100,10, 100, 100)
    btnR2.setGeometry(100,10, 100, 100)
    btnR3.setGeometry(100,10, 100, 100)
    btnR4.setGeometry(100,10, 100, 100)
    #buton kontrolünü tablo içerisinde belirtilen satır ve sütun konumuna yerleştirdik
    table.setCellWidget(1,0, btnR1)
    table.setCellWidget(1,1, btnR2)
    table.setCellWidget(1,2, btnR3)
    table.setCellWidget(1,3, btnR4)

    #TextBox kontrolünün boyutlarını belirledik
    txtR1.setGeometry(100,10, 100, 100)
    txtR2.setGeometry(100,10, 100, 100)
    txtR3.setGeometry(100,10, 100, 100)
    txtR4.setGeometry(100,10, 100, 100)
    #TextBox kontrolünü tablo içerisinde belirtilen satır ve sütun konumuna yerleştirdik
    table.setCellWidget(0,0, txtR1)
    table.setCellWidget(0,1, txtR2)    
    table.setCellWidget(0,2, txtR3)
    table.setCellWidget(0,3, txtR4)

    #Buton ve TextBox'ların olaylarına ilgili metodları bağladık
    btnR1.clicked.connect(btnR1Clicked)
    btnR2.clicked.connect(btnR2Clicked)
    btnR3.clicked.connect(btnR3Clicked)
    btnR4.clicked.connect(btnR4Clicked)
    txtR1.textChanged.connect(txtR1Changed)
    txtR2.textChanged.connect(txtR2Changed)
    txtR3.textChanged.connect(txtR3Changed)
    txtR4.textChanged.connect(txtR4Changed)
    
    table.show()

    #Kontrollerimizin boyutunun yatay ya da dikey olarak otomatik olarak hizalanması amacıyla kullanılan QGridLayout kontrolünü oluşturuyor
    #Tablomuzu bu layout içerisine ekliyoruz.
    izgara=QGridLayout()
    izgara.addWidget(table,0,0)       
    pencere.setLayout(izgara)
    pencere.resize(490, 150)
    pencere.showNormal() 
    
    return app.exec_()


if __name__ == '__main__':    
     main(sys.argv)
