"""
Class to handle grading music theory assinments
"""
import fileInterface
import music21
import os

class Grader(object):
    def __init__(self):
        self.assignmentDir = fileInterface.FileDir()
        self.key = fileInterface.File()
        self.gradeResults = []

    def grade(self):
        total = len(self.key.score)
        for assignment in self.assignmentDir.listOfFiles:
            totalNotes = 0
            correct = 0
            for i in range(total):
                if type(self.key.score[i]) == music21.note.Note:
                    totalNotes += 1
                    if self.key.score[i].nameWithOctave == assignment.score[i].nameWithOctave:
                        correct += 1
            self.gradeResults.append([os.path.split(assignment.filename)[-1], correct, '/', totalNotes, '-', (float(correct)/totalNotes) * 100.0])

    def saveGrades(self, outfileName):
        with open(outfileName, 'w+') as outfile:
            for each in self.gradeResults:
                line = ''
                for section in each:
                    line += str(section)
                line += '\n'
                outfile.write(line)


def main():
    pass

if __name__ == "__main__":
    main()