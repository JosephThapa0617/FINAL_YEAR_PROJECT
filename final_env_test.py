from coppeliasim_zmqremoteapi_client import RemoteAPIClient
client = RemoteAPIClient()
import time

# all simIK.* type of functions and constants
sim = client.getObject('sim')

sphere= sim.getObject('/base_dyn/manipSphere')
g_joint1=sim.getObjectHandle('/base_dyn/gripper_joint1')
g_joint2=sim.getObjectHandle('/base_dyn/gripper_joint2')
cup=sim.getObjectHandle('/Cup[0]/visible_transparent')






#sim.setObjectPosition(sphere, sim.handle_world, [0.87955,-0.06001,1.05219])


# sim.setObjectPosition(sphere, sim.handle_world, [0.22631,0.72169,0.96367])
# time.sleep(1)
# sim.setJointTargetPosition(g_joint1,30*3.14/180)
# sim.setJointTargetPosition(g_joint2,-30*3.14/180)
# sim.setObjectPosition(sphere, sim.handle_world, [0.22631,0.72169,0.76367])


# time.sleep(2)
# sim.setJointTargetPosition(g_joint1,30*3.14/180)
# sim.setJointTargetPosition(g_joint2,-30*3.14/180)
# time.sleep(2)


# sim.setObjectPosition(sphere, sim.handle_world, [0.87608,0.0284,0.96367])
# time.sleep(1)
# sim.setObjectPosition(sphere, sim.handle_world, [0.87608,0.0284,0.86367])
# time.sleep(1)


sim.setShapeColor(cup,None, sim.colorcomponent_ambient_diffuse,[0,1,0])

time.sleep(6)



# sim.setShapeColor(cup,None, sim.colorcomponent_ambient_diffuse,[1,1,1])
