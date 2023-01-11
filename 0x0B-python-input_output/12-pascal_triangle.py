#!/usr/bin/python3
'''Technical interview preparation.'''


def pascal_triangle(n):
    '''
    Function that returns a list of lists of integers.
    Representing the Pascal’s triangle of n.
    '''
    try:
        triangles = [[1]]
        while (len(triangles)) != n:
            tri = triangles[-1]
            tmp = [1]
            for i in (len(tri) - 1):
                tmp.append(tri[i] + tri[i + 1])
            tmp.append(1)
            triangles.append(tmp)
    except n <= 0:
        return []
