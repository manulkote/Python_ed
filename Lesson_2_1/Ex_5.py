import subprocess

import chardet

args_ya = ["ping", "yandex.ru"]
args_yt = ["ping", "youtube.com"]
YA_PING = subprocess.Popen(args_ya, stdout=subprocess.PIPE)
YT_PING = subprocess.Popen(args_yt, stdout=subprocess.PIPE)

for line in YA_PING.stdout:
    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))

for line in YT_PING.stdout:
    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))
