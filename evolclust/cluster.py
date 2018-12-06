# clustering functionality

from numpy.linalg import norm
import numpy as np
from math import log

class Distance:
    @staticmethod
    def manhattan(a, b):
        a = np.array(a)
        b = np.array(b)
        return norm(a-b, ord=1)

    @staticmethod
    def euclidean(a, b):
        a = np.array(a)
        b = np.array(b)
        return norm(a-b, ord=2)


class Centroids:
    @staticmethod
    def cluster(data, centers, dist_func="euclid"):
        ''' dist_func=["euclid","manhat"] '''
        dist_func = Distance.manhattan if dist_func == "manhat" else Distance.euclidean
        samples_num = len(data)
        dist_array = np.full(samples_num, float("inf"))
        labels_array = np.zeros(samples_num)
        for i in range(len(centers)):
            for j in range(samples_num):
                cur_dist = dist_func(centers[i],data[j])
                if cur_dist < dist_array[j]:
                    dist_array[j] = cur_dist
                    labels_array[j] = i
        return labels_array


#TODO: tests
class Evaluate:

    @staticmethod
    def informationGain(true_labs, grouped_labs):
        # h - entropy
        def entropy_addend(probab, log_base):
            return - probab * log(probab, log_base)
        t_labs = np.array(true_labs)
        g_labs = np.array(grouped_labs)
        # true data entropy
        _, cnts = np.unique(t_labs, return_counts=True)
        data_h = 0
        for c in cnts:
            data_h += entropy_addend(c/len(t_labs), len(cnts))
        # entropy in clusters (groups)
        g_uniq, g_cnts = np.unique(g_labs, return_counts=True)
        total_h = 0
        for g_i, cnt_i in zip(g_uniq, g_cnts):
            cur_t_labs = t_labs[g_labs==g_i]
            _, cur_cnts = np.unique(cur_t_labs, return_counts=True)
            cur_h = 0
            for cnt in cur_cnts:
                cur_h += entropy_addend(cnt/cnt_i, len(cnts))
            total_h += cnt_i/len(t_labs) * cur_h
        # information gain
        return data_h - total_h 


    @staticmethod
    def silhouette():
        pass
