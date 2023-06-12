#!/usr/bin/python3
import requests, json, os, sys, random
username    = (sys.argv[1])
password    = (sys.argv[2])
host        = (sys.argv[3])
ip          = (sys.argv[4])
user        = "ansible"
usernames   = (username.split(','))
hosts       = (host.split(','))
ips         = (ip.split(','))

for host in hosts:
    try:
        index = (hosts.index(host))
        ip = (ips[index])
        cmd = "sshpass -p " + password + " ssh -o StrictHostKeyChecking=no" + user "@" + ip + " 'cat /etc/*-release | grep ^VERSION= | cut -d= -f2' > /tmp/so.txt"
        os.system(cmd)
        with open("/tmp/so.txt", "r") as outfile:
            so = (outfile.read())
        replaced = (so.replace('"', ''))
        so = int(replaced[0])
        if so > 6:
            cmd = "bash /scripts/cockpit.hosts.sh " + host + " " + ip + " step1"
            os.system(cmd)
            with open("/tmp/cockpit_check.txt", "r") as outfile:
                result = (outfile.read())
            num = int(result)
            if num == 0:
                hexcolor = ("#{:06x}".format(random.randint(0, 0xFFFFFF)))
                dictionary = {
                    f"{host}": {
                        "visible" : "true",
                        "color" : f"{hexcolor}",
                        "user" : f"{user}",
                        "address" : f"{host}"
                        }
                        }
                json_object = json.dumps(dictionary, indent=4)
                with open("/etc/cockpit/machines.d/" + host + ".json", "w") as outfile:
                    outfile.write(json_object)
                for username in usernames:
                    cmd = "sshpass -p " + password + " ssh-copy-id -i /home/" + username + "/.ssh/id_rsa.pub -o StrictHostKeyChecking=no" + user "@" + ip
                    os.system(cmd)
            else:
                continue
    except BaseException as e:
        index = (hosts.index(host))
        ip = (ips[index])
        cmd = "sshpass -p " + password + " ssh -o StrictHostKeyChecking=no" + user + "@" + ip + " 'cat /etc/*-release | grep ^VERSION= | cut -d= -f2' > /tmp/so.txt"
        os.system(cmd)
        with open("/tmp/so.txt", "r") as outfile:
            so = (outfile.read())
        replaced = (so.replace('"', ''))
        print("Erro adicionar chave: " + host + " - SO: " + replaced + " - Erro: " + str(e))
        continue
    
for host in hosts:
    try:
        index = (hosts.index(host))
        ip = (ips[index])
        cmd = "sshpass -p " + password + " ssh -o StrictHostKeyChecking=no" + user + "@" + ip + " 'cat /etc/*-release | grep ^VERSION= | cut -d= -f2' > /tmp/so.txt"
        os.system(cmd)
        with open("/tmp/so.txt", "r") as outfile:
            so = (outfile.read())
        replaced = (so.replace('"', ''))
        so = int(replaced[0])
        if so > 6:
            cmd = "bash /scripts/cockpit.hosts.sh " + host + " " + ip + " step2"
            os.system(cmd)
            with open("/tmp/cockpit_check.txt", "r") as outfile:
                result = (outfile.read())
            num = int(result)
            if num == 0:
                for username in usernames:
                    cmd = "ssh-keyscan " + host + " >> /home/" + username + "/.ssh/known_hosts"
                    os.system(cmd)
            else:
                continue
    except BaseException as e:
        index = (hosts.index(host))
        ip = (ips[index])
        cmd = "sshpass -p " + password + " ssh -o StrictHostKeyChecking=no" + user + "@" + ip + " 'cat /etc/*-release | grep ^VERSION= | cut -d= -f2' > /tmp/so.txt"
        os.system(cmd)
        with open("/tmp/so.txt", "r") as outfile:
            so = (outfile.read())
        replaced = (so.replace('"', ''))
        print("Erro adicionar chave: " + host + " - SO: " + replaced + " - Erro: " + str(e))
        continue   
