import time

import numpy as np
import cv2
import torch
from PIL import Image
from torchvision import transforms
from torch.utils.data import Dataset, DataLoader
import model

pipe = transforms.Compose([transforms.CenterCrop([600, 1000]), transforms.Resize([224])])
pipe1 = transforms.ToTensor()
device = torch.device('cuda')


class DataTrain(Dataset):
    def __init__(self, train_x=None, train_y=None, transform=pipe):
        self.image = train_x
        self.label = train_y

    def __getitem__(self, index):
        x = self.image[index]
        y = self.label[index]
        return x, y

    def __len__(self):
        return self.image.shape[0]


if __name__ == '__main__':
    data = np.load('data/data_train_0.npz', allow_pickle=True)
    data_image = data['image']/255
    data_label = data['label']
    ds = DataTrain(train_x=data_image, train_y=data_label)
    train_loader=DataLoader(ds,batch_size=8,shuffle=True)

    model_1=model.test()
    model_1.to('cuda')

    lean_rate=0.001
    loss=torch.nn.CrossEntropyLoss()
    optim=torch.optim.Adam(model_1.parameters(),lean_rate)
    for epoch in range(3):
        print(f'epoch :{epoch }')
        total_train_step=0
        avg_loss=0
        total_accuracy=0
        model_1.train()
        for data in train_loader:
            image,label=data[0].float().to(device),data[1].to(device)
            #print(image.shape)
            output=model_1(image)
            res_loss=loss(output,label.float())
            optim.zero_grad()
            res_loss.backward()
            optim.step()
            total_train_step+=1
            avg_loss+=res_loss
            if total_train_step%2==0:
                print(f"total_train_step:{total_train_step},loss:{res_loss},avg_loss:{avg_loss/total_train_step}")

    torch.save(model_1,'model_ep5_bc8')
    # cv2.imshow('1',x[44][0])
    # cv2.waitKey(0)
    # x=x/255
    #
    # print(x[44])
