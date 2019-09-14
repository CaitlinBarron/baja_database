from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMainWindow, QDialog, QFileDialog, QComboBox, QPlainTextEdit, QLineEdit, QDateEdit, QTableWidgetItem, QTableWidget,QMessageBox
from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QActionEvent
from typing import List
import PyQt5.QtSql
import sys
import shutil
import mainUI, detailsUI, editUI, tableUI
import sqlite3
import uuid
import pickle

'''
cd C:\\Users\\Caitlin\\Documents\\repositories\\personal code\
baja_database\\src
use 'pyuic5 filename.ui -o filename.py' to convert UI files
"C:\\Users\\Caitlin\\Documents\\repositories\\personal code\\baja_database\\testing storage"
'''

CONNECTION = sqlite3.connect('baja_data.db')


def strToList(tags):
    tagsShort = []
    for tag in tags.split(','):
        tagsShort.append(tag.strip())
    return tagsShort

def shortFileNames(files):
    filesShort = []
    for file in files:
        filesShort.append(file.split('/')[-1])

    return filesShort

def listToStr(files):
    return ', '.join(files)



class MainApp(QMainWindow, mainUI.Ui_MainWindow):

    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)

        self.addBtn.clicked.connect(self.addData)
        self.viewBtn.clicked.connect(self.viewData)

        self.setUpDatabase()


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
        cursor.execute("""CREATE TABLE if not exists "baja_test_table" (
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
        self.populateTable()

    def populateTable(self):
        cursor = CONNECTION.cursor()
        cursor.execute('''SELECT * FROM baja_test_table ''')
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
        cursor = CONNECTION.cursor()
        dataId = self.tableWidget.item(rowNum, 9).text()
        cursor.execute('SELECT * FROM baja_test_table WHERE dataID=?;', (dataId,))
        row = cursor.fetchall()[0]
        for item in row:
            data.append(item)
        data[9] = pickle.loads(data[9])
        dialog = DetailsWindow(data)
        dialog.show()
        dialog.exec_()
        self.tableWidget.setRowCount(0)
        self.populateTable()


    def filterData(self):
        print('filter data hit')



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
            cursor = CONNECTION.cursor()
            cursor.execute('DELETE FROM baja_test_table where dataID=?;', (self.dataId,))
            CONNECTION.commit()
            self.cancelButton()


    def editData(self):
        #pass this data along somehow
        dialog = EditWindow(self.data)
        dialog.show()
        dialog.exec_()


    def copyData(self):
        print("save a copy of this data")


    def cancelButton(self):
        self.reject()


class EditWindow(QDialog, editUI.Ui_EditWindow):
    carList = ['',
                'j-arm',
                'semi',
                'r15',
                'r16',
                'r17',
                'r18',
                'r19',
                'r20']
    subsystemList = ['',
                    'Frame',
                    'Suspension',
                    'Steering',
                    'Outboard',
                    'Brakes',
                    'Ergonomics',
                    'Reduction',
                    'CVT',
                    'Electrical',
                    'R&D',
                    'Manufacturing',
                    'Engine',
                    'Composites',
                    'Driveline Integration',
                    'Eboard',
                    'Other']
    fileNames = []

    def __init__(self, data = [],parent=None):
        super(EditWindow, self).__init__(parent)
        self.setupUi(self)
        self.fileNames = []
        self.data = data

        self.submitBtn.clicked.connect(self.submitData)
        self.cancelBtn.clicked.connect(self.cancelButton)
        self.fileBtn.clicked.connect(self.fileSelect)

        self.carDrop.addItems(self.carList)
        self.subsystemDrop.addItems(self.subsystemList)
        self.dateSelect.setDate(QDate.currentDate())

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
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        if files:
            self.fileNames = files
            self.fileEdit.setText(listToStr(shortFileNames(files)))


    def submitData(self):
        name = self.nameEdit.text().lower()
        date = self.dateSelect.date().toString('MM/dd/yyyy')
        car = self.carDrop.currentText().lower()
        collector = self.collectorEdit.text().lower()
        subsystem = self.subsystemDrop.currentText()
        project = self.projectEdit.text().lower()
        tags = self.tagEdit.toPlainText().lower()
        description = self.descriptionEdit.toPlainText().lower()
        files = pickle.dumps(self.fileNames)

        if name and date and subsystem and description and self.fileNames:
            data_id = str(uuid.uuid4()).replace('-','')
            print(f"data to submit \nid: {data_id}\nname: {name}\ndate: {date}\ncar: {car}\ncollector: {collector}\nsubsytem: {subsystem}\nproject: {project}\ntags: {tags}\ndesc: {description}\nfiles: {files}")

            cursor = CONNECTION.cursor()
            insertCommand = 'INSERT INTO baja_test_table ("dataID", "name", "date", "car", "collector", "subsystem", "project", "tags", "description", "files") VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);'
            newData = (data_id, name, date, car, collector, subsystem, project, tags, description, files)
            cursor.execute(insertCommand, newData)
            CONNECTION.commit()
            self.cancelButton()


    def cancelButton(self):
        self.reject()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()
    CONNECTION.close()