import os
print(os.access('.', os.R_OK))

#print(os.path.exist('logging1.py'))

print(os.listdir('.'))

def dirlist(path, indent=0):
    print(' '*indent, path)
    if os.path.isdir(path):
        old_path = os.path.abspath('.')
        os.chdir(path)
        for filename in os.listdir('.'):
                dirlist(filename, indent+1)
        os.chdir(old_path)

dirlist('.')
