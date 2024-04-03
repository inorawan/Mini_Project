from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

#adding cookie window
class WebsiteWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Preferred Websites")
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(["Website URL", "Action"])
        self.setCentralWidget(self.treeWidget)
        self.resize(800, 600)

        self.website_label = QLabel("Enter preferred website URL:")
        self.website_input = QLineEdit()
        self.add_button = QPushButton("Add Website")
        self.add_button.clicked.connect(self.add_website)

        self.website_layout = QHBoxLayout()
        self.website_layout.addWidget(self.website_label)
        self.website_layout.addWidget(self.website_input)
        self.website_layout.addWidget(self.add_button)

        self.website_groupbox = QGroupBox("Add Preferred Website")
        self.website_groupbox.setLayout(self.website_layout)

        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.website_groupbox)
        self.main_layout.addWidget(self.treeWidget)

        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        # Load preferred websites from local storage
        self.load_preferred_websites()

    def load_preferred_websites(self):
        # Load preferred websites from local storage
        settings = QSettings()
        preferred_websites = settings.value("preferred_websites", [])
        for website_url in preferred_websites:
            self.add_website_to_list(website_url)

    def add_website(self):
        website_url = self.website_input.text().strip()
        if website_url:
            self.add_website_to_list(website_url)
            self.save_preferred_websites()
            self.website_input.clear()
            self.website_input.setFocus()

    def add_website_to_list(self, website_url):
        # Add website to list
        if not website_url.startswith("http"):
            return  # Skip items that are not website URLs

        item = QTreeWidgetItem(self.treeWidget)
        item.setText(0, website_url)

        delete_button = QPushButton("Delete")
        #delete_button.setFixedSize(80, 30)  # Set fixed size for the button
        delete_button.clicked.connect(lambda: self.delete_website(item))

        self.treeWidget.setItemWidget(item, 1, delete_button)

        self.treeWidget.addTopLevelItem(item)

    def delete_website(self, item):
        website_url = item.text(0)
        self.treeWidget.takeTopLevelItem(self.treeWidget.indexOfTopLevelItem(item))
        self.save_preferred_websites()

    def save_preferred_websites(self):
        # Save preferred websites to local storage
        settings = QSettings()
        preferred_websites = [self.treeWidget.topLevelItem(i).text(0) for i in range(self.treeWidget.topLevelItemCount())]
        settings.setValue("preferred_websites", preferred_websites)


class CookieWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Cookies")
        self.treeWidget = QTreeWidget()
        self.treeWidget.setHeaderLabels(["Name", "Value", "Domain", "Path", "Expiration", "HttpOnly", "Secure", "Session"])
        self.setCentralWidget(self.treeWidget)
        self.resize(800, 600)
        #self.treeWidget.resizeColumnToContents(4)  # Adjust the width of the first column (Name)
        # self.treeWidget.resizeColumnToContents(1)  # Adjust the width of the second column (Value)
        # Repeat this for each column you want to adjust

        # Layout for input fields

        # Layout for main window
        self.main_layout = QVBoxLayout()

        self.main_layout.addWidget(self.treeWidget)

        # Set main layout
        central_widget = QWidget()
        central_widget.setLayout(self.main_layout)
        self.setCentralWidget(central_widget)

        profile = QWebEngineProfile.defaultProfile()
        cookie_store = profile.cookieStore()
        cookie_store.loadAllCookies()
        cookie_store.cookieAdded.connect(self.onCookieAdded)
        cookie_store.cookieRemoved.connect(self.onCookieRemoved)

        # Load preferred websites from local storage




    def addCookieToTree(self, cookie):
        item = QTreeWidgetItem(self.treeWidget)
        item.setText(0, cookie.name().data().decode())
        item.setText(1, cookie.value().data().decode())
        item.setText(2, cookie.domain())
        item.setText(3, cookie.path())
        item.setText(4, cookie.expirationDate().toString())
        item.setText(5, str(cookie.isHttpOnly()))
        item.setText(6, str(cookie.isSecure()))
        item.setText(7, str(cookie.isSessionCookie()))

    def onCookieAdded(self, cookie):
        self.addCookieToTree(cookie)

    def onCookieRemoved(self, cookie):
        for i in range(self.treeWidget.topLevelItemCount()):
            item = self.treeWidget.topLevelItem(i)
            if item.text(0) == cookie.name().data().decode():
                self.treeWidget.takeTopLevelItem(i)
                break



