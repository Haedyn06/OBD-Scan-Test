import obd
import time

# If using OBDLink SX --> Device Manager --> Set Baud Rate To 115200

# connection = obd.OBD("COM5", baudrate=9600, protocol="3", fast=False)
connection = obd.OBD("COM5", baudrate="115200", protocol="3", fast=True)

print("Connected:", connection.status())

ELMVer = connection.query(obd.commands.ELM_VERSION, force=True)
vin = connection.query(obd.commands.VIN, force=True)
stats = connection.query(obd.commands.STATUS, force=True)

baseStats = [ELMVer, vin, stats]

for i in baseStats:
    print(i.value)

while True:
    rpm = connection.query(obd.commands.RPM, force=True)
    speed = connection.query(obd.commands.SPEED, force=True)
    fuel = connection.query(obd.commands.FUEL_LEVEL, force=True)
    fuelstats = connection.query(obd.commands.FUEL_STATUS, force=True)
    throttle = connection.query(obd.commands.THROTTLE_POS, force=True)

    statistics = {"rpm: ": rpm, "speed: ": speed, "fuel: ": fuel, "fuel stats:":  fuelstats, "throttle": throttle}
    count = 0


    for key, val in statistics.items():
        if val is None or val.is_null():
            print(f"{key}: ❌ No Data")
        else:
            print(f"{key}: {val.value}")

    print("-" * 30)
    time.sleep(1)


"""
obd.OBD            # main OBD connection class
obd.Async          # asynchronous OBD connection class
obd.commands       # command tables
obd.Unit           # unit tables (a Pint UnitRegistry)
obd.OBDStatus      # enum for connection status
obd.scan_serial    # util function for manually scanning for OBD adapters
obd.OBDCommand     # class for making your own OBD Commands
obd.ECU            # enum for marking which ECU a command should listen to
obd.logger         # the OBD module's root logger (for debug)



obd.commands.RPM	            Get current RPM
obd.commands.SPEED	            Get speed in km/h
obd.commands.FUEL_LEVEL	        % of fuel remaining (if supported)
obd.commands.THROTTLE_POS	    How hard you’re pressing the gas
obd.commands.MAF	            Mass Air Flow (can help calculate MPG)
obd.commands.ENGINE_LOAD	    % engine load
obd.commands.FUEL_STATUS	    Shows open/closed loop info
"""