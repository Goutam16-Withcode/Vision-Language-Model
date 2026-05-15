# Vision Language Models - Quick Reference Guide

## 🚀 Getting Started (5 minutes)

### 1. Install Everything
```bash
pip install -r requirements.txt
jupyter notebook
```

### 2. Run Your First Notebook
- Open `m2_Embeddings.ipynb`
- Run cells from top to bottom
- Expected: Similarity heatmaps

### 3. Check GPU Status
```python
import torch
print(f"GPU Available: {torch.cuda.is_available()}")
print(f"GPU Name: {torch.cuda.get_device_name(0)}")
print(f"GPU Memory: {torch.cuda.get_device_properties(0).total_memory / 1e9:.2f} GB")
```

---

## 💡 Common Tasks

### Load a Custom Image
```python
from PIL import Image
import requests
from io import BytesIO

# From URL
url = "https://example.com/image.jpg"
img = Image.open(BytesIO(requests.get(url).content)).convert("RGB")

# From Local File
img = Image.open("path/to/image.jpg").convert("RGB")

# Display
display_image(img, title="My Image")
```

### Classify an Image (Zero-Shot)
```python
# Define candidate classes
candidates = ["cat", "dog", "bird", "fish"]

# Process
inputs = processor(images=img, text=candidates, return_tensors="pt", padding=True)

# Compute similarity
with torch.no_grad():
    outputs = model(**inputs)
logits = outputs.logits_per_image[0]
probs = logits.softmax(dim=-1)

# Results
for candidate, prob in zip(candidates, probs):
    print(f"{candidate}: {prob:.2%}")
```

### Detect Objects
```python
# Prepare prompt
msgs = [{
    "role": "user",
    "content": [
        {"type": "image", "image": img},
        {"type": "text", "text": "Detect all objects and return as JSON"}
    ]
}]

# Run inference
bounding_boxes = inference(model, msgs)

# Visualize
img_out = draw_bboxes(img.copy(), bounding_boxes)
display_image(img_out, title="Detections")
```

### Generate Image Caption
```python
# Prepare
inputs = processor(images=img, return_tensors="pt")

# Generate
with torch.no_grad():
    ids = model.generate(**inputs, max_new_tokens=50)

# Decode
caption = processor.decode(ids[0], skip_special_tokens=True)
print(f"Caption: {caption}")
```

---

## ⚠️ Troubleshooting

### Problem: CUDA Out of Memory
```python
# Clear GPU cache
torch.cuda.empty_cache()

# Reduce tokens
max_new_tokens = 64  # Was 256

# Use FP16
torch_dtype = torch.float16

# Try quantization
from transformers import BitsAndBytesConfig
quantization_config = BitsAndBytesConfig(load_in_8bit=True)
```

### Problem: Model Loading Fails
```bash
# Check internet connection
# Clear cache
rm -rf ~/.cache/huggingface

# Set custom cache
export HF_HOME=/custom/path
jupyter notebook
```

### Problem: JSON Parsing Error
```python
# The extract_json() function handles this:
# - Removes ```json``` markers
# - Fixes newlines in strings
# - Parses JSON

# Manual fix:
import json
text = text.replace('\n', ' ')
data = json.loads(text)
```

### Problem: Slow Inference
```python
# Solution 1: Use smaller model
model_id = "Qwen/Qwen2.5-VL-3B-Instruct"

# Solution 2: Enable Flash Attention
attn_implementation="flash_attention_2"

# Solution 3: Reduce resolution
img.thumbnail((768, 768))

# Solution 4: Use greedy decoding
do_sample=False, num_beams=1
```

---

## 📊 Performance Benchmarks

### Memory Usage (Peak)
| Model | FP32 | FP16 | 8-bit |
|-------|------|------|-------|
| CLIP-ViT-B | 2GB | 1GB | N/A |
| Qwen 3B | 8GB | 4GB | 2GB |
| Qwen 7B | 16GB | 8GB | 4GB |

### Inference Speed (batch size 1)
| Model | CPU | GPU |
|-------|-----|-----|
| CLIP | 2-5s | 0.1s |
| Qwen 3B | 30-60s | 1-3s |
| Qwen 7B | 60-120s | 3-5s |

---

## 🔍 Debugging

### Enable Verbose Logging
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Check GPU Memory
```python
import torch
print(torch.cuda.memory_allocated() / 1e9)  # GB
print(torch.cuda.max_memory_allocated() / 1e9)  # Peak GB
torch.cuda.reset_peak_memory_stats()
```

### Profile Code
```python
import time
start = time.time()
# Your code here
print(f"Time: {time.time() - start:.2f}s")
```

---

## 🎯 Model Selection Guide

**Choose CLIP if you want:**
- Fast inference
- Low memory usage
- Embeddings and similarity
- Zero-shot classification

**Choose Qwen 3B if you want:**
- Better accuracy than CLIP
- Moderate memory usage
- Object detection
- Image understanding

**Choose Qwen 7B if you want:**
- Best accuracy
- Complex reasoning
- Detailed descriptions
- Production quality

---

## 📚 Code Snippets

### Save Detections
```python
import json
with open("detections.json", "w") as f:
    json.dump(bounding_boxes, f, indent=2)
```

### Batch Process Images
```python
from pathlib import Path
images = list(Path("images/").glob("*.jpg"))

for img_path in images:
    img = Image.open(img_path).convert("RGB")
    results = inference(model, create_msgs(img))
    print(f"{img_path.name}: {len(results)} objects")
```

### Benchmark Speed
```python
import time
times = []
for _ in range(5):
    start = time.time()
    inference(model, msgs)
    times.append(time.time() - start)
print(f"Avg time: {sum(times)/len(times):.2f}s")
```

### Memory Profile
```python
def memory_profile(func):
    def wrapper(*args, **kwargs):
        torch.cuda.reset_peak_memory_stats()
        result = func(*args, **kwargs)
        print(f"Memory used: {torch.cuda.max_memory_allocated() / 1e9:.2f} GB")
        return result
    return wrapper

@memory_profile
def my_inference():
    return inference(model, msgs)
```

---

## 🔗 Useful Links

- **Model Hub:** https://huggingface.co/models
- **Documentation:** https://huggingface.co/docs/transformers
- **CUDA Setup:** https://pytorch.org/get-started/locally/
- **Issues:** https://github.com/huggingface/transformers/issues

---

## ✅ Checklist Before Running

- [ ] GPU drivers installed and updated
- [ ] PyTorch installed with CUDA support
- [ ] All packages from requirements.txt installed
- [ ] Internet connection available (model download)
- [ ] Sufficient disk space (~20GB for all models)
- [ ] GPU VRAM check passed
- [ ] Jupyter notebook running

---

**Pro Tip:** Always run `torch.cuda.empty_cache()` before inference for best results!
