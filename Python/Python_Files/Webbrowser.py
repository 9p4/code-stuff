import sys
from browser import BrowserDialog
from pyqt5 import QtCore, QtGui
from pyqt5.QtCore import QUrl
from pyqt5.QtWebKit import QWebView
 
class MyBrowser(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        QWebView.__init__(self)
        self.ui = BrowserDialog()
        self.ui.setupUi(self)
        self.ui.lineEdit.returnPressed.connect(self.loadURL)
 
    def loadURL(self):
        url = self.ui.lineEdit.text()
        self.ui.qwebview.load(QUrl(url))
        self.show()  
        #self.ui.lineEdit.setText("")
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyBrowser()
    myapp.ui.qwebview.load(QUrl('http://www.pythonspot.com'))
    myapp.show()
    sys.exit(app.exec_())