import sys
from datetime import datetime
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QDesktopWidget, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import QTimer, QIODevice, pyqtSignal
from Ui_TrackerFinderMainWindow import Ui_TrackerFinderMainWindow
from DigitalClock import DigitalClock

class TrackerFinderMainWindow(QMainWindow, Ui_TrackerFinderMainWindow):

    # Emitted when the window is closing
    closeSignal = pyqtSignal()

    def __init__(self)->None:
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('TrackerFinder')
        clock = DigitalClock(self.clockFrame)
        layout = QHBoxLayout()
        self.clockFrame.setLayout(layout)
        layout.addWidget(clock)


    def aprsMsg(self, msg:dict)->None:
        self.aprsTag.setText(msg['tag'])
        self.aprsLat.setText(msg['lat'])
        self.aprsLon.setText(msg['lon'])
        self.aprsCount.setText(f"{msg['count']: d}")
        self.aprsFailed.setText(f"{msg['failed']: d}")
        self.aprsTime.setText(msg['time'])
        self.aprsAlt.setText(msg['alt'])
        self.aprsDeltaT.setText(f"{msg['deltaTsecs']: d}")

    def pingMsg(self, msg:dict)->None:
        self.pingAge.setText(f"{msg['age']:d}")
        self.pingId.setText(f"{msg['id']:d}")
        self.pingLat.setText(f"{msg['lat']: .6f}")
        self.pingLon.setText(f"{msg['lon']: .6f}")
        self.pingCount.setText(f"{msg['pingCount']: d}")
        self.pingDeltaT.setText(f"{msg['deltaTsecs']: d}")

    def setStatus(self, text:str)->None:
        self.statusBar().showMessage(text)

    def closeEvent(self, a0):
        self.closeSignal.emit()

    def addToLog(self, text:str)->None:
        timeStamp = datetime.now()
        ts = timeStamp.isoformat(sep=' ', timespec='seconds')
        self.log.append(f'{ts} {text}')
