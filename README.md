# ironhack-w3-project-CNN

# CIFAR-10 Image Classification — CNN Comparative Study

A group project exploring CNN architectures and training strategies for image classification on the CIFAR-10 dataset.

**Team:** Charleson, João, Harn

---

## Project Overview

This project investigates how different architectural choices and training configurations affect classification performance on CIFAR-10 (10 classes: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck).

The team built and evaluated **10 models** in total:
- **Model 1** — Baseline, built collaboratively by all three members
- **Models 2, 5, 8** — Member 1
- **Models 3, 6, 9** — Member 2
- **Models 4, 7, 10** — Member 3

---

## Dataset

| Property | Value |
|---|---|
| Dataset | CIFAR-10 |
| Classes | 10 |
| Image Size | 32×32 (resized to 96×96 for Model 8) |
| Train Split | 90% |
| Validation Split | 10% |

---

## Model Summary

### Preprocessing

| Parameter | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Resizing | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |
| Data Augmentation | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |
| Normalization | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ |
| One-hot Encoding | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ | ✗ | ✓ |
| Transfer Learning | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✗ |

### Architecture

| Parameter | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Conv Layers | 3 | 3 | 3 | 3 | 3 | 3 | 3 | MobileNetV2 | 6 | 3 |
| MaxPooling | 3 | 3 | 3 | — | 3 | 3 | 3 | 0 | 3 | 3 |
| Batch Norm | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ | ✓ | ✓ |
| Dropout | ✗ | ✗ | ✓ | ✓ | ✗ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Global Avg Pooling | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | — |
| Flatten | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | ✗ | ✓ | ✓ |
| L2 Regularizer | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ |

### Training Configuration

| Parameter | M1 | M2 | M3 | M4 | M5 | M6 | M7 | M8 | M9 | M10 |
|---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Learning Rate | 0.001 | 0.001 | 0.001 | 0.005 | 0.001 | 0.001 | 0.001 | 0.001→1e-6 | 0.0005 | 0.001 |
| Optimizer | Adam | Adam | Adam | Adam | SGD | Adam | Adam | Adam | Adam | Adam |
| LR Scheduler | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✗ | ✓ |
| Epochs | 10 | 20 | 50 | — | 20 | 50 | 50 | 30+20 | 50 | 50 |
| Batch Size | 64 | 64 | 128 | 64 | 64 | 128 | 64 | 64 | 64 | 128 |
| Early Stopping | ✗ | ✗ | ✗ | ✗ | ✗ | ✗ | ✓ | ✓ | ✓ | ✓ |

---

## Results

| Model | Train Acc | Train Loss | Val Acc | Val Loss | Test Acc |
|---|:---:|:---:|:---:|:---:|:---:|
| M1 — Baseline | 85.87% | 0.4016 | 74.48% | 0.8221 | 73.56% |
| M2 | 95.59% | 0.1227 | 74.10% | 1.3938 | — |
| M3 | 79.21% | 0.5918 | 78.98% | 0.6136 | 78.45% |
| M4 | 77.46% | 0.6474 | 78.42% | 0.6198 | 77.87% |
| M5 | 98.98% | 0.0138 | 75.50% | 0.1954 | — |
| M6 | 79.21% | 0.5918 | 78.98% | 0.6136 | 78.45% |
| M7 | 63.72% | 1.0330 | 69.54% | 0.8579 | 69.37% |
| **M8** | **95.60%** | **0.1306** | **90.90%** | **0.2978** | **90.21%** |
| M9 | 88.17% | 0.3450 | 88.98% | 0.3329 | 87.87% |
| M10 | 82.97% | 0.6251 | 85.40% | 0.5479 | 85.15% |

---

## Key Findings

**Best model: Model 8 — 90.21% test accuracy**
- The only model using transfer learning (MobileNetV2 pretrained on ImageNet)
- Two-phase fine-tuning with LR scheduler (`ReduceLROnPlateau`)
- Resizing to 96×96, data augmentation, batch normalization, and early stopping

**Overfitting was a recurring issue** — Models 2 and 5 achieved very high training accuracy (95–99%) but poor validation accuracy (~74–75%), indicating overfitting without sufficient regularization.

**Regularization helped** — Models with dropout + batch normalization (M9, M10) generalised significantly better than those without, even with simpler architectures.

**Data augmentation was important** — All top-performing models (M8, M9, M10) used augmentation; none of the bottom performers did.

**Cats vs Dogs** — Lots of misclassifications in Cats vs Dogs Classifiacation. Need to probe weights.

---

## Tech Stack

- Python 3
- TensorFlow / Keras
- scikit-learn
- NumPy, Matplotlib, Seaborn
- Gradio (deployment)

---

## Contributors

| Member | Models |
|---|---|
| Charleson | M1, M2, M5, M8 |
| João | M1, M3, M6, M9 |
| Harn | M1, M4, M7, M10 |