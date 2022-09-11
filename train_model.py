import numpy as np
import cv2

if __name__=='__main__':
    data=np.load('data/data_train_0.npy',allow_pickle=True)
    cv2.imshow('1',data[0][0])
    cv2.waitKey(0)
    x=data[-50:]
    print(x.shape)