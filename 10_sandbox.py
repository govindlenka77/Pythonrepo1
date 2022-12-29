from netmiko import ConnectHandler

with open('devices.txt') as routers:
    for IP1 in routers:
        #print(IP1)
        Router={
            "device_type":"cisco_ios",
            "ip":"sandbox-iosxe-latest-1.cisco.com",
            "username":"developer",
            "port":22,
            "password":"C1sco12345"
        }
        net_connect=ConnectHandler(**Router)

        print("Connecting to "+IP1)
        print("-"*79)
        output=net_connect.send_command('sh ip int brief')
        print(output)
        print()
        print('-'*79)

net_connect.disconnect()