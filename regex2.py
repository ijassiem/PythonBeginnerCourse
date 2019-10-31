import re

def read_dict_re(filename):
    config_dict ={}
    content = open(filename).read()
    for match in re.finditer(r'^\s*(.+?)\s*=\s*(.+?)\s*$', content, re.M):
        key, val = match.groups()
        config_dict[key] = val
    return config_dict


#def read_dict_re4(filename):
#    config_dict={}
#    content = open(filename).read()
#    return dict(m.groups() for m in re.finditer(r'^(.+)\s*=\s*(.+?)$', content

x = read_dict_re("cfg.txt")
print(x)
