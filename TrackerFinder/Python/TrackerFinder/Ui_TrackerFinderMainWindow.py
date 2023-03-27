# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TrackerFinderMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TrackerFinderMainWindow(object):
    def setupUi(self, TrackerFinderMainWindow):
        TrackerFinderMainWindow.setObjectName("TrackerFinderMainWindow")
        TrackerFinderMainWindow.resize(414, 362)
        self.centralwidget = QtWidgets.QWidget(TrackerFinderMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setObjectName("label_12")
        self.verticalLayout.addWidget(self.label_12)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.pingId = QtWidgets.QLineEdit(self.centralwidget)
        self.pingId.setReadOnly(True)
        self.pingId.setObjectName("pingId")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pingId)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.pingLat = QtWidgets.QLineEdit(self.centralwidget)
        self.pingLat.setReadOnly(True)
        self.pingLat.setObjectName("pingLat")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pingLat)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.pingLon = QtWidgets.QLineEdit(self.centralwidget)
        self.pingLon.setReadOnly(True)
        self.pingLon.setObjectName("pingLon")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.pingLon)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.pingAge = QtWidgets.QLineEdit(self.centralwidget)
        self.pingAge.setReadOnly(True)
        self.pingAge.setObjectName("pingAge")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.pingAge)
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.pingCount = QtWidgets.QLineEdit(self.centralwidget)
        self.pingCount.setReadOnly(True)
        self.pingCount.setObjectName("pingCount")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.pingCount)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setFrame(False)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setEnabled(True)
        self.lineEdit_2.setFrame(False)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setObjectName("label_16")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.pingDeltaT = QtWidgets.QLineEdit(self.centralwidget)
        self.pingDeltaT.setReadOnly(True)
        self.pingDeltaT.setObjectName("pingDeltaT")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.pingDeltaT)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setObjectName("label_17")
        self.horizontalLayout.addWidget(self.label_17)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setObjectName("label_18")
        self.horizontalLayout.addWidget(self.label_18)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.aprsTag = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsTag.setReadOnly(True)
        self.aprsTag.setObjectName("aprsTag")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.aprsTag)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.aprsLat = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsLat.setReadOnly(True)
        self.aprsLat.setObjectName("aprsLat")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.aprsLat)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.aprsLon = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsLon.setReadOnly(True)
        self.aprsLon.setObjectName("aprsLon")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.aprsLon)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.aprsTime = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsTime.setReadOnly(True)
        self.aprsTime.setObjectName("aprsTime")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.aprsTime)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.aprsCount = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsCount.setReadOnly(True)
        self.aprsCount.setObjectName("aprsCount")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.aprsCount)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.aprsFailed = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsFailed.setReadOnly(True)
        self.aprsFailed.setObjectName("aprsFailed")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.aprsFailed)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.aprsAlt = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsAlt.setReadOnly(True)
        self.aprsAlt.setObjectName("aprsAlt")
        self.formLayout_2.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.aprsAlt)
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setObjectName("label_15")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.aprsDeltaT = QtWidgets.QLineEdit(self.centralwidget)
        self.aprsDeltaT.setReadOnly(True)
        self.aprsDeltaT.setObjectName("aprsDeltaT")
        self.formLayout_2.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.aprsDeltaT)
        self.verticalLayout_2.addLayout(self.formLayout_2)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        TrackerFinderMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TrackerFinderMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 22))
        self.menubar.setObjectName("menubar")
        TrackerFinderMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TrackerFinderMainWindow)
        self.statusbar.setObjectName("statusbar")
        TrackerFinderMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(TrackerFinderMainWindow)
        QtCore.QMetaObject.connectSlotsByName(TrackerFinderMainWindow)

    def retranslateUi(self, TrackerFinderMainWindow):
        _translate = QtCore.QCoreApplication.translate
        TrackerFinderMainWindow.setWindowTitle(_translate("TrackerFinderMainWindow", "MainWindow"))
        self.label_12.setText(_translate("TrackerFinderMainWindow", "Ping"))
        self.label.setText(_translate("TrackerFinderMainWindow", "ID"))
        self.label_3.setText(_translate("TrackerFinderMainWindow", "Lat"))
        self.label_4.setText(_translate("TrackerFinderMainWindow", "Lon"))
        self.label_2.setText(_translate("TrackerFinderMainWindow", "Age"))
        self.label_14.setText(_translate("TrackerFinderMainWindow", "Count"))
        self.label_16.setText(_translate("TrackerFinderMainWindow", "DeltaT"))
        self.label_17.setText(_translate("TrackerFinderMainWindow", " "))
        self.label_18.setText(_translate("TrackerFinderMainWindow", " "))
        self.label_13.setText(_translate("TrackerFinderMainWindow", "APRS"))
        self.label_5.setText(_translate("TrackerFinderMainWindow", "Tag"))
        self.label_6.setText(_translate("TrackerFinderMainWindow", "Lat"))
        self.label_7.setText(_translate("TrackerFinderMainWindow", "Lon"))
        self.label_11.setText(_translate("TrackerFinderMainWindow", "Time"))
        self.label_8.setText(_translate("TrackerFinderMainWindow", "Count"))
        self.label_9.setText(_translate("TrackerFinderMainWindow", "Failed"))
        self.label_10.setText(_translate("TrackerFinderMainWindow", "Alt"))
        self.label_15.setText(_translate("TrackerFinderMainWindow", "DeltaT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrackerFinderMainWindow = QtWidgets.QMainWindow()
    ui = Ui_TrackerFinderMainWindow()
    ui.setupUi(TrackerFinderMainWindow)
    TrackerFinderMainWindow.show()
    sys.exit(app.exec_())
