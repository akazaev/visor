import paramiko
import settings


command = ("netstat -tn 2>/dev/null | grep :%s | awk '{print $5}' | "
           "cut -d: -f1 | sort | uniq -c | sort -nr | head")

client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

for port in settings.ports:
    for stand in settings.pass_stands:
        print '=== %s:%s ===' % (stand, port)
        client.connect(hostname=stand, username=settings.default_usename,
                       password=settings.default_password, port=22)
        _stdin, stdout, stderr = client.exec_command(command % port)
        data = stdout.read() + stderr.read()

        for row in data.split('\n'):
            if row:
                ip_addr = row.split(' ')[-1]
                print settings.users.get(ip_addr, ip_addr)

    for stand in settings.key_stands:
        print '=== %s:%s ===' % (stand, port)
        client.connect(hostname=stand, username=settings.default_usename,
                       port=22, pkey=settings.key)
        _stdin, stdout, stderr = client.exec_command(command % port)
        data = stdout.read() + stderr.read()

        for row in data.split('\n'):
            if row:
                ip_addr = row.split(' ')[-1]
                print settings.users.get(ip_addr, ip_addr)

client.close()
