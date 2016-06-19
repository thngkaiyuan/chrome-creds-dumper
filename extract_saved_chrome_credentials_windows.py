import win32crypt
import win32api
import re
import os
import sys
import sqlite3

def find_all_files(root_folder, rex):
    paths = []
    for root, dirs, files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                paths.append(os.path.join(root,f))
    print('Finished searching on', root_folder)
    return paths

def find_all_files_in_all_drives(file_name):
    paths = []
    rex = re.compile(file_name)
    print('Searching for Google Chrome saved passwords on your computer')
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        paths.extend(find_all_files(drive, rex))
    return paths

def dump_all_credentials():
    for db_file in find_all_files_in_all_drives("^Login Data$"):
        try:
            dump_credentials(db_file)
        except:
            print('Error dumping credentials from', db_file)
            pass

def dump_default_credentials():
    print('Dumping saved passwords from the default location on your computer')
    default_db_file = os.getenv("LOCALAPPDATA") + r'\Google\Chrome\User Data\Default\Login Data'
    dump_credentials(default_db_file)

def dump_credentials(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    for res in cursor.fetchall():
        url = res[0]
        username = res[1]
        password = win32crypt.CryptUnprotectData(res[2])[1]
        if username == '' or password == '':
            continue
        print('------------------------------------------------')
        print('URL:', url)
        print('User:', username)
        print('Pass:', password)
        print('------------------------------------------------')

if __name__ == '__main__':
    if len(sys.argv) > 1 and '-a' in sys.argv[1]:
        dump_all_credentials()
    else:
        dump_default_credentials()
