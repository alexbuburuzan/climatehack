import os
import numpy as np
import torch
import random
import multiprocessing
from submission.ConvLSTM2 import config_3x3_16_3x3_32_3x3_64

# ensure reproducibility
SEED = 666013
os.environ['PYTHONHASHSEED'] = str(SEED)
random.seed(SEED)
np.random.seed(SEED)
torch.manual_seed(SEED)
torch.cuda.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
# torch.backends.cudnn.enabled = False
torch.backends.cudnn.benchmark = False
torch.backends.cudnn.deterministic = True

SATELLITE_ZARR_PATH = "gs://public-datasets-eumetsat-solar-forecasting/satellite/EUMETSAT/SEVIRI_RSS/v3/eumetsat_seviri_hrv_uk.zarr"

config = {
    'dataset_path': "D:\\climate_hack\\eumetsat_seviri_hrv_uk.zarr",
    'data_path': "D:\\climate_hack\\data",
    'batch_size': 6,
    'lr': 1e-4,
    'device': "cuda:0" if torch.cuda.is_available() else "cpu",
    'num_epochs': 30,
    'num_workers': multiprocessing.cpu_count()
}

################
round_name = 'exp' #conv-lstm-unet_no-final-bn_head-conv' #'unet_batch-size-64_num-epochs-10'
################

results_path =  os.path.join("D:/climate_hack/results", round_name)

results_config = {
    'results_path' : results_path,
    'checkpoints_path' : os.path.join(results_path, 'checkpoints'), 
    'logs_path' : os.path.join(results_path, 'logs'),
    'tensorboard_path' : os.path.join(results_path, 'tensorboard')
}

config = {**config, **results_config, **config_3x3_16_3x3_32_3x3_64}