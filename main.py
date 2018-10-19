#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 4 15:29:59 2018
main file for operate with lloyd-max iterative quantizer
python3 -b 8
In 8 bits, after 1e6 iterations, the minimum MSE loss is around 3.6435e-05.
@author: Fuengfusin Ninnart
"""
from utils import normal_dist, expected_normal_dist, MSE_loss, lloyd_max_quantizer
#Guard protection for error: No module named 'tkinter'
try: import matplotlib.pyplot as plt
except ModuleNotFoundError:
    import matplotlib
    matplotlib.use('agg')
    import matplotlib.pyplot as plt

import numpy as np
import argparse, os

parser = argparse.ArgumentParser(description='lloyd-max iteration quantizer')
parser.add_argument('--bit', '-b', type=int, default=3, help='number of bit for quantization')
parser.add_argument('--iteration', '-i', type=int, default=1000+1, help='number of iteration')
parser.add_argument('--range', '-r', type=int, default=10, help='range of the initial distribution')
parser.add_argument('--resolution', '-re', type=int, default=100, help='resolution of the initial distribution')
parser.add_argument('--save_location', '-s', type=str, default='outputs', help='save location of representations and ')
args = parser.parse_args()

if __name__ == '__main__':

    #Generate the 1000 simple of input signal as the gaussain noise in range [0,1].
    x = np.random.normal(0,1,1000)
    repre = lloyd_max_quantizer.start_repre(x, args.bit)
    min_loss = 1.0
    
    for i in range(args.iteration):
        thre = lloyd_max_quantizer.threshold(repre)
        
        #In case wanting to use with another mean or variance, need to change mean and variance in untils.py file
        repre = lloyd_max_quantizer.represent(thre, expected_normal_dist, normal_dist)
        x_hat_q = lloyd_max_quantizer.quant(x, thre, repre)
        loss = MSE_loss(x, x_hat_q)
        
        #print every 10 loops
        if(i%10==0 and i!=0):
            print('iteration: ' + str(i))
            print('thre: ' + str(thre))
            print('repre: ' + str(repre))
            print('loss: ' + str(loss))
            print('++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++')
        
        #keep the threhold and representation that has the lowest MSE loss.
        if(min_loss>loss):
            min_loss = loss
            min_thre = thre
            min_repre = repre
    
    #Save the best thresholds and representations in the numpy format for further using.
    try: os.mkdir(args.save_location)
    except FileExistsError: pass
    np.save(args.save_location + '/' + 'MSE_loss', min_loss)
    np.save(args.save_location + '/' + 'thre', min_thre)
    np.save(args.save_location + '/' + 'repre', min_repre)
    
    #x_hat_q with the lowest amount of loss.
    best_x_hat_q = lloyd_max_quantizer.quant(x, min_thre, min_repre)
    fig = plt.figure()
    ax = fig.add_subplot(3,1,1)
    ax.plot(range(np.size(x)), x, 'b')
    ax = fig.add_subplot(3,1,2)
    ax.plot(range(np.size(best_x_hat_q)), best_x_hat_q, 'rx')
    ax = fig.add_subplot(3,1,3)
    ax.plot(range(np.size(best_x_hat_q)), best_x_hat_q, 'y')
    plt.show()
    fig.savefig(args.save_location + '/' + 'results.png', dpi=fig.dpi)
    