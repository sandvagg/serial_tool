from prepare import *
from package_prepare import *
from logging import getLogger, basicConfig, DEBUG, INFO, WARNING, ERROR

log = getLogger()
log_format = ('%(asctime)s : %(name)15s : %(levelname)8s : %(message)s')
basicConfig(level=DEBUG, format=log_format, datefmt='%Y-%m-%d %H:%M:%S')







if __name__ == '__main__':
    log.info('Program started')
    test = TestName()
    if platform.system() == 'Windows':
        log.debug('Windows detected')
        pass
    else:
        log.debug('Linux detected')
        test.permissions()
    settings = SettingsClass()
    read_from_file = PackagePrepare()
    read_from_file.assembling_from_f(settings.base_path, 'AA')
    log.info('Program ended')
else:
    pass