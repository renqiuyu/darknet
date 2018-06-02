#coding:utf-8
import matplotlib.pyplot as plt
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('usage : python3 pr-curve [image name]')
        sys.exit(1)

    x = list()
    y = list()
    x1 = list()
    x2 = list()
    y1 = list()
    y2 = list()
    with open('brain-tiny-v0.csv', 'r') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            y.append(float(lines[i].strip().split(',')[1]))
            x.append(float(lines[i].strip().split(',')[2]))
    with open('brain-tiny-v1.csv', 'r') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            y1.append(float(lines[i].strip().split(',')[1]))
            x1.append(float(lines[i].strip().split(',')[2]))
    with open('brain-tiny-v2.csv', 'r') as f:
        lines = f.readlines()
        for i in range(1, len(lines)):
            y2.append(float(lines[i].strip().split(',')[1]))
            x2.append(float(lines[i].strip().split(',')[2]))
    plt.figure(1)
    plt.title('Precision-Recall Curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.plot(x, y, 'b--', x1, y1,'g-',x2, y2, 'r-.')
    plt.show()
    plt.savefig('compare.png')
