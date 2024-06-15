import binascii
import os, sys
from configparser import ConfigParser
from logging import getLogger

log = getLogger(__name__)

class PackagePrepare:
    def read_file(self, base_path):
        self.test_list = []
        with open((os.path.join(base_path, 'commands.txt')), 'r') as file:
            self.raw = [line.rstrip().replace(' ', '') for line in file]
            log.debug(f'Read from file: {self.raw}')
            if self.input_file_control(self.raw):
                # self.calc_cs(self.raw)
                for element in self.raw:
                    self.test_list.append(binascii.unhexlify(element))
                    log.debug(self.test_list)
                    log.debug(sum(self.test_list))
                return self.raw
            else:
                return None
    def input_file_control(self, data):
        if all([self.hex_control(each) and self.byte_len_control(each) is True for each in data]):
            log.info('Commands is ok')
            return True
        else:
            log.error('Commands is in an incorrect format. Hexadecimal bytes expected.')
            return False
    def hex_control(self, data):
        try:
            int(data, 16)
            return True
        except ValueError:
            return False
        except TypeError:
            return False

    def byte_len_control(self, data):
        if len(data) % 2 == 0:
            return True
        else:
            return False


    def int_control(self, data):
        try:
            int(data, 10)
            return True
        except TypeError:
            return False

    def calc_cs(self, data):
        # for self.each in data:
        #     log.debug(f'data = {int.from_bytes(self.each)}, data type = {type(int.from_bytes(self.each))}')
        self.check_sum = 0
        for each_line in range(len(data)):
            for each_char in range(len(each_line)):
                log.debug(int.from_bytes(data[each_line][each_char:each_char+1]))
                self.check_sum += int.from_bytes(data[each_line][each_char:each_char+1])







if __name__ == "__main__":
    pass
else:
    pass