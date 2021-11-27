# 作 者：田宗林
# 时 间：2021/8/7
import os
import json

VCR_ANNOTS_DIR = 'E:\\root\\Projects\\r2c\\dataset\\vcr1annots'
split = 'train'
with open(os.path.join(VCR_ANNOTS_DIR, '{}.jsonl'.format(split)), 'r') as f:
    items = [json.loads(s) for s in f]