# Vision Language Models (VLM) Guide

A comprehensive learning resource for mastering Vision Language Models, from embeddings and zero-shot classification to advanced object detection and image captioning.

![Status](https://img.shields.io/badge/Status-Ready-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8%2B-blue) ![License](https://img.shields.io/badge/License-Educational-orange)

---

## ⚡ Quick Start

```bash
# 1. Clone/Download this repository
cd /path/to/VLM-Guide

# 2. Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch Jupyter
jupyter notebook
```

---

## 📑 Table of Contents

- [Quick Start](#-quick-start)
- [Notebooks Overview](#-notebooks-overview)  
- [Requirements](#-requirements)
- [Installation](#-installation)
- [Learning Path](#-learning-path)
- [Key Concepts](#-key-concepts)
- [Troubleshooting](#-troubleshooting)
- [Resources](#-resources)

## 📋 Notebooks

### 1. **m2_Embeddings.ipynb** - Text & Image Embeddings with CLIP
Learn the fundamentals of embeddings and similarity measurement.

**Topics:**
- Tokenization and text preprocessing
- Generating text embeddings
- Generating image embeddings
- Computing cosine similarity matrices
- Visualizing text-text, image-image, and cross-modal similarities

**Models:** `openai/clip-vit-base-patch32`

**Output:** Heatmaps showing semantic similarity between text and images

---

### 2. **m3_Zero-Shot-Classification-CLIP.ipynb** - Classification without Training
Perform image classification using natural language descriptions.

**Topics:**
- Zero-shot classification paradigm
- Leveraging embeddings for classification
- Computing probability scores
- Multi-label classification

**Use Case:** Classify images into custom categories without any training data

---

### 3. **m5_Image-Captioning.ipynb** - Generate Image Descriptions
Automatically generate captions describing image content.

**Topics:**
- Image encoding
- Sequence-to-sequence generation
- Controlling caption length and style
- Beam search vs greedy decoding

**Output:** Natural language descriptions of image content

---

### 4. **m6_Object-Detection-Using-Qwen-2.5VL.ipynb** - Object Detection Basics
Introduction to object detection using Qwen 2.5-VL.

**Topics:**
- Loading Qwen 2.5-VL model
- Object detection prompt formatting
- JSON output parsing
- Drawing bounding boxes

**Models:** `Qwen/Qwen2.5-VL-7B-Instruct`

---

### 5. **Detection-Using-Qwen-2.5VL.ipynb** - Advanced Object Detection
Production-ready object detection with spatial reasoning and visual queries.

**Topics:**
- Chat-based inference
- System prompts for object detection
- JSON utilities for output parsing
- Newline repair for malformed JSON
- Bounding box visualization

**Advanced Features:**
- Natural language queries for specific objects
- Font rendering and text positioning
- Error handling for edge cases

---

### 6. **StepUp.ipynb** - Supplementary Material
Additional exercises and challenges for deeper learning.

---

## ⚙️ Requirements

### Hardware
- **GPU:** NVIDIA GPU with ≥14 GB VRAM (RTX 3090, A100, etc.)
- **CPU:** For CPU-only inference (much slower)
- **RAM:** ≥16 GB system RAM

### Software
```bash
Python 3.8+
PyTorch with CUDA support
Transformers library
```

### Environment Variables (Optional)
```bash
# For memory optimization
PYTORCH_ALLOC_CONF=expandable_segments:True

# For debugging
TRANSFORMERS_VERBOSITY=debug
```

---

## 🚀 Installation

### 1. Clone/Download the Bootcamp
```bash
cd /path/to/VLM\ Bootcamp
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Or manually:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install transformers pillow matplotlib seaborn requests numpy pprint
pip install qwen-vl-utils
pip install bitsandbytes  # For 8-bit quantization (optional)
pip install flash-attn  # For Flash Attention 2 (optional but recommended)
```

### 4. Launch Jupyter
```bash
jupyter notebook
```

---

## 📖 How to Use

### Sequential Learning Path
1. **Start with m2_Embeddings.ipynb** - Understand embeddings and similarity
2. **Move to m3_Zero-Shot-Classification-CLIP.ipynb** - Learn classification
3. **Explore m5_Image-Captioning.ipynb** - Generate descriptions
4. **Progress to m6_Object-Detection-Using-Qwen-2.5VL.ipynb** - Detect objects
5. **Master Detection-Using-Qwen-2.5VL.ipynb** - Advanced detection

### Running a Notebook
```python
# 1. Install required packages (if needed)
!pip install <package_name>

# 2. Import libraries
import torch
from transformers import CLIPModel, CLIPProcessor

# 3. Load model
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32")

# 4. Process inputs
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")
inputs = processor(images=images, text=texts, return_tensors="pt", padding=True)

# 5. Generate outputs
with torch.no_grad():
    outputs = model(**inputs)
```

---

## 🎯 Key Concepts

### Embeddings
Dense vector representations of images/text in a shared space. Similar concepts have similar vectors.

**Application:** Semantic search, clustering, similarity

### Zero-Shot Classification  
Classifying images into categories without prior training, using text descriptions.

**Application:** Custom categorization, flexible classification

### Image Captioning
Generating natural language descriptions of image content.

**Application:** Accessibility, content indexing, understanding

### Object Detection
Identifying and localizing specific objects with bounding boxes.

**Application:** Security, inventory, scene understanding

---

## 🔧 Memory Optimization

### For VRAM Issues

**Option 1: Use FP16 (Default)**
```python
torch_dtype=torch.float16  # ~50% memory savings
```

**Option 2: Flash Attention 2** (Recommended)
```python
attn_implementation="flash_attention_2"  # ~30% additional savings
```

**Option 3: 8-bit Quantization**
```python
from transformers import BitsAndBytesConfig
quantization_config = BitsAndBytesConfig(load_in_8bit=True)
```

**Option 4: Reduce Tokens**
```python
max_new_tokens=128  # Instead of 1000
```

**Option 5: Use Smaller Model**
```python
# Instead of 7B
model_id = "Qwen/Qwen2.5-VL-3B-Instruct"
```

### Memory Clearing
```python
import torch
torch.cuda.empty_cache()           # Clear GPU cache
torch.cuda.synchronize()           # Sync GPU operations
```

---

## 🐛 Troubleshooting

### CUDA Out of Memory Error
**Solution:**
1. Run the GPU memory clearing cell before inference
2. Reduce `max_new_tokens` to 128 or lower
3. Use FP16 instead of FP32
4. Enable Flash Attention 2
5. Use smaller model: `Qwen2.5-VL-3B-Instruct`

### Model Download Issues
**Solution:**
```bash
# Set cache directory
export HF_HOME=/path/to/cache
# Then run notebook
jupyter notebook
```

### JSON Parsing Errors
**Solution:** The `extract_json()` utility handles most cases. It:
- Removes markdown code blocks
- Repairs newlines inside strings
- Validates JSON format

### Slow Inference
**Solution:**
- Use GPU instead of CPU
- Enable Flash Attention 2
- Reduce input image resolution
- Use smaller model (3B instead of 7B)

---

## 📊 Model Comparison

| Model | Size | VRAM | Speed | Quality |
|-------|------|------|-------|---------|
| CLIP ViT-B/32 | 340M | 2GB | Fast | Good |
| Qwen 2.5-VL-3B | 3B | 8GB | Medium | Very Good |
| Qwen 2.5-VL-7B | 7B | 14GB | Slow | Excellent |

---

## 📚 Key Libraries

| Library | Purpose |
|---------|---------|
| **torch** | Tensor operations and GPU acceleration |
| **transformers** | Pre-trained VLMs and processors |
| **PIL** | Image loading and manipulation |
| **matplotlib** | Visualization and plotting |
| **qwen-vl-utils** | Qwen-specific utilities |
| **bitsandbytes** | 8-bit quantization (optional) |
| **flash-attn** | Flash Attention 2 (optional) |

---

## 🎓 Learning Objectives

By completing this guide, you will:

✅ Understand how embeddings encode semantic information  
✅ Perform zero-shot image classification  
✅ Generate descriptive image captions  
✅ Detect objects and extract spatial information  
✅ Optimize VLMs for resource-constrained environments  
✅ Parse and handle model outputs effectively  
✅ Build real-world VLM applications  

---

## 📖 Resources

### Official Documentation
- [Hugging Face Transformers](https://huggingface.co/docs/transformers)
- [PyTorch Official Docs](https://pytorch.org/docs)
- [CLIP Paper](https://arxiv.org/abs/2103.14030)
- [Qwen Models](https://huggingface.co/Qwen)

### Related Topics
- Vision Transformers (ViT)
- Contrastive Learning
- Multimodal Machine Learning
- Transfer Learning

---

## 📝 Best Practices

1. **Run cells sequentially** - Dependencies exist between cells
2. **Clear GPU memory** - Before running inference
3. **Monitor VRAM** - Use `nvidia-smi` or `torch.cuda.memory_allocated()`
4. **Test with small images first** - Before running on large datasets
5. **Save outputs** - Export detected objects and captions
6. **Experiment with prompts** - Different prompts yield different results

---

## 🤝 Contributing

Feel free to:
- Add new models or notebooks
- Improve documentation
- Share optimizations
- Report issues

---

## 📄 License

This bootcamp material is for educational purposes.

---

## ❓ FAQ

**Q: Can I run this on CPU?**  
A: Yes, but it will be very slow. Set `device_map="cpu"` in model loading.

**Q: Which model is best for beginners?**  
A: Start with CLIP (m2_Embeddings.ipynb) - it's lightweight and fast.

**Q: How do I use custom images?**  
A: Replace the URL in image loading cells with your local file path:
```python
from PIL import Image
img = Image.open("path/to/your/image.jpg").convert("RGB")
```

**Q: What if inference is too slow?**  
A: Use the 3B model instead of 7B, or enable Flash Attention 2.

**Q: Can I batch process multiple images?**  
A: Yes, modify the inference function to loop over image lists.

---

## 📞 Support

For issues:
1. Check the Troubleshooting section
2. Review notebook comments
3. Check [Hugging Face Discussions](https://huggingface.co/discussions)
4. Search GitHub Issues

---

**Last Updated:** May 2026  
**Version:** 1.0  
**Status:** ✅ Ready for Learning
