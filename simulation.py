import pybullet as p
import pybullet_data
import time

physicsClient = p.connect(p.GUI)#or p.DIRECT for non-graphical version
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #used by loadURDF
p.setGravity(0,0,-10)
planeId = p.loadURDF("plane.urdf")
cubeStartPos = [0,0,1]
cubeStartOrientation = p.getQuaternionFromEuler([0,0,0])
boxId = p.loadURDF("modeling/URDF/motorcycle_witout_loop.urdf.xacro",cubeStartPos, cubeStartOrientation)
while True:
    p.stepSimulation()
    cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
    print(f"Position: {cubePos}, Orientation: {cubeOrn}")
    time.sleep(0.01)  # Small delay to make the simulation viewable

p.disconnect()