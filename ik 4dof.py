from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
import time

# all simIK.* type of functions and constants
simIK = client.getObject('simIK')
sim = client.getObject('sim')

simBase = sim.getObject('/base_dyn')
simTip = sim.getObject('/base_dyn/tip')
simTarget = sim.getObject('/base_dyn/target')
sphere= sim.getObject('/base_dyn/manipSphere')
g_joint1=sim.getObjectHandle('/base_dyn/gripper_joint1')
g_joint2=sim.getObjectHandle('/base_dyn/gripper_joint2')

# sim.setJointTargetPosition(g_joint1,20*3.14/180)
# sim.setJointTargetPosition(g_joint2,-20*3.14/180)


ikEnv = simIK.createEnvironment()
ikGroup_undamped = simIK.createGroup(ikEnv)
simIK.setGroupCalculation(ikEnv, ikGroup_undamped,
                          simIK.method_pseudo_inverse, 0, 10)
simIK.addElementFromScene(ikEnv, ikGroup_undamped,
                          simBase, simTip, simTarget,simIK.constraint_position+simIK.constraint_alpha_beta)
ikGroup_damped = simIK.createGroup(ikEnv)
simIK.setGroupCalculation(ikEnv, ikGroup_damped,
                          simIK.method_damped_least_squares, 0.3, 99)
simIK.addElementFromScene(ikEnv, ikGroup_damped, simBase,
                          simTip, simTarget, simIK.constraint_position+simIK.constraint_alpha_beta)



def ik(x,y,z):
    sim.setObjectPosition(sphere, sim.handle_world, [x,y,z])
    position1 = [round(num, 4) for num in sim.getObjectPosition(simTip,simBase)]
    position2=position1

    print(position1)
    while position1==position2 :

        position2 = [round(num, 4) for num in sim.getObjectPosition(simTip,simBase)]
        print(position1)


        if simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_undamped,True)==simIK.result_fail :
            simIK.applyIkEnvironmentToScene(ikEnv,ikGroup_damped)




ik(0.87955,-0.06001,1.05219)
#ik(1.02608,0.0034,+1)
time.sleep(3)
ik(0.87955,-0.06001,0.9)
# time.sleep(4)

# sim.setJointTargetPosition(g_joint1,35*3.14/180)
# sim.setJointTargetPosition(g_joint2,-35*3.14/180)

# time.sleep(2)
# ik(0.656,0.541,1)
# sim.setObjectPosition(sphere, sim.handle_world, [+0.00238,+0.05999,2.050])

# sim.setObjectPosition(sphere, sim.handle_world, [+0.656,+0.541,0.780])







#simIK.eraseEnvironment(ikEnv)








