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

def sections(tuples):
    sections_list = []
    curr_section = []
    in_section = False
    for t in tuples:
        if in_section:
            # Check for a section end
            if t[0] == '0' and t[1] == 'ENDSEC':
                sections_list.append(curr_section)
                in_section = False
            else:
                curr_section.append(t)
        else:
            # Check for a section start
            if t[0] == '0' and t[1] == 'SECTION':
                curr_section = []
                in_section = True
    return sections_list

secs = sections(dxf)
