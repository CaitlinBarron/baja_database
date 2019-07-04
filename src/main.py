from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QMainWindow, QDialog
from PyQt5.QtCore import QSize
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
        print(f"{self.width()}x{self.height()}")


class AddWindow(QDialog, addUI.Ui_AddWindow):
    def __init__(self, parent=None):
        super(AddWindow, self).__init__(parent)
        self.setupUi(self)
        self.submitBtn.clicked.connect(self.submitData)
        self.cancelBtn.clicked.connect(self.cancelButton)


    def fileBrowse(self):
        print('browse for file')


    def submitData(self):
        print('submit button hit')
        print(f"{self.width()}x{self.height()}")


    def cancelButton(self):
        self.reject()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec_()