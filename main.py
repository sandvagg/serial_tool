from prepare import *
from package_prepare import *
from to_serial import *
import gui
from logging import getLogger, basicConfig, DEBUG, INFO, WARNING, ERROR

log = getLogger(__name__)
log_format = ('%(asctime)s : %(name)15s : %(levelname)8s : %(message)s')
basicConfig(level=DEBUG, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')

getLogger('PyQt5').setLevel(ERROR)







if __name__ == '__main__':
    log.info('Program started')
    lin_permissions = CheckPermissonsClass()
    if platform.system() == 'Windows':
        log.debug('Windows detected')
        pass
    else:
        log.debug('Linux detected')
        lin_permissions.check_permissions()
    settings = SettingsClass()
    # read_from_file = PackagePrepare()
    # read_from_file.assembling_from_f(settings.base_path, 'AA')

    # transmit = SendSerial()
    log.debug('Start')
    # for x in range(50):
    #     transmit.package_to_send.put(binascii.unhexlify('AA'))
        # transmit.package_to_send.put(binascii.unhexlify('BBBBBBBBBBBBBBBBBBBBBB'))
        # transmit.package_to_send.put(binascii.unhexlify('CCCCCCCCCCCCCCCCCCCCCC'))
    # transmit.package_to_send.put(None)
    # proc_transceive = Process(target=transmit.package2com)
    # proc_transmit = Process(target=transmit.transmit)
    # proc_receive = Process(target=transmit.read)
    # proc_transceive.start()
    gui = gui.GuiClass()
    # proc_receive.start()
    # proc_transmit.start()

    # transmit.rx_packet.get()

    log.info('Program ended')
else:
    pass