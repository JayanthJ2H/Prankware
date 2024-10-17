import os

def system(command):
    if(command == 'shutdown'):
        os.system("shutdown /s /t 1")
    elif(command == 'restart'):
        os.system("shutdown /r /t 1")
    elif(command == 'lock'):
        os.system("rundll32.exe user32.dll,LockWorkStation")
    
