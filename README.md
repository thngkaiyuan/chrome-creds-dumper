# Google Chrome Saved Passwords Dumper (Windows)

Dump login credentials saved by Google Chrome, just for fun :)

![image](https://cloud.githubusercontent.com/assets/10496851/17859952/1d45f368-68be-11e6-8fbb-e021d06ac4a5.png)

## Download 
- The compiled binary for x86-64 machines can be found in [dist/extract_saved_chrome_credentials_windows.exe](https://github.com/thngkaiyuan/chrome-creds-dumper/blob/master/dist/extract_saved_chrome_credentials_windows.exe?raw=true)
- The (uncompiled) script is named [extract_saved_chrome_credentials_windows.py](https://raw.githubusercontent.com/thngkaiyuan/chrome-creds-dumper/master/extract_saved_chrome_credentials_windows.py) in the repository's root directory

## Usage
To dump saved passwords from the default location, execute
`extract_saved_chrome_credentials_windows.exe`

To search for all instances of `Login Data` on your computer before dumping the saved passwords in them, execute `extract_saved_chrome_credentials_windows.exe -a`

## Todo

Compile 32-bit version of binary
