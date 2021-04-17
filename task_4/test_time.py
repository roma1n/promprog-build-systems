import time
import os

cmd1 = './build/main lenna.png map.png main_out.png'
cmd2 = './build/code_gen lenna.png main_out.png'

print('Executing default solution')
start = time.time()
os.system(cmd1)
finish = time.time()
print(f'Time spend: {finish - start:.4f}s')

print('Executing solution with code generation')
start = time.time()
os.system(cmd2)
finish = time.time()
print(f'Time spend: {finish - start:.4f}s')
