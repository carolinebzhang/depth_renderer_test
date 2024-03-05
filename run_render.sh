#!/bin/bash

#SBATCH -N 1
#SBATCH -c 5
#SBATCH -n 5

# activate the conda module
source ~/miniconda3/etc/profile.d/conda.sh
conda activate blender

# python run_render.py --count 5 --categories car airplane
# python run_render.py --count 5 --categories bicyble train
# python run_render.py --count 5 --categories chair camera
# python run_render.py --count 5 --categories sofa lamp
# python run_render.py --count 5 --categories watercraft motorbike
# python run_render.py --count 5 --categories pistol rifle
# python run_render.py --count 5 --categories bed cabinet
# python run_render.py --count 5 --categories rocket loudspeaker
# python run_render.py --count 5 --categories bottle tower
# python run_render.py --count 5 --categories bench bus
# python run_render.py --count 5 --categories washer printer
# python run_render.py --count 5 --categories flowerpot microwaves
# python run_render.py --count 5 --categories telephone earphone
# python run_render.py --count 5 --categories mailbox trashbin
# python run_render.py --count 5 --categories stove bathtub
# python run_render.py --count 5 --categories faucet display
# python run_render.py --count 5 --categories dishwasher microphone
# python run_render.py --count 5 --categories skateboard cap
# python run_render.py --count 5 --categories filecabinet birdhouse
# python run_render.py --count 5 --categories clock bookshelf
# python run_render.py --count 5 --categories can guitar
# python run_render.py --count 5 --categories keyboard laptop
# python run_render.py --count 5 --categories piano bowl
# python run_render.py --count 5 --categories knife basket
# python run_render.py --count 5 --categories bicycle table
# python run_render.py --count 5 --categories jar mug
# python run_render.py --count 5 --categories helmet pillow
# python run_render.py --count 5 --categories remote bag

# python run_render.py --count 20 --categories cabinet bicycle guitar filecabinet rifle train

# python run_render.py --count 5 --categories car # shapenet_renders
# python run_render.py --count 5 --categories airplane # shapenet_renders
# python run_render.py --count 5 --categories chair # shapenet_renders1
# python run_render.py --count 5 --categories motorbike # done shapenet_renders1
# python run_render.py --count 5 --categories sofa # done shapenet_renders1
# python run_render.py --count 5 --categories camera # shapenet_renders2
# python run_render.py --count 5 --categories bowl # shapenet_tabletop_renders
# python run_render.py --count 5 --categories bottle # shapenet_tabletop_renders
# python run_render.py --count 5 --categories can # shapenet_tabletop_renders
# python run_render.py --count 5 --categories bag # shapenet_tabletop_renders
# python run_render.py --count 5 --categories basket # shapenet_tabletop_renders
# python run_render.py --count 5 --categories cap # shapneet_tabletop_renders
# python run_render.py --count 5 --categories clock # shapenet_tabletop_renders
# python run_render.py --count 5 --categories earphone # shapenet_tabletop_renders
# python run_render.py --count 5 --categories flowerpot # shapenet_tabletop_renders
# python run_render.py --count 5 --categories jar # shapenet_tabletop_renders
# python run_render.py --count 5 --categories knife # shapenet_tabletop_renders
# python run_render.py --count 5 --categories lamp # shapenet_tabletop_renders
# python run_render.py --count 5 --categories laptop # shapenet_renders
# python run_render.py --count 5 --categories mug # shapenet_tabletop_renders
# python run_render.py --count 5 --categories microphone # shapenet_tabletop_renders
# python run_render.py --count 5 --categories remote # shapenet_tabletop_renders
# python run_render.py --count 5 --categories telephone # shapenet_tabletop_renders
# python run_render.py --count 5 --categories trashbin # shapenet_tabletop_renders
# python run_render.py --count 5 --categories train # shapenet_renders
# python run_render.py --count 5 --categories watercraft # shapenet_renders
# python run_render.py --count 5 --categories bus # shapenet_renders
# python run_render.py --count 5 --categories helmet # shapenet_tabletop_renders

# python run_render.py --count 5 --categories clock # shapenet_tabletop_renders
# python run_render.py --count 5 --categories earphone # shapenet_tabletop_renders
# python run_render.py --count 5 --categories flowerpot # shapenet_tabletop_renders
# python run_render.py --count 5 --categories jar # shapenet_tabletop_renders
# python run_render.py --count 5 --categories knife # shapenet_tabletop_renders
# python run_render.py --count 5 --categories cellphone # shapenet_tabletop_renders

# python run_render.py --count 5 --categories lamp # shapenet_renders
# python run_render.py --count 5 --categories microphone # shapenet_renders
# python run_render.py --count 5 --categories remote # shapenet_renders
# python run_render.py --count 5 --categories telephone # shapenet_renders
# python run_render.py --count 5 --categories trashbin # shapenet_renders
python run_render.py --count 5 --categories mug camera # shapenet_renders