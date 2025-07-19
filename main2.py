# import serial
# import time

# ser = serial.Serial('COM5', baudrate=115200, timeout=1)
# time.sleep(2)

# # Init ELM327
# ser.write(b'ATZ\r')     # Reset
# time.sleep(1)
# print(ser.readlines())

# ser.write(b'ATE0\r')    # Echo off
# ser.write(b'ATSP3\r')   # Set protocol ISO 9141-2
# time.sleep(1)
# print(ser.readlines())

# # Send RPM request
# ser.write(b'010C\r')
# time.sleep(1)
# print(ser.readlines())


import serial
import time

# Setup serial
ser = serial.Serial('COM5', baudrate=115200, timeout=1)
time.sleep(2)

print("[*] Initializing ELM327...")

# Reset
ser.write(b'ATZ\r')
time.sleep(1)
print("[ATZ]", ser.readlines())

# Echo off + Set protocol to ISO 9141-2
ser.write(b'ATE0\r')
time.sleep(0.3)
ser.write(b'ATSP3\r')
time.sleep(1)
print("[ATE0 + ATSP3]", ser.readlines())

# Request RPM
ser.write(b'010C\r')
time.sleep(1)
response = ser.readlines()
print("[010C]", response)

# Try to decode RPM if valid
for line in response:
    decoded = line.decode().strip()
    if decoded.startswith("41 0C"):
        try:
            parts = decoded.split()
            A = int(parts[2], 16)
            B = int(parts[3], 16)
            rpm = ((A * 256) + B) / 4
            print(f"[✅ RPM] {rpm}")
        except Exception as e:
            print("[❌] Failed to decode RPM:", e)
