from Note import Note
from datetime import datetime
from tkinter import *

def getNotes():
    with open("notes.txt") as fileHandler:
        return fileHandler.read().split("\n")

def writeNotes(notes):
    with open("notes.txt", "w") as fileHandler:
        i = 0
        while notes[i] != "":
            fileHandler.writelines(f"{notes[i]}\n")
            i += 1

def addNote():
    with open("notes.txt", "a") as fileHandler:
        fileHandler.writelines(f"{Note(headEntry.get(), textEntry.get()).getNote()}\n")

def showNotes():
    listbox.delete(0, END)
    with open("notes.txt") as fileHandler:
        lines = fileHandler.readlines()
        for line in lines:
            listbox.insert(END, line)

def deleteNote():
    notes = getNotes()
    notes.pop(int(listbox.curselection()[0]))
    writeNotes(notes)

def changeNote():
    notes = getNotes()
    i = int(listbox.curselection()[0])
    note = notes[i].split(" ")
    head = headEntry.get()
    text = textEntry.get()
    if len(head) > 0:
        note[0] = head + ":"
    if len(text) > 0:
        note[1] = textEntry.get()
    t = str(datetime.now()).split(".")[0]
    notes[i] = f"{note[0]} {note[1]} ({t})"
    writeNotes(notes)

root = Tk()
root.geometry("600x400")
root.title("Notes")
Label(text="Head:").grid(row=0, column=0)
Label(text="Text:").grid(row=0, column=1)
headEntry = Entry(width=30, border=5)
headEntry.grid(row=1, column=0)
textEntry = Entry(width=60, border=5)
textEntry.grid(row=1, column=1)
listbox = Listbox(selectmode=EXTENDED, height=15, width=60, border=5)
listbox.grid(row=2, column=1, rowspan=4)
Button(text="Add note", width=10, border=5, command=addNote).grid(row=2, column=0)
Button(text="Show notes", width=10, border=5, command=showNotes).grid(row=3, column=0)
Button(text="Delete note", width=10, border=5, command=deleteNote).grid(row=4, column=0)
Button(text="Change note", width=10, border=5, command=changeNote).grid(row=5, column=0)
root.mainloop()
