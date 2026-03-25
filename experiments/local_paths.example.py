from pathlib import Path

#setup instruction 
# 1.rename this file it to 'local_paths.py'
# 2.set DATA_ROOT to the path where your 'skimage_segmentation' folder
# 3. make sure that 'paired.csv' inside that folder

DATA_ROOT = Path("/absolute/path/to/skimage_segmentation")

MODEL_CFG = Path("configs/sam2.1/sam2.1_hiera_l.yaml")
SAM2_CHECKPOINT = Path("../checkpoints/sam2.1_hiera_large.pt")