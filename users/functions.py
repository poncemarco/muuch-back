def set_name(name):
    name_length = len(name.split())
    if name_length == 1:
        return name, None
    if name_length == 2:
        return name.split()[0], name.split()[1]
    if name_length == 3:
        return name.split()[0], name.split()[1] + ' ' + name.split()[2]
    return name.split()[0], ' '.join(name.split()[1:])