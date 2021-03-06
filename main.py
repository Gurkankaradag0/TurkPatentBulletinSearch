# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mw_Main(object):
    def setupUi(self, mw_Main):
        mw_Main.setObjectName("mw_Main")
        mw_Main.resize(590, 490)
        mw_Main.setMinimumSize(QtCore.QSize(590, 490))
        mw_Main.setMaximumSize(QtCore.QSize(590, 490))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/favicon/images/favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        mw_Main.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(mw_Main)
        self.centralwidget.setObjectName("centralwidget")
        self.gb_Settings = QtWidgets.QGroupBox(self.centralwidget)
        self.gb_Settings.setGeometry(QtCore.QRect(10, 10, 361, 180))
        self.gb_Settings.setObjectName("gb_Settings")
        self.formLayoutWidget = QtWidgets.QWidget(self.gb_Settings)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 72))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lbl_excelPath = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_excelPath.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_excelPath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_excelPath.setObjectName("lbl_excelPath")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lbl_excelPath)
        self.lbl_dbPath = QtWidgets.QLabel(self.formLayoutWidget)
        self.lbl_dbPath.setMinimumSize(QtCore.QSize(0, 30))
        self.lbl_dbPath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.lbl_dbPath.setObjectName("lbl_dbPath")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lbl_dbPath)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_dbPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_dbPath.setMinimumSize(QtCore.QSize(0, 30))
        self.le_dbPath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.le_dbPath.setObjectName("le_dbPath")
        self.horizontalLayout.addWidget(self.le_dbPath)
        self.tb_dbPath = QtWidgets.QToolButton(self.formLayoutWidget)
        self.tb_dbPath.setMinimumSize(QtCore.QSize(30, 30))
        self.tb_dbPath.setMaximumSize(QtCore.QSize(30, 30))
        self.tb_dbPath.setObjectName("tb_dbPath")
        self.horizontalLayout.addWidget(self.tb_dbPath)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.le_excelPath = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.le_excelPath.setMinimumSize(QtCore.QSize(0, 30))
        self.le_excelPath.setMaximumSize(QtCore.QSize(16777215, 30))
        self.le_excelPath.setObjectName("le_excelPath")
        self.horizontalLayout_2.addWidget(self.le_excelPath)
        self.tb_excelPath = QtWidgets.QToolButton(self.formLayoutWidget)
        self.tb_excelPath.setMinimumSize(QtCore.QSize(30, 30))
        self.tb_excelPath.setMaximumSize(QtCore.QSize(30, 30))
        self.tb_excelPath.setObjectName("tb_excelPath")
        self.horizontalLayout_2.addWidget(self.tb_excelPath)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.pb_excelConnect = QtWidgets.QPushButton(self.gb_Settings)
        self.pb_excelConnect.setGeometry(QtCore.QRect(10, 100, 341, 30))
        self.pb_excelConnect.setMinimumSize(QtCore.QSize(0, 30))
        self.pb_excelConnect.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pb_excelConnect.setObjectName("pb_excelConnect")
        self.pb_startSearch = QtWidgets.QPushButton(self.gb_Settings)
        self.pb_startSearch.setGeometry(QtCore.QRect(10, 140, 341, 30))
        self.pb_startSearch.setMinimumSize(QtCore.QSize(0, 30))
        self.pb_startSearch.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pb_startSearch.setObjectName("pb_startSearch")
        self.lw_excel = QtWidgets.QListWidget(self.centralwidget)
        self.lw_excel.setGeometry(QtCore.QRect(380, 10, 200, 180))
        self.lw_excel.setFocusPolicy(QtCore.Qt.NoFocus)
        self.lw_excel.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.lw_excel.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.lw_excel.setObjectName("lw_excel")
        self.pte_results = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.pte_results.setGeometry(QtCore.QRect(10, 200, 570, 221))
        self.pte_results.setFocusPolicy(QtCore.Qt.NoFocus)
        self.pte_results.setAcceptDrops(False)
        self.pte_results.setReadOnly(True)
        self.pte_results.setObjectName("pte_results")
        self.pb_extractExcel = QtWidgets.QPushButton(self.centralwidget)
        self.pb_extractExcel.setGeometry(QtCore.QRect(10, 430, 571, 30))
        self.pb_extractExcel.setMinimumSize(QtCore.QSize(0, 30))
        self.pb_extractExcel.setMaximumSize(QtCore.QSize(16777215, 30))
        self.pb_extractExcel.setObjectName("pb_extractExcel")
        mw_Main.setCentralWidget(self.centralwidget)
        self.toolBar = QtWidgets.QToolBar(mw_Main)
        self.toolBar.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.toolBar.setMovable(False)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolBar.setObjectName("toolBar")
        mw_Main.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(mw_Main)
        QtCore.QMetaObject.connectSlotsByName(mw_Main)

    def retranslateUi(self, mw_Main):
        _translate = QtCore.QCoreApplication.translate
        mw_Main.setWindowTitle(_translate("mw_Main", "B??lten Arama"))
        self.gb_Settings.setTitle(_translate("mw_Main", "Ayarlar"))
        self.lbl_excelPath.setText(_translate("mw_Main", "Excel Yolu:"))
        self.lbl_dbPath.setText(_translate("mw_Main", "Veritaban?? Yolu:"))
        self.tb_dbPath.setText(_translate("mw_Main", "..."))
        self.tb_excelPath.setText(_translate("mw_Main", "..."))
        self.pb_excelConnect.setText(_translate("mw_Main", "Excel ????eri??ini Getir"))
        self.pb_startSearch.setText(_translate("mw_Main", "Aramay?? Ba??lat"))
        self.pb_extractExcel.setText(_translate("mw_Main", "Excel ????kt??s?? Al"))
        self.toolBar.setWindowTitle(_translate("mw_Main", "toolBar"))
import images_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mw_Main = QtWidgets.QMainWindow()
    ui = Ui_mw_Main()
    ui.setupUi(mw_Main)
    mw_Main.show()
    sys.exit(app.exec_())
