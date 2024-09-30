This folder contains all the necessary files for generating constellations diagrams, model training, datasets.

dataset: It contains 6 folders (2ASK,2FSK,4FSK,8FSK,BPSK,QAM16) and each subfolders contains 5000 constellation images of size 224,224.

Outcomes: It is a folder which contains the following files.
	
	1.Confusion_Matrix: It is the confusion matrix on which we tested our model.
	2.Precision_Recall_Score: It is the precision and recall score of our model.
	3.Training_Progress: It contains all the data while the model was getting trained.
	4.TestAccuracy: It contains the test accuracy of the model while testing the model in the test dataset.
	


Scripts:
	1.plotConstellationBins_of_IQ_CSV_Files.py: It is a script to generate the constellation diagram 	where the input is a csv file of IQ Values(The CSV file is a telemetry data of RFD900).

	2.plotConstellationBins_of_VSG_Data.py: It is a script to generate the constellation diagram where the input is a .complex16s file which was captured using Vector Signal Generator.
	
	3.RF_MODULATION_CLASSIFICATION_MULTICLASS.ipynb: This is the main script where the VGG16 model has been defined, and also the testing codes are defined.



Model: It contains a file named "VGG16_Modulation_Multiclass_Classification.h5" which is the model that 	we got after training, it can be loaded anytime with the load_model function and can be tested.



CapturedSignalsFromVsgForModulationClassification: It contains the actual signal .complex16s files that i 	captured from the VSG of different modulation types. Using this signal data we plotted the 	constellation diagrams.

	1. Samples Captured: 15M
	2. fs = 2MHz
	3. Frequency: 1GHz



rfd900_fsk_csv_files.zip : This file contains actual signals which are telemetry data of RFD900 ,these are all 2 FSK signals which i used to plot constellation diagrams and used in training the model.


Dataset Location:
	1. rfd900_fsk_csv_files.zip: Here itself
	2. CapturedSignalsFromVsgForModulationClassification: Here itself