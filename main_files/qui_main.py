from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
import sys
import sql_bridge

class gui_framework(QMainWindow):
    """
    class for grafical representation of vet database
    """
    def __init__(self):
        """
        constructor of class
        """
        QMainWindow.__init__(self)

        self.my_con = None

        self.button_exit = QPushButton("Exit", self)
        self.init_ui()

    def init_ui(self):
        """
        cascade function (activating functions in correct order
        """
        self.setGeometry(100, 100, 1500, 900)
        self.setWindowTitle("Vet-base")
        self.show()

    def connect_server(self):
        """
        function for establishing connection with sql server
        """
        self.my_con = sql_bridge.establish_connection(host, user, passwd, database)

    def work_buttons(self):
        """
        function for buttons setings
        """
        self.button_exit.setGeometry(550, 495, 130, 25)
        self.button_exit.clicked.connect(sql_bridge.disconnection(self.my_conn))


def main():
    """
    Main section, system exit from application.
    """
    app = QApplication(sys.argv)
    ex_ex = gui_framework()
    sys.exit(app.exec_())

if __name__=="__main__":
    main()