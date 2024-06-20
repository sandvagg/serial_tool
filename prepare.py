import os, sys
import getpass, platform
from configparser import ConfigParser
from logging import getLogger

# available in linux only
try:
    import grp
except ModuleNotFoundError:
    pass

log = getLogger(__name__)


class CheckPermissonsClass:
    def __init__(self):
        pass

    def check_permissions(self):
        self.user_groups = []
        for each in os.getgroups():
            self.user_groups.append(grp.getgrgid(each).gr_name)
        if 'dialout' in self.user_groups:
            log.debug('User have permissions')
        else:
            log.error('User have\'nt permissions')

class SettingsClass:
    def __init__(self):
        self.config = ConfigParser()
        try:
            self.base_path = sys._MEIPASS
        except Exception:
            self.base_path = os.path.abspath('.')
        self.load_settings(self.base_path)

    def load_settings(self, base_path):
        self.settings_path = os.path.join(self.base_path, 'settings.ini')
        if (os.path.isfile(self.settings_path)):
            try:
                self.config.read(self.settings_path)
                if 'default' in self.config.sections():
                    log.info('Settings loaded')
                    pass
                else:
                    log.warning('Restoring default settings')
                    self.restore_default_settings()
            except:
                log.info('Creating settings file')
                self.restore_default_settings()
                log.info('Created settings file')
        else:
            self.restore_default_settings()

    def restore_default_settings(self):
        while True:
            try:
                self.default_settings = [['available_speeds', '9600,14400,19200,38400,56000,57600,115200,128000,256000'],\
                                         ['target_speed', '115200'], ['tpreambuleval', '55AA'], ['tpreambulecheck', 'False'],\
                                         ['tcycles', '1'], ['tmanual', 'False'], ['tcs', 'False']]
                self.config.add_section('default')
                for each in self.default_settings:
                    self.config['default'][each[0]] = each[1]
                with open(self.settings_path, 'w') as configfile:
                    self.config.write(configfile)
                log.info('Default settings restored')
                break
            except Exception:
                for each in self.config.sections():
                    self.config.remove_section(each)
                log.warning('Custom settings was deleted')

    def write_settings(self, section, parameter, value):
        self.config[section][parameter] = value
        with open(self.settings_path, 'w') as configfile:
            self.config.write(configfile)

    def read_parameter(self, section, parameter):
        if self.config.has_option(section,parameter):
            return self.config.get(section,parameter)
        else:
            return self.config.get('default',parameter)

    def read_parameters(self, section):
        self.parameters = self.config.items(section)
        self.parameters_names = [each[0] for each in self.parameters]
        self.parameters_values = [each[1] for each in self.parameters]
        # log.debug(f'{self.parameters_names}\n {self.parameters_values}')
        return self.parameters_names, self.parameters_values

    def test(self):
        return self.read_parameters('default')

    def check_custom_settings(self, parameter):
        self.read_parameters('default')
        if 'custom' in self.config.sections():
            return self.read_parameter('custom', parameter)
        else:
            return False




if __name__ == '__main__':
    lin_permissions = CheckPermissonsClass()
    if platform.system() == 'Windows':
        log.debug('Windows detected')
        pass
    else:
        log.debug('Linux detected')
        lin_permissions.check_permissions()
    settings = SettingsClass()
else:
    pass
