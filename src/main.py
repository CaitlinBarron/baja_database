from tkinter import *
from tkinter import ttk, filedialog, scrolledtext
#import gspread
#from oauth2client.service_account import ServiceAccountCredentials
import datetime
from calendarWidget import Calendar
import sqlite3
import uuid


def main():
    conn = databaseInit()
    print("database opened successfully!")
    #book = spreadsheetInit()
    #print(book.worksheets())
    gui()

"""
def spreadsheetInit():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('bajaDatabase-735456a2663a.json', scope)

    gc = gspread.authorize(credentials)

    book = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yir91DAk2HuJkvjuCnPcn7gAq5UpBjIqTXoel6G6n5A/edit#gid=0")
    return book
"""


def databaseInit():
    #C:\Users\Caitlin\Documents\repositories\personal code\baja_database\src\baja_data.db
    conn = sqlite3.connect('baja_data.db')
    curse = conn.cursor()
    #curse.execute("CREATE TABLE IF NOT EXISTS baja_data_details()")

    return conn


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

    """
    saved = 0
    while (saved != 1)
        ID = str(uuid.uuid4()).replace('-','')
        cursor.execute("SELECT * FROM baja_data_details WHERE DataID = ?", (ID,))
        if len(data) == 0
            #save new data into baja_data_details
            saved = 1
        else
            #make new id
            pass
    """


def searchData(dialog):
    pass


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

    descwidth = 60
    descLbl = Label(dialog, text="Data Description",
                    bg="#FDAC44", width=descwidth)
    descLbl.grid(column=0, row=7, columnspan=4, padx=xpad, pady=ypad)
    descEntry = scrolledtext.ScrolledText(dialog, height=2, width=descwidth, bg="#FFFFFF")
    descEntry.grid(column=0, row=8, columnspan=4, rowspan=2, padx=xpad, pady=ypad)

    filewidth = 70
    fileLbl = Label(dialog, text="Data File",
                    bg="#FDAC44", width=filewidth)
    fileLbl.grid(column=0, row=10, columnspan=4, padx=xpad, pady=ypad)
    fileNameLbl = Label(dialog, text=newData.file,
                    bg="#FFFFFF", width=filewidth)
    fileNameLbl.grid(column=0, row=11, columnspan=4, padx=xpad, pady=ypad)
    fileBtn = Button(dialog, text="Attach File", bg="#FFFFFF", width=int((filewidth/3)),
                     command=lambda: fileSel(fileNameLbl))
    fileBtn.grid(column=0, row=12, columnspan=4, padx=xpad, pady=ypad)


    submitBtn = Button(dialog, text="Submit Data", width=15,
                       command=lambda: addData(newData, nameEntry, selDateLbl, carEntry,
                                               collecteeEntry, subSel, projectEntry,
                                               tagsEntry, descEntry, fileNameLbl))
    submitBtn.grid(column=5, row=5, padx=xpad, pady=ypad)

    rowSpace = 40
    colSpace = 30
    dialog.grid_rowconfigure(3, minsize=rowSpace)
    dialog.grid_rowconfigure(6, minsize=rowSpace)
    dialog.grid_rowconfigure(9, minsize=(rowSpace*2))
    dialog.grid_columnconfigure(4, minsize=colSpace)


def viewDataWindow():
    dialog = Toplevel(root)
    dialog.configure(bg="#FDAC44")
    dialog.resizable(width=0, height=0)
    xpad = 5
    ypad = 5

    searchBtn = Button(dialog, text="Search Data", width=20,
                        command=lambda: searchData(dialog))
    searchBtn.grid(column=1, row=0, padx=xpad, pady=ypad)

    dialog.grid_columnconfigure(0, minsize=30)
    dialog.grid_columnconfigure(2, minsize=30)

    frame = Frame(dialog)
    frame.grid(column=0, row=1, columnspan=3, padx=xpad, pady=ypad)

    tree = ttk.Treeview(frame, selectmode="browse",
                            columns=("date", "car", "project",
                        "subsystem", "tags", "collectee", "description"))
    tree.heading("#0", text="Name", anchor="w")
    tree.column("#0", anchor="w", width=200)

    tree.heading("date", text="Date")
    tree.column("date", anchor="center", width=150)

    tree.heading("car", text="Car")
    tree.column("car", anchor="center", width=50)

    tree.heading("project", text="Project")
    tree.column("project", anchor="center", width=200)

    tree.heading("subsystem", text="Subsystem")
    tree.column("subsystem", anchor="center", width=150)

    tree.heading("tags", text="Tags")
    tree.column("tags", anchor="center", width=200)

    tree.heading("collectee", text="Collected By")
    tree.column("collectee", anchor="center", width=200)

    tree.heading("description", text="Description")
    tree.column("description", anchor="center", width=400)

    tree.tag_configure('gray', background='#cccccc')
    tree.grid(column=0, row=0)

    vsb = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    vsb.grid(column=1, row=0)
    tree.configure(yscrollcommand=vsb.set)

    hsb = ttk.Scrollbar(frame, orient='horizontal', command=tree.xview)
    hsb.grid(column = 0, row=1)
    tree.configure(xscrollcommand=hsb.set)

    tree.insert("", "end", text="test data", values=("05/20/2019",
                "R19", "MR Shocks", "Suspension", "mr, suspension",
                "Forrest", "data from MR shock initial testing"))
    tree.insert("", "end", text="test data", values=("05/20/2019",
                "R19", "MR Shocks", "Suspension", "mr, suspension",
                "Forrest", "data from MR shock initial testing"), tag="gray")


if __name__ == "__main__":
    main()

