from PyQt4 import QtGui
import sys
import PySearch
#gui to search a browser and an engine

class SearchWindowClass(QtGui.QWidget):
    def __init__(self):
        super(SearchWindowClass,self).__init__()
        self.setGeometry(50,50,240,125)
        self.setWindowTitle("Web Searcher")
        self.home()
        self.setFixedSize(240,125)
    def home(self):

        #label for what combo boxes do
        self.labelB = QtGui.QLabel("BROWSER",self)
        self.labelB.move(50,5)

        self.labelE = QtGui.QLabel("ENGINE",self)
        self.labelE.move(170,5)

        #combo box to choose browser to search, only displays browsers available to use
        self.browserChoice = QtGui.QComboBox(self)
        self.browserChoice.move(5,25)

        #getting available search engines
        Avail = PySearch.getAvailableBrowser()
        for x in Avail:
            self.browserChoice.addItem(x)

        #combo box to choose which search engine to use Google, Yahoo, or Bing
        self.Engine = QtGui.QComboBox(self)
        self.Engine.move(160,25)
        self.Engine.addItems(['Google','Yahoo','Bing'])

        #text box to take search string
        self.SearchString =QtGui.QLineEdit('Enter required search' ,self)
        self.SearchString.setFixedWidth(230)
        self.SearchString.move(5,60)

        #search button
        self.Button = QtGui.QPushButton('click to search',self)
        self.Button.move(65,90)
        self.Button.clicked.connect(self.Searcher)

    def Searcher(self):
        #collects engine, browser, and search string and sends it to searcher
        SearchString = str(self.SearchString.text())
        myBrowser = str(self.browserChoice.currentText())
        myEngine = str(self.Engine.currentText())
        PySearch.goIndSearch(myBrowser,SearchString,myEngine)

if __name__=="__main__":

    app = QtGui.QApplication(sys.argv)
    SearchWindow = SearchWindowClass()
    SearchWindow.show()
    app.exec_()
