import subprocess
target = input("Enter the Target IP: ")

def run_masscan(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        return result.stdout
    except subprocess.CalledProcessError as e:
        print(f"Error running masscan: {e.stderr}")
        return None

def syn_scan(target):
    filename = 'syn_scan.json'  # Ensure valid filename with extension
    command = [
        'sudo', 'masscan', '-sS', '-p', '1-65535',
        '--banner', '--rate', '2000000', '-oJ', filename, target
    ]
    result = run_masscan(command)
    return result

def tcp_scan(target):
    filename = 'tcp_scan.json'  # Ensure valid filename with extension
    command = [
        'sudo', 'masscan', '-sT', '-p', '1-65535', 
        '--banner', '--rate', '2000000', '-oJ', filename, target
    ]
    result = run_masscan(command)
    return result



# Display menu to user
print("Choose scan type:")
print("1. SYN Scan")
print("2. TCP Scan")

choice = input("Enter your choice (1 or 2): ")

if choice == '1':
    result = syn_scan(target)
    print(result)
 # Print the output of the scan
elif choice == '2':
    result = tcp_scan(target)
    print(result)  # Print the output of the scan
else:
    print("Invalid choice")
