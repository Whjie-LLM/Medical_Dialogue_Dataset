---
license: Apache License 2.0
task:
  - text-generation
language:
  - zh
tags:
  - medical
  - conversation
---

# 中文医疗对话数据集微调 (Chinese Medical Dialogue Fine-tuning)

本项目旨在处理 [Chinese-medical-dialogue-data](https://github.com/Toyhom/Chinese-medical-dialogue-data) 开源的数据集，将其转换为适用于大语言模型（如 ChatGLM, LLaMA 等）微调的标准 JSONL 格式。

## 0. 处理后的数据集地址

处理好并可直接用于训练的数据集已上传至 ModelScope：
👉 [Medical_Dialogue_Dataset (ModelScope)](https://modelscope.cn/datasets/wwhjie/Medical_Dialogue_Dataset)

## 1. 数据来源

原始数据来自 GitHub 项目 [Toyhom/Chinese-medical-dialogue-data](https://github.com/Toyhom/Chinese-medical-dialogue-data)。该数据集包含 6 个科室的医疗问答对，共计约 79 万条数据：

- **男科 (Andriatria)**: 94,596 组
- **内科 (IM)**: 220,606 组
- **妇产科 (OAGD)**: 183,751 组
- **肿瘤科 (Oncology)**: 75,553 组
- **儿科 (Pediatric)**: 101,602 组
- **外科 (Surgical)**: 115,991 组

## 2. 数据处理

通过运行 [trans.py](file:///d:/Desktop/%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6/Data_%E6%95%B0%E6%8D%AE/Data_%E6%95%B0%E6%8D%AE/trans.py) 脚本，我们将原始 CSV/JSON 数据进行了清洗、转换和划分。

### 处理逻辑：
1. **数据清洗与格式化**：将各科室的问答对统一转换为 OpenAI/ChatML 风格的 `messages` 格式。
2. **自动生成 System Prompt**：根据科室类别，为每条数据生成相应的系统提示词（如：“你是一名专业的医生，擅长解答阳痿相关的医疗问题...”）。
3. **数据集划分**：对每个科室的数据进行随机打乱，并按照以下比例进行切分：
   - **训练集 (Train)**: 80%
   - **验证集 (Val)**: 10%
   - **测试集 (Test)**: 10%
4. **全局合并**：将所有科室处理后的数据合并，并再次进行全局随机打乱，生成最终的 `train.jsonl`, `val.jsonl`, `test.jsonl` 文件。

## 3. 微调数据格式

处理后的 `.jsonl` 文件每行包含一个 JSON 对象，结构如下：

```json
{
  "messages": [
    {
      "role": "system",
      "content": "你是一名专业的医生，擅长解答[科室相关]的医疗问题，请根据用户的提问给出准确、详细的专业回答。"
    },
    {
      "role": "user",
      "content": "用户提出的医疗咨询问题"
    },
    {
      "role": "assistant",
      "content": "医生的专业回答内容"
    }
  ]
}
```

### 示例数据：
```json
{"messages": [{"role": "system", "content": "你是一名专业的医生，擅长解答阳痿相关的医疗问题，请根据用户的提问给出准确、详细的专业回答。"}, {"role": "user", "content": "撸管太多阳痿如何缓解..."}, {"role": "assistant", "content": "建议你可以到当地的医院让医生给你仔细检查..."}]}
```

## 4. 项目结构

```text
.
├── Andriatria_男科/      # 原始数据与各科室子文件
├── IM_内科/
├── OAGD_妇产科/
├── Oncology_肿瘤科/
├── Pediatric_儿科/
├── Surgical_外科/
├── trans.py               # 数据转换与划分脚本
├── train.jsonl            # 最终合并的训练集 (80%)
├── val.jsonl              # 最终合并的验证集 (10%)
└── test.jsonl             # 最终合并的测试集 (10%)
```

## 5. 如何使用

1. 确保原始数据集已按照科室分类存放在对应文件夹下。
2. 运行转换脚本：
   ```bash
   python trans.py
   ```
3. 脚本运行完成后，根目录下会生成 `train.jsonl`, `val.jsonl`, `test.jsonl` 文件，即可直接用于模型微调。