class AboutDialog(QDialog):
   def __init__(self, *args, **kwargs):
       super(AboutDialog, self).__init__(*args, **kwargs)


       QBtn = QDialogButtonBox.Ok  # No cancel
       self.buttonBox = QDialogButtonBox(QBtn)
       self.buttonBox.accepted.connect(self.accept)
       self.buttonBox.rejected.connect(self.reject)


       layout = QVBoxLayout()


       title = QLabel("Mozart")
       font = title.font()
       font.setPointSize(20)
       title.setFont(font)


       layout.addWidget(title)


       logo = QLabel()
       logo.setPixmap(QPixmap(os.path.join('images', 'ma-icon-128.png')))
       layout.addWidget(logo)


       layout.addWidget(QLabel("Version 2018.10"))
       layout.addWidget(QLabel("Copyright 2018 HTOUKOUR COGNITIVE"))


       for i in range(0, layout.count()):
           layout.itemAt(i).setAlignment(Qt.AlignHCenter)


       layout.addWidget(self.buttonBox)


       self.setLayout(layout)




class MainWindow(QMainWindow):
   def __init__(self, *args, **kwargs):
       super(MainWindow, self).__init__(*args, **kwargs)


       self.tabs = QTabWidget()
       self.tabs.setDocumentMode(True)
       self.tabs.tabBarDoubleClicked.connect(self.tab_open_doubleclick)
       self.tabs.currentChanged.connect(self.current_tab_changed)
       self.tabs.setTabsClosable(True)
       self.tabs.tabCloseRequested.connect(self.close_current_tab)


       self.setCentralWidget(self.tabs)


       self.status = QStatusBar()
       self.setStatusBar(self.status)


       navtb = QToolBar("Navigation")
       navtb.setIconSize(QSize(16, 16))
       self.addToolBar(navtb)




       #add cookie window
       self.cookie_window = CookieWindow()
       # Show the cookie window
       self.cookie_window.show()

       self.website_window = WebsiteWindow()
       # Show the cookie window
       self.website_window.show()

       back_btn = QAction(QIcon(os.path.join('images', 'arrow-180.png')), "Back", self)
       back_btn.setStatusTip("Back to previous page")
       back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
       navtb.addAction(back_btn)


       next_btn = QAction(QIcon(os.path.join('images', 'arrow-000.png')), "Forward", self)
       next_btn.setStatusTip("Forward to next page")
       next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
       navtb.addAction(next_btn)


       reload_btn = QAction(QIcon(os.path.join('images', 'arrow-circle-315.png')), "Reload", self)
       reload_btn.setStatusTip("Reload page")
       reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
       navtb.addAction(reload_btn)


       home_btn = QAction(QIcon(os.path.join('images', 'home.png')), "Home", self)
       home_btn.setStatusTip("Go home")
       home_btn.triggered.connect(self.navigate_home)
       navtb.addAction(home_btn)


       navtb.addSeparator()


       self.httpsicon = QLabel()  # Yes, really!
       self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))
       navtb.addWidget(self.httpsicon)


       self.urlbar = QLineEdit()
       self.urlbar.returnPressed.connect(self.navigate_to_url)
       navtb.addWidget(self.urlbar)


       stop_btn = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Stop", self)
       stop_btn.setStatusTip("Stop loading current page")
       stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
       navtb.addAction(stop_btn)


       # Uncomment to disable native menubar on Mac
       # self.menuBar().setNativeMenuBar(False)


       file_menu = self.menuBar().addMenu("&File")


       new_tab_action = QAction(QIcon(os.path.join('images', 'ui-tab--plus.png')), "New Tab", self)
       new_tab_action.setStatusTip("Open a new tab")
       new_tab_action.triggered.connect(lambda _: self.add_new_tab())
       file_menu.addAction(new_tab_action)


       open_file_action = QAction(QIcon(os.path.join('images', 'disk--arrow.png')), "Open file...", self)
       open_file_action.setStatusTip("Open from file")
       open_file_action.triggered.connect(self.open_file)
       file_menu.addAction(open_file_action)



       save_file_action = QAction(QIcon(os.path.join('images', 'disk--pencil.png')), "Save Page As...", self)
       save_file_action.setStatusTip("Save current page to file")
       save_file_action.triggered.connect(self.save_file)
       file_menu.addAction(save_file_action)


       print_action = QAction(QIcon(os.path.join('images', 'printer.png')), "Print...", self)
       print_action.setStatusTip("Print current page")
       print_action.triggered.connect(self.print_page)
       file_menu.addAction(print_action)
       #new feature
       del_cookies = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Delete all cookies", self)
       del_cookies.setStatusTip("Delete all cookies")
       del_cookies.triggered.connect(lambda _: self.delete_cookies())
       file_menu.addAction(del_cookies)


       #only session cookies
       del_cookies = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Delete sesssion cookies", self)
       del_cookies.setStatusTip("Delete session cookies")
       del_cookies.triggered.connect(lambda _: self.delete_session_cookies())
       file_menu.addAction(del_cookies)
       # #check_session_cookies
       # check_cookies = QAction(QIcon(os.path.join('images', 'cross-circle.png')), "Check cookies", self)
       # check_cookies.setStatusTip("Check session cookies")
       # check_cookies.triggered.connect(lambda _: self.check_session_cookies())
       # file_menu.addAction(check_cookies)


       help_menu = self.menuBar().addMenu("&Help")


       about_action = QAction(QIcon(os.path.join('images', 'question.png')), "About Mozart", self)
       about_action.setStatusTip("Find out more about Mozart")  # Hungry!
       about_action.triggered.connect(self.about)
       help_menu.addAction(about_action)


       navigate_mozarella_action = QAction(QIcon(os.path.join('images', 'lifebuoy.png')),
                                           "HTOUKOUR COGNITIVE Homepage", self)
       navigate_mozarella_action.setStatusTip("Go to HTOUKOUR COGNITIVE Homepage")
       navigate_mozarella_action.triggered.connect(self.navigate_mozarella)
       help_menu.addAction(navigate_mozarella_action)


       self.add_new_tab(QUrl('http://www.google.com'), 'Homepage')


       self.show()


       self.setWindowTitle("Mozart")
       self.setWindowIcon(QIcon(os.path.join('images', 'ma-icon-64.png')))


   def add_new_tab(self, qurl=None, label="Blank"):


       if qurl is None:
           qurl = QUrl('')


       browser = QWebEngineView()
       browser.setUrl(qurl)
       i = self.tabs.addTab(browser, label)


       self.tabs.setCurrentIndex(i)

       # More difficult! We only want to update the url when it's from the
       # correct tab
       browser.urlChanged.connect(lambda qurl, browser=browser:
                                  self.update_urlbar(qurl, browser))






       browser.loadFinished.connect(lambda _, i=i, browser=browser:
                                    self.tabs.setTabText(i, browser.page().title()))


       #handle cookie pop-up
       browser.loadFinished.connect(lambda: self.handle_cookie_popup(browser, browser.url().toString()))


   #delete all the cookies
   def delete_cookies(self):
       current_browser = self.tabs.currentWidget()
       if current_browser:
           cookie_store = current_browser.page().profile().cookieStore()
           cookie_store.deleteAllCookies()
           print("All cookies deleted.")


   # delete all the cookies
   def delete_session_cookies(self):
       current_browser = self.tabs.currentWidget()
       if current_browser:
           cookie_store = current_browser.page().profile().cookieStore()
           cookie_store.deleteSessionCookies()
           print("Session cookies deleted.")


   #handle the pop-ups

   def handle_cookie_popup(self, browser, current_url):
       def execute_js():
           print("inside")
           try:
               print("Inside the js")
               script = """var popup = document.getElementById("btn accept");
                              if (popup) {
                                  popup.click();
                                  console.log("Clicked on reject all button");
                           that    } else {
                                  console.error("Reject all button not found");
                              }
                              """
               browser.page().runJavaScript(script)

           except Exception as e:
               print("Error handling cookie popup:", e)

       def page_load_finished(ok):

           if ok:
               print("Load finished")
               QTimer.singleShot(5000, execute_js)  # Delay execution for 5 seconds
           else:
               print("Page load failed")

       settings = QSettings()
       preferred_websites = settings.value("preferred_websites", [])
       print("checking the list")


       print(preferred_websites)
       print(current_url)
       if current_url in preferred_websites:
           print("The url is present on the list")
           QTimer.singleShot(1000, execute_js)




   # def handle_cookie_popup(self, browser):
   #     print("entered the pop-up");
   #     def execute_js():
   #         try:
   #             script = """
   #             var popup = document.getElementById("onetrust-reject-all-handler");
   #             if (popup) {
   #                 popup.click();
   #                 console.log("Clicked on reject all button");
   #             } else {
   #                 console.error("Reject all button not found");
   #             }
   #             """
   #             browser.page().runJavaScript(script)
   #         except Exception as e:
   #             print("Error handling cookie popup:", e)
   #
   #     # Define a slot to handle page load finished event
   #     def page_load_finished(ok):
   #         current_url = browser.url().toString()
   #         print(current_url)
   #         with open('preferred_list.txt', 'r') as file:
   #             preferred_websites = file.readlines()
   #             preferred_websites = [url.strip() for url in preferred_websites]
   #
   #
   #         if current_url in preferred_websites:
   #             print("The website is on the list")
   #             QTimer.singleShot(1000, execute_js)  # Delay execution for 5 seconds
   #         else:
   #             print("Page load failed")
   #
   #     # Connect the page_load_finished slot to the loadFinished signal
   #     browser.loadFinished.connect(page_load_finished)


   def tab_open_doubleclick(self, i):
       if i == -1:  # No tab under the click
           self.add_new_tab()


   def current_tab_changed(self, i):
       qurl = self.tabs.currentWidget().url()
       self.update_urlbar(qurl, self.tabs.currentWidget())
       self.update_title(self.tabs.currentWidget())


   def close_current_tab(self, i):
       if self.tabs.count() < 2:
           return


       self.tabs.removeTab(i)


   def update_title(self, browser):
       if browser != self.tabs.currentWidget():
           # If this signal is not from the current tab, ignore
           return


       title = self.tabs.currentWidget().page().title()
       self.setWindowTitle("%s - Mozart" % title)


   def navigate_mozarella(self):
       self.tabs.currentWidget().setUrl(QUrl("https://htoukour.co.za"))


   def about(self):
       dlg = AboutDialog()
       dlg.exec_()


   def open_file(self):
       filename, _ = QFileDialog.getOpenFileName(self, "Open file", "",
                                                 "Hypertext Markup Language (*.htm *.html);;"
                                                 "All files (*.*)")


       if filename:
           with open(filename, 'r') as f:
               html = f.read()


           self.tabs.currentWidget().setHtml(html)
           self.urlbar.setText(filename)


   def save_file(self):
       filename, _ = QFileDialog.getSaveFileName(self, "Save Page As", "",
                                                 "Hypertext Markup Language (*.htm *html);;"
                                                 "All files (*.*)")


       if filename:
           html = self.tabs.currentWidget().page().mainFrame().toHtml()
           with open(filename, 'w') as f:
               f.write(html.encode('utf8'))


   def print_page(self):
       dlg = QPrintPreviewDialog()
       dlg.paintRequested.connect(self.browser.print_)
       dlg.exec_()


   def navigate_home(self):
       self.tabs.currentWidget().setUrl(QUrl("http://www.google.com"))


   def navigate_to_url(self):  # Does not receive the Url
       q = QUrl(self.urlbar.text())
       if q.scheme() == "":
           q.setScheme("http")


       self.tabs.currentWidget().setUrl(q)


   def update_urlbar(self, q, browser=None):


       if browser != self.tabs.currentWidget():
           # If this signal is not from the current tab, ignore
           return


       if q.scheme() == 'https':
           # Secure padlock icon
           self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-ssl.png')))


       else:
           # Insecure padlock icon
           self.httpsicon.setPixmap(QPixmap(os.path.join('images', 'lock-nossl.png')))


       self.urlbar.setText(q.toString())
       self.urlbar.setCursorPosition(0)




app = QApplication(sys.argv)
app.setApplicationName("Mozart")
app.setOrganizationName("HTOUKOUR COGNITIVE")
app.setOrganizationDomain("htoukour.co.za")


window = MainWindow()


app.exec_()

