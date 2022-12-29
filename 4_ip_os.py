import os,ipaddress

os.system('cls')    #os.system will clear the console at the start of the excecution
print("type 'end' to finish")
while True:
    ip=input("Enter ip addesdd: ")
    try:
        print(ipaddress.ip_address(ip))#<package: ipaddress>.<ip_address>.<attribute:ip>
        print("IP is valid")

    except:
        print('-'*30)
        print("IP is not valid")
    finally:
        if ip=='end':
            print("Script finished")
            break
