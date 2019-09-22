from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMainWindow, QDialog, QFileDialog, QComboBox, QPlainTextEdit, QLineEdit, QDateEdit, QTableWidgetItem, QTableWidget,QMessageBox
from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QActionEvent
from typing import List
import PyQt5.QtSql
import os
import sys
import shutil
import mainUI, detailsUI, editUI, tableUI, filterUI
import sqlite3
import uuid
import pickle
from config import STORAGE, CARS_LIST, SUBSYSTEMS_LIST

'''
cd C:\\Users\\Caitlin\\Documents\\repositories\\personal code\
baja_database\\src
use 'pyuic5 filename.ui -o filename.py' to convert UI files
"C:\\Users\\Caitlin\\Documents\\repositories\\personal code\\baja_database\\testing storage"
'''

CONNECTION = sqlite3.connect('baja_data.db')
DB_COLS = ["dataID", "name", "date", "car", "collector", "subsystem", "project", "tags", "description", "files"]


def strToList(tags):
    tagsShort = []
    for tag in tags.split(','):
        tagsShort.append(tag.strip())
    return tagsShort

def shortFileNames(files):
    filesShort = []
    for file in files:
        splitStr = file.split('/')[-1]
        filesShort.append(splitStr.split('\\')[-1])

    return filesShort


def getShortName(file):
    splitStr = file.split('/')[-1]
    return(splitStr.split('\\')[-1])


def listToStr(files):
    return ', '.join(files)

def checkStorage():
    if not os.path.isdir(STORAGE):
        return(False)
    else:
        folders = []
        for _, dirs, _ in os.walk(STORAGE):
            for name in dirs:
                folders.append(name)
        for system in SUBSYSTEMS_LIST:
            if system not in folders:
                os.mkdir(os.path.join(STORAGE, system))
        return(True)

class MainApp(QMainWindow, mainUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self.addBtn.clicked.connect(self.addData)
        self.viewBtn.clicked.connect(self.viewData)

        self.setUpDatabase()
        if not checkStorage():
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Storage Path Error")
            msg.setText("ERROR: Please check the path to the data storage directory")
            msg.exec_()
            sys.exit()


    def addData(self):
        dialog = EditWindow()
        dialog.show()
        dialog.exec_()


    def viewData(self):
        dialog = TableWindow()
        dialog.show()
        dialog.exec_()


    def setUpDatabase(self):
        #C:\Users\Caitlin\Documents\repositories\personal code\baja_database\src\baja_data.db

        cursor = CONNECTION.cursor()
        cursor.execute("""CREATE TABLE if not exists "baja_data_table" (
                    "dataID"        TEXT,
                    "name"          TEXT NOT NULL,
                    "date"          TEXT NOT NULL,
                    "car"           TEXT,
                    "collector"     TEXT,
                    "subsystem"     TEXT NOT NULL,
                    "project"       TEXT,
                    "tags"          TEXT,
                    "description"   TEXT NOT NULL,
                    "files"         BLOB NOT NULL,
                    PRIMARY KEY("dataID"))""")



class TableWindow(QDialog, tableUI.Ui_TableWindow):
    def __init__(self, parent=None):
        super(TableWindow, self).__init__(parent)
        self.setupUi(self)
        self.detailsBtn.clicked.connect(self.dataDetails)
        self.tableWidget.cellDoubleClicked.connect(self.dataDetails)
        self.filterBtn.clicked.connect(self.filterData)
        self.resetBtn.clicked.connect(self.populateTable)
        self.populateTable()

    def populateTable(self, rows = []):
        self.tableWidget.setRowCount(0)
        if not rows:
            cursor = CONNECTION.cursor()
            cursor.execute('''SELECT * FROM baja_data_table ''')
            rows = cursor.fetchall()

        self.tableWidget.setColumnCount(10)
        headerList = ['Name', 'Date', 'Car', 'Collector', 'Subsystem', 'Project', 'Tags', 'Description', 'Files', 'id']
        self.tableWidget.setHorizontalHeaderLabels(headerList)

        for row in rows:
            i = rows.index(row)
            files = pickle.loads(row[9])
            shortFiles = shortFileNames(files)
            filestr = listToStr(shortFiles)
            name = row[1]
            self.tableWidget.insertRow(i)
            self.tableWidget.setItem(i, 0, QTableWidgetItem(row[1]))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(row[2]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(row[3]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(row[4]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(row[5]))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(row[6]))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(row[7]))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(row[8]))
            self.tableWidget.setItem(i, 8, QTableWidgetItem(filestr))
            self.tableWidget.setItem(i, 9, QTableWidgetItem(row[0]))

        self.tableWidget.setColumnHidden(9, True)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.showGrid()


    def dataDetails(self):
        data = []
        rowNum = self.tableWidget.currentRow()
        if rowNum == -1:
            rowNum = 0
        cursor = CONNECTION.cursor()
        dataId = self.tableWidget.item(rowNum, 9).text()
        cursor.execute('SELECT * FROM baja_data_table WHERE dataID=?;', (dataId,))
        row = cursor.fetchall()[0]
        for item in row:
            data.append(item)
        data[9] = pickle.loads(data[9])
        dialog = DetailsWindow(data = data, parent = self)
        dialog.show()
        dialog.exec_()


    def filterData(self):
        dialog = FilterWindow(parent = self)
        dialog.show()
        dialog.exec_()



