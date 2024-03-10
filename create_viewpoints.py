# # This script is to create 20 viewpoints (vertices of a regular dodecahedron) around shapes.
# import math

# if __name__ == '__main__':
#     phi = (1 + math.sqrt(5)) / 2. # golden_ratio
#     circumradius = math.sqrt(3)
#     distance = circumradius*1.2
#     # this creates the vertices of a regular dodecahedron
#     dodecahedron = [[-1, -1, -1],
#                     [ 1, -1, -1],
#                     [ 1,  1, -1],
#                     [-1,  1, -1],
#                     [-1, -1,  1],
#                     [ 1, -1,  1],
#                     [ 1,  1,  1],
#                     [-1,  1,  1],
#                     [0, -phi, -1 / phi],
#                     [0, -phi,  1 / phi],
#                     [0,  phi, -1 / phi],
#                     [0,  phi,  1 / phi],
#                     [-1 / phi, 0, -phi],
#                     [-1 / phi, 0,  phi],
#                     [ 1 / phi, 0, -phi],
#                     [ 1 / phi, 0,  phi],
#                     [-phi, -1 / phi, 0],
#                     [-phi,  1 / phi, 0],
#                     [ phi, -1 / phi, 0],
#                     [ phi, 1 / phi, 0]]

#     # get Azimuth, Elevation angles
#     # Azimuth varies from -pi to pi
#     # Elevation from -pi/2 to pi/2
#     view_points = open('./view_points.txt', 'w+')
#     for vertice in dodecahedron:
#         elevation = math.asin(vertice[2] / circumradius)
#         azimuth = math.atan2(vertice[1], vertice[0])
#         view_points.write('%f %f %f %f\n' % (azimuth, elevation, 0., distance))
#     view_points.close()


import math

if __name__ == '__main__':
    circumradius = math.sqrt(3)
    distance = circumradius * 1.2
    # Define the vertices of a cube
    cube = [[-1, -1, -1],
            [1, -1, -1],
            [1, 1, -1],
            [-1, 1, -1],
            [-1, -1, 1],
            [1, -1, 1],
            [1, 1, 1],
            [-1, 1, 1]]
    
    # Define the indices of vertices that form each face of the cube
    # cube_faces = [
    #     [0, 1, 2, 3],  # Bottom face
    #     [4, 5, 6, 7],  # Top face
    #     [0, 1, 5, 4],  # Side face 1
    #     [1, 2, 6, 5],  # Side face 2
    #     [2, 3, 7, 6],  # Side face 3
    #     [3, 0, 4, 7]   # Side face 4
    # ]

    # Get Azimuth, Elevation angles
    # Azimuth varies from -pi to pi
    # Elevation from -pi/2 to pi/2
    view_points = open('./view_points.txt', 'w+')
    for face in cube:
        # Calculate the center of the face
        center = [sum([cube[i][j] for i in face]) / len(face) for j in range(3)]
        elevation = math.asin(center[2] / circumradius)
        azimuth = math.atan2(center[1], center[0])
        view_points.write('%f %f %f %f\n' % (azimuth, elevation, 0., distance))
    view_points.close()