import sys
import ctypes
from start import startApp

def check_single_instance():
    mutex_name = "prankware"
    mutex = ctypes.windll.kernel32.CreateMutexW(None, True, mutex_name)

    if ctypes.windll.kernel32.GetLastError() == 183:
        return False
    return True

if __name__ == "__main__":
    if not check_single_instance():
        sys.exit(0)

    startApp()
