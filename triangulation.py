import data_structures as dt

def is_ear(vertex_index, points):
    current_point = points[vertex_index]
    previous_point = None
    previous_point_index = None
    #Caso estejamos avaliando o primeiro vértice do polígono, como a lista não é duplamente encadeada, o elemento anterior será o último do polígono
    if vertex_index == 0:
        previous_point_index = len(points)-1
    else :
        previous_point_index = vertex_index-1
    previous_point = points[previous_point_index]

    next_point = None
    next_point_index = None
    #De forma similar, o próximo elemento para o último vértice será o primeiro do polígono
    if vertex_index == len(points)-1:
        next_point_index = 0
    else:
        next_point_index = vertex_index+1
    next_point = points[next_point_index]

    if(dt.orient(previous_point, current_point, next_point) <= 0):
        return None

    possible_triangle = dt.Triangle(previous_point, current_point, next_point)

    for point in points:
        if possible_triangle.is_point_inside(point):
            return None
    
    return possible_triangle

def triangulation_recursion(points, triangles):
    initial_points_length = len(points)
    if not len(points) == 3:
        for i in range(initial_points_length):
            orelha = is_ear(i, points)

            if orelha != None :
                triangles.append(orelha)
                del points[i]
                break
        return triangulation_recursion(points, triangles)
    #Acrescenta o triângulo que sobra
    else:
        new_triangle = dt.Triangle(points[0], points[1], points[2])
        triangles.append(new_triangle)

    return triangles

def ear_clipping_method(points):
    triangles = []

    return triangulation_recursion(points, triangles)

