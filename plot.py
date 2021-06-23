#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
import matplotlib.patches as patches

auToKm = 149597900

def main():
    filename = 'data.txt'
    xs = []
    ys = []
    vxs = []
    vys = []
    with open(filename, 'r') as f:
        for line in f:
            l = line.replace('[','').replace(']','').replace('(','').replace(')','').split(',')
            l = [float(el) for el in l]
            xs.append(l[0]/auToKm)
            ys.append(l[1]/auToKm)
            vxs.append(l[2])
            vys.append(l[3])

    fig, ax = plt.subplots(figsize=(4,4), facecolor='#000000')
    ax.set_facecolor('#000000')
    line, = ax.plot([], [], marker='o', linestyle='none', color='C0', markeredgecolor='white', markersize=10)
    ax.plot(0,0 , marker='*', linestyle='none', color='#DAA520', markeredgecolor='white', markersize=10)
    ax.plot(xs, ys, linestyle='--', color='white', alpha=0.1, linewidth=3)

    box_size = 2
    ax.set_xlim(-box_size*1.1, box_size*1.1)
    ax.set_ylim(-box_size*1.1, box_size*1.1)
    ax.set_aspect('equal')
    #ax.grid()

    def init():
        return line,

    def animate(i):
        line.set_data(xs[i], ys[i])

        scale = 0.025
        print(vxs[i]*scale,vys[i]*scale)
        arr = patches.Arrow(xs[i], ys[i], vxs[i]*scale, vys[i]*scale, facecolor='C1', edgecolor='white', animated=True, width=0.25)
        ax.add_patch(arr)

        return line,arr,

    anim = animation.FuncAnimation(fig,
                                   animate,
                                   init_func=init,
                                   frames=len(xs),
                                   interval=20,
                                   blit=True)

    '''
    ax.plot(xs,ys, marker='o', linestyle='none')
    ax.quiver(xs,ys,vxs,vys)
    '''

    padding_scale = 1.3
    ax.set_xlim(padding_scale*min(xs), padding_scale*max(xs))
    ax.set_ylim(padding_scale*min(ys), padding_scale*max(ys))
    ax.xaxis.set_ticklabels([])
    ax.yaxis.set_ticklabels([])
    plt.show()

if __name__=='__main__':
    main()
