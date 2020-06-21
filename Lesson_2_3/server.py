from socket import SOCK_STREAM, socket
from sys import argv

import json
import time

list_args = argv[1:]
dict_args = dict(((list_args[i], list_args[i + 1]) for i in range(0, len(list_args), 2)))

if '-p' in dict_args:
    dict_args['-p'] = int(dict_args['-p'])
else:
    dict_args['-p'] = 7777
if '-a' in dict_args:
    pass
else:
    dict_args['-a'] = ''
sock = socket(type=SOCK_STREAM)
sock.bind((dict_args['-a'], dict_args['-p']))
sock.listen(1)
conn, addr = sock.accept()

try:
    while True:
        data = conn.recv(1024)
        if not data:
            break
        msg_resp = {
            "response": 200,
            "time": time.strftime('%c', time.gmtime())
        }
        msg_byte = json.dumps(msg_resp).encode('utf-8')
        conn.send(msg_byte)
finally:
    conn.close()
