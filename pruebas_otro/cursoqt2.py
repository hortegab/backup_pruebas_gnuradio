import sys
from PyQt4 import QtGui

def main():
  app = QtGui.QApplication(sys.argv)

  widget = QtGui.QWidget()
  widget.resize(250, 150)
  widget.move(300, 300)
  widget.setWindowTitle('Simple')
  widget.show()

  return app.exec_()

if __name__ == '__main__':
  sys.exit(main())
