print('hello world')
f = open("z:/Projets/hot_plate/graph.gcode","w")
#f.write("testy testisusoliucoliuh\n")
t1=150
t2=230
for i in range (100):
    f.write("M104 S{}\n".format(str(t1)))
    f.write("G4 P1000\n")
for i in range (30):
    f.write("M104 S{}\n".format(str(t2)))
    f.write("G4 P1000\n")
f.write("M104 S0\n")