import numpy as np
import re
import imageio
import json
import os
import os.path as osp
from glob import glob
import sys 
sys.path.append('../')
from data_config import shapenet_categlory_pair, synset_category_pair
imageio.plugins.freeimage.download()
from datasets import load_dataset
def read_obj(model_path, flags = ('v')):
    fid = open(model_path, 'r', encoding="utf-8")

    data = {}

    for head in flags:
        data[head] = []

    for line in fid:
        line = line.strip()
        if not line:
            continue
        line = re.split('\s+', line)
        if line[0] in flags:
            data[line[0]].append(line[1:])

    fid.close()

    if 'v' in data.keys():
        data['v'] = np.array(data['v']).astype(np.float)

    if 'vt' in data.keys():
        data['vt'] = np.array(data['vt']).astype(np.float)

    if 'vn' in data.keys():
        data['vn'] = np.array(data['vn']).astype(np.float)

    return data

def read_exr(exr_file_list):
    '''
    read exr files and output a matrix.
    :param exr_file_list:
    :return:
    '''
    if isinstance(exr_file_list, str):
        exr_file_list = [exr_file_list]

    im_list = []

    for exr_file in exr_file_list:
        if not exr_file.endswith('exr'):
            raise TypeError('file is not with the format of .exr.')

        im_list.append(imageio.imread(exr_file, format='exr')[:,:,0])

    return np.array(im_list)

def read_txt(txt_file_list):
    '''
    read txt files and output a matrix.
    :param exr_file_list:
    :return:
    '''
    if isinstance(txt_file_list, str):
        txt_file_list = [txt_file_list]

    output_list = []
    for txt_file in txt_file_list:
        output_list.append(np.loadtxt(txt_file))

    return np.array(output_list)

def read_image(image_file_list):
    '''
    read image files and output a matrix.
    :param exr_file_list:
    :return:
    '''
    if isinstance(image_file_list, str):
        image_file_list = [image_file_list]

    output_list = []
    for output_file in image_file_list:
        output_list.append(imageio.imread(output_file, format='png'))

    return np.array(output_list)

def write_obj(objfile, data):
    '''
    Write data into obj_file.
    :param objfile (str): file path.
    :param data (dict): obj contents to be writen.
    :return:
    '''
    with open(objfile, 'w+') as file:
        for key, item in data.items():
            for point in item:
                file.write(key + ' %s' * len(point) % tuple(point) + '\n')

def read_json(file):
    '''
    read json file
    :param file: file path.
    :return:
    '''
    with open(file, 'r') as f:
        output = json.load(f)
    return output

def write_json(file, data):
    '''
    read json file
    :param file: file path.
    :param data: dict content
    :return:
    '''
    assert os.path.exists(os.path.dirname(file))

    with open(file, 'w') as f:
        json.dump(data, f)

'''
report the categories + paths that have been not been completely rendered 
and also remove them ??
'''
def remove_incomplete_instances(shapenet_renders_paths, filename, remove=False):
    # save the results to a file first 
    # s.no. | category id | category name | instance id | rendered path folder | full path
    incomplete_instances = list()
    for shapenet_renders_path in shapenet_renders_paths:
        categories = glob(shapenet_renders_path + '/*')
        for category in categories:
            print(f'Inside shapenet renders path : {shapenet_renders_path}, category : {category}')
            category_id = category.split('/')[-1]
            instances = glob(category + '/*')
            for instance in instances:
                count = len(glob(instance + '/*'))
                if count < 40:
                    incomplete_instances.append([category_id, synset_category_pair[category_id], instance.split('/')[-1], osp.basename(shapenet_renders_path), instance])

            if remove:
                for instance in incomplete_instances:
                    os.system(f'rm -rf {instance}')

    # write the contents of the data to a csv file
    print(f'Writing contents to file : {filename}')
    with open(filename, 'w') as f:
        f.write('s.no, category id, category name, instance id, rendered path folder, full path\n')
        for i, row in enumerate(incomplete_instances):
            f.write(f'{i+1}, {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}\n')

'''
script for computing the total number of instances per category that have been rendered 
for the rendering paths specified 
also compare it against the ground truth number of instances
'''
def compute_instance_count(shapenet_path, shapenet_renders_paths, filepath):
    # category_name | category_id | total instances | rendered instances | rendered path
    data = dict()

    # create a dict of data categories initially 
    print(f'Creating an initial dict of all categories')
    all_category_ids = glob(shapenet_path + '/*')
    for category_id in all_category_ids:
        category_name = synset_category_pair[osp.basename(category_id)]
        # num_objects = len(glob(category_id + '/*/models/model_normalized.obj'))
        num_objects = len(os.listdir(category_id))
        data[category_name] = [osp.basename(category_id), num_objects, 0, '']

    print(f'Going through the rendered folders')
    # find the number of rendered instances in the renders paths provided
    for shapenet_renders_path in shapenet_renders_paths:
        categories = glob(shapenet_renders_path + '/*')
        for category in categories:
            print(f'Processing shapenet renders path : {shapenet_renders_path}, category : {category}')
            rendered_instances = len(glob(category + '/*'))

            # number of model instances for the given category
            category_id = osp.basename(category)

            category_name = synset_category_pair[category_id]
            data[category_name] = [category_id, data[category_name][1], rendered_instances, osp.basename(shapenet_renders_path)]

    # with open(filepath, 'w') as f:
    #     f.write('s.no, category id, category name, total instances, rendered instances, rendered path folder\n')
    #     for i, row in enumerate(data):
    #         f.write(f'{i+1}, {row[0]}, {row[1]}, {row[2]}, {row[3]}, {row[4]}\n')
            
    print(f'Writing contents to file : {filepath}')
    with open(filepath, 'w') as f:
        f.write('Category, ShapeNet ID, Total Objects, Rendered Objects, Rendered path\n')
        for key, value in sorted(data.items()):
            f.write(f'{key}, {value[0]}, {value[1]}, {value[2]}, {value[3]}\n')

