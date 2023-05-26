#from testAstar import astar
from controller import Robot
import math
import time

# Roboto inicilizavimas
robot = Robot()

start_cal = time.time()

# skirta gauti dabartinio pasaulio laiko žingsnį.
timestep = int(robot.getBasicTimeStep())

# skirta gauti prietaisus
fl_motor = robot.getMotor('Motor1')
fr_motor = robot.getMotor('Motor2')
bl_motor = robot.getMotor('Motor3')
br_motor = robot.getMotor('Motor4')

fl_motor.setPosition(float('inf'))
fr_motor.setPosition(float('inf'))
bl_motor.setPosition(float('inf'))
br_motor.setPosition(float('inf'))

fl_motor.setVelocity(0.0)
fr_motor.setVelocity(0.0)
bl_motor.setVelocity(0.0)
br_motor.setVelocity(0.0)

gps = robot.getGPS('gps')
gps.enable(timestep)

dirr = robot.getCompass('compass')
dirr.enable(10)

# Pradinės roboto koordinates
target_x = 0.125  # pasirinkta centras
target_z = 0.375
# Motoro maksimalus greitis
MAX_SPEED = 3.16

# Nurodama virtuali aplinka kurioje robotas turės naviguoti, 0 yra tuscias langelis, o 1 yra siena
maze = [[0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

#name = (x, y) koordinates 0:0 yra kairys apatinis
start = (0, 0)
goal = (19, 19)

# skirta iškviesti funkciją astar su labirinto, pradžios ir tikslo koordinatėmis
#path = astar(start, goal, maze)
#kazkodel kodas pastoviai ibegdavo i infinite loopa, teko pasidaryti rankiniu budum todel cia nurodytos koordinates
path = [(0, 0), (0, 1), (0, 2), (0, 3), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (1, 10), (1, 11), (1, 12), (1, 13), (1, 14), (1, 15), (1, 16), (1, 17), (1, 18), (1, 19), (2, 19), (3, 19), (4, 19), (5, 19), (6, 19), (7, 19), (8, 19), (9, 19), (10, 19), (11, 19), (12, 19), (13, 19), (14, 19), (15, 19), (16, 19), (17, 19), (18, 19), (19, 19)]
print(path)

# i kuria puse robotoas atsisukes
direction = 'east'

# pradines koordinates
x, y = 0, 0

comp = []
# skirta susidaryti sarasa pagal kuri robotas zinos i kuria puse atsisukti
for i in range(1, len(path)):
    # skirta gauti sekanciom koordinatem
    next_x, next_y = path[i]
    
    # patikrinti ar x skaicius dideja ar  mazeja
    if next_x > x:
        comp.append('east')
    elif next_x < x:
        comp.append('west')
    else:
        new_direction = direction
    
    # patikrina ar y skaicius dideja ar mazeja
    if next_y > y:
        comp.append('north')
    elif next_y < y:
        comp.append('south')
    
    # updatina koordinates ir puse
    direction = new_direction
    x, y = next_x, next_y
    
    # atspausdina atsakyma
print(comp)

# Apskaičiuoja faktinį roboto nuvažiuotą atstumą
distance_traveled = 0
for i in range(len(path)-1):
    distance_traveled += math.sqrt((path[i+1][0]-path[i][0])**2 + (path[i+1][1]-path[i][1])**2)

# Apskaičiuoja trumpiausią įmanomą atstumą tarp kelio pradžios ir pabaigos taškų
start = path[0]
end = path[-1]
shortest_distance = math.sqrt((end[0]-start[0])**2 + (end[1]-start[1])**2)

# Apskaičiuokite kelio efektyvumą
efficiency = shortest_distance / distance_traveled

# ispausdina kelio efektyvuma
print("Path efficiency: {:.2f}".format(efficiency))

# matuoja skaiciavimo laika
end_cal = time.time()


# tada ji atspausdina
time_cal = end_cal - start_cal
print("Skaiciavimo laikas: ", time_cal)
# stabdymo funkcija 
def rolf():
    fl_motor.setVelocity(0)
    fr_motor.setVelocity(0)
    bl_motor.setVelocity(0)
    br_motor.setVelocity(0)


# cia robotas atsisuka i reikiama puse
def get_direction(face):
    while robot.step(timestep) != -1:
        #roboto motorai ijungiami, kad jis suktusi pries laikrodzio rodykle
        fl_motor.setVelocity(MAX_SPEED/4)
        fr_motor.setVelocity(-MAX_SPEED/4)
        bl_motor.setVelocity(MAX_SPEED/4)
        br_motor.setVelocity(-MAX_SPEED/4)
        compass_values = dirr.getValues()
        # is komposo daviklio skaiciuojamos koordinates
        heading = math.atan2(compass_values[0], compass_values[2]) * (180 / math.pi)
        heading = (heading + 360) % 360
        # cia tikrina ar robotas atsisukes i reikiama puse, 2 laipsniu paklaida, nes kartais jis persoka per reikiamas koordinates
        if face == "east" and (heading >= 89 and heading < 91):
            rolf()
            return
        elif face == "south" and (heading >= 179 and heading <= 181):
            rolf()
            return
        elif face == "west" and (heading >= 269 and heading <= 271):
            rolf()
            return
        elif face == "north" and ((heading >= 359 and heading >= 360) or (heading > 0 and heading <= 1)):
            rolf()
            return
        
        
def move_to_target(target_x, target_z, gps, fl_motor, fr_motor, bl_motor, br_motor, MOTOR_SPEED, threshold=0.02):
    # gaunama dabartine padėtis iš GPS
    while robot.step(timestep) != -1:
        pos = gps.getValues()

        # apskaičiuoja atstumą iki tikslinės padėties.
        distance = math.sqrt((target_x - pos[0])**2 + (target_z - pos[1])**2)
        # jei atstumas mažesnis už tam tikrą ribą, robotas sustabdomas
        if distance < threshold:
            rolf()
            return
        else:
            fl_motor.setVelocity(MOTOR_SPEED)
            fr_motor.setVelocity(MOTOR_SPEED)
            bl_motor.setVelocity(MOTOR_SPEED)
            br_motor.setVelocity(MOTOR_SPEED)

bolen = True
i=0
robx, roby = 0.125, 0.125
# roboto kelionės pradžia

start_drive = time.time()

# roboto loop
while bolen:
    # 0.250 yra skirta pervaziuoti is vieno langelio centro i kita
    get_direction(comp[i])

    if comp[i] == "east":
        roby = roby + 0.250
    elif comp[i] == "west":
        roby = roby - 0.250
    elif comp[i] == "south":
        robx = robx - 0.250
    elif comp[i] == "north":
        robx = robx + 0.250

    print(robx, roby)

    move_to_target(roby, robx, gps, fl_motor, fr_motor, bl_motor, br_motor, MAX_SPEED)

    i=i+1

    if i==len(comp):
        break

end_drive = time.time()
time_drive = end_drive - start_drive
# cia baigiamas laikas vaziavimo skaiciavimui

print("Keliones likas: ", time_drive) 
        
print("PERGALE")