import threading
import subprocess


def f1():
    subprocess.run(["python", "-m", "ServerManagers.pharmacistmanager"])

def f2():
    subprocess.run(["python", "-m", "ServerManagers.userinterfacemanager"])

thread1 = threading.Thread(target=f1)
thread2 = threading.Thread(target=f2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
