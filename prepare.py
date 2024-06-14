import os, sys
import getpass, grp
from configparser import ConfigParser


class TestName:
    def __init__(self):
        pass
    def permissions(self):
        self.user_groups = []
        for each in os.getgroups():
            self.user_groups.append(grp.getgrgid(each).gr_name)
        if 'dialout' in self.user_groups:
            return print('yes')
        else:
            return print('no')

class SettingsClass:
    def __init__(self):
        self.config = ConfigParser()
        try:
            self.base_path = sys._MEIPASS
        except Exception:
            self.base_path = os.path.abspath('.')
        self.settings_path = os.path.join(self.base_path, 'settings')
        if (os.path.isfile(self.settings_path)):
            try:
                self.config.read(self.settings_path)
                print('readed')
                if 'default' in self.config.sections():
                    print('default')
                    pass
                else:
                    print("not default")
                    self.write_settings()
            except:
                print('no sections')
                self.write_settings()
            # print(self.config.sections())
            # if 'default' in self.config:
            #     print('default')
            # else:
            #     print('no section')
        else:
            self.write_settings()
    def write_settings(self):
        print('write settings')



if __name__ == '__main__':
    test = TestName()
    test.permissions()
    settings = SettingsClass()
else:
    pass
