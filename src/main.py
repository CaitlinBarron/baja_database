from tkinter import *
import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials


def main():
    print("Hello World!")
    book = spreadsheet_init()
    print(book.worksheets())
    gui()


def spreadsheet_init():
    scope = ['https://spreadsheets.google.com/feeds',
             'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('bajaDatabase-735456a2663a.json', scope)

    gc = gspread.authorize(credentials)

    book = gc.open_by_url("https://docs.google.com/spreadsheets/d/1Yir91DAk2HuJkvjuCnPcn7gAq5UpBjIqTXoel6G6n5A/edit#gid=0")
    return book


def gui():
    window = Tk()
    window.title("RIT Baja Database")
    window.geometry('350x200')
    openbtn = Button(window, text="Open File")
    openbtn.grid(column=0, row=0)
    window.mainloop()


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
