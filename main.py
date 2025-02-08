from Note import Note
from datetime import datetime

def saveNotes(notes):
    with open("notes.txt", "a") as fileHandler:
        for i in range(len(notes)):
            fileHandler.writelines(f"{notes[i].getNote()}\n")
    return []

def getNotes():
    with open("notes.txt") as fileHandler:
        return fileHandler.read().split("\n")

def printNotes():
    with open("notes.txt") as fileHandler:
        print(f"{fileHandler.read()}")

notes = []
while True:
    print("What do you want to do?")
    print("1 - show notes")
    print("2 - add note")
    print("3 - delete note")
    print("4 - change head")
    print("5 - change text")
    print("6 - save notes")
    print("7 - exit")
    a = input("Your choice: ")
    if a == "1":
        notes = saveNotes(notes)
        printNotes()
    elif a == "2":
        notes.append(Note(input("Enter head: "), input("Enter text: ")))
    elif a == "3":
        saveNotes(notes)
        notes = getNotes()
        notes.pop(int(input("Enter index: ")) - 1)
        with open("notes.txt", "w") as fileHandler:
            i = 0
            while notes[i] != "":
                fileHandler.writelines(f"{notes[i]}\n")
                i += 1
        notes = []
    elif a == "4":
        saveNotes(notes)
        notes = getNotes()
        i = int(input("Enter index: ")) - 1
        note = notes[i].split(" ")
        note[0] = input("Enter head: ")
        t = str(datetime.now()).split(".")[0]
        notes[i] = f"{note[0]}: {note[1]} ({t})"
        with open("notes.txt", "w") as fileHandler:
            i = 0
            while notes[i] != "":
                fileHandler.writelines(f"{notes[i]}\n")
                i += 1
        notes = []
    elif a == "5":
        saveNotes(notes)
        notes = getNotes()
        i = int(input("Enter index: ")) - 1
        note = notes[i].split(" ")
        note[1] = input("Enter text: ")
        t = str(datetime.now()).split(".")[0]
        notes[i] = f"{note[0]} {note[1]} ({t})"
        with open("notes.txt", "w") as fileHandler:
            i = 0
            while notes[i] != "":
                fileHandler.writelines(f"{notes[i]}\n")
                i += 1
        notes = []
    elif a == "6":
        notes = saveNotes(notes)
    elif a == "7":
        saveNotes(notes)
        print("Goodbye")
        break