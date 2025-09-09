import threading
import subprocess

def f1():
    subprocess.run(["python", "-m", "ServerManagers.pharmacistmanager"])

def f2():
    subprocess.run(["python", "-m", "ServerManagers.userinterfacemanager"])

def f3():
    subprocess.run(["python", "-m", "ServerManagers.standalonemanager"])

def f4():
    subprocess.run(["python", "-m", "ServerManagers.hardwaremanager"])

thread1 = threading.Thread(target=f1)
thread2 = threading.Thread(target=f2)
thread3 = threading.Thread(target=f3)
thread4 = threading.Thread(target=f4)

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()
