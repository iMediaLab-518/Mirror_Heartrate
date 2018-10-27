from base import MiBand2
import sys
from requests import post
import time


# MAC = sys.argv[1]
def get_heartrate():
    MAC = "DF:2B:B6:A1:E3:8D"
    band = MiBand2(MAC, debug=True)
    band.initialize()
    try:
        band.setSecurityLevel(level="medium")
        band.authenticate()
        obj = band.start_raw_data_realtime()
        for _ in range(100):
            heart = obj.next()
            post("http://localhost:5000/heartrate", data={'heartrate': heart})
            print(heart)
        band.disconnect()
    except Exception as e:
        print(e)
        return


if __name__ == '__main__':
    while 1:
        get_heartrate()
        time.sleep(30)
