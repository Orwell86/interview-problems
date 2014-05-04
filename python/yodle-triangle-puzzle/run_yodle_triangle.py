import trianglepuzzle

def load_triangle(filename):
    """Loads the triangle.txt into a flat array"""
    values = list()
    with open(filename) as f:
        next_line = f.readline()
        while next_line:
            values.extend(map(lambda x: int(x), next_line.split(' ')))
            next_line = f.readline()
    return values

if __name__ == "__main__":
    values = load_triangle('./triangle.txt')
    print trianglepuzzle.find_triangle_path(values)

