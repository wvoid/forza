import numpy as np
import time
import torch
import image_capture
import torch.nn.functional as f
import press_keys
device = torch.device('cuda')

if __name__=='__main__':
    #time.sleep(3)
    model_1=torch.load('model_ep5_bc8')
    while True:
        x=image_capture.collect_frames()
        x=np.reshape(x,(1,)+x.shape)
        y=model_1(torch.from_numpy(x).float().to(device))
        z=f.softmax(y,dim=1)
        print(z)
        # op=z.data.max(1,keepdim=True)[1]
        # press_keys.switch[op[0,0].item()]()
        # print(op)
