#coding:utf-8
import matplotlib
# matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('usage : python3 pr-curve ./[filename].csv ./[image name]')
        sys.exit(1)

    x = list()
    y = list()
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            y.append(float(lines[i].strip().split(',')[1]))
            x.append(float(lines[i].strip().split(',')[2]))
    plt.figure(1)
    plt.title('Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.plot(x, y, 'b--')
    plt.show()
    plt.savefig(sys.argv[2])
