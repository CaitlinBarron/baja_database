from tkinter import *
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


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


def gui():
    global root
    root = Tk()
    root.title("RIT Baja Database")
    root.configure(bg="#FDAC44")
    addBtn = Button(root, text="Add Data", width="15", height="2",
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: addData())
    addBtn.grid(column=0, row=0, padx=20, pady=30)
    viewBtn = Button(root, text="View or Edit Data", width="17", height="2",
                    bg="#FFFFFF", font=("Arial", "10", "bold"), command=lambda: viewData())
    viewBtn.grid(column=1, row=0, padx=20, pady=30)
    root.mainloop()


def addData():
    dialog = Toplevel()
    #fix this?
    dialog.wait_window(root)


def viewData():
    dialog = Toplevel()


class Datafile:
    dataName = ""
    collectionDate = datetime.datetime.now()
    car = ""
    collectee = ""
    subsystem = ("Frame", "Suspension", "Steering", "Outboard", "Brakes",
                 "Ergonomics", "Reduction", "CVT", "Electrical", "R&D",
                 "Manufacturing", "Engine", "Composites", "Driveline Integration",
                 "Eboard", "Other")
    projectName = ""
    tags = []
    description = ""


if __name__ == "__main__":
    main()

