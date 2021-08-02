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
import math

def cal_angles(x,y,z):

    a1=0.055

    t1=math.atan(y/x)
    r=math.sqrt(x*x+y*y)
    t2=math.atan((z/(r-a1)))
    
    t1=t1-0.78947
    
    if t2<0:
        t2=t2+0.78947
        t2=-t2
    else:
        t2=t2-0.78947
        
       
    #t2=t2
    print(t1,t2)
    return t1,t2




def actuate(clientID):
    ret,j11=sim.simxGetObjectHandle(clientID,'Rev11',sim.simx_opmode_blocking) 
    ret,j12=sim.simxGetObjectHandle(clientID,'Rev12',sim.simx_opmode_blocking)
    ret,j21=sim.simxGetObjectHandle(clientID,'Rev21',sim.simx_opmode_blocking)
    ret,j22=sim.simxGetObjectHandle(clientID,'Rev22',sim.simx_opmode_blocking)
    ret,j31=sim.simxGetObjectHandle(clientID,'Rev31',sim.simx_opmode_blocking)
    ret,j32=sim.simxGetObjectHandle(clientID,'Rev32',sim.simx_opmode_blocking)
    ret,j41=sim.simxGetObjectHandle(clientID,'Rev41',sim.simx_opmode_blocking)
    ret,j42=sim.simxGetObjectHandle(clientID,'Rev42',sim.simx_opmode_blocking)

    ret,end_eff1=sim.simxGetObjectHandle(clientID,'end_eff1',sim.simx_opmode_blocking)
    ret,frame1=sim.simxGetObjectHandle(clientID,'frame1',sim.simx_opmode_blocking)
    ret,origin=sim.simxGetObjectHandle(clientID,'origin',sim.simx_opmode_blocking)
    
    ##initialize legs
    
        #t1,t2=cal_angles(0.070515349507332, 0.0064974501729012, 0.062181476503611)
        #sim.c_SetJointTargetPosition(clientID,j32,-0.2850,sim.simx_opmode_oneshot) 
        #time.sleep(1)
        #sim.c_SetJointTargetPosition(clientID,j31,t1,sim.simx_opmode_oneshot) 
        #time.sleep(1)
        #sim.c_SetJointTargetPosition(clientID,j32,t2,sim.simx_opmode_oneshot) 
        #time.sleep(1)

        #t1,t2=cal_angles(0.0074975416064262, 0.069483518600464, 0.06218147277832)
        #sim.c_SetJointTargetPosition(clientID,j42,-0.2850,sim.simx_opmode_oneshot) 
        #time.sleep(1)
        #sim.c_SetJointTargetPosition(clientID,j41,t1,sim.simx_opmode_oneshot) 
        #time.sleep(1)
        #sim.c_SetJointTargetPosition(clientID,j42,t2,sim.simx_opmode_oneshot) 
        #time.sleep(1)
    while(1):
        ##A##
        print("A")
        sim.c_SetJointTargetPosition(clientID,j12,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j22,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j32,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j42,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j11,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j21,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j31,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        sim.c_SetJointTargetPosition(clientID,j41,0,sim.simx_opmode_oneshot) 
        time.sleep(0.25)
        ##B##   
        print("B")
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j12,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j32,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        ##C##
        print("C")
        sim.c_SetJointTargetPosition(clientID,j21,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j41,0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        ##D##
        print("D")
        sim.c_SetJointTargetPosition(clientID,j12,0,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j32,0,sim.simx_opmode_oneshot) 
        time.sleep(1)

        sim.c_SetJointTargetPosition(clientID,j22,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j42,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        ##E##
        print("E")
        sim.c_SetJointTargetPosition(clientID,j31,0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j11,-0.2850,sim.simx_opmode_oneshot) 
        time.sleep(1)
        ##F##
        print("F")
        sim.c_SetJointTargetPosition(clientID,j22,0,sim.simx_opmode_oneshot) 
        time.sleep(1)
        sim.c_SetJointTargetPosition(clientID,j42,0,sim.simx_opmode_oneshot) 
        time.sleep(1)
        


    '''
    sim.c_SetJointTargetPosition(clientID,j12,-0.2850,sim.simx_opmode_oneshot) 
    time.sleep(1)
    sim.c_SetJointTargetPosition(clientID,j11,-0.7853,sim.simx_opmode_oneshot)
    time.sleep(1) 
    sim.c_SetJointTargetPosition(clientID,j12,0,sim.simx_opmode_oneshot) 
    time.sleep(1)

    sim.c_SetJointTargetPosition(clientID,j22,-0.2850,sim.simx_opmode_oneshot) 
    time.sleep(1)
    sim.c_SetJointTargetPosition(clientID,j21,0.7853,sim.simx_opmode_oneshot)
    time.sleep(1) 
    sim.c_SetJointTargetPosition(clientID,j22,0,sim.simx_opmode_oneshot) 
    time.sleep(1)

    sim.c_SetJointTargetPosition(clientID,j32,-0.2850,sim.simx_opmode_oneshot) 
    time.sleep(1)
    sim.c_SetJointTargetPosition(clientID,j31,-0.7853,sim.simx_opmode_oneshot)
    time.sleep(1) 
    sim.c_SetJointTargetPosition(clientID,j32,0,sim.simx_opmode_oneshot) 
    time.sleep(1)

    sim.c_SetJointTargetPosition(clientID,j42,-0.2850,sim.simx_opmode_oneshot) 
    time.sleep(1)
    sim.c_SetJointTargetPosition(clientID,j41,0.7853,sim.simx_opmode_oneshot)
    time.sleep(1) 
    sim.c_SetJointTargetPosition(clientID,j42,0,sim.simx_opmode_oneshot) 
    time.sleep(1)
    '''

    

   
   
    
    

if __name__ == "__main__":
    print ('Program started')
    sim.simxFinish(-1) # just in case, close all opened connections
    clientID=sim.simxStart('127.0.0.1',19999,True,True,5000,5) # Connect to V-REP
    if clientID!=-1:
       
        actuate(clientID)
    else:
        print ('Failed connecting to remote API server')
        exit(0)
