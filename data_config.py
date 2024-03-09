# configuration file to claim the data we used
# author: ynie
# date: Jan, 2020
import os
import os.path as osp
from datetime import datetime
#from huggingface_hub import DatasetCard
#from huggingface_hub import login
#login()
#import datasets
#shapenet_normalized_path = datasets.load_dataset("ShapeNet/ShapeNetCore")
shapenet_categlory_pair = {
    'table' : '04379243',
    'jar' : '03593526',
    'skateboard' : '04225987',
    'car' : '02958343',
    'bottle' : '02876657',
    'tower' : '04460130',
    'chair' : '03001627',
    'bookshelf' : '02871439',
    'camera' : '02942699',
    'airplane' : '02691156',
    'laptop' : '03642806',
    'basket' : '02801938',
    'sofa' : '04256520',
    'knife' : '03624134',
    'can' : '02946921',
    'rifle' : '04090263',
    'train' : '04468005',
    'pillow' : '03938244',
    'lamp' : '03636649',
    'trashbin' : '02747177',
    'mailbox' : '03710193',
    'watercraft' : '04530566',
    'motorbike' : '03790512',
    'dishwasher' : '03207941',
    'bench' : '02828884',
    'pistol' : '03948459',
    'rocket' : '04099429',
    'loudspeaker' : '03691459',
    'filecabinet' : '03337140',
    'bag' : '02773838',
    'cabinet' : '02933112',
    'bed' : '02818832',
    'birdhouse' : '02843684',
    'display' : '03211117',
    'piano' : '03928116',
    'earphone' : '03261776',
    'telephone' : '04401088',
    'stove' : '04330267',
    'microphone' : '03759954',
    'bus' : '02924116',
    'mug' : '03797390',
    'remote' : '04074963',
    'bathtub' : '02808440',
    'bowl' : '02880940',
    'keyboard' : '03085013',
    'guitar' : '03467517',
    'washer' : '04554684',
    # 'bicycle' : '02834778', # not present in shapenet2 
    'faucet' : '03325088',
    'printer' : '04004475',
    'cap' : '02954340',
    'clock' : '03046257',
    'helmet' : '03513137',
    'flowerpot' : '03991062',
    'microwaves' : '03761084',
    'cellphone' : '02992529'
}

synset_category_pair = {value:key for key, value in shapenet_categlory_pair.items()}

our_categories = ['chair', 'bed']
our_categories = [shapenet_categlory_pair[cat] for cat in our_categories]

# dataset_dir = '../../datasets/depth_renderer_dataset'
# dataset_dir = '../../datasets'
dataset_dir = '/users/czhan157/Downloads/depth_renderer_test'

# shapenet_path = './datasets/ShapeNetCore.v2'
# shapenet_path = '/home/aditya/Research/phd/code/datasets/ShapeNetCore.v2'
# shapenet_path = '/home/aditya/Research/phd/code/datasets/shapenetcore'
# shapenet_normalized_path= './datasets/ShapeNetCore.v2_normalized'
# shapenet_normalized_path = './datasets/ShapeNetCore.v2_sample'
# shapenet_normalized_path = './datasets/test_shapenet_normalized'
# shapenet_normalized_path = osp.join(dataset_dir, 'test_shapenet_core')
# shapenet_normalized_path = '/home/gridsan/aagarwal/Research/phd/datasets/depth_renderer_dataset/test_shapenet_core'
# shapenet_normalized_path = '/home/gridsan/aagarwal/Research/phd/datasets/ShapeNetCore_Zip'
#shapenet_normalized_path = osp.join(dataset_dir, 'ShapeNetCore_Zip')
# shapenet_normalized_path = './datasets/ShapeNetCore.v2_normalized'
shapenet_normalized_path = './ShapeNetCore'

# shapenet_normalized_path = './datasets/snet_test'
# shapenet_rendering_path = './datasets/snet_renderings'
# shapenet_rendering_path = './datasets/shapenet_sample_renderings'
# shapenet_rendering_path = './datasets/test_shapenet_renders'
# shapenet_rendering_path = '../../datasets/test_shapenet_renders'
# shapenet_rendering_path = osp.join(dataset_dir, 'test_shapenet_renders')
# shapenet_rendering_path = '/home/gridsan/aagarwal/Research/phd/datasets/depth_renderer_dataset/test_shapenet_renders4'
# shapenet_rendering_path = '/home/gridsan/aagarwal/Research/phd/datasets/shapenetcore_renders'
# shapenet_rendering_path = '/home/gridsan/aagarwal/Research/phd/datasets/shapenet_renders2'
shapenet_rendering_path = osp.join(dataset_dir, 'shapenet_renders')
# shapenet_rendering_path = osp.join(dataset_dir, 'shapenet_tabletop_renders')
# camera_setting_path = './datasets/camera_settings'
# camera_setting_path = osp.join(dataset_dir, 'camera_settings')
# camera_setting_path = '/home/gridsan/aagarwal/Research/phd/datasets/depth_renderer_dataset/camera_settings'
camera_setting_path = osp.join(dataset_dir, 'camera_settings')

now = datetime.now()

model_view_path = './model_view_metadata/{}/result.pkl'.format(now.strftime('%Y-%m-%d_%H-%M-%S'))
# watertight_mesh_path = './datasets/ShapeNetCore.v2_watertight'
# watertight_mesh_path = osp.join(dataset_dir, 'test_shapenet_watertight')
# watertight_mesh_path = '/home/gridsan/aagarwal/Research/phd/datasets/depth_renderer_dataset/test_shapenet_watertight'
watertight_mesh_path = osp.join(dataset_dir, now.strftime('%Y-%m-%d_%H-%M-%S'), 'ShapeNetCore.v2_watertight')

shape_scale_padding = 0
total_view_nums = 20