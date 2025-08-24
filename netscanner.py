import subprocess


target = input("Enter the Target IP Address: ")

def powerscanner(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running nmap: {e.stderr}")
        return None



def check_alive(target):
    command = ['nmap', '-sn', target]
    result = powerscanner(command)
    print(result)


def stealth_scan(target):
    command = ['nmap', '-sS', '-p-', '-A', target]
    
    result = powerscanner(command)
    
    if result is None:
        print("Stealth scan failed. No results to save.")
        return  
    
    output_filename = "nmap.stealthscan"
    
    with open(output_filename, "w") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename}")


def tcpconnect_scan(target):
    command = ['nmap', '-sT','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.tcpconnectscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")


def udp_scan(target):
    command = ['nmap', '-sU','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.udpscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")

def null_scan(target):
    command = ['nmap', '-sN','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.nullscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")

def fin_scan(target):
    command = ['nmap', '-sF','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.finscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")


def Xmas_scan(target):
    command = ['nmap', '-sX','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.xmasscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")

def tcp_ack_scan(target):
    command = ['nmap', '-sA','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.tcp_ack_scan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")


def ip_proto_scan(target):
    command = ['nmap', '-sT','-p-', '-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.ip_proto_scan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")


def fragment_scan(target):
    command = ['nmap', '-f','-p-','-sV', '-O','-oN', '-',target]
    result = powerscanner(command)

    output_filename = "nmap.fragmentscan"

    with open(output_filename, "a") as f:
        f.write(result)
        print(f"Result of the scan is saved to {output_filename} ")



command_list = """1.Check Host Alive
2.stealth scan
3.tcpconnect scan
4.udp scan
5.null scan
6.fin scan
7.Xmas scan
8.tcp_ack scan
9.ip_protocol scan
10.fragment scan for firewall detection
"""

print(command_list)




choice = input("Enter your choice: ")

if '1' in choice:
    print(check_alive(target))
elif '2' in choice:
    print(stealth_scan(target))
elif '3' in choice:
    print(tcpconnect_scan(target))
elif '4' in choice:
    print(udp_scan(target))
elif '5' in choice:
    print(null_scan(target))
elif '6' in choice:
    print(fin_scan(target))
elif '7' in choice:
    print(Xmas_scan(target))
elif '8' in choice:
    print(tcp_ack_scan(target))
elif '9' in choice:
    print(ip_proto_scan(target))
elif '10' in choice:
    print(fragment_scan(target))
else:
    print("Ivalid choice!")
