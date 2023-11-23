import serial.tools.list_ports

# Get a list of all available serial ports
available_ports = serial.tools.list_ports.comports()

if not available_ports:
    print("No serial ports found")
else:
    print("Available serial ports:")
    for port in available_ports:
        print(port.device)
