from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtWidgets, uic
import prepare, os

from logging import getLogger, basicConfig, DEBUG, INFO, WARNING, ERROR
log = getLogger()
log_format = ('%(asctime)s : %(name)15s : %(levelname)8s : %(message)s')
basicConfig(level=DEBUG, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

class GuiClass:
    def __init__(self):
        self.lin_permission = prepare.CheckPermissonsClass()
        self.settings = prepare.SettingsClass()
        self.app = QtWidgets.QApplication([])
        self.ui_file = os.path.join(self.settings.base_path, 'test_spacer.ui')
        self.ui = uic.loadUi(self.ui_file)

        self.lin_permission.check_permissions()
        self.ui.show()
        self.app.exec()





if __name__ == '__main__':

    gui = GuiClass()

else:
    pass