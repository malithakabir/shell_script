from __future__ import absolute_import, unicode_literals
from .celery import app
from subprocess import PIPE, Popen

@app.task
def add(x, y):
    return x + y

@app.task
def run_script(script_path):
    p = Popen(["python", "-u", script_path],stdout=PIPE)
    p.wait()
    out = p.stdout.readlines()
    filename = script_path.replace('py', 'txt')
    with open(filename, 'wb') as f:
        for line in out:
            f.write(line)
            
    return 'done!'
