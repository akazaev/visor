import os
from os.path import expanduser

import paramiko

home = expanduser("~")
try:
    key = paramiko.RSAKey.from_private_key_file(os.path.join(home, "key.pem"))
except:
    key = None

default_usename = 'pi'
default_password = 'raspberry'
default_key_path = ''

pass_stands = [
    '192.168.0.4',
]

key_stands = [
]

users = {
    '192.168.0.2': 'Alexey',

}

ports = [22, 80]
