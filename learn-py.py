import threading
import time

def deamon():
    print('Starting')
    time.sleep(2)
    print('Exiting')

x = threading.Thread(target=deamon, daemon=True)

x.start()

print('Main thread exiting')
print(x.daemon)