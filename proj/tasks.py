from __future__ import absolute_import, unicode_literals
from .celery import app
from subprocess import PIPE, Popen
import os

NOTEBOOK_BASE_DIR = '/home/ubuntu/jupyter/notebook/'
TRAIN_MODULE_DIR = '/home/ubuntu/jupyter/notebook/objDetectTF/models/research/object_detection'

@app.task
def add(x, y):
    return x + y

@app.task
def run_script(logfile_path, script_path):
    p = Popen(["python", "-u", script_path],stdout=PIPE)
    p.wait()
    out = p.stdout.readlines()
    with open(logfile_path, 'wb') as f:
        for line in out:
            f.write(line)
            
    return 'done!'

@app.task
def run_command(logfile_path, config_path, train_dir):
    
    lg = NOTEBOOK_BASE_DIR + logfile_path
    cp=NOTEBOOK_BASE_DIR + config_path
    td=NOTEBOOK_BASE_DIR + train_dir
    
    os.chdir(TRAIN_MODULE_DIR)
    p = Popen(["python", "-u", 'train.py', '--logtostderr', '--pipeline_config_path=%s'%cp, '--train_dir=%s'%td],stdout=PIPE)
    p.wait()
    out = p.stdout.readlines()
    
    with open(lg, 'wb') as f:
        for line in out:
            f.write(line)
            
    return 'done!'
