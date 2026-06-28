# 🏭 Edge AI Predictive Maintenance for Industrial Bearings

## Overview
This project implements an end-to-end TinyML pipeline that detects catastrophic mechanical failures in industrial motors. It extracts high-frequency vibration data, trains a lightweight machine learning model, translates the model into raw C++ logic, and deploys it directly onto an ESP32 microcontroller for real-time edge inference.

---

## 🛠️ The Hardware & Dataset
The data used in this project is from the **NASA/IMS Bearing Dataset**. The physical test rig was highly constrained to induce structural degradation:
* **Rotation Speed:** Constant 2000 RPM (AC Motor)
* **Radial Load:** 6000 lbs 
* **Sensors:** High Sensitivity Quartz ICP accelerometers (sampled at 20 kHz)
* **Bearings:** Rexnord ZA-2115 double row bearings

Because microcontrollers cannot store 20,480 high-frequency sensor readings per second, the raw data was mathematically compressed into four distinct temporal features.

---

## 🧠 The AI Architecture

### 1. Feature Engineering
Raw vibration signals were compressed into the following statistical features:
* **RMS (Root Mean Square):** Tracks overall kinetic energy and friction heat.
* **Kurtosis:** Identifies transient peaks caused by micro-cracks in the bearing race.
* **Peak-to-Peak:** Measures extreme deviation limits.
* **Skewness:** Tracks wear-pattern asymmetry.

### 2. Machine Learning Optimization
Initial testing utilized a 50-tree Random Forest Classifier, which achieved 99% accuracy but was too memory-intensive for edge deployment. 

The model was optimized down to a single **Decision Tree Classifier**, which achieved a **95% recall rate** on the failure class while reducing the memory footprint by approximately 98%.

### 3. Edge Deployment (C++ Translation)
Using the `m2cgen` library, the trained Python model was translated into pure, dependency-free C math (`model.h`). This eliminated the need for heavy operating systems or Python interpreters on the microchip, allowing inference to occur in microseconds.

---

## 🚀 Live Hardware Simulation
You do not need to download this repository to see the Edge AI in action. The C++ logic has been deployed to a virtual ESP32 microchip.

👉 **[Click here to run the Live Wokwi ESP32 Simulation](https://wokwi.com/projects/465550883679291393)**

**How to read the simulation:**
When you hit "Play", the ESP32 bootloader will initialize. The chip will then continuously process simulated arrays of the four engineered features. Watch the Serial Monitor to see the chip successfully distinguish between normal operation and an active anomaly.

---

## 💻 How to Run Locally

If you wish to re-train the model or engineer new features:

1. **Install dependencies:**
   ```bash
   pip install numpy pandas scikit-learn joblib m2cgen
