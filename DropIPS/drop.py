import os
for ip in open('ips.txt', 'r'):
    print(f"Dropping {ip}")
    os.system(f"sudo iptables -A INPUT -s {ip}/32 -d 0/0 -j DROP")