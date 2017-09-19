#import svgutils
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog, QLineEdit
from PyQt5.QtCore import pyqtSlot

class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Icon Generator'
        self.left = 50
        self.top = 50
        self.width = 640
        self.height = 480
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setFixedSize(self.size())

        # Create Load Button
        btnLoadSvg = QPushButton('Load SVG', self)
        btnLoadSvg.setToolTip('Select the image SVG to convert')
        btnLoadSvg.move(20,20)
        btnLoadSvg.clicked.connect(self.openFileDialog)

        # Create Textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(100, 20)
        self.textbox.resize(350, 22)
        self.textbox.setStyleSheet('QLineEdit {padding-left:5}')

        self.show()

    @pyqtSlot()
    def openFileDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, 'QFileDiaglog.getOpenFileName()', '', 'All Files (*);;SVG Images (*.svg)', options=options)
        if fileName:
            self.textbox.setText(fileName)
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()

    sys.exit(app.exec_())