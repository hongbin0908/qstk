#!/usr/bin/env python

#Third Party Imports
import matplotlib.pyplot as plt
import pandas as pd




def main():
    symbols = ["A", "B", "C"]
    key = [1,2,3]
    price = [[1,2,3,4,5,6,7,8,9,10],
             [1,3,5,7,9,11,13,15,17,19],
             [2,4,6,8,10,12,14,16,10,20],
             ]
    plt.clf()
    plt.plot(key, price)
    plt.savefig("testmatplot1.pdf", format='pdf')
if __name__ == '__main__':
    main()
