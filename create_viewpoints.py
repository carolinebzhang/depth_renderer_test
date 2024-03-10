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

def calculate_face_center(vertices):
    # Calculate the average of the vertices to find the center
    return [sum(coord) / len(vertices) for coord in zip(*vertices)]

if __name__ == '__main__':
    circumradius = math.sqrt(3)
    distance = circumradius * 1.2
    # Define the vertices of a cube
    vertices = [
        [-1, -1, -1],
        [1, -1, -1],
        [1, 1, -1],
        [-1, 1, -1],
        [-1, -1, 1],
        [1, -1, 1],
        [1, 1, 1],
        [-1, 1, 1]
    ]

    # Define faces using indices from the vertices list
    faces = [
        [0, 1, 2, 3], # Bottom face
        [4, 5, 6, 7], # Top face
        [0, 1, 5, 4], # Side face 1
        [2, 3, 7, 6], # Side face 2
        [0, 3, 7, 4], # Side face 3
        [1, 2, 6, 5]  # Side face 4
    ]

    # Open a file to write the view points
    with open('./view_points.txt', 'w+') as view_points:
        for face_indices in faces:
            face_vertices = [vertices[i] for i in face_indices]
            center = calculate_face_center(face_vertices)
            elevation = math.asin(center[2] / circumradius)
            azimuth = math.atan2(center[1], center[0])
            view_points.write(f'{azimuth} {elevation} 0.0 {distance}\n')