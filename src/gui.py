import pyforms
from pyforms import BaseWidget
from pyforms.Controls import ControlText
from pyforms.Controls import ControlButton

class Application(BaseWidget):
    def __init__(self):
        super(Application, self).__init__('Application')

        self.mainmenu = [
            { 'File': [
                {'Open': self.__openEvent},
                '-',
                {'Save': self.__saveEvent},
                {'Save as': self.__saveAsEvent}
            ]},
            {'Edit': [
                {'Copy': self.__editEvent},
                {'Paste': self.__pasteEvent}
            ]}
        ]

    def __openEvent(self):
        pass

    def __saveEvent(self):
        pass

    def __saveAsEvent(self):
        pass

    def __editEvent(self):
        pass

    def __pasteEvent(self):
        pass

#Execute the application
if __name__ == "__main__":
    pyforms.startApp(Application)