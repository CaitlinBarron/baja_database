from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMainWindow, QDialog, QFileDialog, QComboBox, QPlainTextEdit, QLineEdit, QDateEdit
from PyQt5.QtCore import QSize, QDate
import sys
import mainUI, addUI, viewUI

class MainApp(QMainWindow, mainUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainApp, self).__init__(parent)
        self.setupUi(self)
        self.addBtn.clicked.connect(self.addData)
        self.viewBtn.clicked.connect(self.viewData)


    def addData(self):
        dialog = AddWindow()
        dialog.show()
        dialog.exec_()


    def viewData(self):
        dialog = ViewWindow()
        dialog.show()
        dialog.exec_()


class ViewWindow(QDialog, viewUI.Ui_ViewWindow):
    def __init__(self, parent=None):
        super(ViewWindow, self).__init__(parent)
        self.setupUi(self)
        self.editBtn.clicked.connect(self.editData)


    def editData(self):
        print('edit button hit')


class AddWindow(QDialog, addUI.Ui_AddWindow):
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
        super(AddWindow, self).__init__(parent)
        self.setupUi(self)

        self.submitBtn.clicked.connect(self.submitData)
        self.cancelBtn.clicked.connect(self.cancelButton)
        self.fileBtn.clicked.connect(self.fileBrowse)

        self.carDrop.addItems(self.carList)
        self.subsystemDrop.addItems(self.subsystemList)
        self.dateSelect.setDate(QDate.currentDate())


    def fileBrowse(self):
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
        collectee = self.collecteeEdit.text()
        subsystem = self.subsystemDrop.currentText()
        project = self.projectEdit.text()
        tags = self.tagEdit.selectAll()
        description = self.descriptionEdit.selectAll()
        files = self.fileNames
        print(f"data to submit \nname: {name}\ndate: {date}\ncar: {car}\ncollectee: {collectee}\nsubsytem: {subsystem}\nproject: {project}\ntags: {tags}\ndesc: {description}\nfiles: {files}")


    def cancelButton(self):
        self.reject()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()