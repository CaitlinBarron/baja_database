from tkinter import *
from tkinter import ttk
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from calendarWidget import Calendar


def main():
    print("Hello World!")
    book = spreadsheetInit()
    print(book.worksheets())
    gui()


def spreadsheetInit():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('bajaDatabase-735456a2663a.json', scope)

    gc = gspread.authorize(credentials)

    book = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yir91DAk2HuJkvjuCnPcn7gAq5UpBjIqTXoel6G6n5A/edit#gid=0")
    return book


class Datafile:
    def __init__(self):
        self.dataName = ""
        self.collectionDate = datetime.date.today()
        self.car = ""
        self.collectee = ""
        self.subsystemList = ("Frame", "Suspension", "Steering", "Outboard", "Brakes",
                     "Ergonomics", "Reduction", "CVT", "Electrical", "R&D",
                     "Manufacturing", "Engine", "Composites", "Driveline Integration",
                     "Eboard", "Other")
        self.subsystem=0
        self.projectName = ""
        self.tags = []
        self.description = ""


def gui():
    global root
    root = Tk()
    root.title("RIT Baja Database")
    root.configure(bg="#FDAC44")

    addBtn = Button(root, text="Add Data", width=15, height=2,
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: addData())
    addBtn.grid(column=0, row=0, padx=20, pady=30)

    viewBtn = Button(root, text="View or Edit Data", width=17, height=2,
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: viewData())
    viewBtn.grid(column=1, row=0, padx=20, pady=30)

    root.mainloop()


def selDate(dialog, data, dateLbl):
    child = Toplevel(dialog)
    cal = Calendar(child, data, dateLbl)


def addData():
    newData = Datafile()
    dialog = Toplevel(root)
    dialog.configure(bg="#FDAC44")

    namewidth = 15
    nameLbl = Label(dialog, text="Name of Data",
                    bg="#FDAC44", width=namewidth)
    nameLbl.grid(column=0, row=0, padx=5, pady=2)
    nameEntry = Entry(dialog, width=namewidth, bg="#FFFFFF")
    nameEntry.grid(column=0, row=1, padx=5, pady=2)

    datewidth = 13
    dateLbl = Label(dialog, text="Date Collected",
                    bg="#FDAC44", width=datewidth)
    dateLbl.grid(column=1, row=0, padx=5, pady=2)
    selDateLbl = Label(dialog, text=newData.collectionDate.strftime("%x"),
                    bg="#FFFFFF", width=datewidth)
    selDateLbl.grid(column=1, row=1, padx=5, pady=2)
    calBtn = Button(dialog, text="Select Date", width=datewidth, bg="#FFFFFF", height=1,
                    command=lambda: selDate(dialog, newData.collectionDate, selDateLbl))
    calBtn.grid(column=1, row=2, padx=5, pady=2)

    carwidth = 10
    carLbl = Label(dialog, text="For Car",
                    bg="#FDAC44", width=carwidth)
    carLbl.grid(column=2, row=0, padx=5, pady=2)
    carEntry = Entry(dialog, width=carwidth, bg="#FFFFFF")
    carEntry.grid(column=2, row=1, padx=5, pady=2)

    collecteewidth = 20
    collecteeLbl = Label(dialog, text="Who Collected This",
                    bg="#FDAC44", width=collecteewidth)
    collecteeLbl.grid(column=3, row=0, padx=5, pady=2)
    collecteeEntry = Entry(dialog, width=collecteewidth, bg="#FFFFFF")
    collecteeEntry.grid(column=3, row=1, padx=5, pady=2)

    subwidth=15
    subLbl = Label(dialog, text="Subsystem",
                        bg="#FDAC44", width=collecteewidth)
    subLbl.grid(column=4, row=0, padx=5, pady=2)
    subSel = ttk.Combobox(dialog, width=collecteewidth,
                        values=["Frame", "Suspension", "Steering", "Outboard", "Brakes",
                        "Ergonomics", "Reduction", "CVT", "Electrical", "R&D",
                        "Manufacturing", "Engine", "Composites", "Driveline Integration",
                        "Eboard", "Other"])
    subSel.grid(column=4, row=1, padx=5, pady=2)

    dialog.mainloop()


def viewData():
    dialog = Toplevel(root)


if __name__ == "__main__":
    main()

