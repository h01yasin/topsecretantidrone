# Anti-Drone Defense System - Quick Start Guide

## 🚀 5-Minute Setup

### Prerequisites Check

```bash
# Check Python version (need 3.10+)
python --version

# Check pip
pip --version

# Check CUDA (optional, for GPU)
nvidia-smi
```

### Installation

```bash
# 1. Navigate to project
cd C:\Users\Yasin\Desktop\Anti-Drone-Defense-System

# 2. Create virtual environment
python -m venv venv

# 3. Activate virtual environment
.\venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac

# 4. Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
```

### Download Models

```bash
# YOLOv8 will download automatically on first run
# Or manually:
python -c "from ultralytics import YOLO; YOLO('yolov8n.pt')"
```

### First Run

```bash
# Run the system (demo mode with camera)
python unified_defense_system.py
```

**Expected output:**
```
🚀 Initializing Unified Defense System...
📹 Camera 0 initialized
📡 RF detector initialized (simulated)
🔊 Acoustic detector initialized (simulated)
📻 Radar system initialized (simulated)
✅ System Ready!
👁️  Starting detection system...
✅ All detection threads started
============================================================
🛡️  UNIFIED ANTI-DRONE DEFENSE SYSTEM ACTIVE
============================================================
Press Ctrl+C to stop
============================================================
```

### Test Without Hardware

If you don't have cameras or SDR hardware yet:

```python
# unified_defense_system.py will run in simulated mode
# Edit config to disable hardware:

config = {
    'vision': {
        'cameras': []  # Empty list = no cameras
    },
    'rf': {'device': None},
    'acoustic': {'microphones': []},
    'radar': {'type': 'simulated'}
}
```

---

## 📚 Next Steps

### 1. Add Your Camera

```python
config = {
    'vision': {
        'cameras': [
            {'source': 0, 'position': (0, 0, 10), 'fov': 90},
            # 0 = default webcam
            # or 'rtsp://ip:port/stream' for IP camera
        ]
    }
}
```

### 2. Train Custom Model (Optional)

```bash
# Collect drone images (1000+)
# Annotate with labels
# Train YOLOv8

python scripts/train_custom_model.py --data drone_dataset.yaml
```

### 3. Deploy on Jetson

```bash
# Copy files to Jetson
scp -r . user@jetson-ip:/home/user/anti-drone

# SSH into Jetson
ssh user@jetson-ip

# Install dependencies (Jetson-optimized)
sudo apt update
sudo apt install python3-pip
pip3 install -r requirements.txt

# Run
python3 unified_defense_system.py --edge
```

---

## 🐛 Troubleshooting

### Problem: "No module named 'torch'"

```bash
# Reinstall PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

### Problem: "Camera not found"

```bash
# Check available cameras (Windows)
python -c "import cv2; print(cv2.videoio_registry.getCameraBackends())"

# Test camera
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened())"
```

### Problem: "CUDA not available"

```bash
# Check CUDA
python -c "import torch; print(torch.cuda.is_available())"

# If False, PyTorch will use CPU (slower but works)
```

### Problem: "Permission denied for audio"

```bash
# Windows: Check microphone permissions in Settings
# Linux: Add user to audio group
sudo usermod -a -G audio $USER
```

---

## 📊 System Requirements

### Minimum (Development/Testing)
- CPU: Intel i5 or equivalent
- RAM: 8GB
- Storage: 50GB
- OS: Windows 10/11, Ubuntu 20.04+
- Webcam (optional)

### Recommended (Production)
- CPU: Intel i7/i9 or AMD Ryzen 7/9
- GPU: NVIDIA RTX 3060+ (12GB VRAM)
- RAM: 32GB
- Storage: 500GB SSD
- OS: Ubuntu 22.04 LTS
- Multiple cameras, SDR, microphones

### Edge Deployment
- NVIDIA Jetson AGX Orin (32/64GB)
- Industrial cameras (4x)
- Network switch (PoE)
- UPS (2000VA)

---

## 📞 Support

**Issues:** Create GitHub issue or email  
**Documentation:** See `/docs` folder  
**Team contact:** [GitHub Issues](https://github.com/h01yasin/topsecretantidrone/issues)  

---

## ✅ Checklist

- [ ] Python 3.10+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed
- [ ] YOLOv8 model downloaded
- [ ] Camera tested (optional)
- [ ] System runs without errors
- [ ] Read full documentation

---

**Ready to start development!** 🚀
