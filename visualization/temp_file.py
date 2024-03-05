import open3d
import numpy as np
from copy import deepcopy

# create the coordinate frame 
mesh_frame = open3d.create_mesh_coordinate_frame(size=1, origin=[0, 0, 0])

# create a random 4x4 transformation matrix
cam_pose1 = np.eye(4)

# transform the mesh frame by the cam pose 
cam_pos1_transformed = deepcopy(mesh_frame).transform(cam_pose1)

