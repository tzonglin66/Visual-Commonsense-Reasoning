# 作 者：田宗林
# 时 间：2021/11/1
import argparse
from allennlp.common.params import Params
from dataloaders.vcr import VCR

import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(name)s - %(message)s', level=logging.DEBUG)

parser = argparse.ArgumentParser(description='train')

# 增加可选参数params，属性名为params
parser.add_argument('-params', dest='params', help='Params location', type=str, )
# 增加可选参数rationale，不指定为False
parser.add_argument('-folder', dest='folder', help='folder location', type=str, )
# 增加可选参数to_tqdm，属性名为no_tqdm，不指定为FALSE
parser.add_argument('-rationale', action="store_true", help='use rationale', )
# 增加可选参数folder，属性名为folder
parser.add_argument('-no_tqdm', dest='no_tqdm', action='store_true', )
# 解析参数
args = parser.parse_args()
"""输入参数-params multiatt/default.json -folder saves/flagship_answer 得到
    args.params = 'multiatt/default.json'
    args.folder = 'saves/flagship_answer'
    args.rationale = False
    args.no_tqdm = False
"""

# 根据args.params提供的路径创建一个参数对象（本质就是一个字典）
params = Params.from_file(args.params)

# params['dataset_reader']没有'embs'和'only_use_relevant_dets'属性，所以get方法返回指定值
# embs_to_load = 'bert_da'
# only_use_relevant_dets = True
# VCR是一个类对象，splits是一个类方法，同时创建三个类对象
train, val, test = VCR.splits(mode='answer', embs_to_load='bert_da')
img = train[0]