class DetailsWindow(QDialog, detailsUI.Ui_DetailsWindow):
    def __init__(self, data, parent=None):
        super(DetailsWindow, self).__init__(parent)
        self.setupUi(self)

        self.deleteBtn.clicked.connect(self.deleteData)
        self.editBtn.clicked.connect(self.editData)
        self.copyBtn.clicked.connect(self.copyData)
        self.cancelBtn.clicked.connect(self.cancelButton)

        self.data = data
        self.dataId = data[0]
        self.nameDisp.setText(data[1])
        self.dateDisp.setText(data[2])
        self.carDisp.setText(data[3])
        self.collectorDisp.setText(data[4])
        self.subsystemDisp.setText(data[5])
        self.projectDisp.setText(data[6])
        self.tagDisp.setPlainText(data[7])
        self.descriptionDisp.setPlainText(data[8])
        self.fileDisp.setText(listToStr(shortFileNames(data[9])))


    def deleteData(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Are you sure you want to delete this data?")
        msg.setWindowTitle("Delete data?")
        msg.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        confirm = msg.exec_()
        if confirm == QMessageBox.Yes:
            for file in self.data[9]:
                os.remove(file)

            cursor = CONNECTION.cursor()
            cursor.execute('DELETE FROM baja_data_table where dataID=?;', (self.dataId,))
            CONNECTION.commit()

            self.parent().populateTable()
            self.cancelButton()


    def editData(self):
        #pass this data along somehow
        dialog = EditWindow(self.data)
        dialog.show()
        dialog.exec_()
        self.parent().populateTable()
        self.updateWindow()


    def copyData(self):
        saveLocation = QFileDialog()
        options = QFileDialog.Options()
        options |= QFileDialog.ShowDirsOnly
        location = QFileDialog.getExistingDirectory(self,"Select where to save a copy", options=options)
        if location:
            for file in self.data[9]:
                short = getShortName(file)
                newPath = os.path.join(location, short)
                shutil.copyfile(file, newPath)
            self.cancelButton()


    def updateWindow(self):
        cursor = CONNECTION.cursor()
        cursor.execute('SELECT * FROM baja_data_table WHERE dataID=?;', (self.dataId,))
        newData = cursor.fetchall()[0]
        for i in range(0,10):
            self.data[i] = newData[i]
            if i == 9:
                self.data[i] = pickle.loads(self.data[i])

        self.nameDisp.setText(self.data[1])
        self.dateDisp.setText(self.data[2])
        self.carDisp.setText(self.data[3])
        self.collectorDisp.setText(self.data[4])
        self.subsystemDisp.setText(self.data[5])
        self.projectDisp.setText(self.data[6])
        self.tagDisp.setPlainText(self.data[7])
        self.descriptionDisp.setPlainText(self.data[8])
        self.fileDisp.setText(listToStr(shortFileNames(self.data[9])))


    def cancelButton(self):
        self.reject()



class EditWindow(QDialog, editUI.Ui_EditWindow):
    fileNames = []

    def __init__(self, data = [], parent=None):
        super(EditWindow, self).__init__(parent)
        self.setupUi(self)
        self.fileNames = []
        self.data = data
        self.newData = False
        if not data:
            self.newData = True

        self.cancelBtn.clicked.connect(self.cancelButton)
        self.fileBtn.clicked.connect(self.fileSelect)
        cars = ['Select a Car'] + CARS_LIST
        self.carDrop.addItems(cars)
        subs = ['Select a Subsystem'] + SUBSYSTEMS_LIST
        self.subsystemDrop.addItems(subs)
        self.dateSelect.setDate(QDate.currentDate())

        if self.newData:
            self.submitBtn.clicked.connect(self.submitAddData)
        else:
            self.submitBtn.clicked.connect(self.submitEditData)

        if data:
            self.nameEdit.setText(data[1])
            date = data[2].split('/')
            self.dateSelect.setDate(QDate(int(date[2]), int(date[0]), int(date[1])))
            self.carDrop.setCurrentText(data[3])
            self.collectorEdit.setText(data[4])
            self.subsystemDrop.setCurrentText(data[5])
            self.projectEdit.setText(data[6])
            self.tagEdit.setPlainText(data[7])
            self.descriptionEdit.setPlainText(data[8])
            self.fileNames = data[9]
            self.fileEdit.setText(listToStr(shortFileNames(self.fileNames)))


    def fileSelect(self):
        options = QFileDialog.Options()
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*)", options=options)
        if files:
            self.fileNames = files
            self.fileEdit.setText(listToStr(shortFileNames(files)))


    def submitAddData(self):
        name = self.nameEdit.text().lower()
        date = self.dateSelect.date().toString('MM/dd/yyyy')
        car = self.carDrop.currentText().lower()
        collector = self.collectorEdit.text().lower()
        subsystem = self.subsystemDrop.currentText()
        project = self.projectEdit.text().lower()
        tags = self.tagEdit.toPlainText().lower()
        description = self.descriptionEdit.toPlainText().lower()
        movedFiles = []

        if car == 'Select a Car':
            car = ''

        if name and date and (subsystem != 'Select a Subsystem') and description and self.fileNames:
            data_id = str(uuid.uuid4()).replace('-','')

            for filename in self.fileNames:
                path = os.path.join(STORAGE,subsystem, getShortName(filename))
                shutil.copyfile(filename, path)
                movedFiles.append(path)

            movedBytes = pickle.dumps(movedFiles)
            cursor = CONNECTION.cursor()
            insertCommand = 'INSERT INTO baja_data_table ("dataID", "name", "date", "car", "collector", "subsystem", "project", "tags", "description", "files") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
            newData = (data_id, name, date, car, collector, subsystem, project, tags, description, movedBytes)
            cursor.execute(insertCommand, newData)
            CONNECTION.commit()
            self.cancelButton()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Missing Info!")
            msg.setText("You are missing required information")
            confirm = msg.exec_()


    def submitEditData(self):
        updateStrStart = "UPDATE baja_data_table SET"
        newData = []
        newData.append(self.data[0])
        newData.append(self.nameEdit.text().lower())
        newData.append(self.dateSelect.date().toString('MM/dd/yyyy'))
        newData.append(self.carDrop.currentText().lower())
        newData.append(self.collectorEdit.text().lower())
        newData.append(self.subsystemDrop.currentText())
        newData.append(self.projectEdit.text().lower())
        newData.append(self.tagEdit.toPlainText().lower())
        newData.append(self.descriptionEdit.toPlainText().lower())
        newData.append(self.fileNames)

        cursor = CONNECTION.cursor()

        oldSub = self.data[5]

        if newData[3] == 'Select a Car':
            newData[3] = self.data[3]

        if newData[1] and newData[2] and (newData[5] != 'Select a Subsystem') and newData[8] and newData[9]:
            for i in [1, 2, 3, 4, 6, 7, 8]:
                if newData[i] != self.data[i]:

                    updateStr = f"{updateStrStart} {DB_COLS[i]} = '{newData[i]}' WHERE dataID = '{self.data[0]}';"
                    cursor.execute(updateStr)

            if self.fileNames != self.data[9]:
                movedFiles = []
                for filename in self.fileNames:
                    path = os.path.join(STORAGE, self.data[5], getShortName(filename))

                    shutil.copyfile(filename, path)
                    movedFiles.append(path)

                for file in self.data[9]:
                    os.remove(file)

                movedBytes = pickle.dumps(movedFiles)
                updateStr = f"{updateStrStart} {DB_COLS[9]} = ? WHERE dataID = '{self.data[0]}';"
                cursor.execute(updateStr, (movedBytes,))
                self.data[9] = movedFiles

            if newData[5] != self.data[5]:
                movedFiles = []
                for filename in self.fileNames:
                    path = os.path.join(STORAGE, newData[5], getShortName(filename))

                    shutil.copyfile(filename, path)
                    movedFiles.append(path)

                for file in self.data[9]:
                    os.remove(file)

                movedBytes = pickle.dumps(movedFiles)
                updateStr = f"{updateStrStart} {DB_COLS[5]} = ? WHERE dataID = '{self.data[0]}';"
                cursor.execute(updateStr, (newData[5],))

                updateStr = f"{updateStrStart} {DB_COLS[9]} = ? WHERE dataID = '{self.data[0]}';"
                cursor.execute(updateStr, (movedBytes,))



            CONNECTION.commit()
            self.cancelButton()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("Missing Info!")
            msg.setText("You are missing required information")
            confirm = msg.exec_()


    def cancelButton(self):
        self.reject()



