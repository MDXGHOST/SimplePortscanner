import socket
import time
import sys


def scan_ports():
    print("\n=== Port Scanner ===")

    target = input("Enter target IP address (example: 127.0.0.1): ")

    # Validate starting port
    while True:
        try:
            start_port = int(input("Enter starting port number (1-65535): "))
            if 1 <= start_port <= 65535:
                break
            else:
                print("Port must be between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Validate ending port
    while True:
        try:
            end_port = int(input("Enter ending port number (1-65535): "))
            if 1 <= end_port <= 65535:
                break
            else:
                print("Port must be between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    if start_port > end_port:
        print("Starting port cannot be greater than ending port.")
        return

    open_ports = []

    print("\nScanning...")
    start_time = time.time()

    for port in range(start_port, end_port + 1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        result = sock.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN]   Port {port}")
            open_ports.append(port)
        else:
            print(f"[CLOSED] Port {port}")

        sock.close()

    end_time = time.time()

    print("\n" + "=" * 40)
    print("Scan Summary")
    print("=" * 40)

    if open_ports:
        print(f"Total Open Ports: {len(open_ports)}")
        for port in open_ports:
            print(f" - {port}")
    else:
        print("No open ports found.")

    print(f"\nScan completed in {round(end_time - start_time, 2)} seconds.")
    print("=" * 40)


def main():
    while True:
        print("\n" + "=" * 40)
        print("        Ghostnmap v1.0")
        print("   Simple Python Port Scanner")
        print("=" * 40)
        print("1. Scan Ports")
        print("2. Exit")

        choice = input("Select an option (1-2): ")

        if choice == "1":
            scan_ports()
        elif choice == "2":
            print("Exiting program. Goodbye.")
            sys.exit()
        else:
            print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
