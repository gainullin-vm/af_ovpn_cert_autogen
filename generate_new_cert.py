import os
import subprocess

#author @Lani_Ka_Nani

#pass = ""
local_to_remote = "/Users/v.gaynullin/Desktop/dev02_access"
host = "user@ip"
vpnUserName = input("Enter VPN username: ")
vpnContainerName = ""



def userVPN(local_to_remote, host, vpnUserName, vpnContainerName):
    commandList = [
        "docker run -v /home/vpn/opt/vpn-data:/etc/openvpn --rm -it " + vpnContainerName + " easyrsa build-client-full" + vpnUserName + "nopass " + "</home/vitaly/testvpn/passfile",
        "docker run -v /home/vpn/opt/vpn-data:/etc/openvpn --rm " + vpnContainerName + " ovpn_getclient " + vpnUserName + " > /home/vitaly/" + vpnUserName + ".ovpn",
    ]
    for command in commandList:
        ssh = subprocess.Popen(["ssh", "-o", "StrictHostKeyChecking=no", "-i", local_to_remote, host, "-p", "22193", command],
                            shell=False,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()
        error = ssh.stderr.readlines()
        print(result)
        print(error)

userVPN(local_to_remote, host, vpnUserName, vpnContainerName)
os.system("scp -o Stricthostkeychecking=no -i " + local_to_remote + " -P port " + host + ":/home/vitaly/testvpn/" + vpnUserName + ".ovpn /Users/v.gaynullin/Desktop/")
print("User successfully created!")
