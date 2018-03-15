import telnetlib

tn = telnetlib.Telnet(ip, timeout)
tn.read_util('Username:', timeout)
tn.write(username + '\n')
tn.read_util('Password:', timeout)
tn.write(passwoed + '\n')
