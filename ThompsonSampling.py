# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 22:36:08 2020

@author: kingslayer
"""

#Thompson Sampling

#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random


#importing the dataset
dataset=pd.read_csv(r"Ads_CTR_Optimisation.csv")

#Applying the Thompson Sampling
N=10000
d=10
ads_selected=[]
numbers_of_reward1=[0]*d
numbers_of_reward0=[0]*d
total_reward=0
for n in range(0,N):
    ad=0
    max_random=0
    for i in range(0,d):
        random_beta=random.betavariate(numbers_of_reward1[i]+1,numbers_of_reward0[i]+1)
        if random_beta>max_random:
            max_random=random_beta
            ad=i
    ads_selected.append(ad)
    reward=dataset.values[n,ad]
    if reward==1:
        numbers_of_reward1[ad]+=1
    else:
        numbers_of_reward0[ad]+=1
    total_reward+=reward


#Visualing results
plt.hist(ads_selected)
plt.xlabel("Ads")
plt.ylabel("No.of selections")
plt.title("Thompson Sampling")
plt.show()
