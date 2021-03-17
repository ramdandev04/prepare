import os
import requests
import socket

def clonerep():
    s = "https://github.com/ramdandev04/product-installations.git /etc/sun/i"
    os.system('git clone {}'.format(s))

clonerep()

os.system('cp reb.py /usr/bin')

def one():
    f = open('/etc/rc.local', 'r')
    st = f.read()
    st = st.replace('exit 0', '')
    f.close()
    w = open('/etc/rc.local', 'w')
    w.write(st)
    w.close()

one()

def two():
    f = open('/etc/rc.local', 'a')
    f.write("python3 /usr/bin/reb.py &\nexit 0")
    f.close()

two()

def three():
    f = open('/etc/sun/i/installer/installer/settings.py', 'r')
    fr = f.read()
    fr = fr.replace("###<----->###", socket.gethostbyname(socket.gethostname()))
    f.close()
    w = open('/etc/sun/i/installer/installer/settings.py', 'w')
    w.write(fr)
    w.close()

three()

os.system('systemctl start rc-local && systemctl enable rc-local')