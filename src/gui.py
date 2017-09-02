from Tkinter import Tk, Frame, Button
from tkFileDialog import askopenfilename


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.QUIT = Button(self)
        self.openKey = Button(self)
        self.setQuit()
        self.setOpenKey()

    def setQuit(self):
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

    def setOpenKey(self):
        self.openKey["text"] = "Key",
        self.openKey["command"] = self.openFile
        self.openKey.pack({"side": "left"})

    def setOpenAssignments(self):
        pass

    def openFile(self):
        print askopenfilename()

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    root.destroy()
