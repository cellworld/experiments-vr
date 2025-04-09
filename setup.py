import datetime
from colorama import Fore, Style, init
import os
init(autoreset=True)

class Log:
    def __init__(self, name='LOG', use_time=True):
        self.name = name
        self.use_time = use_time

    def _format(self, level, msg, color=''):
        time_str = f'[{datetime.datetime.now().strftime("%H:%M:%S")}]' if self.use_time else ''
        return f'{color}{time_str}[{self.name}][{level}] {msg}{Style.RESET_ALL}'

    def log(self, msg):
        print(self._format('LOG', msg))

    def warning(self, msg):
        print(self._format('WARNING', msg, Fore.YELLOW))

    def error(self, msg):
        print(self._format('ERROR', msg, Fore.RED))

    def success(self, msg):
        print(self._format('SUCCESS', msg, Fore.GREEN))


# if __name__ == '__main__':
#     log = Log('SETUP')
#     log.log("This is a regular log message")
#     log.warning("This is a warning")
#     log.error("This is an error")
#     log.success("This is a success message")

log = Log('SETUP')

cellworld_cache_env_var = 'CELLWORLD_CACHE'
cellworld_cache_folder = os.environ.get(cellworld_cache_env_var)

if not cellworld_cache_folder: 
    log.warning(f'Cellworld cache folder not found! Make sure to set new SYSTEM Environment Variable: {cellworld_cache_env_var}:<path/to/cellworld_cache>') 
else: 
    log.success('Cellworld cache environment variable found.')

# print(cellworld_cache_folder)
log.success('Finished setup SUCCESS.')
