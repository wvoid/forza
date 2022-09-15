import numpy as np
import cv2
import torch
from PIL import Image
from torchvision import transforms
import model

pipe=transforms.Compose([ transforms.CenterCrop([600,1000]),transforms.Resize([224])])

if __name__=='__main__':
    data=np.load('data/data_train_1.npy',allow_pickle=True)
    x = data[0:10,0]
    cv2.imshow('p',x[1])
    cv2.waitKey(0)
    for i in x:
        x1=Image.fromarray(i)
        y=pipe(x1)
    y=np.array(y)
    print(y)
    net=model.test()
    y=np.reshape(y,(1,1)+y.shape)
    print(y.shape)
    z=net(torch.Tensor(y))
    print(z)
    #print(x.shape)
    #model.test()