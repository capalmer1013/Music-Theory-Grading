"""
Class to handle grading music theory assinments
"""
import fileInterface
import music21


class Grader(object):
    def __init__(self):
        self.assignmentDir = fileInterface.FileDir()
        self.key = fileInterface.File()

    def grade(self):
        total = len(self.key.score)
        totalNotes = 0
        correct = 0
        for assignment in self.assignmentDir.listOfFiles:
            for i in range(total):
                if type(self.key.score[i]) == music21.note.Note:
                    totalNotes += 1
                    if self.key.score[i].nameWithOctave == assignment.score[i].nameWithOctave:
                        correct += 1
            print assignment, correct, '/', totalNotes, float(correct)/totalNotes
        pass

    def saveGrades(self):
        pass


def main():
    pass

if __name__ == "__main__":
    main()