n=int(input("enter number of energy readings:"))
energy_readings=[]
for i in range(n):
    value=int(input("enter energy reading:"))
    energy_readings.append(value)
energy_dict={
    "efficient":[],
    "moderate":[],
    "high":[],
    "invalid":[]
}
for e in energy_readings:
    if e < 0:
        energy_dict["invalid"].append(e)
    elif e <= 50:
        energy_dict["efficient"].append(e)
    elif e <= 150:
        energy_dict["moderate"].append(e)
    else:
        energy_dict["high"].append(e)
vaild_readings=[x for x in energy_readings if x >= 0]
total=sum(vaild_readings)
buildings=len(vaild_readings)
summary=(total,buildings)
high_count=len(energy_dict["high"])
efficient_count=len(energy_dict["efficient"])
moderate_count=len(energy_dict["moderate"])
if total > 600:
    result="Energy Waste Detected"
elif high_count > 3:
    result="Moderate Usage"
elif efficient_count == moderate_count:
    result = "Efficient Campus"
else:
    result="Moderate Usage"
print("\nEnergy Category Report")
print("Efficient:", energy_dict["efficient"])
print("Moderate:", energy_dict["moderate"])
print("High:", energy_dict["high"])
print("Invalid:", energy_dict["invalid"])
print("\nTotal Consumption:",summary[0])
print("Number of Buildings:", summary[1])
print("\nEfficiency Result:", result)
