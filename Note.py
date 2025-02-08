from datetime import datetime

class Note:
    def __init__(self, head, text):
        self.__head = head
        self.__text = text
        self.__setTime()

    def __setTime(self):
        self.__time = str(datetime.now()).split(".")[0]

    def printNote(self):
        print(f"{self.__head}: {self.__text} - ({self.__time})")