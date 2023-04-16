f = open("graph.gcode","w") #opens and/or create the file graph.gcode in which the temperature commands are stored
t1=150 #first level of temperature for the first 100s
t2=230 #second level of temperature for the following 30s

for i in range (100):#Write in the file the value of temperature for the first 100s
    f.write("M104 S{}\n".format(str(t1)))#set heater at t1 ->M104 St1
    f.write("G4 P1000\n")#wait 1s
for i in range (30):#Write in the file the value of temperature for the following 30s
    f.write("M104 S{}\n".format(str(t2)))#set heater at t1 ->M104 St2
    f.write("G4 P1000\n")#wait 1s
f.write("M104 S0\n")#shuts off the heater
