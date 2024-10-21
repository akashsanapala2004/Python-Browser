import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
class MainWin(QMainWindow):
    def __init__(self):
        super(MainWin,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://search.brave.com/'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar  = QToolBar()
        self.addToolBar(navbar)

        back_btn = QAction('Venakki',self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        frwd_btn = QAction('Mundiki',self)
        frwd_btn.triggered.connect(self.browser.forward)
        navbar.addAction(frwd_btn)

        reload_btn = QAction('Relaoad',self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)
        
        home_btn = QAction('Home',self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)
        self.url_bar =  QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)

        self.browser.urlChanged.connect(self.update_url)
    def navigate_home(self):
        '''# Correctly formatting the local file path
        file_url = QUrl.fromLocalFile('C:/path/to/your/localfile.html')
        self.browser.setUrl(file_url)'''
        self.browser.setUrl(QUrl('https://search.brave.com/'))
    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))
    def update_url(self,q):
        self.url_bar.setText(q.toString())

app = QApplication(sys.argv)
QApplication.setApplicationName("Edo Oka try Esa")
window = MainWin()
app.exec_()
    
