with open('setup.conf', 'r') as f:
    env = f.readlines()
f.closed

with open('flower.conf', 'r') as f:
    data = f.readlines()
f.closed

var = []
for line in env:
    line_sp = line.replace('\n','').split('=')
    if len(line_sp)>1:
        var.append(line_sp)
var_d = dict(var)

for i in range(len(data)):
    if '[PATH_TO_EXEC]' in data[i]:
        data[i] = data[i].replace('[PATH_TO_EXEC]', var_d['CONDA_DIR']+'/bin/flower')
    if '[CELERY_APP_DIR]' in data[i]:
        data[i] = data[i].replace('[CELERY_APP_DIR]', var_d['CELERY_APP_DIR'])
    if '[LOG_DIR]' in data[i]:
        data[i] = data[i].replace('[LOG_DIR]', var_d['LOG_DIR'])
        
with open('flower.conf', 'w') as f:
    for line in data:
        f.write(line)
f.closed

