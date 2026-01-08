# Garbage Classification with CNN and ResNet34

This repository implements an image classification system for garbage
sorting using deep learning models, including a custom CNN and ResNet34.

The project focuses on comparing model performance and generalization
capability on a real-world waste classification dataset.

---

## Features

- End-to-end image classification pipeline built with PyTorch
- Custom 7-layer CNN model
- ResNet34 fine-tuning for improved generalization
- Performance comparison between shallow CNN and deep residual networks
- Experimental analysis using accuracy and confusion matrices

---

## Project Structure

```text
garbage_classification/
├── README.md
├── garbage_CNN.py
├── garbage_resnet34.py
├── dataset_handle.py
├── dataset_count.py
├── testCuda.py
├── datasets/        
├── result/          
├── runs/            
└── model.pt
```
---        

## Dtaset

The dataset contains images from six garbage categories (e.g., paper,
cardboard, plastic, metal, glass, and trash).

## How to Run
1. Environment Setup
pip install torch torchvision numpy matplotlib

2. Train CNN Model
python garbage_CNN.py

3. Train ResNet34 Model
python garbage_resnet34.py

---

## Experimental Results

The custom CNN achieves fast convergence but shows signs of overfitting

ResNet34 achieves higher test accuracy and better generalization

Confusion matrix analysis shows improved classification performance
on visually similar classes (e.g., paper vs cardboard)

---

## Notes

This project was developed as part of a coursework

The code is intended for experimentation and learning purposes

Trained models and intermediate results are not committed to keep
the repository lightweight

---

## License

MIT License
