# Vision Language Models (VLM)

> A comprehensive project for working with Vision Language Models using PyTorch and Transformers

[![Status](https://img.shields.io/badge/Status-Active-brightgreen)](https://github.com)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](https://www.python.org)
[![PyTorch](https://img.shields.io/badge/PyTorch-2.0%2B-red)](https://pytorch.org)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Last Updated](https://img.shields.io/badge/Last%20Updated-May%202026-blue)](#)

---

## 📖 Table of Contents

- [About](#-about)
- [Features](#-features)
- [Project Structure](#-project-structure)
- [Getting Started](#-getting-started)
- [Installation](#-installation)
- [Usage](#-usage)
- [Notebooks](#-notebooks)
- [Requirements](#-requirements)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 About

This project provides a collection of Jupyter notebooks and utilities for working with Vision Language Models (VLMs). It demonstrates practical applications of CLIP and Qwen 2.5-VL models for tasks including:

- Semantic embedding generation
- Zero-shot image classification
- Automatic image captioning
- Object detection with natural language queries

All notebooks are production-ready with optimizations for GPU memory management and inference speed.

---

## ✨ Features

- 📊 **Multiple VLM Models** - CLIP, Qwen 2.5-VL with different sizes
- 🔧 **Optimization Tools** - FP16, Flash Attention 2, 8-bit quantization
- 📓 **Self-contained Notebooks** - No external dependencies between notebooks
- 💾 **Memory Efficient** - Handles large models on limited VRAM
- 🚀 **Production Ready** - Tested and optimized for real-world usage
- 📚 **Well Documented** - Detailed comments and reference guides
- 🛠️ **Easy Setup** - Single-command installation with pip

---

## 📁 Project Structure

```
.
├── README.md                                    # This file
├── QUICK_REFERENCE.md                          # Quick reference guide
├── requirements.txt                             # Python dependencies
│
├── Notebooks/
│   ├── m2_Embeddings.ipynb                     # CLIP embeddings & similarity
│   ├── m3_Zero-Shot-Classification-CLIP.ipynb  # Image classification
│   ├── m5_Image-Captioning.ipynb               # Generate captions
│   ├── m6_Object-Detection-Using-Qwen-2.5VL.ipynb  # Object detection (basic)
│   ├── Detection-Using-Qwen-2.5VL.ipynb        # Object detection (advanced)
│   └── StepUp.ipynb                            # Additional exercises
│
└── utils/                                       # (Optional) Utility functions
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have:

- **Python 3.8** or higher
- **NVIDIA GPU** with CUDA 11.8+ (recommended for speed)
- **8GB+ VRAM** for CLIP models, **14GB+** for Qwen models
- **20-30GB disk space** for model downloads

### Quick Setup

```bash
# 1. Clone or download this repository
git clone <repository-url>
cd VLM-Project

# 2. Create a virtual environment
python -m venv venv

# Activate it
source venv/bin/activate    # Linux/Mac
# or
venv\Scripts\activate       # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

---

## ⚙️ Installation

### Full Installation (Recommended)

```bash
pip install -r requirements.txt
pip install bitsandbytes    # 8-bit quantization (optional)
pip install flash-attn      # Flash Attention 2 (optional)
```

### Minimal Installation

```bash
pip install torch transformers pillow matplotlib jupyter
pip install qwen-vl-utils requests
```

### Verify Installation

```bash
python -c "import torch; print(f'GPU Available: {torch.cuda.is_available()}')"
```

---

## 💻 Usage

### Example 1: Generate Text and Image Embeddings

```python
from transformers import CLIPModel, CLIPProcessor
import torch

# Load model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Encode text
text_inputs = processor(text=["a cat", "a dog"], return_tensors="pt", padding=True)
with torch.no_grad():
    text_embeddings = model.get_text_features(**text_inputs)

# Encode image
image_inputs = processor(images=[image], return_tensors="pt")
with torch.no_grad():
    image_embeddings = model.get_image_features(**image_inputs)

# Compute similarity
similarity = torch.cosine_similarity(text_embeddings, image_embeddings)
```

### Example 2: Zero-Shot Image Classification

```python
# Classify image into custom categories
categories = ["cat", "dog", "bird", "fish", "car"]
predictions = classify_image(image, categories, model, processor)

print(f"Top prediction: {predictions[0]['label']} ({predictions[0]['score']:.2%})")
```

### Example 3: Object Detection

```python
# Detect objects with natural language query
query = "Detect all animals in the image"
detections = detect_objects(image, query, model, processor)

for detection in detections:
    print(f"Found: {detection['label']} at {detection['bbox_2d']}")
```

---

## 📓 Notebooks

| Notebook | Task | Model | Time |
|----------|------|-------|------|
| **m2_Embeddings.ipynb** | Text & image embeddings | CLIP ViT-B/32 | 15 min |
| **m3_Zero-Shot-Classification-CLIP.ipynb** | Image classification | CLIP | 10 min |
| **m5_Image-Captioning.ipynb** | Generate captions | CLIP | 20 min |
| **m6_Object-Detection-Using-Qwen-2.5VL.ipynb** | Detect objects (basic) | Qwen 7B | 30 min |
| **Detection-Using-Qwen-2.5VL.ipynb** | Detect objects (advanced) | Qwen 7B | 45 min |
| **StepUp.ipynb** | Exercises & challenges | Various | N/A |

---

## ⚙️ Requirements

### Hardware
- **GPU:** NVIDIA RTX 3090, A100, RTX 4090, etc. (8GB+ minimum, 14GB+ recommended)
- **CPU:** 4+ cores recommended
- **RAM:** 8GB minimum, 16GB+ recommended
- **Storage:** 20-30GB for all models

### Software Requirements
```
Python 3.8+
PyTorch 2.0+ with CUDA support
Transformers 4.40+
CUDA Toolkit 11.8+ (for GPU acceleration)
```


## 🔧 Configuration & Optimization

### GPU Memory Optimization

**Option 1: Use FP16** (50% memory reduction)
```python
model = CLIPModel.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto"
)
```

**Option 2: Enable Flash Attention 2** (30% additional savings)
```python
model = CLIPModel.from_pretrained(
    model_id,
    attn_implementation="flash_attention_2"
)
```

**Option 3: 8-bit Quantization** (60% total savings)
```python
from transformers import BitsAndBytesConfig
config = BitsAndBytesConfig(load_in_8bit=True)
model = CLIPModel.from_pretrained(model_id, quantization_config=config)
```

**Option 4: Use Smaller Model**
```python
model_id = "Qwen/Qwen2.5-VL-3B-Instruct"  # 3B instead of 7B
```

**Option 5: Clear GPU Cache**
```python
import torch
torch.cuda.empty_cache()
torch.cuda.synchronize()
```

---

## 📊 Model Comparison

| Model | Size | VRAM | Speed | Quality | Best For |
|-------|------|------|-------|---------|----------|
| CLIP ViT-B/32 | 340M | 2GB | ⚡⚡⚡ | Good | Classification |
| Qwen 2.5-VL-3B | 3B | 4-8GB | ⚡⚡ | Very Good | General tasks |
| Qwen 2.5-VL-7B | 7B | 8-14GB | ⚡ | Excellent | Complex tasks |

---

## ❓ Troubleshooting

### CUDA Out of Memory Error

**Solution:** Apply optimizations from [Configuration & Optimization](#-configuration--optimization) section in this order:

1. Clear GPU cache: `torch.cuda.empty_cache()`
2. Reduce max_new_tokens: `max_new_tokens=128`
3. Enable Flash Attention 2
4. Use FP16 dtype
5. Switch to smaller model (3B)

### Model Download Fails

```bash
# Option 1: Clear Hugging Face cache
rm -rf ~/.cache/huggingface/

# Option 2: Set custom cache location
export HF_HOME=/path/to/cache
jupyter notebook
```

### Slow Inference Speed

- Use GPU acceleration (CUDA-capable GPU)
- Enable Flash Attention 2
- Reduce image resolution
- Use smaller model variant (3B)
- Reduce `max_new_tokens` parameter

### JSON Parsing Issues

The notebooks include `extract_json()` utility that:
- Automatically removes markdown code blocks
- Repairs newlines in string values  
- Validates JSON format

---

## 📖 Documentation

### Files
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** - Commands and code snippets
- **[requirements.txt](requirements.txt)** - All Python dependencies
- **Notebook Comments** - Inline documentation in each notebook

### External Resources
- [Hugging Face Model Hub](https://huggingface.co/models)
- [CLIP: Learning Transferable Models for Computational Vision](https://arxiv.org/abs/2103.14030)
- [Qwen Vision Language Models](https://huggingface.co/Qwen)
- [PyTorch Documentation](https://pytorch.org/docs)
- [Hugging Face Transformers Guide](https://huggingface.co/docs/transformers)

---


## 📄 License

This project is for educational and research purposes. See LICENSE file for details.

---

## 🆘 Support

**Need help?**

- Review [Troubleshooting](#-troubleshooting) section above
- Check notebook comments for detailed explanations
- Search [Hugging Face Discussions](https://huggingface.co/discussions)
- Explore [Stack Overflow](https://stackoverflow.com/questions/tagged/transformers)

---

## 📈 Project Status

| Component | Status |
|-----------|--------|
| CLIP Embeddings | ✅ Tested |
| Zero-Shot Classification | ✅ Tested |
| Image Captioning | ✅ Tested |
| Object Detection | ✅ Tested |
| GPU Optimization | ✅ Implemented |
| Documentation | ✅ Complete |

---

**Last Updated:** May 2026  
**Python Version:** 3.8+  
**PyTorch:** 2.0+  
**Status:** ✅ Active Development