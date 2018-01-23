# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Admin.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import csv
from random import *
import os
def appendsym(sym):

    newsym=[]
    existingid=[]
    with open("sym.csv","r") as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            existingid.append(line[0])
    newsymid=randint(1,1000)
    while str(newsymid) in existingid:
        newsymid=randint(1,1000)

    newsym.append(newsymid)
    newsym.append(sym)
    with open("sym.csv","a") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(newsym)

    return newsymid



def appenddis(dis,typ,spec):
    newdis=[]
    existingid=[]

    with open("dia.csv","r") as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            existingid.append(line[0])
    newdid=randint(1,5000)
    while str(newdid) in existingid:
        newdid=randint(1,5000)

    newdis.append(newdid)
    newdis.append(dis)
    newdis.append(typ)
    newdis.append(spec)

    with open("dia.csv","a") as csvfile:
        writer=csv.writer(csvfile)
        writer.writerow(newdis)

    return newdid

def symvdis(symid,disid,acc):
    rowlength,counter=0,0
    matrix=[]
    with open("sym_dis_matrix.csv","r") as csvfile:
        reader=csv.reader(csvfile)
        for line in reader:
            counter+=1
            if counter==1:
                line.append(disid)
            else:
                line.append(0)
            l=[]
            l=line
            matrix.append(l)
            rowlength=len(l)

    with open("sym_dis_matrix.csv","w") as csvfile:
        writer=csv.writer(csvfile)
        for row in matrix:
            writer.writerow(row)

    with open("sym_dis_matrix.csv","a") as csvfile:
        writer=csv.writer(csvfile)
        row=[]
        row.append(symid)
        for i in range(rowlength-2):
            row.append(0)
        row.append(acc)
        writer.writerow(row)



try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Admin(object):
    def setupUi(self, Admin):
        Admin.setObjectName(_fromUtf8("Admin"))
        Admin.setGeometry(0, 0, 827, 557)
        Admin.setMinimumSize(QtCore.QSize(827, 557))
        Admin.setMaximumSize(QtCore.QSize(827, 557))
        self.centralwidget = QtGui.QWidget(Admin)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 280, 731, 191))
        self.formLayoutWidget.setObjectName(_fromUtf8("formLayoutWidget"))
        self.formLayout = QtGui.QFormLayout(self.formLayoutWidget)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setMargin(0)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.symptomslineedit = QtGui.QLineEdit(self.formLayoutWidget)
        self.symptomslineedit.setObjectName(_fromUtf8("symptomslineedit"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.symptomslineedit)
        self.label_2 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.diseaselineedit = QtGui.QLineEdit(self.formLayoutWidget)
        self.diseaselineedit.setObjectName(_fromUtf8("diseaselineedit"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.diseaselineedit)
        self.label_3 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.label_3)
        self.occurrence = QtGui.QLineEdit(self.formLayoutWidget)
        self.occurrence.setObjectName(_fromUtf8("occurrence"))
        self.formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.occurrence)
        self.label_4 = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_4)
        self.type = QtGui.QLineEdit(self.formLayoutWidget)
        self.type.setObjectName(_fromUtf8("type"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.type)
        self.doctor = QtGui.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.doctor.setFont(font)
        self.doctor.setObjectName(_fromUtf8("doctor"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.doctor)
        self.type_2 = QtGui.QLineEdit(self.formLayoutWidget)
        self.type_2.setObjectName(_fromUtf8("type_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.type_2)
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(-120, 0, 1131, 221))
        self.label_13.setText(_fromUtf8(""))
        self.label_13.setPixmap(QtGui.QPixmap(_fromUtf8("../../Python/Python3/background.jpg")))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setEnabled(False)
        self.label_14.setGeometry(QtCore.QRect(190, 150, 441, 71))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 9, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 7, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 4, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 9, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 7, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 4, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(13, 9, 54))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(11, 7, 45))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(6, 4, 24))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(4, 3, 18))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(9, 6, 36))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        self.label_14.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAutoFillBackground(True)
        self.label_14.setFrameShape(QtGui.QFrame.Box)
        self.label_14.setFrameShadow(QtGui.QFrame.Plain)
        self.label_14.setLineWidth(5)
        self.label_14.setAlignment(QtCore.Qt.AlignCenter)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.submitbutton = QtGui.QPushButton(self.centralwidget)
        self.submitbutton.setGeometry(QtCore.QRect(330, 480, 181, 28))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.submitbutton.setFont(font)
        self.submitbutton.setObjectName(_fromUtf8("submitbutton"))
        Admin.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(Admin)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        Admin.setStatusBar(self.statusbar)

        self.retranslateUi(Admin)
        QtCore.QMetaObject.connectSlotsByName(Admin)
        self.submitbutton.clicked.connect(self.button_click)

        
        #QtCore.QCoreApplication.instance().quit()

    def button_click(self):
        
        symdata=self.symptomslineedit.text()
        disdata=self.diseaselineedit.text()
        typ=self.type.text()
        acc=self.occurrence.text()
        spec=self.type_2.text()
        if symdata != "" and disdata != "" and typ != "" and acc != "" and spec != "":
            symid=appendsym(symdata)
            disid=appenddis(disdata,typ,spec)
            symvdis(symid,disid,acc)


    def retranslateUi(self, Admin):
        Admin.setWindowTitle(_translate("Admin", "Admin", None))
        self.label.setText(_translate("Admin", "SYMPTOMS :", None))
        self.label_2.setText(_translate("Admin", "DISEASE :", None))
        self.label_3.setText(_translate("Admin", "OCCURRENCE:(1-5)", None))
        self.label_4.setText(_translate("Admin", "TYPE:", None))
        self.doctor.setText(_translate("Admin", "SPECIALIST DETAILS:", None))
        self.label_14.setText(_translate("Admin", "<html><head/><body><p><span style=\" color:#00aaff;\">Health Prediction</span></p></body></html>", None))
        self.submitbutton.setText(_translate("Admin", "STORE DETAILS", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Admin = QtGui.QMainWindow()
    ui = Ui_Admin()
    ui.setupUi(Admin)
    Admin.show()
    sys.exit(app.exec_())

