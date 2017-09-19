#import svgutils
import sys
from PyQt5.QtWidgets import QApplication, QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)

    wgen = QWidget()
    wgen.resize(250, 150)
    wgen.move(300, 300)
    wgen.setWindowTitle('Icon Generator')
    wgen.show()

    sys.exit(app.exec_())