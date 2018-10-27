from base import MiBand2
import sys
from requests import post

# MAC = sys.argv[1]
MAC = "DF:2B:B6:A1:E3:8D"
band = MiBand2(MAC, debug=True)
if len(sys.argv) > 2:
    band.initialize()
    print('ok')
else:
    try:
        band.setSecurityLevel(level="medium")
        band.authenticate()
        obj = band.start_raw_data_realtime()
        for _ in range(100):
            heart = obj.next()
            post("http://localhost:5000/heartrate", data={'heartrate': heart})
            print(heart)
        band.disconnect()
    except:
        print('error')
