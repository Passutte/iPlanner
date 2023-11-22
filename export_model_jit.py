import argparse
import time
import numpy as np
import torch
import cv2
import sys
import os
import matplotlib.pyplot as plt
sys.path.append('iplanner')

from iplanner.plannernet import IPlannerAlgo

PATH_MODEL = '/home/pascal/Developer/legged_robotics/iPlanner/iplanner/models/plannernet_dimensionless_emb512.pt'

def main():

    parser = argparse.ArgumentParser(
                        prog='iPlanner',
                        description='Imperative learning for path planning',
                        epilog='')
    args = parser.parse_args(args=[])
    args.model_save = PATH_MODEL
    args.crop_size = [360,640]
    args.sensor_offset_x = 0.0
    args.sensor_offset_y = 0.0
    args.camera_tilt = 0.0

    ip_algo = IPlannerAlgo(args=args)
    model = ip_algo.net
    torch.jit.save(torch.jit.script(model), 'iplanner_emb512.pt')
    print("Model saved to jit")


if __name__ == "__main__":
    main()