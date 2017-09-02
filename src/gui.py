from Tkinter import Tk, Frame, Button, Label, RAISED, StringVar
from tkFileDialog import askopenfilename, askdirectory
import grader

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()

        # buttons
        self.QUIT = Button(self)
        self.openKeyButton = Button(self)
        self.openAssignmentsButton = Button(self)
        self.gradeButton = Button(self)
        self.outputText = StringVar("")
        self.output = Label(self, textvariable=self.outputText, relief=RAISED)

        # button styling
        self.setQuit()
        self.setOpenKey()
        self.setOpenAssignments()
        self.setGrade()
        self.setOutput()

        self.grader = grader.Grader()

    def setOutput(self):
        self.output.pack({"side": "bottom"})

    def setGrade(self):
        self.gradeButton['text'] = "Grade"
        self.gradeButton['fg'] = 'green'
        self.gradeButton['command'] = self.grade
        self.gradeButton.pack({"side": "left"})

    def setQuit(self):
        self.QUIT["text"] = "Quit"
        self.QUIT["fg"] = "red"
        self.QUIT["command"] = self.quit
        self.QUIT.pack({"side": "left"})

    def setOpenKey(self):
        self.openKeyButton["text"] = "Key",
        self.openKeyButton["command"] = self.openKey
        self.openKeyButton.pack({"side": "left"})

    def setOpenAssignments(self):
        self.openAssignmentsButton["text"] = "Assignments",
        self.openAssignmentsButton["command"] = self.openAssignments
        self.openAssignmentsButton.pack({"side": "left"})

    def grade(self):
        self.grader.grade()

    def openAssignments(self):
        self.outputText.set(self.grader.assignmentDir.openDir(askdirectory()))

    def openKey(self):
        self.outputText.set(self.grader.key.open(askopenfilename()))

if __name__ == "__main__":
    root = Tk()
    app = Application(master=root)
    app.mainloop()
    try:
        root.destroy()

    except:
        pass
