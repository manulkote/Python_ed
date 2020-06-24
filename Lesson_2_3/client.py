from socket import SOCK_STREAM, socket
from sys import argv

import json
import time

addr = argv[1]
if len(argv[1:]) < 2:
    port = 7777
else:
    port = int(argv[2])
sock = socket(type=SOCK_STREAM)
statuses = {200: 'OK', 500: 'NOT OKAY'}
msg_dict = {
    "action": "presence",
    "time": time.strftime('%c', time.gmtime()),
    "type": "status",
    "user": {
        "account_name": "user",
        "status": "Yep, I am here!"
    }
}
msg_byte = json.dumps(msg_dict).encode('utf-8')
sock.connect((addr, port))
sock.send(msg_byte)

data = sock.recv(1024)
sock.close()
obj = json.loads(data.decode('utf-8'))
status = obj['response']
print(statuses[status])
