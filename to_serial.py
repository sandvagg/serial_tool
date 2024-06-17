import time, serial
from serial import Serial
from multiprocessing import Queue, Process
from logging import getLogger
import binascii

log = getLogger(__name__)

class SendSerial:
    def __init__(self):
        self.ser = Serial()
        self.ser.baudrate = 115200
        self.ser.bytesize = serial.EIGHTBITS
        self.ser.parity = serial.PARITY_NONE
        self.ser.stopbits = serial.STOPBITS_ONE
        self.ser.port = ('/dev/ttyUSB0')
        self.ser.open()

        self.ser.timeout = 0.01
        self.sleep_time = 0.004993
        self.num_bytes = 11

        self.package_to_send = Queue()
        self.rx_packet = Queue()

    def package2com(self):
        while True:
            log.debug('Entered in loop')
            try:
                self.next_time = time.time() + self.sleep_time
                self.data = self.package_to_send.get()
                log.debug(f'Data to send: {self.data}')
                if self.data is None:
                    self.rx_packet.put(None)
                    log.debug('End of transmission')
                    break
                else:
                    self.ser.write(self.data)
                    log.debug(f'Transmitted')
                    self.receive    = self.ser.read(self.num_bytes)
                    log.debug(f'Recieved: {self.receive}')
                    if not self.rx_packet.full():
                        self.rx_packet.put(self.receive)
                    log.debug('Recieved package transferred')
                while time.time() < self.next_time:
                    time.sleep(0.00000000000001)

            except KeyboardInterrupt:
                break
        log.debug('Exit from loop')

    def transmit(self):
        while True:
            log.debug('Start transmit')
            try:
                self.next_time = time.time() + self.sleep_time
                self.data = self.package_to_send.get()
                log.debug(f'Data to send: {self.data}')
                if self.data is None:
                    # self.rx_packet.put(None)
                    log.debug('End of transmission')
                    break
                else:
                    self.ser.write(self.data)
                    log.debug(f'Transmitted')
            except KeyboardInterrupt:
                break

    def read(self):
        while True:
            log.debug('Start receive')
            try:
                self.receive = self.ser.readline()
                log.debug(f'Recieved: {self.receive}')
                if not self.rx_packet.full():
                    self.rx_packet.put(self.receive)
                # log.debug('Recieved package transferred')
            except KeyboardInterrupt:
                break

if __name__ == "__main__":
    transmit = SendSerial()
    log.debug('Start')
    transmit.package_to_send.put(binascii.unhexlify('AAAAAAAAAAAAAAAAAAAAAA'))
    proc_transmit = Process(target=transmit.package2com())
    transmit.rx_packet.get()
    log.debug('Finish')

else:
    pass