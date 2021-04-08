import os

dir_path = os.path.dirname(os.path.realpath(__file__))

with open(os.path.join(dir_path, 'index.h'), 'w') as f:
    f.write('#include<stdio.h>')

