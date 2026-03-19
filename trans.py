import os
import json
import random

# 配置路径
base_dir = "Data_数据"
# 你的 6 个大目录（根据你之前的 ls 结果）
sub_dirs = ["Andriatria_男科", "IM_内科", "OAGD_妇产科", "Oncology_肿瘤科", "Pediatric_儿科", "Surgical_外科"]

train_file = os.path.join(base_dir, "train.jsonl")
val_file = os.path.join(base_dir, "val.jsonl")
test_file = os.path.join(base_dir, "test.jsonl")

def split_and_merge():
    all_train, all_val, all_test = [], [], []

    for sub_dir in sub_dirs:
        file_path = os.path.join(base_dir, sub_dir, "medical.jsonl")
        if not os.path.exists(file_path):
            print(f"跳过不存在的文件: {file_path}")
            continue
        
        print(f"正在处理: {sub_dir}")
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        # 随机打乱当前目录的数据
        random.shuffle(lines)
        
        total = len(lines)
        n_test = int(total * 0.1)
        n_val = int(total * 0.1)
        
        # 按照 10% 测试, 10% 验证, 其余 80% 训练进行切片
        test_data = lines[:n_test]
        val_data = lines[n_test : n_test + n_val]
        train_data = lines[n_test + n_val :]
        
        all_test.extend(test_data)
        all_val.extend(val_data)
        all_train.extend(train_data)
        
        print(f"  - 原始总数: {total}")
        print(f"  - 训练集: {len(train_data)}, 验证集: {len(val_data)}, 测试集: {len(test_data)}")

    # 再次全局打乱合并后的数据（可选，建议打乱）
    random.shuffle(all_train)
    
    # 写入文件
    print("\n正在保存合并后的文件...")
    for data, path in zip([all_train, all_val, all_test], [train_file, val_file, test_file]):
        with open(path, 'w', encoding='utf-8') as f:
            for line in data:
                f.write(line)
        print(f"已保存: {path}, 共 {len(data)} 条数据")

if __name__ == "__main__":
    split_and_merge()