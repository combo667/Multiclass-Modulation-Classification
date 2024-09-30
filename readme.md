# Signal Modulation Classification with VGG16 and ADALM-PLUTO SDR

### Description

This project demonstrates multi-class modulation classification of radio signals using a VGG16-based deep learning model. The signals were captured using the ADALM-PLUTO SDR, with a Vector Signal Generator generating various modulation types at 915 MHz. Signals were preprocessed in Python, utilizing features such as constellation diagrams for training the model.

---

## Folder Structure

### **Dataset**
This folder contains 6 subfolders (for different modulation types: 2ASK, 2FSK, 4FSK, 8FSK, BPSK, QAM16). Each subfolder contains 5000 constellation images of size `224x224`.

### **Outcomes**
This folder contains the following results from the trained model:
1. **Confusion Matrix**: Displays the confusion matrix for testing results.
2. **Precision and Recall Scores**: Provides precision and recall metrics for model performance.
3. **Training Progress**: Tracks data from the model training process.
4. **Test Accuracy**: Contains accuracy values for testing the model with the test dataset.

---

## Scripts

1. **`plotConstellationBins_of_IQ_CSV_Files.py`**  
   Generates constellation diagrams from CSV files containing IQ values (telemetry data from the RFD900).

2. **`plotConstellationBins_of_VSG_Data.py`**  
   Generates constellation diagrams from `.complex16s` files captured using a Vector Signal Generator.

3. **`RF_MODULATION_CLASSIFICATION_MULTICLASS.ipynb`**  
   This Jupyter Notebook contains the code for defining the VGG16 model and testing it for multi-class modulation classification.

---

## Model

- **`VGG16_Modulation_Multiclass_Classification.h5`**  
  The trained model file. It can be loaded anytime using the `load_model` function for testing and evaluation.

---

## Captured Signals

- **`CapturedSignalsFromVsgForModulationClassification`**  
  Contains `.complex16s` files, which are actual signals captured from the VSG for different modulation types. These signals were used to generate constellation diagrams.

  - **Samples Captured**: 15M
  - **Sampling Frequency (fs)**: 2 MHz
  - **Carrier Frequency**: 1 GHz

---

## Dataset Location: [Click Here](https://drive.google.com/drive/folders/18eN73YtTSq2oIr6DMJ8n8drYpesFLfij?usp=sharing)


1. **`rfd900_fsk_csv_files.zip`**  
   Contains actual telemetry signals (2FSK signals) from the RFD900, used for generating constellation diagrams and training the model.

2. **`CapturedSignalsFromVsgForModulationClassification`**  
   Contains signal data used for generating constellation diagrams and model training.

---

## How to Run

1. **Preprocess Signals**: Use `plotConstellationBins_of_IQ_CSV_Files.py` or `plotConstellationBins_of_VSG_Data.py` to generate constellation diagrams.
2. **Train the Model**: Use the notebook `RF_MODULATION_CLASSIFICATION_MULTICLASS.ipynb` to define, train, and evaluate the VGG16-based model.
3. **Evaluate Results**: The `Outcomes` folder contains evaluation metrics such as confusion matrix, precision-recall scores, and test accuracy.

---

## License

[MIT License](LICENSE)
