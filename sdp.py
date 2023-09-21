from privacy_data_generator import generate_address,generate_id_number,generate_name,generate_weixin_number
from faker import Faker
import random
import os

number=2000

fake=Faker(locale='zh_CN')
file_name='sdp.txt'
sdp=[]
sdp_raw=[]
sdp_items=[]
for _ in range(number):
    id_card=next(generate_id_number())
    name=next(generate_name())
    address=next(generate_address())
    weixin_number=next(generate_weixin_number())
    sdp_items.extend([
        name,id_card,address,weixin_number
    ])
    raw_text=f'姓名{name}，身份证{id_card}，地址{address}，微信号{weixin_number}'
    masked_text=f'姓名{name}，身份证*******,地址{fake.sentence()}，微信号aabbcc'
    sdp_raw.append(raw_text)
    sdp.append(masked_text)

with open('./data/sdp/sdp_raw.txt','w',encoding='utf-8') as f:
    for line in sdp_raw:
        f.write(line+'\n')

with open('./data/sdp/sdp.txt','w',encoding='utf-8') as f:
    for line in sdp[:300]:
        f.write(line+'\n')

with open('./data/sdp/privacy.txt','w',encoding='utf-8') as f:
    for line in sdp_items:
        f.write(line+'\n')

