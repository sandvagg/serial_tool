from PyQt5.QtCore import QObject, pyqtSignal
from PyQt5 import QtWidgets, uic
import prepare, os
import serial.tools.list_ports
import to_serial

from logging import getLogger, basicConfig, DEBUG, INFO, WARNING, ERROR
log = getLogger(__name__)
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
        self.set_default_settings()

        self.ui.listports.activated.connect(self.setting_comport)
        self.ui.scanButton.clicked.connect(self.scan_ports)
        self.ui.PortInfoButton.clicked.connect(self.port_info)

        self.serial = to_serial.SendSerial()

        self.ui.show()
        self.app.exec()

    def set_default_settings(self):
        self.scan_ports()
        # self.available_speeds = (self.settings.check_custom_settings('available_speeds'))
        self.parameters_names, self.parameters_values = self.settings.test()
        log.debug(f'{self.parameters_names}\n {self.parameters_values}')

    def setting_comport(self):
        log.debug('setting port')
        if self.ui.listports.currentText() == 'No COM ports':
            self.ui.manOpen.setEnabled(False)
            self.ui.manClose.setEnabled(False)
            self.ui.startButton.setEnabled(False)
            self.ui.stopButton.setEnabled(False)
        else:
            self.serial.ser.port = self.ui.listports.currentText()

    def scan_ports(self):
        self.ui.listports.clear()
        self.ui.listports.addItems(self.list_ports())

    def list_ports(self):
        self.available_ports = serial.tools.list_ports.comports()
        self.available_ports_list = []
        for each in self.available_ports:
            self.available_ports_list.append(each.device)
        if not self.available_ports_list:
            self.available_ports_list.append('No COM ports')
            return self.available_ports_list
        else:
            return self.available_ports_list

    def port_info(self):
        self.ser_status = 'Opened' if self.serial.ser.is_open else 'Closed'
        self.ui.PortInfoLine.setText(str(self.serial.ser.port) + ', ' + str(self.serial.ser.baudrate) + ', ' + self.ser_status)






if __name__ == '__main__':

    gui = GuiClass()

else:
    pass