class FilterWindow(QDialog, filterUI.Ui_FilterWindow):
    filters = []

    def __init__(self, data = [], parent=None):
        super(FilterWindow, self).__init__(parent)
        self.setupUi(self)
        self.data = data
        self.cancelBtn.clicked.connect(self.cancelButton)
        self.searchBtn.clicked.connect(self.filterData)
        cars = ['Select a Car'] + CARS_LIST
        self.carDrop.addItems(cars)
        subs = ['Select a Subsystem'] + SUBSYSTEMS_LIST
        self.subsystemDrop.addItems(subs)
        self.dateSelect.setDate(QDate.currentDate())

        self.nameCheck.setCheckState(0)
        self.dateCheck.setCheckState(0)
        self.carCheck.setCheckState(0)
        self.collectorCheck.setCheckState(0)
        self.subsystemCheck.setCheckState(0)
        self.projectCheck.setCheckState(0)
        self.tagCheck.setCheckState(0)
        self.descCheck.setCheckState(0)

        self.nameEdit.setDisabled(True)
        self.dateSelect.setDisabled(True)
        self.carDrop.setDisabled(True)
        self.collectorEdit.setDisabled(True)
        self.subsystemDrop.setDisabled(True)
        self.projectEdit.setDisabled(True)
        self.tagEdit.setDisabled(True)
        self.descriptionEdit.setDisabled(True)

        self.nameCheck.stateChanged.connect(self.nameChange)
        self.dateCheck.stateChanged.connect(self.dateChange)
        self.carCheck.stateChanged.connect(self.carChange)
        self.collectorCheck.stateChanged.connect(self.collectChange)
        self.subsystemCheck.stateChanged.connect(self.subChange)
        self.projectCheck.stateChanged.connect(self.projChange)
        self.tagCheck.stateChanged.connect(self.tagChange)
        self.descCheck.stateChanged.connect(self.descChange)
        self.filters = [0,0,0,0,0,0,0,0]


    def filterData(self):
        params = []
        params.append(self.nameEdit.text().lower())
        params.append(self.dateSelect.date().toString('MM/dd/yyyy'))
        params.append(self.carDrop.currentText().lower())
        params.append(self.collectorEdit.text().lower())
        params.append(self.subsystemDrop.currentText())
        params.append(self.projectEdit.text().lower())
        params.append(self.tagEdit.toPlainText().lower())
        params.append(self.descriptionEdit.toPlainText().lower())
        searchStrStart = "SELECT * FROM baja_data_table WHERE"
        searchStrs = []
        results = []

        for i in range(0,8):
            if params[i] and self.filters[i]:
                if i == 1 or i == 2 or i == 4:
                    searchStrs.append(f"{DB_COLS[i+1]} = '{params[i]}'")
                else:
                    searchStrs.append(f"{DB_COLS[i+1]} LIKE '%{params[i]}%'")

        if searchStrs:
            searchStr = f"{searchStrStart} {' AND '.join(searchStrs)};"
            cursor = CONNECTION.cursor()
            cursor.execute(searchStr)
            results = cursor.fetchall()

        if results:
            self.parent().populateTable(rows = results)
        elif not searchStrs:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("No Filters Selected!")
            msg.setText("No filters were input")
            confirm = msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle("No Results Found!")
            msg.setText("No results were found using these filters")
            confirm = msg.exec_()


    def nameChange(self):
        state = self.nameCheck.checkState()
        if state == 2:
            self.nameEdit.setDisabled(False)
            self.filters[0] = 1
        else:
            self.nameEdit.setDisabled(True)
            self.filters[0] = 0


    def dateChange(self):
        state = self.dateCheck.checkState()
        if state == 2:
            self.dateSelect.setDisabled(False)
            self.filters[1] = 1
        else:
            self.dateSelect.setDisabled(True)
            self.filters[1] = 0


    def carChange(self):
        state = self.carCheck.checkState()
        if state == 2:
            self.carDrop.setDisabled(False)
            self.filters[2] = 1
        else:
            self.carDrop.setDisabled(True)
            self.filters[2] = 0


    def collectChange(self):
        state = self.collectorCheck.checkState()
        if state == 2:
            self.collectorEdit.setDisabled(False)
            self.filters[3] = 1
        else:
            self.collectorEdit.setDisabled(True)
            self.filters[3] = 0


    def subChange(self):
        state = self.subsystemCheck.checkState()
        if state == 2:
            self.subsystemDrop.setDisabled(False)
            self.filters[4] = 1
        else:
            self.subsystemDrop.setDisabled(True)
            self.filters[4] = 0


    def projChange(self):
        state = self.projectCheck.checkState()
        if state == 2:
            self.projectEdit.setDisabled(False)
            self.filters[5] = 1
        else:
            self.projectEdit.setDisabled(True)
            self.filters[5] = 0


    def tagChange(self):
        state = self.tagCheck.checkState()
        if state == 2:
            self.tagEdit.setDisabled(False)
            self.filters[6] = 1
        else:
            self.tagEdit.setDisabled(True)
            self.filters[6] = 0


    def descChange(self):
        state = self.descCheck.checkState()
        if state == 2:
            self.descriptionEdit.setDisabled(False)
            self.filters[7] = 1
        else:
            self.descriptionEdit.setDisabled(True)
            self.filters[7] = 0


    def cancelButton(self):
        self.reject()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()
    CONNECTION.close()