from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_AdminPage(object):
    def setupUi(self, AdminPage, switch_to_main):
        AdminPage.setObjectName("AdminPage")
        AdminPage.resize(1081, 812)
        self.centralwidget = QtWidgets.QWidget(parent=AdminPage)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setText("ANA MENU")
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 200, 40))
        self.pushButton_5.clicked.connect(switch_to_main)

 # Admin sayfasındaki butonlar ve içerik
        self.pushButton_admin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_admin.setText("ADMIN PANEL")
        self.pushButton_admin.setGeometry(QtCore.QRect(50, 100, 200, 40))

        AdminPage.setCentralWidget(self.centralwidget)

    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admin Panel"))


class Ui_MainWindow(object):
    def setupUi(self, MainWindow, switch_to_preferences, switch_to_admin):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 701)
        MainWindow.setStyleSheet("QPushButton {\n"
"    font: 11pt \"MS Shell Dlg 2\";\n"
"    background-color: white; /* Beyaz arka plan */\n"
"    color: black; /* Siyah yazı rengi */\n"
"    border: 2px solid gray; /* Gri kenarlık (opsiyonel) */\n"
"    border-radius: 5px; /* Kenarları yuvarlak yapmak için */\n"
"}")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(170, 170, 201, 71))
        self.label.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 260, 201, 71))
        self.label_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(472, 390, 231, 51))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.login_check)

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(470, 480, 231, 51))
        self.pushButton_2.setObjectName("pushButton_2")

        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 190, 341, 41))
        self.lineEdit.setObjectName("lineEdit")

        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 270, 341, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.switch_to_preferences = switch_to_preferences
        self.switch_to_admin = switch_to_admin

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "KULLANICI ADI:"))
        self.label_2.setText(_translate("MainWindow", "PAROLA:"))
        self.pushButton.setText(_translate("MainWindow", "GIRIS YAP"))
        self.pushButton_2.setText(_translate("MainWindow", "CIKIS"))

    def login_check(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        if username == "mehmet" and password == "itforever":
            # Kullanıcı doğru bilgileri girdi, kullanici sayfasına geçiş yapıyoruz
            self.switch_to_preferences()
        elif username == "selim" and password == "cyber_warrior":
            self.switch_to_preferences()
        elif username == "s" and password == "d":
            self.switch_to_preferences()
        elif username == "ahmet" and password == "werhere":
            # kullanıcı adı ve şifre doğruysa admin sayfasına geçiş
            self.switch_to_admin()
        elif username == "a" and password == "b":
            self.switch_to_admin()
        elif username == "q" and password == "w":
            self.switch_to_admin()
        
class Ui_PreferencesPage(object):
    def setupUi(self, PreferencesPage, switch_to_main):
        PreferencesPage.setObjectName("PreferencesPage")
        PreferencesPage.resize(1081, 812)
        
        self.centralwidget = QtWidgets.QWidget(parent=PreferencesPage)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setText("ANA MENU")
        self.pushButton_5.setGeometry(QtCore.QRect(50, 50, 200, 40))
        self.pushButton_5.clicked.connect(switch_to_main)

        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setText("KAPAT")
        self.pushButton_4.setGeometry(QtCore.QRect(50, 100, 200, 40))

        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setText("BASVURULAR")
        self.pushButton.setGeometry(QtCore.QRect(50, 200, 200, 40))

        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setText("MULAKATLAR")
        self.pushButton_2.setGeometry(QtCore.QRect(50, 250, 200, 40))

        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setText("MENTOR GORUSMESI")
        self.pushButton_3.setGeometry(QtCore.QRect(50, 300, 200, 40))

        PreferencesPage.setCentralWidget(self.centralwidget)

    def retranslateUi(self, PreferencesPage):
        _translate = QtCore.QCoreApplication.translate
        PreferencesPage.setWindowTitle(_translate("PreferencesPage", "User Panel"))


class MainApp(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.main_window_ui = Ui_MainWindow()
        self.preferences_page_ui = Ui_PreferencesPage()
        self.admin_page_ui = Ui_AdminPage()

        self.setWindowTitle("Login Page")
        self.setGeometry(100, 100, 1012, 701)

        self.stacked_widget = QtWidgets.QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        # Giriş sayfasını ekliyoruz
        self.main_window = QtWidgets.QMainWindow(self)
        self.main_window_ui.setupUi(self.main_window, self.show_preferences_page, self.show_admin_page)
        self.stacked_widget.addWidget(self.main_window)

        # Kullanici sayfasını ekliyoruz
        self.preferences_page = QtWidgets.QMainWindow(self)
        self.preferences_page_ui.setupUi(self.preferences_page, self.show_main_page)
        self.stacked_widget.addWidget(self.preferences_page)

        # Admin sayfasını ekliyoruz
        self.admin_page = QtWidgets.QMainWindow(self)
        self.admin_page_ui.setupUi(self.admin_page, self.show_main_page)
        self.stacked_widget.addWidget(self.admin_page)

    def show_preferences_page(self):
        # Giriş sayfasından kullanici sayfasına geçiş yap
        self.stacked_widget.setCurrentWidget(self.preferences_page)

    def show_main_page(self):
        # Kullanici sayfasından giriş sayfasına geçiş yap
        self.stacked_widget.setCurrentWidget(self.main_window)

    def show_admin_page(self):
        # Admin sayfasına geçiş yap
        self.stacked_widget.setCurrentWidget(self.admin_page)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    main_app = MainApp()
    main_app.show()
    sys.exit(app.exec())
