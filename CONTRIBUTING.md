# Contributing to Anti-Drone Defense System

Thank you for your interest in contributing to this project!

## 🚨 IMPORTANT: This is a Private Project

This is a **proprietary defense technology project**. Contributions are restricted to:
- Authorized AzTU team members
- Approved collaborators with signed NDAs
- Government partners with clearance

**Unauthorized contributions will be rejected.**

---

## 📋 For Authorized Contributors

### Getting Started

1. **Read Documentation First**
   ```bash
   # Must read (in order):
   - SUMMARY.md        # Quick overview
   - README.md         # System design
   - PROJECT_PLAN.md   # Full details
   - QUICK_START.md    # Setup instructions
   ```

2. **Setup Development Environment**
   ```bash
   # Windows
   setup.bat
   
   # Or manually:
   python -m venv venv
   venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Understand the Architecture**
   - Review `unified_defense_system.py`
   - Check module documentation in `docs/`
   - Ask team lead if unclear

---

## 🔄 Development Workflow

### 1. Create Feature Branch
```bash
git checkout -b feature/your-feature-name

# Branch naming:
# - feature/xyz    : New feature
# - fix/xyz        : Bug fix
# - docs/xyz       : Documentation
# - refactor/xyz   : Code refactoring
# - test/xyz       : Tests
```

### 2. Make Changes
```python
# Follow these principles:
- Write clean, documented code
- Add type hints
- Include docstrings
- Write unit tests
- Keep functions small (<50 lines)
- Follow PEP 8 style guide
```

### 3. Test Your Changes
```bash
# Run tests
pytest tests/ -v

# Check code style
flake8 src/
black src/

# Type checking
mypy src/
```

### 4. Commit
```bash
git add .
git commit -m "feat: add trajectory prediction optimization"

# Commit message format:
# feat: new feature
# fix: bug fix
# docs: documentation
# refactor: code refactoring
# test: add tests
# chore: miscellaneous
```

### 5. Push and Create Pull Request
```bash
git push origin feature/your-feature-name

# Then create PR on GitHub/GitLab
```

---

## 📝 Code Standards

### Python Style Guide

```python
# ✅ Good
def detect_drone(
    image: np.ndarray,
    confidence_threshold: float = 0.7
) -> List[DroneDetection]:
    """
    Detect drones in an image using YOLOv8.
    
    Args:
        image: Input image as numpy array (H, W, C)
        confidence_threshold: Minimum confidence score (0-1)
    
    Returns:
        List of detected drones with positions and confidence
    
    Example:
        >>> image = cv2.imread('drone.jpg')
        >>> detections = detect_drone(image, confidence_threshold=0.8)
        >>> print(f"Found {len(detections)} drones")
    """
    # Implementation here
    pass

# ❌ Bad
def detectDrone(img, th=0.7):  # No type hints, bad naming
    # detect drones
    pass
```

### Documentation

```python
# All modules should have:
# 1. Module docstring
# 2. Class docstrings
# 3. Function docstrings
# 4. Inline comments for complex logic

"""
vision_detector.py - Computer vision module for drone detection

This module handles real-time drone detection using YOLOv8 model.
Supports multiple cameras, day/night modes, and 3D position estimation.

Author: [Your Name]
Date: [Date]
"""
```

### Testing

```python
# tests/test_vision.py
import pytest
from src.vision import VisionDetector

def test_vision_detector_initialization():
    """Test that VisionDetector initializes correctly"""
    config = {'model_path': 'yolov8n.pt'}
    detector = VisionDetector(config)
    assert detector is not None

def test_drone_detection():
    """Test drone detection on sample image"""
    detector = VisionDetector({'model_path': 'yolov8n.pt'})
    image = load_test_image('drone.jpg')
    detections = detector.detect(image)
    assert len(detections) > 0
    assert detections[0].confidence > 0.5
```

---

## 🐛 Reporting Issues

### Bug Reports

**Template:**
```markdown
## Bug Description
Clear description of the bug

## Steps to Reproduce
1. Step 1
2. Step 2
3. ...

## Expected Behavior
What should happen

## Actual Behavior
What actually happens

## Environment
- OS: Windows 11
- Python: 3.10.5
- CUDA: 11.8
- GPU: RTX 3060

## Logs
```
paste relevant logs here
```

## Screenshots
If applicable
```

### Feature Requests

**Template:**
```markdown
## Feature Description
What feature do you want?

## Use Case
Why is this needed?

## Proposed Solution
How should it work?

## Alternatives Considered
Other possible approaches

## Additional Context
Screenshots, diagrams, etc.
```

---

## 🔍 Code Review Process

All code must be reviewed before merging:

1. **Self-Review**: Review your own code first
2. **Automated Checks**: CI/CD must pass
3. **Peer Review**: At least 1 team member approval
4. **Tech Lead Review**: For critical changes
5. **Testing**: All tests must pass

### Review Checklist

- [ ] Code follows style guide
- [ ] Tests added/updated
- [ ] Documentation updated
- [ ] No performance regression
- [ ] Security considerations addressed
- [ ] No sensitive data exposed

---

## 🔒 Security Guidelines

### DO:
- ✅ Sign commits (`git config --global commit.gpgsign true`)
- ✅ Use environment variables for secrets
- ✅ Review dependencies for vulnerabilities
- ✅ Report security issues privately via: [GitHub Security Tab](https://github.com/h01yasin/topsecretantidrone/security)

### DON'T:
- ❌ Commit credentials, API keys, passwords
- ❌ Share code publicly without approval
- ❌ Discuss sensitive details in public forums
- ❌ Use untrusted third-party libraries

---

## 📅 Sprint Process

We follow 2-week sprints:

**Sprint Schedule:**
```
Week 1:
  Monday: Sprint planning (9:00 AM)
  Daily: Standups (9:00 AM, 15 min)
  Friday: Sprint review & demo (3:00 PM)

Week 2:
  Monday-Thursday: Development
  Friday: Retrospective + next sprint planning
```

**Standup Format:** (max 15 min)
- What did you do yesterday?
- What will you do today?
- Any blockers?

---

## 🎓 For Students (Thesis Projects)

### Thesis Guidelines

1. **Topic Assignment**: Discuss with advisor
2. **Literature Review**: 2-4 weeks
3. **Implementation**: 8-12 weeks
4. **Testing**: 2-4 weeks
5. **Writing**: 4-6 weeks
6. **Defense**: Schedule with committee

### Thesis Structure

```
1. Introduction
   - Background
   - Problem statement
   - Objectives
   
2. Literature Review
   - Existing systems
   - Related work
   
3. Methodology
   - System design
   - Algorithms
   
4. Implementation
   - Technologies used
   - Challenges faced
   
5. Results & Evaluation
   - Experiments
   - Performance metrics
   
6. Conclusion
   - Summary
   - Future work
   
References
Appendices
```

---

## 📞 Contact

**Questions?**
- Technical: [Tech Lead Email]
- Process: [Project Manager Email]
- Security: [GitHub Security](https://github.com/h01yasin/topsecretantidrone/security)
- General: [GitHub Issues](https://github.com/h01yasin/topsecretantidrone/issues)

**Office Hours:**
- Monday-Friday: 9:00 AM - 6:00 PM (Asia/Baku)
- Location: [AzTU Lab Location]

---

## 📜 License

This project is proprietary. See [LICENSE](LICENSE) for details.

By contributing, you agree to:
1. Sign NDA
2. Assign IP rights to AzTU
3. Follow security protocols
4. Maintain confidentiality

---

**Thank you for contributing to Azerbaijan's defense technology!** 🇦🇿
