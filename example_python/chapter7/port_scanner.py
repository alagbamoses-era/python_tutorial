#!/usr/bin/python3


import socket

def port_scan(target, start_port, end_port):
    print(f"scanning {target} from port {start_port} to {end_port}")

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.5) # Set a timeout for responsiveness

        if sock.connect_ex((target, port)) == 0:
            print(f"[+] Port {port} is OPEN")
        else:
            continue # skip to the next port

        sock.close()

# Main loop to enter target details

while True:
    target_ip = input("Enter target IP (or type 'exit' to quit): ")

    if target_ip.lower() == 'exit':
        print('Exiting program...')
        break # Exit the loop
    try:
        start_port = int(input('Enter start port: '))
        end_port = int(input('Enter end port: '))

        if start_port > end_port:
            print('Invalid range. Start port should be less than or equal to end port.')
            continue # Restart the loop
        port_scan(target_ip, start_port, end_port)

    except ValueError:
        print('Invalid input. Please enter numeric values.')
        pass # Placeholder for future error handling

print('Program terminated.')



