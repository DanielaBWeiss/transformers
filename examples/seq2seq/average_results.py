import numpy as np


PATH_LOG_FILES = '.'

R1 = []
R2 = []
RL = []

for i in range(1,21):
    with open("{}/val_{}.log".format(PATH_LOG_FILES,i), "r") as f:
        val_lines = f.readlines()

    for line in val_lines[::-1]:
        if 'val_rouge1 = ' in line:
            value = float(line.split('=')[-1])
            R1.append(value)
        elif 'val_rouge2 = ' in line:
            value = float(line.split('=')[-1])
            R2.append(value)
        elif 'val_rougeL = ' in line:
            value = float(line.split('=')[-1])
            RL.append(value)

print('R1 mean: ',np.mean(R1))
print('R1 var: ',np.var(R1))
print('R2 mean: ',np.mean(R2))
print('R2 var: ',np.var(R2))
print('RL mean: ',np.mean(RL))
print('RL var: ',np.var(RL))




#average results on thadani data


R1 = []
R2 = []
RL = []



for i in range(1,21):
    with open("{}/val_thadani_{}.log".format(PATH_LOG_FILES,i), "r") as f:
        val_lines = f.readlines()

    for line in val_lines[::-1]:
        if 'val_rouge1 = ' in line:
            value = float(line.split('=')[-1])
            R1.append(value)
        elif 'val_rouge2 = ' in line:
            value = float(line.split('=')[-1])
            R2.append(value)
        elif 'val_rougeL = ' in line:
            value = float(line.split('=')[-1])
            RL.append(value)

print('thadani R1 mean: ',np.mean(R1))
print('thadani R1 var: ',np.var(R1))
print('thadani R2 mean: ',np.mean(R2))
print('thadani R2 var: ',np.var(R2))
print('thadani RL mean: ',np.mean(RL))
print('thadani RL var: ',np.var(RL))
