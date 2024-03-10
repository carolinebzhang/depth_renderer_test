"""Parallel rendering script

Author: Yinyu
Reference:
https://github.com/weiaicunzai/blender_shapenet_render
"""

import subprocess
import pickle
from time import time
from render_helper import *
from settings import *
from data_config import total_view_nums, shapenet_normalized_path, shapenet_categlory_pair, shapenet_rendering_path
import multiprocessing
from tools.read_and_write import load_data_path
import argparse

def render_cmd(result_dict):
    #render rgb
    command = [g_blender_excutable_path, '--background', '--python', 'render_all.py', '--', result_dict]
    # subprocess.run(command)
    # suppress blender outputs because its too much
    subprocess.run(command, stdout=subprocess.DEVNULL)

def group_by_cpu(result_list, count):
    '''
    deploy model-view result to different kernels
    :param result_list: model-view result
    :param count: kernel count
    :return:
    '''
    num_per_batch = int(len(result_list)/count)
    result_list_by_group = []
    for batch_id in range(count):
        if batch_id != count-1:
            result_list_by_group.append(result_list[batch_id*num_per_batch: (batch_id+1)*num_per_batch])
        else:
            result_list_by_group.append(result_list[batch_id * num_per_batch:])
    return result_list_by_group

if __name__ == '__main__':
    '''sample viewpoints'''
    # categories = ['car']

    # category_ids = list() # list of categories that need to be rendered 
    # for category in categories:
    #     category_ids.append(shapenet_categlory_pair[category])
    # all_objects = load_data_path(shapenet_normalized_path, category_ids)

# read count as an argparse argument 
    parser = argparse.ArgumentParser()
    parser.add_argument("--count", help="Number of CPUs to use for rendering", type=int, default=4)
    parser.add_argument("--categories", help="Categories to render", nargs='+', default=['car'])
    args = parser.parse_args()
    count = args.count
    categories = args.categories # list of categories that need to be rendered
    category_ids = [shapenet_categlory_pair[cat] for cat in categories]
    print(f'Running for categories : {categories}')

    all_objects = load_data_path(shapenet_normalized_path,shapenet_rendering_path, category_ids)
    print(f'Total number of objects to render : {len(all_objects)}, example path - {all_objects[0]}')
    # print(f'All objects are {all_objects}, and the number of objects to be rendered : {len(all_objects)}')
    # assert False
    result_list = collect_obj_and_vps(all_objects, total_view_nums)
    # print(result_list)
    print(f'Example result list : {result_list[0]}')

    model_view_dir = os.path.dirname(g_result_dict)
    if not os.path.exists(model_view_dir):
        os.mkdir(model_view_dir)
        print(model_view_dir)

    # save for parallel rendering
    # count = 4
    print('Core Num: %d are used.' % (count))

    result_list_by_group = group_by_cpu(result_list, count)

    model_view_paths = []
    print(f'Going inside the loop')
    for batch_id, result_per_group in zip(range(count), result_list_by_group):
        # print(f'Batch id is {batch_id}')
        file_name = str(batch_id) + '_' + os.path.basename(g_result_dict)
        print(file_name)
        print('model view path')
        single_model_view_path = os.path.join(model_view_dir, file_name)
        model_view_paths.append(single_model_view_path)
        print(single_model_view_path)
        with open(single_model_view_path, 'wb') as f:
            print('in the pickle dump')
            pickle.dump(result_per_group, f)

    pool = multiprocessing.Pool(processes=count)
    start = time()
    # print(model_view_paths)
    # assert False
    pool.map(render_cmd, model_view_paths)
    end = time()
    print('Time elapsed: %f.' % (end-start))