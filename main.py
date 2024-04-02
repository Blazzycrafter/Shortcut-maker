# imports
import os


# classes
class BCOLOR:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


class logger:
    def __init__(self, log_type):
        # log type can be 'error', 'warning', 'info', 'debug'
        self.log_type = log_type

    def info(self, *args):
        print(f"{BCOLOR.OKGREEN}{BCOLOR.BOLD}[LOG]{BCOLOR.ENDC} " + " ".join(map(str, args)))

    def error(self, *args):
        print(f"{BCOLOR.FAIL}{BCOLOR.BOLD}[ERROR]{BCOLOR.ENDC} " + " ".join(map(str, args)))

    def warning(self, *args):
        print(f"{BCOLOR.WARNING}{BCOLOR.BOLD}[WARNING]{BCOLOR.ENDC} " + " ".join(map(str, args)))

    def debug(self, *args):
        if self.log_type == 'debug':
            print(f"{BCOLOR.OKCYAN}{BCOLOR.BOLD}[DEBUG]{BCOLOR.ENDC} " + " ".join(map(str, args)))


class Platform:
    def __init__(self):
        self.os = os.name
    clear = 'cls' if os.name == 'nt' else 'clear'

# global variables
DEBUG = False

l = logger('info')
if DEBUG:
    l.log_type = 'debug'
    l.info('Debug mode enabled')


p = Platform()
username = None





def init():
    if not os.name == 'nt':
        print('This program only works on Windows')
        exit()
    # get user name
    global username
    username = os.getlogin()
    l.debug(f'Username: {username}')
    # check if path exist:
    ## C:\Users\username\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\shortcut_maker

    if os.path.exists('C:\\Users\\' + username + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\shortcut_maker'):
        l.debug('Path exist')
    else:
        l.debug('Path does not exist')
        # explain to user that path does not exist and ask if they want to create it
        print('The Start Menu path for this program (Shortcut Maker) does not exist')
        q = input('do you want to create it? (y/n): ')
        if q == 'y':
            os.mkdir('C:\\Users\\' + username + '\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\shortcut_maker')
        else:
            print('exiting program')
            exit()



def main():
    if not DEBUG: os.system(p.clear)
    print("Name: ")
    print("Path: ")
    print(f"Icon: {BCOLOR.FAIL}{BCOLOR.BOLD}PLANNED{BCOLOR.ENDC}")
    while True:
        name = input('what is the name of the new Shortcut: ')
        if name == "":
            print("please enter a name")
            continue
        else:
            break
    if not DEBUG: os.system(p.clear)
    print("Name: "+name)
    print("Path: ")
    print(f"Icon: {BCOLOR.FAIL}{BCOLOR.BOLD}PLANNED{BCOLOR.ENDC}")
    while True:
        path = input('what is the path of the new Shortcut: ')
        if path == "":
            print("please enter a path")
            continue
        else:
            break
    if not DEBUG: os.system(p.clear)
    print("Name: "+name)
    print("Path: "+path)
    print(f"Icon: {BCOLOR.FAIL}{BCOLOR.BOLD}PLANNED{BCOLOR.ENDC}")
    last_check = input('are you sure you want to create this Shortcut? (y/n): ')
    if last_check == 'y':
        l.info('Shortcut created')
        os.system(f'mklink "C:\\Users\\{username}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\shortcut_maker\\{name}" "{path}"')
    else:
        l.info('Shortcut not created')

if __name__ == '__main__':
    init()
    main()