# script for removing the folders that were not rendered completely
def remove_incomplete_folders(shapenet_renders_path, category_ids):
    incomplete_instances = list()
    for category_id in category_ids:
        # get all the instances 
        # print(f'Shapenet renders path : {shapenet_renders_path}, category id : {category_id}')
        instances = get_cate_instances(shapenet_renders_path, category_id)
        # print(instances[0])
        # assert False
        # get the number of files inside each of the instances 
        # count = len(glob(instances + '/*'))
        for instance in instances:
            count = len(glob(osp.join(shapenet_renders_path, category_id, instance) + '/*'))
            if count < 40:
                incomplete_instances.append(osp.join(shapenet_renders_path, category_id, instance))
    
    # remove the incomplete instances 
    print(f'Incomplete instances are {incomplete_instances}, count : {len(incomplete_instances)}')
    for instance in incomplete_instances:
        print(f'removing instance : {instance}')
        os.system(f'rm -rf {instance}')

# get the instances of a certain category for which renders have been generated
def get_cate_instances(shapenet_renders_path, category_id):
    instances = glob(osp.join(shapenet_renders_path, category_id) + '/*')
    instances = [instance.split('/')[-1] for instance in instances]
    return instances

def load_data_path(shapenet_path, shapenet_renders_path, category_ids):
    data_paths = []
    for category_id in category_ids:
        instances = get_cate_instances(shapenet_renders_path, category_id)
        category_paths = glob(osp.join(shapenet_path, category_id) + '/*/models/model_normalized.obj')
        #category_paths_filtered = [category_path for category_path in category_paths if category_path.split('/')[-3] not in instances]
        print('Category {}; Instances rendered : {}, instances to be rendered : {}, total instances : {}'.format(category_id, len(instances), len(category_paths_filtered), len(category_paths)))
        #data_paths.extend(category_paths_filtered)
        if len(category_paths > 100):
            category_paths = category_paths[:100]
        data_paths.extend(category_paths)
    
    return data_paths

# def load_data_path(shapenet_path):
#     target_obj_file = 'model_normalized.obj'
#     data_path = []
#     for root, dirs, files in os.walk(shapenet_path, topdown=True):
#         if target_obj_file in files:
#             obj_path = os.path.join(root, target_obj_file)
#             data_path.append(obj_path)
#     return data_path

# def load_data_path(shapenet_path, category_ids):
#     print(f'Loading data list')
#     target_obj_file = 'model_normalized.obj'
#     data_path = []
#     for root, _, files in os.walk(shapenet_path, topdown=True):
#         if target_obj_file in files:
#             # if category_ids is not None:
#             for category_id in category_ids:
#                 if category_id in root:
#                     obj_path = os.path.join(root, target_obj_file)
#                     data_path.append(obj_path)
#                     break
#     return data_path

if __name__ == '__main__':
    # create argparse for removing the instances that have not been completeley rendered 
    dataset_dirpath = '/home/gridsan/aagarwal/Research/phd/datasets'
    shapenet_renders_paths = [
        # osp.join(dataset_dirpath, 'shapenet_tabletop_renders'),
        osp.join(dataset_dirpath, 'shapenet_renders'),
        # osp.join(dataset_dirpath, 'shapenet_renders1'),
        # osp.join(dataset_dirpath, 'shapenet_renders2'),
    ]

    # removed_folders_filepath = '../removed_folders.csv'
    # remove_incomplete_instances(shapenet_renders_paths, removed_folders_filepath)
    # assert False

    filepath = '../current_instances_combined.csv'
    compute_instance_count(osp.join(dataset_dirpath, 'ShapeNetCore_Zip'), shapenet_renders_paths, filepath)

    assert False

    # import argparse
    # parser = argparse.ArgumentParser()
    # parser.add_argument("--shapenet_renders_path", help="Path to the shapenet renders", type=str, default='/home/gridsan/aagarwal/Research/phd/datasets/depth_renderer_dataset/shapenet_tabletop_renders')
    # parser.add_argument("--category_ids", help="Category ids to render", nargs='+', default=['03001627'])
    # args = parser.parse_args()

    # shapenet_renders_path = osp.join(dataset_dirpath, args.shapenet_renders_path)
    # category_ids = args.category_ids

    # remove_incomplete_folders(shapenet_renders_path, category_ids)