from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import json, os

from main import Ui_mw_Main
from AboutMe import Ui_mw_AboutMe

import webbrowser
import openpyxl
from Connection import Connection
import pandas as pd
from datetime import datetime

class BulletinSearch(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui = Ui_mw_Main()
        self.ui.setupUi(self)

        self.AboutMePage = QMainWindow()
        self.Abui = Ui_mw_AboutMe()
        self.Abui.setupUi(self.AboutMePage)

        self.SaveJson = "Settings.json"
        self.SaveDir = "./" + self.SaveJson
        self.JsonLayout = {}

        self.data = []

        self.Load()
        self.ActionButton()

    def GetAboutMePage(self):
        self.AboutMePage.show()

    def Load(self):
        if os.path.exists(self.SaveDir):
            with open(self.SaveDir,"r") as json_data:
                self.JsonLayout = json.load(json_data)

            if "Settings" in self.JsonLayout:
                if "DBPath" in self.JsonLayout["Settings"]:
                    dbPath = self.JsonLayout["Settings"]["DBPath"]
                    if dbPath != "":
                        if os.path.exists(dbPath):
                            self.ui.le_dbPath.setText(dbPath)

                if "ExcelPath" in self.JsonLayout["Settings"]:
                    excelPath = self.JsonLayout["Settings"]["ExcelPath"]
                    if excelPath != "":
                        if os.path.exists(excelPath):
                            self.ui.le_excelPath.setText(excelPath)
                            self.GetExcelContents(excelPath)

    def Save(self):
        self.JsonLayout.clear()
        self.JsonLayout["Settings"] = {}
        dbPath = self.ui.le_dbPath.text()
        excelPath = self.ui.le_excelPath.text()
        self.JsonLayout["Settings"]["DBPath"] = dbPath
        self.JsonLayout["Settings"]["ExcelPath"] = excelPath

        with open(self.SaveDir, "w") as json_data:
            json.dump(self.JsonLayout, json_data, indent=4)

    def ActionButton(self):
        button_action = QAction("Hakkımda", self)
        button_action.triggered.connect(self.GetAboutMePage)
        self.ui.toolBar.addAction(button_action)

        self.ui.tb_dbPath.clicked.connect(self.GetDBPath)
        self.ui.tb_excelPath.clicked.connect(self.GetExcelPath)
        self.ui.pb_excelConnect.clicked.connect(self.excelConnect)
        self.ui.pb_startSearch.clicked.connect(self.Start)
        self.ui.pb_extractExcel.clicked.connect(self.ExtractExcel)

        self.Abui.label.mousePressEvent = self.goLink

    def goLink(self, event):
        chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
        webbrowser.get(chrome_path).open('https://github.com/Ezentere')
            
    def CreateMessageBox(self, message, title="UYARI", buttons=(QMessageBox.Ok | QMessageBox.Cancel)):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(message)
        msg.setWindowTitle(title)
        msg.setStandardButtons(buttons)
        retval = msg.exec_()
        return retval

    def GetDBPath(self):
        file = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.le_dbPath.setText(file)
        self.Save()

    def GetExcelPath(self):
        file = QFileDialog.getOpenFileName(self, "Select File", "", "Excel Files (*.xlsx)")
        self.ui.le_excelPath.setText(file[0])
        self.Save()

    def excelConnect(self):
        excelPath = self.ui.le_excelPath.text()
        if excelPath == "":
            self.CreateMessageBox("Excel Yolu Belirtilmemiş...", title="Hata", buttons=QMessageBox.Ok)
        else:
            if os.path.exists(excelPath):
                self.GetExcelContents(excelPath)
            else:
                self.CreateMessageBox("Excel Yolu Bulunamadı...", title="Hata", buttons=QMessageBox.Ok)

    def GetExcelContents(self, excelPath):
        try:
            excel = openpyxl.load_workbook(excelPath)
            sheet = excel.active
            self.ui.lw_excel.clear()
            for row in sheet.iter_rows():
                for cell in row:
                    self.ui.lw_excel.addItem(cell.value)
            print("işlem tamam")
        except:
            self.CreateMessageBox("Excel Dosyasını Açık Durumda\nLütfen Excel Dosyasını Kapatınız...", title="Hata", buttons=QMessageBox.Ok)


    def Start(self):
        path = self.ui.le_dbPath.text()
        if path == "":
            self.CreateMessageBox("Veritabanı Yolu Belirtilmemiş...", title="Hata", buttons=QMessageBox.Ok)
        else:
            if os.path.exists(f"{path}/hsqldb.jar"):
                self.ui.pte_results.clear()
                self.data = []
                conn = Connection(path)
                searchList = []
                for i in range(self.ui.lw_excel.count()):
                    old_item = self.ui.lw_excel.item(i).text()
                    item = '%'+old_item+'%'

                    searchList.append((item,))

                    results = conn.querys("SELECT * FROM TRADEMARK WHERE NAME LIKE ?", (item,))
                    # print(f"'{old_item}' kelimesi aranıyor...")
                    # self.ui.pte_results.appendPlainText(f"'{old_item}' kelimesi aranıyor...")
                    # print(f"{len(results)} adet '{old_item}' kelimesine rastlandı;")
                    self.ui.pte_results.appendPlainText(f"{len(results)} adet '{old_item}' kelimesine rastlandı...")
                    for i, result in enumerate(results):
                        # print(f"{i+1}) {result[0]} - {result[5]}")
                        # self.ui.pte_results.appendPlainText(f"{i+1}) {result[0]} - {result[5]}")
                        self.data.append([old_item,result[0],result[5]])
                    # print("-----------------------------------------------------")
                    # self.ui.pte_results.appendPlainText("-----------------------------------------------------")
                    
            else:
                self.CreateMessageBox("HSQLDB driver bulunamadı.", title="Hata", buttons=QMessageBox.Ok)

    def ExtractExcel(self):
        if len(self.data) != 0:
            file = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx)")
            if file[0] != "":
                df = pd.DataFrame(self.data, columns=["ARANAN","BAŞVURU NO", "MARKA"])
                try:
                    writer = pd.ExcelWriter(file[0], engine='xlsxwriter')
                    df.to_excel(writer, sheet_name='SONUCLAR', encoding='utf-8', index=False)  # send df to writer
                    worksheet = writer.sheets['SONUCLAR']
                    for idx, col in enumerate(df): 
                        series = df[col]
                        max_len = max((
                            series.astype(str).map(len).max(),
                            len(str(series.name)) 
                            )) + 1 
                        if max_len < 8:
                            max_len = 8
                        worksheet.set_column(idx, idx, max_len)
                    writer.save()
                    self.CreateMessageBox("Excel Dosyası Başarıyla Oluşturuldu...", title="Bilgi", buttons=QMessageBox.Ok)
                    self.data.clear()
                except Exception as e:
                    if str(e).find("Permission denied") != -1:
                        self.CreateMessageBox("Excel Dosyası Açık Durumda...", title="Hata", buttons=QMessageBox.Ok)
                    else:
                        self.CreateMessageBox("Excel Dosyası Oluşturulurken Hata Oluştu...", title="Hata", buttons=QMessageBox.Ok)
                        with open("log.txt", "a") as log:
                            log.writelines(str(datetime.now()) + ": " + str(e) + "\n")
        else:
            self.CreateMessageBox("Sonuç Bulunamadı...", title="Hata", buttons=QMessageBox.Ok)
        
    def closeEvent(self, event):
        if self.AboutMePage.isVisible():
            self.AboutMePage.close()

def main():
	app = QApplication([])
	app.setStyle("Vista")
	ui = BulletinSearch()
	ui.show()
	app.exec_()

if __name__ == '__main__':
    main()