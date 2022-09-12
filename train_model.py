import numpy as np
import cv2
import torch
import model

if __name__=='__main__':
    data=np.load('data/data_train_0.npy',allow_pickle=True)
    #cv2.imshow('p',data[100][0])
    #cv2.waitKey(0)
    #x=data[:,1]
    #print(x[:])
    model.test()