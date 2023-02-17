import os
import subprocess
import time


def connect():
    servers = ["us1.freevpn724.com","nl1.freevpn724.com","sg1.freevpn724.com","cz1.freevpn724.com","ch1.freevpn724.com"]
    print("Select the number corresponding to the desired location.\n1.United States\n2.Nehterlands\n3.Singapore\n4.Czech Republic\n5.Switzerland")
    def switch(inp):
        if inp == 1:
            ser_loc = servers[0]
            print("Selected Location : United States")
        elif inp == 2:
            ser_loc = servers[1]
            print("Selected Location : Netherlands")
        elif inp == 3:
            ser_loc = servers[2]
            print("Selected Location : Singapore")
        elif inp == 4:
            ser_loc = servers[3]
            print("Selected Location : Czech Republic")
        elif inp == 5:
            ser_loc = servers[4]
            print("Selected Location : Switzerland")
        else:
            print("Hello blind person.")
        return ser_loc
        
    inp = int(input("Server Location: "))
    server = switch(inp)
    subprocess.run(["powershell", "Add-VpnConnection -Name Thunder_VPN -ServerAddress " + server], capture_output=False)
    os.system("rasdial Thunder_VPN freevpn724 u5tf696")
    print("Connection Successful!")
    
def remove():
   os.system("rasdial Thunder_VPN /disconnect")
   os.system("rasphone -R Thunder_VPN")
   print("Disconnected from the VPN.")
   
    
def main():
    print("Options:-\n1.Activate the VPN\n2.Disconnect the VPN")
    ans = int(input())
    if ans == 1:
        connect()
    elif ans == 2:
        remove()
    else:
        print("Yo yo blind person!!!")

if __name__=="__main__":
    main()
        
    