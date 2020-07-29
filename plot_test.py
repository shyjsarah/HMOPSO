# encoding: utf-8
import numpy as np
import os
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
# from mpl_toolkits.mplot3d import Axes3D
import fitness_funs as fit


class Plot_pareto:

    def show(self, in_, fitness_, archive_in, archive_fitness,i,path_s):

        fig,ax3=plt.subplots()
        ax3.set_title(str(i))
        ax3.set_xlim((0, 0.5))
        ax3.set_ylim((0, 0.5))
        ax3.set_xlabel('cpu_std')
        ax3.set_ylabel('memory_std')
        ax3.scatter(fitness_[:, 0], fitness_[:, 1], s=10, c='blue', marker=".")
        ax3.scatter(archive_fitness[:, 0], archive_fitness[:, 1], s=30, c='red', marker=".", alpha=1.0)
        #plt.savefig(path_s+'/'+str(i)+'.png')
        #print(path_s+'/'+str(i)+'.png')
        #plt.show()
        plt.close()

