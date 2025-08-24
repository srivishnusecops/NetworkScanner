import subprocess
import getpass


target = input("Enter the Ip Address: ")

def powerscanner(command):
    try:
        # If the command requires sudo, handle sudo password input
        if 'sudo' in command:
            sudo_password = getpass.getpass("Enter your sudo password: ")  # Secure password input

            # Run the command with the sudo password passed to stdin
            result = subprocess.run(command, capture_output=True, text=True, check=True, input=sudo_password + "\n")
        else:
            # Run without sudo
            result = subprocess.run(command, capture_output=True, text=True, check=True)

        # Debugging output
        print(result.stdout)  # Print result for debugging
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e.stderr}")
        return None


def stealth_powerscan(target):
    command = ['sudo','nmap' ,'-sS','-sV','-O','--script=banner,vuln,default','-p-', target]
    result = powerscanner(command)

    output_filename = "nmap.stealty_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")

def  tcpconnect_powerscan(target):
    command = ['sudo','nmap' ,'-sT','-sV','-O','--script=banner,vuln,default', target]
    result = powerscanner(command)

    output_filename = "nmap.tcpconnect_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")

def udp_powerscan(target):
    command = ['sudo','nmap' ,'-sU','-sV','-O','--script=banner,vuln,default', target]
    result = powerscanner(command)

    output_filename = "nmap.udp_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")


def ipspoofed_powerscan(target):
    command = ['sudo','nmap' ,'-D', 'RND:50','-sS','-sV','-O','--script=banner,vuln,default', target]
    result = powerscanner(command)

    output_filename = "nmap.ipspoofed_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")




def rand_data_powerscan(target):
    command = ['sudo','nmap' ,'-sS','-sV','-O','nmap --data-length 200','--script=banner,vuln,default', target]
    result = powerscanner(command)

    output_filename = "nmap.rand_data_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")



def ipv6_powerscan(target):
    command = ['sudo','nmap' ,'-6','-sS','-sV','-O','--script=banner,vuln,default', target]
    result = powerscanner(command)

    output_filename = "nmap.udp_powerscan"

    with open(output_filename, "w") as d:
        d.write(result)

        print(f"Result of the scan is saved to {output_filename}")


command_list = """1.stealth_powerscan
2.tcpconnect_powerscan
3.udp_powerscan
4."ipspoofed_powerscan
5.randomdata_powerscan
6.ipv6 scan"""

print(command_list)

choice = input("Enter the choice: ")


if '1' in choice:
    print(stealth_powerscan(target))
elif '2' in choice:
    print(tcpconnect_powerscan(target))
elif '3' in choice:
    print(udp_powerscan(target))
elif '4' in choice:
    print(ipspoofed_powerscan(target))
elif '5' in choice:
    print(rand_data_powerscan(target))
elif '6' in choice:
    print(ipv6_powerscan(target))
else:
    print("Invalid choice")
