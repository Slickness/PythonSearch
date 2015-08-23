from PyQt4 import QtCore, QtGui, Qt
import sys
import PySearch
class SearchWindowClass(QtGui.QWidget):
    def __init__(self):
        super(SearchWindowClass,self).__init__()
        self.setGeometry(50,50,200,200)
        self.setWindowTitle("Web Searcher")
        self.home()
    def home(self):
        self.LabelStatus = QtGui.QLabel("Search any search engine",self)
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.Engine = QtGui.QComboBox(self)
        self.Engine.move(5,50)
        self.Engine.addItems(['google','yahoo','Bing'])
        self.browserChoice = QtGui.QComboBox(self)
        self.browserChoice.move(5,25)
        Avail = PySearch.getAvailableBrowser()
        for x in Avail:
            self.browserChoice.addItem(x)
        # self.LabelA = QtGui.QLabel("Enter Search String",self)
        # self.LabelA.move(5,75)
        self.SearchString =QtGui.QLineEdit('Enter required search' ,self)
        self.SearchString.setFixedWidth(175)
        self.SearchString.move(5,100)

        self.Button = QtGui.QPushButton('click to search',self)

        self.Button.move(20,125)
        self.Button.clicked.connect(self.Searcher)
    def Searcher(self):
        SearchString = str(self.SearchString.text())
        myBrowser = str(self.browserChoice.currentText())
        myEngine = str(self.Engine.currentText())
        PySearch.goSearch(myBrowser,SearchString)

if __name__=="__main__":
    #print PySearch.urls
    app = QtGui.QApplication(sys.argv)
    SearchWindow = SearchWindowClass()
    SearchWindow.show()
    app.exec_()
