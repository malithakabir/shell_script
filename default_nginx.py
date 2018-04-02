with open('setup.conf', 'r') as f:
    env = f.readlines()
f.closed

with open('default', 'r') as f:
    data = f.readlines()
f.closed

var = []
for line in env:
    line_sp = line.replace('\n','').split('=')
    if len(line_sp)>1:
        var.append(line_sp)
var_d = dict(var)

for i in range(len(data)):
    if '[PUBLIC_IP]' in data[i]:
        data[i] = data[i].replace('[PUBLIC_IP]', var_d['PUBLIC_IP'])

with open('default', 'w') as f:
    for line in data:
        f.write(line)
f.closed

