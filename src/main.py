from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
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
        self.subsystem = ""
        self.projectName = ""
        self.tags = []
        self.description = ""
        self.file = ""


def gui():
    global root
    global dataPath
    dataPath = "C:\\Users\\Caitlin\\Documents\\repositories\\personal code\\baja_database\\testing storage"
    root = Tk()
    root.title("RIT Baja Database")
    root.configure(bg="#FDAC44")

    addBtn = Button(root, text="Add Data", width=15, height=2,
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: addDataWindow())
    addBtn.grid(column=0, row=0, padx=20, pady=30)

    viewBtn = Button(root, text="View or Edit Data", width=17, height=2,
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: viewDataWindow())
    viewBtn.grid(column=1, row=0, padx=20, pady=30)

    root.mainloop()


def selDate(dialog, data, dateLbl):
    child = Toplevel(dialog)
    cal = Calendar(child, data, dateLbl)


def fileSel(fileNameLbl):
    filename = filedialog.askopenfilename(initialdir="/",title="Select file")
    fileNameLbl.configure(text=filename)


def addData(newData, nameEntry, selDateLbl, carEntry, collecteeEntry, subSel, projectEntry, tagsEntry, descEntry, fileNameLbl):
    newData.dataName = nameEntry.get()
    newData.car = carEntry.get()
    newData.collectee = collecteeEntry.get()
    newData.subsystem = subSel.get()
    newData.projectName = projectEntry.get()
    newData.tags = tagsEntry.get().split
    newData.description = descEntry.get()
    newData.file = fileNameLbl.cget("text")


def addDataWindow():
    newData = Datafile()
    dialog = Toplevel(root)
    dialog.configure(bg="#FDAC44")

    xpad = 2
    ypad = 2
    namewidth = 15
    nameLbl = Label(dialog, text="Name of Data",
                    bg="#FDAC44", width=namewidth)
    nameLbl.grid(column=0, row=0, padx=xpad, pady=ypad)
    nameEntry = Entry(dialog, width=namewidth, bg="#FFFFFF")
    nameEntry.grid(column=0, row=1, padx=xpad, pady=ypad)

    datewidth = 13
    dateLbl = Label(dialog, text="Date Collected",
                    bg="#FDAC44", width=datewidth)
    dateLbl.grid(column=1, row=0, padx=xpad, pady=ypad)
    selDateLbl = Label(dialog, text=newData.collectionDate.strftime("%x"),
                    bg="#FFFFFF", width=datewidth)
    selDateLbl.grid(column=1, row=1, padx=xpad, pady=ypad)
    calBtn = Button(dialog, text="Select Date", width=datewidth, bg="#FFFFFF", height=1,
                    command=lambda: selDate(dialog, newData.collectionDate, selDateLbl))
    calBtn.grid(column=1, row=2, padx=xpad, pady=ypad)

    carwidth = 10
    carLbl = Label(dialog, text="For Car",
                    bg="#FDAC44", width=carwidth)
    carLbl.grid(column=2, row=0, padx=xpad, pady=ypad)
    carEntry = Entry(dialog, width=carwidth, bg="#FFFFFF")
    carEntry.grid(column=2, row=1, padx=xpad, pady=ypad)

    collecteewidth = 20
    collecteeLbl = Label(dialog, text="Who Collected This",
                    bg="#FDAC44", width=collecteewidth)
    collecteeLbl.grid(column=3, row=0, padx=xpad, pady=ypad)
    collecteeEntry = Entry(dialog, width=collecteewidth, bg="#FFFFFF")
    collecteeEntry.grid(column=3, row=1, padx=xpad, pady=ypad)

    subwidth=15
    subLbl = Label(dialog, text="Subsystem",
                        bg="#FDAC44", width=collecteewidth)
    subLbl.grid(column=0, row=4, padx=xpad, pady=ypad)
    subSel = ttk.Combobox(dialog, width=collecteewidth,
                        values=["Frame", "Suspension", "Steering", "Outboard", "Brakes",
                        "Ergonomics", "Reduction", "CVT", "Electrical", "R&D",
                        "Manufacturing", "Engine", "Composites", "Driveline Integration",
                        "Eboard", "Other"])
    subSel.grid(column=0, row=5, padx=xpad, pady=ypad)

    projwidth=20
    projectLbl = Label(dialog, text="Project Name",
                         bg="#FDAC44", width=projwidth)
    projectLbl.grid(column=1, row=4, padx=xpad, pady=ypad)
    projectEntry = Entry(dialog, width=projwidth, bg="#FFFFFF")
    projectEntry.grid(column=1, row=5, padx=xpad, pady=ypad)

    tagswidth = 30
    tagsLbl = Label(dialog, text="Tags (separate with commas)",
                       bg="#FDAC44", width=tagswidth)
    tagsLbl.grid(column=2, row=4, columnspan=2, padx=xpad, pady=ypad)
    tagsEntry = Entry(dialog, width=tagswidth, bg="#FFFFFF")
    tagsEntry.grid(column=2, row=5, columnspan=2, padx=xpad, pady=ypad)

    descwidth = 45
    descLbl = Label(dialog, text="Data Description",
                    bg="#FDAC44", width=descwidth)
    descLbl.grid(column=0, row=7, columnspan=2, padx=xpad, pady=ypad)
    descEntry = scrolledtext.ScrolledText(dialog, height=3, width=descwidth, bg="#FFFFFF")
    descEntry.grid(column=0, row=8, columnspan=2, rowspan=2, padx=xpad, pady=ypad)

    filewidth = 30
    fileLbl = Label(dialog, text="Data File",
                    bg="#FDAC44", width=filewidth)
    fileLbl.grid(column=2, row=7, columnspan=2, padx=xpad, pady=ypad)
    fileNameLbl = Label(dialog, text=newData.file,
                    bg="#FFFFFF", width=filewidth)
    fileNameLbl.grid(column=2, row=8, columnspan=2, padx=xpad, pady=ypad)
    fileBtn = Button(dialog, text="Attach File", bg="#FFFFFF", width=int((filewidth/2)),
                     command=lambda: fileSel(fileNameLbl))
    fileBtn.grid(column=2, row=9, columnspan=2, padx=xpad, pady=ypad)


    submitBtn = Button(dialog, text="Submit Data", width=15,
                       command=lambda: addData(newData, nameEntry, selDateLbl, carEntry,
                                               collecteeEntry, subSel, projectEntry,
                                               tagsEntry, descEntry, fileNameLbl))
    submitBtn.grid(column=5, row=5, padx=xpad, pady=ypad)

    dialog.grid_rowconfigure(3, minsize=20)
    dialog.grid_rowconfigure(6, minsize=20)
    dialog.grid_columnconfigure(4, minsize=30)


def viewDataWindow():
    dialog = Toplevel(root)


if __name__ == "__main__":
    main()

