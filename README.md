---
license: Apache License 2.0
task:
  - text-generation
language:
  - zh
tags:
  - medical
  - conversation
  - fine-tuning
  - chatml
size_categories:
  - 100K<n<1M
source_datasets:
  - Chinese-medical-dialogue-data
---
# 🏥 中文医疗对话数据集 (Medical_Dialogue_Dataset)

<p align="left">
    <a href="https://modelscope.cn/datasets/wwhjie/Medical_Dialogue_Dataset"><img src="https://img.shields.io/badge/ModelScope-Dataset-blue.svg" alt="ModelScope"></a>
    <img src="https://img.shields.io/badge/Language-Chinese-red.svg" alt="Language">
    <img src="https://img.shields.io/badge/Format-JSONL-green.svg" alt="Format">
</p>

本项目基于 [Chinese-medical-dialogue-data](https://github.com/Toyhom/Chinese-medical-dialogue-data) 开源数据集，经过专业清洗与格式转换，生成了适用于大语言模型（如 ChatGLM, LLaMA, Qwen 等）微调的标准 **ChatML (Messages)** 格式数据集。

---

## 🚀 快速获取

处理好的数据集已同步至 ModelScope：
👉 **[点击跳转数据集主页](https://modelscope.cn/datasets/wwhjie/Medical_Dialogue_Dataset)**

---

## 📊 数据概览

数据集包含 **6 个科室** 的医疗问答对，总计约 **79 万条** 专业对话数据：

| 科室             | 英文名     | 数据量 (对) | 描述                       |
| :--------------- | :--------- | :---------- | :------------------------- |
| **男科**   | Andriatria | 94,596      | 涵盖男性生殖、性功能等问题 |
| **内科**   | IM         | 220,606     | 涵盖呼吸、消化、心血管等   |
| **妇产科** | OAGD       | 183,751     | 涵盖孕产、妇科疾病等       |
| **肿瘤科** | Oncology   | 75,553      | 涵盖各类肿瘤防治与咨询     |
| **儿科**   | Pediatric  | 101,602     | 涵盖婴幼儿发育、常见病等   |
| **外科**   | Surgical   | 115,991     | 涵盖普通外科、手术咨询等   |

---

## 🛠️ 处理逻辑

我们通过 [trans.py](file:///d:/Desktop/%E4%B8%B4%E6%97%B6%E6%96%87%E4%BB%B6/Data_%E6%95%B0%E6%8D%AE/Data_%E6%95%B0%E6%8D%AE/trans.py) 脚本完成了以下工作：

1. **格式对齐**：统一转换为 OpenAI 推荐的 `messages` 列表格式。
2. **角色定义**：为每个科室定制了专属的 `system` 角色提示词。
3. **随机采样**：各科室数据均经过随机打乱，保证训练分布均匀。
4. **科学划分**：按照 **8:1:1** 比例自动划分为：
   - `train.jsonl` (训练集)
   - `val.jsonl` (验证集)
   - `test.jsonl` (测试集)

---

## 📝 数据格式示例

每条数据均为标准的 JSONL 格式，示例如下：

```json
{
  "messages": [
    {
      "role": "system",
      "content": "你是一名专业的医生，擅长解答男科相关的医疗问题..."
    },
    {
      "role": "user",
      "content": "撸管太多阳痿如何缓解..."
    },
    {
      "role": "assistant",
      "content": "建议你可以到当地的医院让医生给你仔细检查..."
    }
  ]
}
```

---

## 📂 项目目录

```text
.
├── Andriatria_男科/      # 原始数据子目录
├── ...
├── trans.py               # 核心转换脚本
├── train.jsonl            # 最终合并训练集
├── val.jsonl              # 最终合并验证集
└── test.jsonl             # 最终合并测试集
```

---

## ⚖️ 许可说明

本数据集代码部分采用 **Apache License 2.0** 协议。原始数据归原作者所有，使用时请遵守相关法律法规。
