import binascii
import os
from logging import getLogger

log = getLogger(__name__)


class PackagePrepare:

    def assembling_from_f(self, base_path, preambule):
        self.convert2bytes = []
        self.commands_path = os.path.join(base_path, 'commands.txt')
        if os.path.isfile(self.commands_path):
            self.raw_file = self.read_file(self.commands_path)
            self.raw_w_preambule = [preambule + self.each for self.each in self.raw_file]
            log.debug(f'Packet from file with preambule: {self.raw_w_preambule}')
            [self.convert2bytes.append(binascii.unhexlify(self.each)) for self.each in self.raw_w_preambule]
            log.debug('Start calculating checksum')
            return self.calc_cs_mod8(self.convert2bytes)
        else:
            log.error('File with commands does not exist or no read permissions.')


    def read_file(self, commands_path):
        with open(self.commands_path, 'r') as file:
            self.raw = [line.rstrip().replace(' ', '') for line in file]
            log.debug(f'Read from file: {self.raw}')
            if self.input_file_control(self.raw):
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

    def calc_cs_mod8(self, data):
        self.sum = 0
        self.packet_w_cs = []
        for self.each_line in range(len(data)):
            for each_byte in range(len(data[self.each_line])):
                self.sum += int.from_bytes(data[self.each_line][each_byte:each_byte+1])
            self.check_sum = self.sum % 8
            log.debug(f'checksum for {data[self.each_line]} and sum {self.sum}: {self.check_sum}')
            self.sum = 0
            self.packet_w_cs.append(data[self.each_line] + self.check_sum.to_bytes())
        log.debug(f'Packet with checksum: {self.packet_w_cs}')
        return self.packet_w_cs








if __name__ == "__main__":
    pass
else:
    pass