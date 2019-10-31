
def get_val(key):
    with open('cfg.txt') as f:
        for line in f:
            line_key, val = line.split('=')
            if line_key.strip() == key:
                return val.strip()

def read_dict(filename):
    config_dict ={}
    with open('cfg.txt') as f:
        for line in f:
            try:
                key, val = line.split('=')
                config_dict[key.strip()] = val.strip()
            except ValueError:
                pass
    return config_dict

#print(get_val('port'))

#print(get_val('user'))

#print(read_dict('user'))

FILENAME = 'cfg.txt'

class Config:

    def __init__(self, filename=FILENAME):
        self.filename = filename
        self.config_dict = read_dict(filename)

    def get_val(self, key):
        return self.config_dict[key]

    def set_val(self, key, val):
        self.config_dict[key] = val

    def show_config(self):
        out = []
        for item in self.config_dict.items():
            out.append('%s = %s' % item)
        return '\n'.join(out)

    #def write(self):
        #with open(self.filename,'w') as f:
            #f.write(self.show_config())
            #f.close()

    def write(self):
        f=open('write.txt','w+')
        f.write(self.show_config())
        f.close()
        
    
    
config = Config()
print(config.get_val('port'))
print(config.get_val('user'))
print(config.show_config())
config.set_val('user','IJ')
print(config.get_val('user'))
print(config.show_config())
config.write()


