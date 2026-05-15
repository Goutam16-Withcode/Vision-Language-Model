import streamlit as st
from pathlib import Path
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="VLM Bootcamp - Vision Language Models",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding-top: 0rem;
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
        font-size: 1.2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 5px solid #0066cc;
    }
    .feature-box {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 1rem;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("🎯 Navigation")
    page = st.radio(
        "Select a section:",
        ["🏠 Home", "📚 Notebooks", "📊 Features", "🚀 Getting Started", "ℹ️ About"]
    )

# ============================================================
# HOME PAGE
# ============================================================
if page == "🏠 Home":
    st.markdown("""
    <div style="text-align: center;">
        <h1 style="color: #0066cc; font-size: 3rem;">🤖 Vision Language Models</h1>
        <h3 style="color: #666;">Comprehensive VLM Bootcamp Project</h3>
        <p style="font-size: 1.1rem; color: #888;">Master the cutting-edge Vision Language Models with Qwen 2.5-VL and CLIP</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Quick stats
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("📓 Total Notebooks", "5", "Interactive Jupyter")
    with col2:
        st.metric("🔧 Features", "4+", "VLM Applications")
    with col3:
        st.metric("🎓 Modules", "Complete", "Production Ready")
    with col4:
        st.metric("📦 Models", "2+", "CLIP & Qwen 2.5-VL")
    
    st.markdown("---")
    
    # Main features
    st.subheader("✨ What You'll Learn")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 🖼️ Image Analysis
        - **Semantic Embeddings**: Generate vector embeddings for images and text
        - **Similarity Search**: Find related images using CLIP
        - **Vector Databases**: Store and retrieve embeddings efficiently
        """)
    
    with col2:
        st.markdown("""
        #### 🎨 Image Understanding
        - **Zero-Shot Classification**: Classify images without training data
        - **Image Captioning**: Automatically generate image descriptions
        - **Object Detection**: Detect and locate objects with natural language
        """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### ⚡ Optimization
        - **GPU Memory Management**: Efficient VRAM usage
        - **Mixed Precision**: FP16 for faster inference
        - **Quantization**: 8-bit and other optimization techniques
        """)
    
    with col2:
        st.markdown("""
        #### 📚 Best Practices
        - **Production-Ready Code**: Optimized and tested
        - **Self-Contained Notebooks**: No external dependencies
        - **Clear Documentation**: Detailed comments and guides
        """)

# ============================================================
# NOTEBOOKS PAGE
# ============================================================
elif page == "📚 Notebooks":
    st.title("📓 Available Notebooks")
    st.markdown("Explore all interactive Jupyter notebooks in this project")
    
    notebooks = {
        "Zero_Shot_classification_using_CLIP.ipynb": {
            "title": "🎯 Zero-Shot Classification with CLIP",
            "description": "Learn to classify images without training data using CLIP. Perfect for novel categories and rapid prototyping.",
            "topics": ["CLIP", "Image Classification", "Zero-Shot Learning", "Transfer Learning"],
            "difficulty": "Beginner",
            "duration": "30 mins",
            "models": ["CLIP (ViT-B/32)"]
        },
        "Embedding.ipynb": {
            "title": "🌐 Image & Text Embeddings",
            "description": "Generate semantic embeddings for images and text using CLIP. Learn similarity search and embedding visualization.",
            "topics": ["Embeddings", "Semantic Search", "Vector Representations", "Similarity Metrics"],
            "difficulty": "Intermediate",
            "duration": "45 mins",
            "models": ["CLIP"]
        },
        "Image_captioining.ipynb": {
            "title": "📝 Automatic Image Captioning",
            "description": "Generate natural language descriptions for images using Qwen 2.5-VL. Understand vision-to-language tasks.",
            "topics": ["Image Captioning", "Vision-Language", "NLP", "Multimodal Learning"],
            "difficulty": "Intermediate",
            "duration": "40 mins",
            "models": ["Qwen 2.5-VL"]
        },
        "Detection-Using-Qwen-2.5VL.ipynb": {
            "title": "🔍 Advanced Object Detection",
            "description": "Perform object detection with natural language queries using Qwen 2.5-VL. Locate and describe objects in images.",
            "topics": ["Object Detection", "Grounding", "Language Queries", "Qwen 2.5-VL"],
            "difficulty": "Advanced",
            "duration": "50 mins",
            "models": ["Qwen 2.5-VL"]
        },
        "StepUp.ipynb": {
            "title": "🚀 Advanced Exercises & Extensions",
            "description": "Challenge yourself with advanced exercises and extensions. Build upon the foundational notebooks.",
            "topics": ["Integration", "Custom Tasks", "Performance Tuning", "Production Deployment"],
            "difficulty": "Advanced",
            "duration": "Variable",
            "models": ["Multiple Models"]
        }
    }
    
    for notebook_name, info in notebooks.items():
        with st.expander(f"**{info['title']}**", expanded=False):
            col1, col2, col3 = st.columns([2, 1, 1])
            
            with col1:
                st.markdown(f"**Description:** {info['description']}")
            with col2:
                difficulty_color = {"Beginner": "🟢", "Intermediate": "🟡", "Advanced": "🔴"}
                st.markdown(f"**Difficulty:** {difficulty_color[info['difficulty']]} {info['difficulty']}")
                st.markdown(f"**Duration:** {info['duration']}")
            with col3:
                st.markdown(f"**Models Used:**")
                for model in info['models']:
                    st.markdown(f"- {model}")
            
            st.markdown("**Topics Covered:**")
            cols = st.columns(len(info['topics']))
            for col, topic in zip(cols, info['topics']):
                col.markdown(f"🏷️ `{topic}`")
            
            st.markdown(f"**File:** `{notebook_name}`")
            
            if st.button(f"📖 Open {info['title'].split()[1]}", key=notebook_name):
                st.info(f"Open `{notebook_name}` in your Jupyter environment to get started!")

# ============================================================
# FEATURES PAGE
# ============================================================
elif page == "📊 Features":
    st.title("✨ Project Features")
    
    st.markdown("""
    ## 🤖 Supported Models
    
    This project works with state-of-the-art Vision Language Models:
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 🎯 CLIP (Contrastive Language-Image Pre-training)
        - **Publisher:** OpenAI
        - **Variants:** ViT-B/32, ViT-B/16, ViT-L/14
        - **Strengths:** 
            - Fast inference
            - Excellent zero-shot performance
            - Low memory requirements
        - **Use Cases:** Classification, Embedding, Similarity Search
        """)
    
    with col2:
        st.markdown("""
        ### 🌟 Qwen 2.5-VL (Alibaba)
        - **Publisher:** Alibaba Cloud
        - **Sizes:** 3B, 7B, 32B parameters
        - **Strengths:**
            - Superior image understanding
            - Multi-language support
            - Better caption quality
        - **Use Cases:** Captioning, Detection, Dense QA
        """)
    
    st.markdown("---")
    
    st.subheader("⚡ Optimization Techniques")
    
    opt_col1, opt_col2, opt_col3 = st.columns(3)
    
    with opt_col1:
        st.markdown("""
        **Mixed Precision (FP16)**
        - 2x faster inference
        - 50% memory usage
        - Minimal accuracy loss
        """)
    
    with opt_col2:
        st.markdown("""
        **Flash Attention 2**
        - 2-3x faster attention
        - Reduced memory footprint
        - Better scalability
        """)
    
    with opt_col3:
        st.markdown("""
        **8-bit Quantization**
        - 4x memory reduction
        - Supports larger models
        - bitsandbytes library
        """)
    
    st.markdown("---")
    
    st.subheader("🎯 Task Support")
    
    tasks = {
        "Image Classification": ["✅ Zero-shot learning", "✅ Multi-label classification", "✅ Confidence scores"],
        "Image Captioning": ["✅ Multiple captions", "✅ Custom prompts", "✅ Length control"],
        "Object Detection": ["✅ Bounding boxes", "✅ Language queries", "✅ Confidence scores"],
        "Semantic Search": ["✅ Batch processing", "✅ Vector similarity", "✅ Fast retrieval"],
    }
    
    for task, features in tasks.items():
        st.markdown(f"**{task}**")
        for feature in features:
            st.markdown(f"  {feature}")
        st.markdown("")

# ============================================================
# GETTING STARTED PAGE
# ============================================================
elif page == "🚀 Getting Started":
    st.title("🚀 Getting Started Guide")
    
    st.markdown("## Step 1️⃣: Prerequisites")
    st.code("""
    System Requirements:
    - Python 3.8 or higher
    - NVIDIA GPU with 8GB+ VRAM (CLIP) or 14GB+ (Qwen)
    - 20-30GB disk space for model downloads
    - CUDA 11.8+ (for GPU acceleration)
    """)
    
    st.markdown("## Step 2️⃣: Installation")
    
    with st.expander("**Windows Installation**", expanded=True):
        st.code("""
# Create virtual environment
python -m venv venv
venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# For Jupyter support
pip install jupyter jupyterlab

# Launch Jupyter
jupyter lab
        """, language="bash")
    
    with st.expander("**Linux/Mac Installation**"):
        st.code("""
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# For Jupyter support
pip install jupyter jupyterlab

# Launch Jupyter
jupyter lab
        """, language="bash")
    
    st.markdown("## Step 3️⃣: Verify Installation")
    st.code("""
# Test if PyTorch is installed correctly
python -c "import torch; print(f'PyTorch: {torch.__version__}')"

# Test if CUDA is available
python -c "import torch; print(f'CUDA Available: {torch.cuda.is_available()}')"

# Test if transformers is installed
python -c "import transformers; print(f'Transformers: {transformers.__version__}')"
    """, language="bash")
    
    st.markdown("## Step 4️⃣: Running Notebooks")
    st.code("""
# Open Jupyter Lab
jupyter lab

# Select a notebook to get started:
# 1. Start with Zero_Shot_classification_using_CLIP.ipynb (Beginner)
# 2. Move to Embedding.ipynb (Intermediate)
# 3. Try Image_captioining.ipynb (Intermediate)
# 4. Explore Detection-Using-Qwen-2.5VL.ipynb (Advanced)
# 5. Challenge yourself with StepUp.ipynb (Advanced)
    """, language="bash")
    
    st.markdown("---")
    
    st.subheader("⚠️ Troubleshooting")
    
    with st.expander("**CUDA Not Available**"):
        st.markdown("""
        If PyTorch runs on CPU instead of GPU:
        1. Check NVIDIA Driver: `nvidia-smi`
        2. Verify CUDA Toolkit installation
        3. Reinstall PyTorch for your CUDA version:
           ```
           pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
           ```
        """)
    
    with st.expander("**Out of Memory (OOM) Error**"):
        st.markdown("""
        If you get memory errors:
        1. Use smaller models (CLIP ViT-B instead of ViT-L)
        2. Reduce batch sizes in the notebooks
        3. Enable mixed precision (FP16)
        4. Use quantization (8-bit)
        """)
    
    with st.expander("**Model Download Issues**"):
        st.markdown("""
        If models fail to download:
        1. Check internet connection
        2. Verify disk space (20-30GB needed)
        3. Set HuggingFace cache: 
           ```
           export HF_HOME=/path/to/cache
           ```
        """)

# ============================================================
# ABOUT PAGE
# ============================================================
elif page == "ℹ️ About":
    st.title("ℹ️ About This Project")
    
    st.markdown("""
    ## 📚 Project Overview
    
    This is a comprehensive **Vision Language Models (VLM) Bootcamp** project designed to teach 
    practical applications of modern multimodal AI models. The project focuses on:
    
    - **CLIP**: OpenAI's Contrastive Language-Image Pre-training model
    - **Qwen 2.5-VL**: Alibaba's advanced Vision-Language model
    
    All notebooks are **production-ready**, well-optimized, and self-contained with no external 
    dependencies between them.
    """)
    
    st.markdown("---")
    
    st.subheader("🎯 Learning Path")
    
    st.markdown("""
    1. **Beginner Level** 👶
       - Start with Zero-Shot Classification
       - Understand CLIP's power without training
    
    2. **Intermediate Level** 👨‍💻
       - Explore Embeddings and Semantic Search
       - Learn Image Captioning with Qwen
    
    3. **Advanced Level** 🚀
       - Object Detection with Natural Language
       - Performance Optimization Techniques
       - Custom Model Combinations
    """)
    
    st.markdown("---")
    
    st.subheader("📦 Technologies Used")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        **Deep Learning**
        - PyTorch 2.0+
        - Transformers 4.40+
        - CUDA 11.8+
        """)
    
    with col2:
        st.markdown("""
        **Image Processing**
        - PIL/Pillow
        - OpenCV
        - Matplotlib
        """)
    
    with col3:
        st.markdown("""
        **Development**
        - Jupyter Lab
        - IPython
        - NumPy & SciPy
        """)
    
    st.markdown("---")
    
    st.subheader("📊 Project Statistics")
    
    stats_col1, stats_col2, stats_col3, stats_col4 = st.columns(4)
    
    with stats_col1:
        st.metric("Notebooks", "5", "Production-Ready")
    with stats_col2:
        st.metric("Lines of Code", "1000+", "Well-Documented")
    with stats_col3:
        st.metric("Models", "2+", "State-of-the-Art")
    with stats_col4:
        st.metric("Tasks", "4+", "End-to-End")
    
    st.markdown("---")
    
    st.subheader("📄 License & Credits")
    
    st.markdown("""
    **License:** MIT License
    
    **Models Credit:**
    - CLIP © OpenAI
    - Qwen 2.5-VL © Alibaba Cloud
    
    **Last Updated:** May 2026
    
    **Status:** ✅ Active Development
    """)
    
    st.markdown("---")
    
    if st.button("📂 Open Project Folder"):
        st.info("Navigate to: `e:\\Download\\VLM Bootcamp`")

# ============================================================
# FOOTER
# ============================================================
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #888; padding: 2rem 0;">
    <p>🤖 Vision Language Models Bootcamp | Made with ❤️ using Streamlit</p>
    <p><small>© 2026 | Production-Ready VLM Examples</small></p>
</div>
""", unsafe_allow_html=True)
