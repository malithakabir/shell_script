with open('var.sh', 'r') as f:
    env = f.readlines()
f.closed

with open('default', 'r') as f:
    data = f.readlines()
f.closed

head = env[0].replace('PUBLIC_IP=','').replace('\n','')
comm = data[2].replace('[SERVER_PUBLIC_IP_HERE]', head)
data[2] = comm

with open('default', 'w') as f:
    for line in data:
        f.write(line)
f.closed

