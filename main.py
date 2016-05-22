import pdb

def file_tuples(filename):
    f = open(filename, 'r')
    tuples = []
    code = None
    for line in f:
        if code:
            tuples.append((code, line.strip()))
            code = None
        else:
            code = line.strip()

    return tuples

dxf = file_tuples('example.dxf')
