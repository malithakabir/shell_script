with open('setup.conf', 'r') as f:
    env = f.readlines()
f.closed

with open('flower.conf', 'r') as f:
    data = f.readlines()
f.closed

head = env[1].replace('CONDA_DIR=','').replace('\n','')
tail = '/miniconda3/bin/flower'
comm = data[1].replace('[PATH]', head+ tail) 
data[1] = comm

head = env[1].replace('CONDA_DIR=','').replace('\n','')
comm = data[2].replace('[DIR]', head)
data[2] = comm

head = env[1].replace('CONDA_DIR=','').replace('\n','')
tail = '/logfiles/'
comm = data[11].replace('[LOG_FILE_DIR]', head+tail)
data[11] = comm
comm = data[12].replace('[LOG_FILE_DIR]', head+tail)
data[12] = comm

with open('flower.conf', 'w') as f:
    for line in data:
        f.write(line)
f.closed

