"""
Pretrained Pytorch face detection (MTCNN) and recognition (InceptionResnet) models
https://github.com/timesler/facenet-pytorch
"""
import torch
from facenet_pytorch import MTCNN


def get_model_face_detection():
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print('Running on device: {}'.format(device))
    net = MTCNN(keep_all=True, device=device)
    return net


# instance of net
model = get_model_face_detection()
