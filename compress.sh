#!/bin/bash

#SBATCH -N 1
#SBATCH -c 5
#SBATCH -n 5

# activate the conda module
source ~/miniconda3/etc/profile.d/conda.sh
conda activate blender

cd /home/gridsan/aagarwal/Research/phd/datasets
tar -czvf shapenet_renders.tar.gz shapenet_renders