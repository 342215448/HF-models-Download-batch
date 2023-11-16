import os
from functools import partial
import argparse
import requests
import subprocess
import time
from bs4 import BeautifulSoup
from tqdm import tqdm


# 创建文件夹的函数
def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"direct '{folder_path}'succeed in creating...")
    else:
        print(f"direct '{folder_path}' is already there...")


def download_with_resume(url, download_path):
    # 设置文件保存路径

    # 检查本地文件是否存在
    if os.path.exists(download_path):
        resume_header = {'Range': 'bytes=%d-' % os.path.getsize(download_path)}
        response = requests.get(url, headers=resume_header, stream=True)

    else:
        response = requests.get(url, stream=True)

    # 检查服务器是否支持断点续传
    if 'Accept-Ranges' in response.headers and response.headers[
        'Accept-Ranges'] == 'bytes' and response.status_code != 416:

        total_size = int(response.headers['Content-Length'])

        with open(download_path, 'ab') as file, tqdm(
                desc=os.path.split(download_path)[-1],
                total=total_size,
                unit='iB',
                unit_scale=True,
                unit_divisor=1024,
        ) as bar:
            for data in response.iter_content(chunk_size=4096):
                size = file.write(data)
                bar.update(size)
    else:
        downloaded_size = os.path.getsize(download_path)
        print(f"total length: {downloaded_size} bytes")


# 下载预训练好的模型到指定目录下 每次调用相当于下载了一个对应的模型
def download_pretrained_models(model_name, url, download_folder, max_retries=500):
    # download_folder = download_folder + '/' + url.split('/')[-3]
    download_folder = os.path.abspath(os.path.join(download_folder, model_name))

    create_folder_if_not_exists(download_folder)
    retries_cnt = 0
    while retries_cnt < max_retries:
        time.sleep(1)
        try:
            response = requests.get(url)
            break
        except requests.exceptions.RequestException:
            print('failed in geting url root:', url)
            retries_cnt += 1
            print(f'retrying ({retries_cnt}/{max_retries})...')
    soup = BeautifulSoup(response.content, 'html.parser')

    # 查找具有特定标题的所有a标签
    remote_file_list = soup.find('ul', {'class': 'mb-8 rounded-b-lg border border-t-0 dark:border-gray-800 '
                                                 'dark:bg-gray-900'}).find_all('li',
                                                                               {
                                                                                   'class': 'grid h-10 grid-cols-12 '
                                                                                            'place-content-center '
                                                                                            'gap-x-3 border-t px-3 '
                                                                                            'dark:border-gray-800'})

    remote_file_name_list = [r.find('span', {'class': 'truncate group-hover:underline'}).text.strip() for r in
                             remote_file_list]
    remote_url_list = ['https://huggingface.co' + r.find('a', title="Download file").get('href') for r in
                       remote_file_list]

    for remote_file_name, remote_url in zip(remote_file_name_list, remote_url_list):
        retries = 0
        while retries < max_retries:
            time.sleep(3)
            try:
                if remote_file_name.endswith(('ot', 'h5', 'pth', 'msgpack', 'safetensors')):
                    print(f'{remote_file_name}not torch model, skip')
                    break
                download_with_resume(remote_url, os.path.join(download_folder, remote_file_name))
                break

            except subprocess.CalledProcessError:
                print('failed download:', remote_file_name)
                retries += 1
                print(f'retrying ({retries}/{max_retries})...')

        if retries == max_retries:
            print(f'can\'t download: {remote_file_name}')


# 批量下载所有指定的模型
def download_models(folder_name, model_name_list):
    # 设置模型的文件夹
    #download_folder = 'models/'
    download_folder = folder_name

    create_folder_if_not_exists(download_folder)

    # 设置调用列表
    # model_name_list = {
    #     "roberta-base",
    # }

    for model_name in model_name_list:
        url = 'https://huggingface.co/' + model_name + '/tree/main'
        download_pretrained_models(model_name, url, download_folder)
    print('Downloading done...')


# if __name__ == '__main__':
#     parser = argparse.ArgumentParser(
#         description="downloading pytorch model(s) in Hugging Face. powered by Junhao Ruan & Peinan Feng(NEUNLPLAB)")
#     parser.add_argument("--output_dir", type=str,
#                         help="the direct of model(s) will be store", default='models')
#     parser.add_argument("--model_list", type=str,
#                         help="the name of the model(s) in Hugging Fance. (Like bert-base-uncased roberta-base SamLowe/roberta-base-go_emotions)", nargs='+', required=True)
#     args = parser.parse_args()
#     output_dir = args.output_dir
#     model_list = args.model_list
#     download_models(output_dir,model_list)
#     print('done...')
