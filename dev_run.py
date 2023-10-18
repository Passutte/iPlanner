import argparse
import time
import numpy as np
import torch
import cv2
import sys
import os
import matplotlib.pyplot as plt
sys.path.append('iplanner')

from iplanner.ip_algo import *
from iplanner.percept_net import *
from iplanner.torchutil import *



def main():

    cwd = os.getcwd()

    file_path = f'{cwd}/../iPlanner_Data/data/TrainingData/2n8kARJN3HM/depth/0.png'

    # Load the image
    img = cv2.imread(file_path, 0)

    parser = argparse.ArgumentParser(description='iPlanner')
    args = parser.parse_args(args=[])

    args.model_save = f'{cwd}/iplanner/models/plannernet_pretrained.pt'
    args.crop_size = [360,640]
    args.sensor_offset_x = 0.
    args.sensor_offset_y = 0.0


    ip_algo = IPlannerAlgo(args=args)

    curr_img = img.copy()
    goal_rb = torch.from_numpy(np.array([0.0, 5.0, 0.0, 1.0, 0.0, 0.0, 0.0])[None,:]).float()

    preds, waypoints, fear_output, _ = ip_algo.plan(curr_img, goal_rb)

    print(preds.shape)
    print(preds)
    print(fear_output)



if __name__ == "__main__":
    main()