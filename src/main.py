from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMainWindow, QDialog, QFileDialog, QComboBox, QPlainTextEdit, QLineEdit, QDateEdit
from PyQt5.QtCore import QSize, QDate
from PyQt5.QtGui import QActionEvent
from typing import List
import PyQt5.QtSql
import sys
import shutil
from dataclasses import dataclass
import mainUI, detailsUI, editUI, tableUI
import sqlite3
import uuid

'''
use 'pyuic filename.ui -o filename.py' to convert UI files
"C:\\Users\\Caitlin\\Documents\\repositories\\personal code\\baja_database\\testing storage"
'''

connection = sqlite3.connect('baja_data.db')


@dataclass
class Datafile:
    dataID: str
    name: str
    date: str
    car: str
    collector: str
    subsystem: str
    project: str
    tags: str
    description: str
    files: List[str]

    def tagsToList():
        return self.tags.split(",")

    def shortFilesString():
        filesShort = []
        for file in self.Files:
            filesShort.append(file.split('/')[-1])
        return ', '.join(filesShort)

    def longFilesString():
        return ', '.join(self.files)



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

        cursor = connection.cursor()
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
        self.editBtn.clicked.connect(self.editData)
        self.filterBtn.clicked.connect(self.filterData)
        print(connection)


    def editData(self):
        print('edit button hit')


    def filterData(self):
        print('filter data hit')



class DetailsWindow(QDialog, detailsUI.Ui_DetailsWindow):
    def __init__(self, parent=None):
        super(DetailsWindow, self).__init__(parent)
        self.setupUi(self)

        self.deleteBtn.clicked.connect(self.deleteData)
        self.editBtn.clicked.connect(self.editData)
        self.copyBtn.clicked.connect(self.copyData)
        self.cancelBtn.clicked.connect(self.cancelButton)

        print(connection)


    def deleteData(self):
        print("delete this data")


    def editData(self):
        #pass this data along somehow
        dialog = EditWindow()
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

    def __init__(self, parent=None):
        super(EditWindow, self).__init__(parent)
        self.setupUi(self)

        self.submitBtn.clicked.connect(self.submitData)
        self.cancelBtn.clicked.connect(self.cancelButton)
        self.fileBtn.clicked.connect(self.fileSelect)

        self.carDrop.addItems(self.carList)
        self.subsystemDrop.addItems(self.subsystemList)
        self.dateSelect.setDate(QDate.currentDate())
        print(connection)


    def fileSelect(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        files, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileNames()", "","All Files (*);;Python Files (*.py)", options=options)
        filesShort = []
        if files:
            print(files)
            self.fileNames = files
            for file in files:
                filesShort.append(file.split('/')[-1])
            uiStr = ', '.join(filesShort)
            self.fileEdit.setText(uiStr)


    def submitData(self):
        name = self.nameEdit.text()
        date = self.dateSelect.date()
        car = self.carDrop.currentText()
        collector = self.collectorEdit.text()
        subsystem = self.subsystemDrop.currentText()
        project = self.projectEdit.text()
        tags = self.tagEdit.selectAll()
        description = self.descriptionEdit.selectAll()
        files = self.fileNames

        print(f"data to submit \nname: {name}\ndate: {date}\ncar: {car}\ncollector: {collector}\nsubsytem: {subsystem}\nproject: {project}\ntags: {tags}\ndesc: {description}\nfiles: {files}")

        data_id = str(uuid.uuid4()).replace('-','')
        print(data_id)
        #test = Datafile("1", "crio data", "7/22/2019", "r19", "caitlin", "R&D", "database", "lame, testing, cats are best", "this is 4 practicing", ["src/detailsUI.ui"])
        #print(test.date)


    def cancelButton(self):
        self.reject()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()
    connection.close()
    print(connection)