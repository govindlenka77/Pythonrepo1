from netmiko import ConnectHandler

with open('devices.txt') as routers:
    Router = {
        "device_type": "cisco_ios",
        "ip": "sandbox-iosxe-latest-1.cisco.com",
        "username": "developer",
        "port": 22,
        "password": "C1sco12345"
    }
    net_connect = ConnectHandler(**Router)


hostname=net_connect.send_command('show run | i host')

hostname.split(" ")

hostname,device,*rest=hostname.split(" ")

print("Backing up " + device)

filename = "C:/Users/user706/PycharmProjects/pythonProject1/Best-one/backingData.txt"
showrun=net_connect.send_command('show run')
showvlan=net_connect.send_command('show vlan')
showver=net_connect.send_command('show ver')
log_file=open(filename,"a")
log_file.write(showrun)
log_file.write("\n")
log_file.write(showvlan)
log_file.write("\n")
log_file.write(showver)
log_file.write("\n")

net_connect.disconnect()