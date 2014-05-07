import os
import subprocess

class NoAirport(Exception):
    def __init__(self, error):
        print(error)

def airport_util():
    """Returns the XML output of the OSX command line WiFi utility as a string.
    """
    airport_util_path = "/System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport"
    if not os.path.exists(airport_util_path):
        raise NoAirport('Airport utility could not be found.')
    airport_util_cmd = subprocess.check_output([airport_util_path, "-s", "-x"])
    return airport_util_cmd.decode("utf-8")

def main():
    print(airport_util())

if __name__ == '__main__':
    main()
