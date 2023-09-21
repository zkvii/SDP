import random

import datetime

from faker import Faker

fake=Faker(locale='zh_CN')

def generate_phone_number():
    while True:
        # China's mobile phone numbers start with 13, 14, 15, 17, 18, or 19.
        # Here we use 13 as an example, you can change it as needed.
        first_two = "13"
        # Generate the next 9 digits randomly
        last_nine = "".join(str(random.randint(0, 9)) for _ in range(9))
        yield first_two + last_nine


# generate id_card


def generate_id_number():
    while True:
        # 随机生成地区代码
        area_code = str(random.randint(100000, 999999))

        # 随机生成生日
        today = datetime.date.today()
        year = str(random.randint(1950, today.year))
        month = str(random.randint(1, 12))
        day = str(random.randint(1, 28))
        if day == "28" and month in ["2", "4", "6", "9", "11"]:
            day = "29"
        elif day == "29" and month not in ["2", "4", "6", "9", "11"]:
            day = "28"
        elif day == "31" and month not in ["1", "3", "5", "7", "8", "10", "12"]:
            day = "30"
        birthdate = year + month + day

        # 随机生成顺序号
        gender = random.choice(["男", "女"])
        if gender == "男":
            sequence_number = str(random.randint(1, 9))
        else:
            sequence_number = str(random.randint(0, 9))

        # 计算校验码
        id_number = area_code + birthdate + sequence_number
        weight_factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
        check_code_dict = {
            0: "1",
            1: "0",
            2: "X",
            3: "9",
            4: "8",
            5: "7",
            6: "6",
            7: "5",
            8: "4",
            9: "3",
            10: "2",
        }
        check_sum = sum(int(a) * b for a, b in zip(id_number, weight_factors))
        check_code = check_code_dict[check_sum % 11]

        # 添加校验码到身份证号码中
        id_number += check_code

        yield id_number

# 生成随机的信用卡号  
def generate_credit_card_number():  
    while True:
    # 信用卡号通常由16位数字组成  
        yield ''.join(str(random.randint(0, 9)) for _ in range(16))  
  
# 生成随机的银行卡号  
def generate_bank_card_number(): 
    while True: 
    # 银行卡号通常由16位数字组成  
        yield ''.join(str(random.randint(0, 9)) for _ in range(16))  
  
# 生成随机的QQ号  
def generate_qq_number():  
    # QQ号通常由5到12位的数字组成 
    while True: 
        length = random.randint(5, 12)  
        yield ''.join(str(random.randint(0, 9)) for _ in range(length))  
  
# 生成随机的微信号  
def generate_weixin_number():  
    # 微信号可以由6到20位的字母或数字组成  
    while True:
        length = random.randint(6, 20)  
        characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'  
        yield ''.join(random.choice(characters) for _ in range(length)) 

# 生成随机的邮箱
def generate_email():
    while True:
        yield fake.email()

# 生成随机的姓名
def generate_name():
    while True:
        yield fake.name()

# 生成随机的地址
def generate_address():
    while True:
        yield fake.address()

privacy_data = []
privacy_data_items=[]

number=2000

def get_privacy_item():
    id_card=next(generate_id_number())
    phone_number=next(generate_phone_number())
    credit_card_number=next(generate_credit_card_number())
    bank_card_number=next(generate_bank_card_number())
    qq_number=next(generate_qq_number())
    weixin_number=next(generate_weixin_number())
    email=next(generate_email())
    name=next(generate_name())
    address=next(generate_address())
    sex=random.choice(["男","女"])
    age=random.randint(18,60)
    privacy_data.extend([
        id_card,
        phone_number,
        credit_card_number,
        bank_card_number,
        qq_number,
        weixin_number,
        email,
        address,
        name
    ])
    items=[
        f'姓名{name}',
        # f'年龄{age}',
        f'身份证{id_card}',
        f'手机号{phone_number}',
        # f'信用卡号{credit_card_number}',
        f'银行卡号{bank_card_number}',
        # f'QQ号{qq_number}',
        f'微信号{weixin_number}',
        f'邮箱{email}',
        f'地址{address}',
        # f'{sex}'
    ]
    random.shuffle(items)
    cat_str=''
    for item in items:
        cat_str=cat_str+fake.sentence()[:4]+item
    return cat_str

# for i in range(number):
#     privacy_data_items.append(get_privacy_item())

# with open('./data/nsc_train_text.txt','w',encoding='utf-8') as f:
#     for item in privacy_data_items:
#         f.write(item+'\n')

# with open('./data/nsc_privacy_db.txt','w',encoding='utf-8') as f:
#     for item in privacy_data:
#         f.write(item+'\n')


# from datasets import load_dataset

# dataset = load_dataset("qgyd2021/chinese_ner_sft",'Bank')


# samples=dataset['train']['text']
# collection_1_base=samples[:4000]
# collection_2_base=samples[4000:8000]
# collection_1=[]
# collection_2=[]

# for i in range(number):
#     if i <200:
#         collection_1.append(random.choice(collection_1_base))
#         collection_2.append(random.choice(collection_2_base))
#     else:
#         collection_1.append(random.choice(privacy_data_items))
#         collection_2.append(random.choice(privacy_data_items))
# random.shuffle(collection_1)
# random.shuffle(collection_2)

# with open('./data/nsc_collection_1.txt','w',encoding='utf-8') as f:
#     for item in collection_1:
#         f.write(item+'\n')

# with open('./data/nsc_collection_2.txt','w',encoding='utf-8') as f:
#     for item in collection_2:
#         f.write(item+'\n')
        