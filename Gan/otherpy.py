import numpy as np
import gradio as gr
import torch
import os
import models.generator
from torch.autograd import Variable
from torchvision.utils import save_image
import cv2
import matplotlib.pyplot as plt

# Set device where training will be progressed & base Tensor type (dtype=float32)
if torch.cuda.is_available():
    device = torch.device("cuda")
    Tensor = torch.cuda.FloatTensor
else:
    device = torch.device("cpu") 
    Tensor = torch.FloatTensor

###### GAN 모델 호출
GANmodel = models.generator.Generator(latent_dim=100,image_shape=(3,224,224))

GANmodel.load_state_dict(torch.load("generator.pth", map_location=device))

GANmodel.eval()
#######

# z = Variable(Tensor(np.random.normal(0, 1, (images.size(0), args.latent_dim))))
# z = Variable(Tensor(np.random.normal(0, 1, (생성 개수 인듯!, args.latent_dim))))
z = Variable(Tensor(np.random.normal(0, 1, (1, 100))))


gen_images = GANmodel(z)

save_image(gen_images.data, '생성.png', normalize=True)



# print(gen_images[0].shape)
# torch.Size([1, 3, 224, 224])
# (480, 640, 3)

from torchvision.transforms.functional import to_pil_image
img = gen_images[0]

plt.figure()
plt.imshow(to_pil_image(0.5*img+0.5), cmap='gray')
plt.title('train')

img = to_pil_image(0.5*img+0.5)

print(img) # PIL 이미지임
imgArray = np.array(img) # 넘파이로 변경
print(imgArray.shape)

# img = gen_images[0] # Tensor형태의 이미지. [C, H, W]
# # print(img.shape) # torch.Size([3, 224, 224])

# img = img.detach().cpu().numpy() # tensor -> numpy
# # print(img.shape) # (3, 224, 224)

# img = np.transpose(img, (1, 2, 0)) # [C,H,W] -> [H,W,C]

# img = img * 255.0  # *255 or IMAGENET denorm 방법 < 이게 맞을까요
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) # RGB 채널
# img = img.astype(np.uint8).copy() # np.float32 -> np.uint8
# cv2.imshow('w', img)
# cv2.waitKey(0)

