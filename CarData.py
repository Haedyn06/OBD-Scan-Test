import pandas as pd
import time

dataPath = r"c:\Users\hayde\OneDrive\Documents\OBDwiz\CSV Logs\WMWRC33566TK16589\LogMiniTrip.csv"

df = pd.read_csv(dataPath, skiprows=1)
secValues = df.iloc[:, 2].tolist()
totalDist = 0

def getRowValues(rowPos):
    specificRow = df.iloc[rowPos]
    columns = df.columns.tolist()
    # "Time(s)", "Speed(km/h)", "RPM", "Throttle(%)", "Fuel(l/hr)", "Coolant Temp(°C)", "Air Intake", "Distance (km)"
    order = [0, 1, 3, 2, 4, 5, 6, 7] 
    orderedRow = specificRow[[columns[i] for i in order]]
    return orderedRow

for i in range(len(secValues)):
    #Values
    statValues = getRowValues(i)

    #Time
    secTime = statValues.iloc[0]
    minutes = int(secTime//60)
    seconds = round(secTime%60)


    # Values
    speed = statValues.iloc[1]
    rpm = statValues.iloc[2]
    throttle = statValues.iloc[3]

    # Distance calc
    prevTime = df.iloc[i - 1, 0] if i > 0 else 0
    delta_hr = (secTime - prevTime) / 3600
    distance = speed * delta_hr
    totalDist += distance

    print(f"Time: {minutes}m {seconds}s ; RPM: {rpm} ; Speed: {speed}km/h")
    # print(f"Time: {minutes}m {seconds}s ; RPM: {rpm}")
    # print(f"Time: {minutes}m {seconds}s ; Throttle: {throttle}%")

    # print(f"{i} = Time: {minutes}m {seconds}s ; Speed(km/h): {speed}km/h ; Distance(Km): {round(totalDist, 2)}km")
    
    # time.sleep(1)