try:
    import sim
except:
    print ('--------------------------------------------------------------')
    print ('"sim.py" could not be imported. This means very probably that')
    print ('either "sim.py" or the remoteApi library could not be found.')
    print ('Make sure both are in the same folder as this file,')
    print ('or appropriately adjust the file "sim.py"')
    print ('--------------------------------------------------------------')
    print ('')

import time

def actuate(clientID):
    angle=3.14159
    ret,motor=sim.simxGetObjectHandle(clientID,'Rev1',sim.simx_opmode_blocking) 
    time.sleep(5)
    sim.c_SetJointTargetPosition(clientID,motor,angle,sim.simx_opmode_oneshot) 
    time.sleep(5) 
    sim.c_SetJointTargetPosition(clientID,motor,0,sim.simx_opmode_oneshot)  
    time.sleep(5)
    sim.c_SetJointTargetPosition(clientID,motor,1.5708,sim.simx_opmode_oneshot)
    time.sleep(5)


if __name__ == "__main__":
    print ('Program started')
    sim.simxFinish(-1) # just in case, close all opened connections
    clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
        print ('Connected to remote API server')
        actuate(clientID)
    else:
        print ('Failed connecting to remote API server')
        exit(0)
